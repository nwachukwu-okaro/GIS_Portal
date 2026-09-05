#!/usr/bin/env python
"""
migrate_add_metadata_json.py

One-time schema migration for the p_pycsw.records consolidation: p_pycsw.records
is becoming the single source of truth for portal search, QGIS MetaSearch, and
the LLM agent, replacing the separate metadata_builder/output/metadata/*.json
files as the agent's read path. This adds:

  - schema_name, table_name (varchar) - for easy ad-hoc querying/maintenance
    by a database admin, without having to parse the identifier column.
  - metadata_json (JSONB) - the full gemini/technical/columns payload that
    scripts/ingest_authoritative.py builds per table (see that script for the
    structure), plus a GIN index so JSONB containment/path queries stay fast
    once every authoritative table's full record lives in this one column.

Every statement uses IF NOT EXISTS, so this script is safe to run more than
once - it checks what already exists before making each change and reports
exactly what it did, rather than assuming a clean slate.

Usage:
    python scripts/migrate_add_metadata_json.py
    python scripts/migrate_add_metadata_json.py --dry-run   # print the SQL, no DB connection

If GIS_DB_USER is unset or still the YOUR_DB_USER placeholder (e.g. on a dev
laptop with no VPN access to the real PostGIS server), the script
automatically falls back to --dry-run instead of failing outright, matching
scripts/ingest_authoritative.py's convention.
"""
import argparse
import sys
from pathlib import Path

from dotenv import load_dotenv
import os

try:
    import psycopg2
except ImportError:  # pragma: no cover - dry-run only works without this
    psycopg2 = None

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent

load_dotenv(BASE_DIR / '.env', override=True)

# Same env vars / defaults as the rest of this project's DB-connecting scripts
# (metadata_builder/extract_schema.py, scripts/ingest_authoritative.py).
DB_CONFIG = {
    'host': os.environ.get('GIS_DB_HOST', 'gisdb.systra.info'),
    'port': os.environ.get('GIS_DB_PORT', '5432'),
    'dbname': os.environ.get('GIS_DB_NAME', 'uk_irl'),
    'user': os.environ.get('GIS_DB_USER', ''),
    'password': os.environ.get('GIS_DB_PASSWORD', ''),
    'sslmode': os.environ.get('GIS_DB_SSLMODE', 'require'),
}

TABLE_EXISTS_SQL = """
    SELECT 1 FROM information_schema.tables
    WHERE table_schema = 'p_pycsw' AND table_name = 'records'
"""

# (label, ALTER/CREATE statement, "does this already exist?" check run first)
STATEMENTS = [
    (
        'schema_name column',
        'ALTER TABLE p_pycsw.records ADD COLUMN IF NOT EXISTS schema_name varchar(255)',
        "SELECT 1 FROM information_schema.columns "
        "WHERE table_schema = 'p_pycsw' AND table_name = 'records' AND column_name = 'schema_name'",
    ),
    (
        'table_name column',
        'ALTER TABLE p_pycsw.records ADD COLUMN IF NOT EXISTS table_name varchar(255)',
        "SELECT 1 FROM information_schema.columns "
        "WHERE table_schema = 'p_pycsw' AND table_name = 'records' AND column_name = 'table_name'",
    ),
    (
        'metadata_json column',
        'ALTER TABLE p_pycsw.records ADD COLUMN IF NOT EXISTS metadata_json JSONB',
        "SELECT 1 FROM information_schema.columns "
        "WHERE table_schema = 'p_pycsw' AND table_name = 'records' AND column_name = 'metadata_json'",
    ),
    (
        'metadata_json GIN index',
        'CREATE INDEX IF NOT EXISTS idx_records_metadata_json ON p_pycsw.records USING GIN (metadata_json)',
        "SELECT 1 FROM pg_indexes "
        "WHERE schemaname = 'p_pycsw' AND tablename = 'records' AND indexname = 'idx_records_metadata_json'",
    ),
]


def _is_db_unconfigured():
    # Same placeholder check as catalogue/views.py's _is_gis_db_mock().
    return not DB_CONFIG['user'] or DB_CONFIG['user'] == 'YOUR_DB_USER'


def run(dry_run):
    if dry_run:
        print('DRY-RUN: would execute the following against p_pycsw.records - no DB connection made.\n')
        for label, sql, _check in STATEMENTS:
            print(f'-- {label}')
            print(sql + ';\n')
        return 0

    if psycopg2 is None:
        print('psycopg2 is required for a live migration. Install the project requirements first.', file=sys.stderr)
        return 1

    conn = psycopg2.connect(**DB_CONFIG)
    conn.autocommit = True  # each statement is independently safe/idempotent (IF NOT EXISTS)
    try:
        with conn.cursor() as cur:
            cur.execute(TABLE_EXISTS_SQL)
            if cur.fetchone() is None:
                print(
                    'p_pycsw.records does not exist on this database - nothing to migrate. '
                    'Run the pycsw setup / ingest scripts first.',
                    file=sys.stderr,
                )
                return 1

            results = []
            for label, sql, check_sql in STATEMENTS:
                cur.execute(check_sql)
                already_existed = cur.fetchone() is not None
                cur.execute(sql)
                results.append((label, already_existed))
    except Exception as exc:
        print(f'FAILED: {exc}', file=sys.stderr)
        return 1
    finally:
        conn.close()

    print('Migration complete on p_pycsw.records:\n')
    for label, already_existed in results:
        status = 'already existed (no-op)' if already_existed else 'created'
        print(f'  [{status:<22}] {label}')
    print('\nSuccess.')
    return 0


def main():
    parser = argparse.ArgumentParser(
        description='Add schema_name, table_name and metadata_json (with a GIN index) to p_pycsw.records.'
    )
    parser.add_argument(
        '--dry-run', action='store_true',
        help='Print the SQL that would run, without connecting to the database.',
    )
    args = parser.parse_args()

    dry_run = args.dry_run
    if not dry_run and _is_db_unconfigured():
        print(
            'GIS_DB_USER is not configured (still the YOUR_DB_USER placeholder or unset) - '
            'falling back to --dry-run. Set GIS_DB_HOST/PORT/NAME/USER/PASSWORD in .env and '
            'ensure VPN/network access to the real PostGIS server to run this for real.\n'
        )
        dry_run = True

    sys.exit(run(dry_run))


if __name__ == '__main__':
    main()
