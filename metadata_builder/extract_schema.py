import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = Path(__file__).resolve().parent / 'output'
OUTPUT_PATH = OUTPUT_DIR / 'raw_schema.json'

load_dotenv(BASE_DIR / '.env')

SCHEMA_PREFIX = 'a_'
TEXT_TYPES = {'character varying', 'text', 'character'}
SAMPLE_LIMIT = 5

# Same env vars / defaults as portal/settings.py's GIS_DB_CONFIG.
DB_CONFIG = {
    'host': os.environ.get('GIS_DB_HOST', 'gisdb.systra.info'),
    'port': os.environ.get('GIS_DB_PORT', '5432'),
    'dbname': os.environ.get('GIS_DB_NAME', 'uk_irl'),
    'user': os.environ.get('GIS_DB_USER', ''),
    'password': os.environ.get('GIS_DB_PASSWORD', ''),
    'sslmode': os.environ.get('GIS_DB_SSLMODE', 'require'),
}


def _is_db_unconfigured():
    # Same placeholder check as catalogue/views.py's _is_gis_db_mock().
    return not DB_CONFIG['user'] or DB_CONFIG['user'] == 'YOUR_DB_USER'


def _format_type(data_type, char_max_len, udt_name):
    if data_type == 'USER-DEFINED':
        return udt_name

    short = {
        'character varying': 'varchar',
        'character': 'char',
        'timestamp without time zone': 'timestamp',
        'timestamp with time zone': 'timestamptz',
    }.get(data_type, data_type)

    if short in ('varchar', 'char') and char_max_len:
        return f'{short}({char_max_len})'
    return short


