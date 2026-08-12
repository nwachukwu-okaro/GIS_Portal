"""Credit-free, incremental metadata builder for authoritative PostGIS schemas.

The builder treats JSON as the canonical agent-readable format and renders
Markdown from it.  It can extract from PostGIS, use bundled mock data, or build
from an existing raw_schema.json file.  No external AI service is used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tempfile
import traceback
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

import extract_schema

BUILDER_VERSION = 1
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
CONFIG_DIR = SCRIPT_DIR / 'config'
OUTPUT_DIR = SCRIPT_DIR / 'output'
RAW_SCHEMA_PATH = OUTPUT_DIR / 'raw_schema.json'
METADATA_DIR = OUTPUT_DIR / 'metadata'
TABLES_DIR = OUTPUT_DIR / 'tables'
INDEX_PATH = OUTPUT_DIR / 'agent_index.json'
STATE_PATH = OUTPUT_DIR / 'build_state.json'
REPORT_JSON_PATH = OUTPUT_DIR / 'run_report.json'
REPORT_TEXT_PATH = OUTPUT_DIR / 'run_report.txt'

STOPWORDS = {
    'a', 'an', 'and', 'as', 'at', 'by', 'data', 'dataset', 'for', 'from', 'in',
    'is', 'of', 'on', 'or', 'table', 'the', 'to', 'with',
}

GEOMETRY_CAPABILITIES = [
    'filter', 'select', 'reproject', 'validate_geometry', 'buffer', 'clip',
    'intersect', 'spatial_join', 'export',
]
NONSPATIAL_CAPABILITIES = ['filter', 'select', 'attribute_join', 'export']


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def read_yaml(path):
    if not path.exists():
        raise FileNotFoundError(f'Required configuration file not found: {path}')
    return yaml.safe_load(path.read_text(encoding='utf-8')) or {}


def read_json(path, default=None):
    if not path.exists():
        return {} if default is None else default
    return json.loads(path.read_text(encoding='utf-8'))


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode='w', encoding='utf-8', newline='\n', delete=False, dir=path.parent,
        prefix=f'.{path.name}.', suffix='.tmp',
    ) as handle:
        handle.write(text)
        temporary_path = Path(handle.name)
    temporary_path.replace(path)


def write_json(path, value):
    atomic_write(path, json.dumps(value, indent=2, ensure_ascii=False, default=str) + '\n')


def slug_words(value):
    return [word for word in re.split(r'[^A-Za-z0-9]+', value or '') if word]


def humanise(value):
    words = slug_words(value)
    known = {
        'bgs': 'BGS', 'cso': 'CSO', 'dft': 'DfT', 'gis': 'GIS', 'gss': 'GSS',
        'hm': 'HM', 'irl': 'Ireland', 'lidar': 'LIDAR', 'nisra': 'NISRA',
        'nrs': 'NRS', 'ons': 'ONS', 'os': 'OS', 'tfgm': 'TfGM', 'uk': 'UK',
    }
    return ' '.join(known.get(word.lower(), word.capitalize()) for word in words)


def canonical_identifier(table):
    return f"{table['schema']}/{table['table']}"


def output_stem(table):
    return f"{table['schema']}__{table['table']}"


def normalised_source_profile(config, schema):
    defaults = config.get('defaults', {})
    profile = {**defaults, **config.get('schemas', {}).get(schema, {})}
    profile.setdefault('organisation', humanise(schema.removeprefix('a_')))
    profile.setdefault('product', None)
    profile.setdefault('source_url', None)
    profile.setdefault('documentation_url', None)
    profile.setdefault('themes', [])
    profile.setdefault('geographic_coverage', None)
    profile.setdefault('notes', None)
    return profile


def column_metadata(column, schema, geometry_column, dictionary, samples=None, profile=None):
    name = column['name']
    schema_exact = (
        dictionary.get('schemas', {}).get(schema, {}).get('columns', {}).get(name.lower())
    )
    exact = schema_exact or dictionary.get('columns', {}).get(name.lower())
    provenance = 'database_comment' if column.get('comment') else None
    description = column.get('comment')
    semantic_role = None

    if not description and exact:
        description = exact.get('description')
        semantic_role = exact.get('semantic_role')
        provenance = 'schema_column_dictionary' if schema_exact else 'column_dictionary'

    if not description:
        for pattern in dictionary.get('patterns', []):
            if name.lower().endswith(pattern.get('suffix', '').lower()):
                description = pattern.get('description')
                semantic_role = pattern.get('semantic_role')
                provenance = 'column_dictionary_pattern'
                break

    if name == geometry_column:
        description = description or 'Spatial geometry of the represented feature.'
        semantic_role = 'geometry'
        provenance = provenance or 'geometry_rule'

    if not description:
        description = 'Source attribute; its precise meaning has not yet been documented.'
        provenance = 'safe_fallback'

    lower_type = column.get('data_type', '').lower()
    filterable = lower_type != 'geometry'
    searchable = bool(exact.get('searchable')) if exact else False
    if not searchable and semantic_role in {'feature_name', 'alternative_name', 'description'}:
        searchable = True
    joinable = bool(exact.get('joinable')) if exact else False
    return {
        'name': name,
        'data_type': column.get('data_type'),
        'description': description,
        'semantic_role': semantic_role,
        'filterable': filterable,
        'searchable': searchable,
        'joinable': joinable,
        'identifier_system': exact.get('identifier_system') if exact else None,
        'entity_type': exact.get('entity_type') if exact else None,
        'geography_type': exact.get('geography_type') if exact else None,
        'geography_version': exact.get('geography_version') if exact else None,
        'unit': exact.get('unit') if exact else None,
        'related_column': exact.get('related_column') if exact else None,
        'measure_concept': exact.get('measure_concept') if exact else None,
        'population': exact.get('population') if exact else None,
        'statistic_type': exact.get('statistic_type') if exact else None,
        'reference_period': exact.get('reference_period') if exact else None,
        'aggregation_method': exact.get('aggregation_method') if exact else None,
        'value_profile': {
            'examples': list(samples or [])[:5],
            'null_fraction': (profile or {}).get('null_fraction'),
            'estimated_distinct': (profile or {}).get('estimated_distinct'),
            'statistics_source': (profile or {}).get('source'),
        },
        'provenance': provenance,
        'confidence': 'verified' if provenance == 'database_comment' else (
            'curated' if provenance and 'column_dictionary' in provenance else 'generated'
        ),
    }


def infer_feature_concept(table_name):
    value = re.sub(r'^(os_open_|os_|tbl_)', '', table_name.lower())
    value = re.sub(r'[^a-z0-9]+', '_', value).strip('_')
    return value or 'spatial_feature'


def infer_description(table, title, profile, feature_concept):
    if table.get('table_comment'):
        return table['table_comment'], 'database_comment', 'verified'
    organisation = profile['organisation']
    product = profile.get('product')
    geometry = table.get('geometry_type')
    subject = humanise(feature_concept).lower()
    if product:
        base = f'{title} is part of {product}, published by {organisation}.'
    else:
        base = f'{title} is an authoritative dataset published by {organisation}.'
    if geometry:
        base += f' It represents {subject} features using {humanise(geometry).lower()} geometry.'
    else:
        base += f' It contains records relating to {subject}.'
    return base, 'deterministic_template', 'generated'


def keywords_for(table, title, profile, override, columns):
    values = [title, table['schema'], table['table'], profile.get('organisation', '')]
    values.extend(profile.get('themes') or [])
    values.extend(override.get('synonyms') or [])
    values.extend(c['name'] for c in columns if c.get('semantic_role'))
    words = []
    seen = set()
    for value in values:
        for word in slug_words(str(value)):
            lower = word.lower()
            if len(lower) < 2 or lower in STOPWORDS or lower in seen:
                continue
            seen.add(lower)
            words.append(lower)
    return words[:50]


def fingerprint(table, profile, override, dictionary):
    payload = {
        'builder_version': BUILDER_VERSION,
        'table': table,
        'source': profile,
        'override': override,
        'column_dictionary_version': dictionary.get('version'),
    }
    encoded = json.dumps(payload, sort_keys=True, default=str).encode('utf-8')
    return hashlib.sha256(encoded).hexdigest()


def build_record(table, sources, overrides, dictionary):
    identifier = canonical_identifier(table)
    dotted_identifier = f"{table['schema']}.{table['table']}"
    profile = normalised_source_profile(sources, table['schema'])
    override = overrides.get('tables', {}).get(dotted_identifier, {})
    title = override.get('title') or humanise(table['table'])
    feature_concept = override.get('feature_concept') or infer_feature_concept(table['table'])
    sample_values = table.get('sample_values') or {}
    column_profiles = table.get('column_profiles') or {}
    columns = [
        column_metadata(
            column, table['schema'], table.get('geometry_column'), dictionary,
            sample_values.get(column['name'], []), column_profiles.get(column['name'], {}),
        )
        for column in table.get('columns', [])
    ]
    description, description_source, description_confidence = infer_description(
        table, title, profile, feature_concept,
    )
    geometry_type = table.get('geometry_type')
    capabilities = GEOMETRY_CAPABILITIES if geometry_type else NONSPATIAL_CAPABILITIES
    record = {
        'metadata_version': 1,
        'identifier': identifier,
        'schema': table['schema'],
        'table': table['table'],
        'title': title,
        'description': description,
        'feature_concept': feature_concept,
        'synonyms': override.get('synonyms', []),
        'publisher': {
            'organisation': profile['organisation'],
            'product': profile.get('product'),
            'source_url': profile.get('source_url'),
            'documentation_url': profile.get('documentation_url'),
            'licence_name': profile.get('licence_name'),
            'licence_url': profile.get('licence_url'),
            'attribution': profile.get('attribution'),
            'verification_status': profile.get('verification_status'),
            'licence_scope': profile.get('licence_scope'),
        },
        'themes': profile.get('themes') or [],
        'geographic_coverage': profile.get('geographic_coverage'),
        'geometry': {
            'column': table.get('geometry_column'),
            'type': geometry_type,
            'srid': table.get('srid'),
            'crs': table.get('crs'),
            'bbox_wgs84': table.get('bbox_wgs84'),
            'units': 'metres' if table.get('srid') == 27700 else None,
            'is_geographic': table.get('srid') == 4326,
        },
        'row_count': table.get('row_count'),
        'primary_key': table.get('primary_key') or [],
        'indexes': table.get('indexes') or [],
        'columns': columns,
        'capabilities': {name: True for name in capabilities},
        'operation_requirements': {
            'buffer': {
                'requires_projected_crs': True,
                'current_crs_suitable': bool(table.get('srid') and table.get('srid') != 4326),
            },
            'intersect': {'requires_matching_crs': True},
            'clip': {'requires_matching_crs': True},
            'spatial_join': {'requires_matching_crs': True},
        } if geometry_type else {},
        'discovery_hints': {
            'filterable_columns': [c['name'] for c in columns if c['filterable']],
            'searchable_columns': [c['name'] for c in columns if c['searchable']],
            'joinable_columns': [c['name'] for c in columns if c['joinable']],
            'relationship_policy': (
                'Candidate relationships must be validated against live values and '
                'presented to the user for confirmation before execution.'
            ),
        },
        'keywords': [],
        'provenance': {
            'technical_metadata': 'PostGIS',
            'publisher_metadata': 'metadata_builder/config/sources.yml',
            'description': description_source,
            'description_confidence': description_confidence,
        },
        'quality': {
            'metadata_status': 'source_mapped' if profile.get('source_url') else 'technical',
            'warnings': [],
        },
        'build': {
            'builder_version': BUILDER_VERSION,
            'generated_at': utc_now(),
        },
    }
    record['keywords'] = keywords_for(table, title, profile, override, columns)
    if not profile.get('source_url'):
        record['quality']['warnings'].append('No source URL is configured for this schema.')
    if not profile.get('licence_name'):
        record['quality']['warnings'].append('Licence has not yet been verified.')
    if profile.get('licence_scope') and 'verify' in profile['licence_scope'].lower():
        record['quality']['warnings'].append(profile['licence_scope'])
    return record, fingerprint(table, profile, override, dictionary)


def validate_record(record):
    errors = []
    for key in ('identifier', 'schema', 'table', 'title', 'description', 'publisher', 'columns'):
        if key not in record or record[key] in (None, ''):
            errors.append(f'Missing required field: {key}')
    names = [column.get('name') for column in record.get('columns', [])]
    duplicates = [name for name, count in Counter(names).items() if count > 1]
    if duplicates:
        errors.append(f'Duplicate column names: {", ".join(duplicates)}')
    geom_column = record.get('geometry', {}).get('column')
    if geom_column and geom_column not in names:
        errors.append(f'Geometry column {geom_column!r} is missing from columns')
    return errors


def markdown_for(record):
    publisher = record['publisher']
    geometry = record['geometry']
    lines = [
        f"# {record['title']}", '', '## Overview', '',
        f"- **Identifier:** `{record['identifier']}`",
        f"- **Source organisation:** {publisher['organisation']}",
    ]
    if publisher.get('product'):
        lines.append(f"- **Product:** {publisher['product']}")
    if publisher.get('source_url'):
        lines.append(f"- **Source:** {publisher['source_url']}")
    lines.extend([
        f"- **Schema:** `{record['schema']}`",
        f"- **Table:** `{record['table']}`",
        f"- **Geometry:** {geometry.get('type') or 'Non-spatial'}",
        f"- **CRS:** {geometry.get('crs') or 'Not applicable or unknown'}",
        f"- **Rows:** {record.get('row_count') if record.get('row_count') is not None else 'Unknown'}",
        f"- **Metadata status:** {record['quality']['metadata_status']}",
        '', '## Description', '', record['description'], '', '## Columns', '',
        '| Column | Data type | Meaning | Semantic role | Filter | Search | Join |',
        '|---|---|---|---|---|---|---|',
    ])
    for column in record['columns']:
        description = str(column['description']).replace('|', '\\|').replace('\n', ' ')
        lines.append(
            f"| `{column['name']}` | `{column['data_type']}` | {description} | "
            f"{column.get('semantic_role') or 'Unclassified'} | "
            f"{'Yes' if column['filterable'] else 'No'} | "
            f"{'Yes' if column['searchable'] else 'No'} | "
            f"{'Yes' if column['joinable'] else 'No'} |"
        )
    lines.extend(['', '## Supported operations', ''])
    lines.extend(f"- {name}" for name, enabled in record['capabilities'].items() if enabled)
    if record.get('operation_requirements'):
        lines.extend(['', '## Operation requirements', '',
                      '- Intersect, clip and spatial-join inputs must use matching coordinate reference systems.',
                      '- Buffer operations require a suitable projected coordinate reference system.',
                      '- Reprojection is performed on working outputs; source tables remain unchanged.'])
    if record['quality']['warnings']:
        lines.extend(['', '## Metadata warnings', ''])
        lines.extend(f"- {warning}" for warning in record['quality']['warnings'])
    lines.extend(['', '## Provenance', '',
                  'Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.', ''])
    return '\n'.join(lines)


def index_entry(record, metadata_path, markdown_path):
    important_columns = [
        {
            'name': c['name'], 'semantic_role': c.get('semantic_role'),
            'identifier_system': c.get('identifier_system'),
            'geography_type': c.get('geography_type'),
            'geography_version': c.get('geography_version'),
            'filterable': c.get('filterable'), 'searchable': c.get('searchable'),
            'joinable': c.get('joinable'), 'value_examples': c.get('value_profile', {}).get('examples', []),
        }
        for c in record['columns'] if c.get('semantic_role')
    ]
    return {
        'identifier': record['identifier'],
        'schema': record['schema'],
        'table': record['table'],
        'title': record['title'],
        'summary': record['description'],
        'publisher': record['publisher']['organisation'],
        'source_url': record['publisher'].get('source_url'),
        'themes': record['themes'],
        'feature_concept': record['feature_concept'],
        'synonyms': record['synonyms'],
        'keywords': record['keywords'],
        'geometry_type': record['geometry'].get('type'),
        'crs': record['geometry'].get('crs'),
        'geographic_coverage': record.get('geographic_coverage'),
        'important_columns': important_columns,
        'capabilities': sorted(name for name, value in record['capabilities'].items() if value),
        'metadata_status': record['quality']['metadata_status'],
        'metadata_path': metadata_path.relative_to(PROJECT_DIR).as_posix(),
        'markdown_path': markdown_path.relative_to(PROJECT_DIR).as_posix(),
    }


def persist_raw_schema(tables, errors, database, mode):
    raw = {
        'run_timestamp': utc_now(), 'mode': mode, 'database': database,
        'schema_prefix': 'a_', 'table_count': len(tables), 'tables': tables,
        'errors': errors,
    }
    write_json(RAW_SCHEMA_PATH, raw)
    return raw


def obtain_raw(args):
    if args.from_raw:
        raw = read_json(RAW_SCHEMA_PATH)
        if not raw:
            raise FileNotFoundError(f'{RAW_SCHEMA_PATH} does not exist or is empty')
        if args.schemas:
            wanted = set(args.schemas)
            raw['tables'] = [t for t in raw.get('tables', []) if t['schema'] in wanted]
            raw['errors'] = [e for e in raw.get('errors', []) if e.get('schema') in wanted]
        raw['mode'] = f"{raw.get('mode', 'unknown')}-from-raw"
        return raw
    if args.mock:
        tables, errors, database = extract_schema.extract_mock(args.schemas)
        return persist_raw_schema(tables, errors, database, 'mock')
    tables, errors, database = extract_schema.extract_live(args.schemas)
    return persist_raw_schema(tables, errors, database, 'live')


def new_failure(schema, table, stage, exc, retryable=True):
    return {
        'schema': schema, 'table': table, 'identifier': f'{schema}/{table}',
        'stage': stage, 'error_type': type(exc).__name__, 'message': str(exc),
        'retryable': retryable, 'timestamp': utc_now(),
    }


def build_report(started, finished, mode, table_results, extraction_errors, index_count):
    by_schema = defaultdict(lambda: {
        'tables_found': 0, 'successful': 0, 'built': 0, 'unchanged': 0,
        'failed': 0, 'failed_tables': [],
    })
    for result in table_results:
        stats = by_schema[result['schema']]
        stats['tables_found'] += 1
        status = result['status']
        if status in ('built', 'unchanged'):
            stats['successful'] += 1
            stats[status] += 1
        else:
            stats['failed'] += 1
            stats['failed_tables'].append(result)
    for error in extraction_errors:
        stats = by_schema[error.get('schema', 'unknown')]
        stats['tables_found'] += 1
        stats['failed'] += 1
        stats['failed_tables'].append({
            'schema': error.get('schema'), 'table': error.get('table'),
            'status': 'failed', 'stage': error.get('stage', 'extract'),
            'error_type': error.get('error_type', 'ExtractionError'),
            'message': error.get('error', 'Unknown extraction failure'),
            'retryable': True,
        })
    totals = {
        'schemas': len(by_schema),
        'tables_found': sum(v['tables_found'] for v in by_schema.values()),
        'successful': sum(v['successful'] for v in by_schema.values()),
        'built': sum(v['built'] for v in by_schema.values()),
        'unchanged': sum(v['unchanged'] for v in by_schema.values()),
        'failed': sum(v['failed'] for v in by_schema.values()),
        'agent_index_entries': index_count,
    }
    totals['success_rate'] = round(
        totals['successful'] * 100 / totals['tables_found'], 2,
    ) if totals['tables_found'] else 0.0
    return {
        'report_version': 1, 'started_at': started, 'finished_at': finished,
        'mode': mode, 'schemas': dict(sorted(by_schema.items())), 'totals': totals,
    }


def report_text(report):
    lines = ['=' * 72, 'GIS Portal - Phase One Metadata Build Report', '=' * 72,
             f"Mode:      {report['mode']}", f"Started:   {report['started_at']}",
             f"Finished:  {report['finished_at']}", '', 'Per-schema results', '-' * 72]
    for schema, stats in report['schemas'].items():
        lines.extend([
            schema,
            f"  Tables found: {stats['tables_found']}",
            f"  Successful:   {stats['successful']}",
            f"  Built:        {stats['built']}",
            f"  Unchanged:    {stats['unchanged']}",
            f"  Failed:       {stats['failed']}",
        ])
        if stats['failed_tables']:
            lines.append('  Failed tables:')
            for failure in stats['failed_tables']:
                lines.append(
                    f"    - {failure.get('table')} [{failure.get('stage')}]: "
                    f"{failure.get('message')}"
                )
        lines.append('')
    totals = report['totals']
    lines.extend(['Totals', '-' * 72,
                  f"  Schemas:              {totals['schemas']}",
                  f"  Tables found:         {totals['tables_found']}",
                  f"  Successful/current:   {totals['successful']}",
                  f"  Built this run:       {totals['built']}",
                  f"  Unchanged:            {totals['unchanged']}",
                  f"  Failed:               {totals['failed']}",
                  f"  Success rate:         {totals['success_rate']:.2f}%",
                  f"  Agent index entries:  {totals['agent_index_entries']}", '',
                  'Generated files', '-' * 72,
                  f'  {REPORT_TEXT_PATH}', f'  {REPORT_JSON_PATH}',
                  f'  {INDEX_PATH}', f'  {STATE_PATH}', '=' * 72, ''])
    return '\n'.join(lines)


def run(args):
    started = utc_now()
    sources = read_yaml(CONFIG_DIR / 'sources.yml')
    overrides = read_yaml(CONFIG_DIR / 'table_overrides.yml')
    dictionary = read_yaml(CONFIG_DIR / 'column_dictionary.yml')
    raw = obtain_raw(args)
    previous_state = {} if args.full_rebuild else read_json(STATE_PATH, {'tables': {}})
    state = previous_state if isinstance(previous_state, dict) else {'tables': {}}
    state.setdefault('tables', {})
    # A targeted or retry run must merge into the existing catalogue rather
    # than replacing unrelated successful entries.
    existing_index = read_json(INDEX_PATH, {}) if (args.schemas or args.retry_failed) else {}
    index = existing_index if isinstance(existing_index, dict) else {}
    results = []

    retry_ids = None
    if args.retry_failed:
        previous_report = read_json(REPORT_JSON_PATH, {})
        retry_ids = {
            f"{failure.get('schema')}/{failure.get('table')}"
            for stats in previous_report.get('schemas', {}).values()
            for failure in stats.get('failed_tables', [])
        }

    for table in raw.get('tables', []):
        identifier = canonical_identifier(table)
        if retry_ids is not None and identifier not in retry_ids:
            continue
        schema, table_name = table['schema'], table['table']
        stem = output_stem(table)
        metadata_path = METADATA_DIR / f'{stem}.json'
        markdown_path = TABLES_DIR / f'{stem}.md'
        try:
            record, digest = build_record(table, sources, overrides, dictionary)
            validation_errors = validate_record(record)
            if validation_errors:
                raise ValueError('; '.join(validation_errors))
            previous = state['tables'].get(identifier, {})
            unchanged = (
                not args.full_rebuild and previous.get('fingerprint') == digest
                and metadata_path.exists() and markdown_path.exists()
            )
            if unchanged:
                record = read_json(metadata_path)
                status = 'unchanged'
            else:
                write_json(metadata_path, record)
                atomic_write(markdown_path, markdown_for(record))
                status = 'built'
            index[identifier] = index_entry(record, metadata_path, markdown_path)
            state['tables'][identifier] = {
                'fingerprint': digest, 'status': 'successful',
                'last_successful_at': utc_now(), 'metadata_path': str(metadata_path),
                'markdown_path': str(markdown_path),
            }
            results.append({'schema': schema, 'table': table_name, 'status': status})
            print(f'    {status:<9} {schema}.{table_name}')
        except Exception as exc:
            failure = new_failure(schema, table_name, 'build', exc)
            state['tables'][identifier] = {
                **state['tables'].get(identifier, {}), 'status': 'failed',
                'last_failure': failure,
            }
            results.append({**failure, 'status': 'failed'})
            print(f'    FAILED    {schema}.{table_name} - {exc}', file=sys.stderr)
            if args.verbose:
                traceback.print_exc()

    state.update({'state_version': 1, 'builder_version': BUILDER_VERSION, 'updated_at': utc_now()})
    write_json(INDEX_PATH, dict(sorted(index.items())))
    write_json(STATE_PATH, state)
    finished = utc_now()
    report = build_report(
        started, finished, raw.get('mode', 'unknown'), results,
        raw.get('errors', []), len(index),
    )
    write_json(REPORT_JSON_PATH, report)
    atomic_write(REPORT_TEXT_PATH, report_text(report))
    print('\n' + report_text(report))
    return 1 if report['totals']['failed'] else 0


def parse_args():
    parser = argparse.ArgumentParser(
        description='Build deterministic, agent-ready metadata for authoritative GIS tables.',
    )
    source = parser.add_mutually_exclusive_group()
    source.add_argument('--mock', action='store_true', help='Extract and build bundled mock tables.')
    source.add_argument('--from-raw', action='store_true', help='Build from output/raw_schema.json without a DB connection.')
    parser.add_argument('--schema', action='append', dest='schemas', help='Process one schema; repeat for more.')
    parser.add_argument('--full-rebuild', action='store_true', help='Ignore fingerprints and rebuild selected tables.')
    parser.add_argument('--retry-failed', action='store_true', help='Process only tables failed in the previous report.')
    parser.add_argument('--verbose', action='store_true', help='Print tracebacks for per-table failures.')
    return parser.parse_args()


def main():
    try:
        return run(parse_args())
    except Exception as exc:
        print(f'FATAL: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