def _parse_box2d(box_text):
    # ST_Extent returns 'BOX(xmin ymin,xmax ymax)', or NULL for an empty table.
    if not box_text:
        return None
    coords = box_text.replace('BOX(', '').replace(')', '')
    (xmin, ymin), (xmax, ymax) = (
        list(map(float, pair.strip().split())) for pair in coords.split(',')
    )
    return {'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax}


def _get_a_schemas(cur):
    # '~' regex match (not LIKE) so the '_' in 'a_' is treated literally, not as a wildcard.
    cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name ~ '^a_' ORDER BY schema_name")
    return [row[0] for row in cur.fetchall()]


def _get_tables(cur, schema):
    cur.execute(
        "SELECT table_name FROM information_schema.tables "
        "WHERE table_schema = %s AND table_type = 'BASE TABLE' ORDER BY table_name",
        (schema,),
    )
    return [row[0] for row in cur.fetchall()]


def _get_columns(cur, schema, table):
    cur.execute(
        "SELECT column_name, data_type, character_maximum_length, udt_name "
        "FROM information_schema.columns "
        "WHERE table_schema = %s AND table_name = %s ORDER BY ordinal_position",
        (schema, table),
    )
    return cur.fetchall()


def _get_geometry_info(cur, schema, table):
    cur.execute(
        "SELECT f_geometry_column, type, srid FROM geometry_columns "
        "WHERE f_table_schema = %s AND f_table_name = %s",
        (schema, table),
    )
    row = cur.fetchone()
    if not row:
        return None, None, None
    geom_col, geom_type, _srid = row
    # Find_SRID is PostGIS's recommended canonical lookup, rather than trusting geometry_columns directly.
    cur.execute('SELECT Find_SRID(%s, %s, %s)', (schema, table, geom_col))
    confirmed_srid = cur.fetchone()[0]
    return geom_col, geom_type, confirmed_srid


def _get_row_count(cur, schema, table):
    cur.execute(sql.SQL('SELECT COUNT(*) FROM {}.{}').format(sql.Identifier(schema), sql.Identifier(table)))
    return cur.fetchone()[0]


def _get_bbox_wgs84(cur, schema, table, geom_col):
    if not geom_col:
        return None
    cur.execute(
        sql.SQL('SELECT ST_Extent(ST_Transform({geom}, 4326))::text FROM {schema}.{table}').format(
            geom=sql.Identifier(geom_col), schema=sql.Identifier(schema), table=sql.Identifier(table)
        )
    )
    return _parse_box2d(cur.fetchone()[0])


def _get_table_comment(cur, schema, table):
    cur.execute("SELECT obj_description(%s::regclass, 'pg_class')", (f'"{schema}"."{table}"',))
    return cur.fetchone()[0]


def _get_sample_values(cur, schema, table, columns, geom_col):
    samples = {}
    for col_name, data_type, _char_len, _udt in columns:
        if col_name == geom_col or data_type not in TEXT_TYPES:
            continue
        cur.execute(
            sql.SQL('SELECT DISTINCT {col} FROM {schema}.{table} WHERE {col} IS NOT NULL LIMIT %s').format(
                col=sql.Identifier(col_name), schema=sql.Identifier(schema), table=sql.Identifier(table)
            ),
            (SAMPLE_LIMIT,),
        )
        samples[col_name] = [row[0] for row in cur.fetchall()]
    return samples


def _extract_table(cur, schema, table):
    columns = _get_columns(cur, schema, table)
    geom_col, geom_type, srid = _get_geometry_info(cur, schema, table)

    return {
        'identifier': f'{schema}/{table}',
        'schema': schema,
        'table': table,
        'columns': [
            {
                'name': name,
                'data_type': 'geometry' if name == geom_col else _format_type(data_type, char_len, udt),
            }
            for name, data_type, char_len, udt in columns
        ],
        'geometry_column': geom_col,
        'geometry_type': geom_type,
        'srid': srid,
        'crs': f'EPSG:{srid}' if srid else None,
        'row_count': _get_row_count(cur, schema, table),
        'bbox_wgs84': _get_bbox_wgs84(cur, schema, table, geom_col),
        'table_comment': _get_table_comment(cur, schema, table),
        'sample_values': _get_sample_values(cur, schema, table, columns, geom_col),
    }


def extract_live():
    if _is_db_unconfigured():
        print(
            'GIS_DB_USER is not set in .env (still the YOUR_DB_USER placeholder).\n'
            'The production PostGIS server also requires VPN. Run with --mock instead.',
            file=sys.stderr,
        )
        sys.exit(1)

    conn = psycopg2.connect(**DB_CONFIG)
    tables = []
    errors = []
    try:
        with conn.cursor() as cur:
            schemas = _get_a_schemas(cur)
            print(f"Found {len(schemas)} schema(s) matching '{SCHEMA_PREFIX}*': {', '.join(schemas)}")
            for schema in schemas:
                table_names = _get_tables(cur, schema)
                print(f'  {schema}: {len(table_names)} table(s)')
                for table in table_names:
                    try:
                        tables.append(_extract_table(cur, schema, table))
                        print(f'    ok      {schema}.{table}')
                    except Exception as exc:
                        conn.rollback()
                        errors.append({'schema': schema, 'table': table, 'error': str(exc)})
                        print(f'    FAILED  {schema}.{table} - {exc}', file=sys.stderr)
    finally:
        conn.close()

    database = {'host': DB_CONFIG['host'], 'port': DB_CONFIG['port'], 'dbname': DB_CONFIG['dbname']}
    return tables, errors, database


# The BGS spec says "Columns (57 total)" but only lists 26 (plus geom) — using
# exactly what was supplied rather than inventing the other 31.
_MOCK_TABLES = [
    {
        'schema': 'a_british_geological_survey',
        'table': '625k_bedrock_geology',
        'columns': [
            ('lex', 'varchar(5)'), ('lex_d', 'varchar(200)'), ('lex_rcs', 'varchar(12)'),
            ('rcs', 'varchar(6)'), ('rcs_x', 'varchar(50)'), ('rcs_d', 'varchar(200)'),
            ('rank', 'varchar(16)'), ('bed_eq', 'varchar(5)'), ('bed_eq_d', 'varchar(200)'),
            ('mb_eq', 'varchar(5)'), ('mb_eq_d', 'varchar(200)'), ('fm_eq', 'varchar(5)'),
            ('fm_eq_d', 'varchar(200)'), ('subgp_eq', 'varchar(5)'), ('subgp_eq_d', 'varchar(200)'),
            ('gp_eq', 'varchar(5)'), ('gp_eq_d', 'varchar(200)'), ('supgp_eq', 'varchar(5)'),
            ('supgp_eq_d', 'varchar(200)'), ('max_time_d', 'varchar(32)'), ('min_time_d', 'varchar(32)'),
            ('max_time_y', 'bigint'), ('min_time_y', 'bigint'), ('max_index', 'bigint'),
            ('min_index', 'bigint'),
        ],
        'geometry_column': 'geom',
        'geometry_type': 'MULTIPOLYGON',
        'srid': 27700,
        'row_count': 70245,
        'bbox_wgs84': {'xmin': -7.9, 'ymin': 49.7, 'xmax': 2.1, 'ymax': 60.9},
    },
    {
        'schema': 'a_historic_england',
        'table': 'battlefields',
        'columns': [
            ('listentry', 'integer'), ('name', 'text'), ('regdate', 'timestamp'),
            ('amenddate', 'timestamp'), ('capturescale', 'varchar(15)'), ('hyperlink', 'varchar(255)'),
            ('area_ha', 'real'), ('ngr', 'varchar(1000000)'), ('easting', 'real'),
            ('northing', 'real'), ('objectid', 'bigint'),
        ],
        'geometry_column': 'geom',
        'geometry_type': 'MULTIPOLYGON',
        'srid': 27700,
        'row_count': 47,
        'bbox_wgs84': {'xmin': -3.2, 'ymin': 50.1, 'xmax': 1.8, 'ymax': 55.6},
    },
    {
        'schema': 'a_os_built_up_areas',
        'table': 'os_open_built_up_areas',
        'columns': [
            ('gsscode', 'varchar'), ('name1_text', 'varchar'), ('name1_language', 'varchar'),
            ('name2_text', 'varchar'), ('name2_language', 'varchar'), ('areahectares', 'double precision'),
            ('geometry_area_m', 'double precision'), ('fid', 'bigint'),
        ],
        'geometry_column': 'geom',
        'geometry_type': 'MULTIPOLYGON',
        'srid': 27700,
        'row_count': 12680,
        'bbox_wgs84': {'xmin': -6.4, 'ymin': 49.9, 'xmax': 1.8, 'ymax': 60.9},
    },
]

_MOCK_TEXT_TYPES = ('varchar', 'text', 'char')


def extract_mock():
    print(f'MOCK mode: using {len(_MOCK_TABLES)} bundled sample table(s), no database connection made.')
    print(
        "NOTE: the BGS table spec says 'Columns (57 total)' but only lists 26 - "
        'this mock uses exactly the 26 supplied, not 57.'
    )
    tables = []
    for spec in _MOCK_TABLES:
        columns = spec['columns'] + [(spec['geometry_column'], 'geometry')]
        tables.append({
            'identifier': f"{spec['schema']}/{spec['table']}",
            'schema': spec['schema'],
            'table': spec['table'],
            'columns': [{'name': name, 'data_type': dtype} for name, dtype in columns],
            'geometry_column': spec['geometry_column'],
            'geometry_type': spec['geometry_type'],
            'srid': spec['srid'],
            'crs': f"EPSG:{spec['srid']}",
            'row_count': spec['row_count'],
            'bbox_wgs84': spec['bbox_wgs84'],
            'table_comment': None,
            # No row-level data was supplied for the mock tables, so sample
            # values are left empty rather than invented.
            'sample_values': {
                name: [] for name, dtype in spec['columns'] if dtype.startswith(_MOCK_TEXT_TYPES)
            },
        })
        print(f"    ok      {spec['schema']}.{spec['table']}  ({spec['row_count']} rows, {len(columns)} columns)")
    return tables, [], None


def main():
    parser = argparse.ArgumentParser(description='Extract PostGIS schema metadata for the Systra GIS Portal.')
    parser.add_argument('--mock', action='store_true', help='Use bundled sample data instead of a live DB connection.')
    args = parser.parse_args()

    run_timestamp = datetime.now(timezone.utc).isoformat()

    if args.mock:
        tables, errors, database = extract_mock()
        mode = 'mock'
    else:
        tables, errors, database = extract_live()
        mode = 'live'

    output = {
        'run_timestamp': run_timestamp,
        'mode': mode,
        'database': database,
        'schema_prefix': SCHEMA_PREFIX,
        'table_count': len(tables),
        'tables': tables,
        'errors': errors,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, indent=2, default=str), encoding='utf-8')

    print(f'\nWrote {len(tables)} table(s) to {OUTPUT_PATH}')
    if errors:
        print(f'{len(errors)} table(s) failed extraction (see "errors" in the output file).')


if __name__ == '__main__':
    main()
