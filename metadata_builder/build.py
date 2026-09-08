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

PLACEHOLDER_COLUMN_DESCRIPTION = 'Source attribute; its precise meaning has not yet been documented.'

# Geometry types with no meaningful spatial resolution/scale, per Task 6.
POINT_GEOMETRY_TYPES = {'POINT', 'MULTIPOINT'}


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def parse_human_date(value):
    """
    table_overrides.yml stores 'official_dataset_updated' as a human-readable
    string (e.g. '28 August 2026'), used as-is elsewhere for Markdown display.
    UK GEMINI2's Dataset Reference Date needs ISO 8601, so this converts it -
    returning None (not the raw string) when the format can't be parsed,
    rather than writing a value that would fail metadata_record.schema.json.
    """
    if not value:
        return None
    try:
        return datetime.strptime(str(value).strip(), '%d %B %Y').strftime('%Y-%m-%d')
    except ValueError:
        return None


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


def column_metadata(
    column, schema, geometry_column, dictionary, samples=None, profile=None,
    table_override=None,
):
    name = column['name']
    table_exact = (table_override or {}).get(name.lower())
    schema_exact = (
        dictionary.get('schemas', {}).get(schema, {}).get('columns', {}).get(name.lower())
    )
    exact = table_exact or schema_exact or dictionary.get('columns', {}).get(name.lower())
    provenance = 'table_override' if table_exact else (
        'database_comment' if column.get('comment') else None
    )
    description = table_exact.get('description') if table_exact else column.get('comment')
    semantic_role = table_exact.get('semantic_role') if table_exact else None

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
        description = PLACEHOLDER_COLUMN_DESCRIPTION
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
            'curated' if provenance and (
                'column_dictionary' in provenance or provenance == 'table_override'
            ) else 'generated'
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
            override.get('columns', {}),
        )
        for column in table.get('columns', [])
    ]
    if override.get('description'):
        description = override['description']
        description_source = 'table_override'
        description_confidence = 'curated'
    else:
        description, description_source, description_confidence = infer_description(
            table, title, profile, feature_concept,
        )
    geometry_type = table.get('geometry_type')
    capabilities = GEOMETRY_CAPABILITIES if geometry_type else NONSPATIAL_CAPABILITIES

    # UK GEMINI2 element 26 (Use Constraints) - derived from the same licence
    # fields already resolved into 'publisher', not a separate sources.yml key.
    licence_name = profile.get('licence_name')
    licence_url = profile.get('licence_url')
    if licence_name and licence_url:
        use_constraints = f'{licence_name} — {licence_url}'
    else:
        use_constraints = licence_name or licence_url or None

    # UK GEMINI2 element 8 (Dataset Reference Date). Uses the curated
    # 'official_dataset_updated' table_overrides.yml value (a revision date
    # from the source organisation) when one exists. Deliberately NOT
    # defaulted to today's build date when absent - that would be Systra's
    # rebuild time, not the resource's own reference date, and this codebase
    # marks unknown information as unknown rather than inventing it (see
    # metadata_builder/README.md). Left null and flagged for manual entry
    # (table_overrides.yml) instead.
    official_updated = parse_human_date(override.get('official_dataset_updated'))
    dataset_reference_date = (
        {'date': official_updated, 'date_type': 'revision'} if official_updated else None
    )

    record = {
        'metadata_version': 1,
        'identifier': identifier,
        'schema': table['schema'],
        'table': table['table'],
        'title': title,
        'description': description,
        'local_dataset_version': override.get('local_dataset_version'),
        'official_dataset_updated': override.get('official_dataset_updated'),
        'official_dataset_url': override.get('official_dataset_url'),
        'documentation_sources': override.get('documentation_sources', []),
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
        'column_count': len(columns),
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

        # UK GEMINI2 fields (see metadata_builder/config/metadata_record.schema.json).
        # topic_category, lineage, dataset_language, metadata_language,
        # metadata_point_of_contact and conformity come straight from
        # sources.yml via 'profile'; temporal_extent comes from extract_schema.py's
        # auto-detection; use_constraints and dataset_reference_date are derived
        # above. limitations_on_public_access and frequency_of_update are read
        # from 'profile' too, but sources.yml does not currently set either
        # default for any schema, so both are null until sources.yml is
        # extended or a table_overrides.yml entry supplies them.
        'topic_category': profile.get('topic_category'),
        'temporal_extent': table.get('temporal_extent'),
        'dataset_reference_date': dataset_reference_date,
        'lineage': profile.get('lineage'),
        'dataset_language': profile.get('dataset_language'),
        'metadata_language': profile.get('metadata_language'),
        'metadata_point_of_contact': profile.get('metadata_point_of_contact'),
        'use_constraints': use_constraints,
        'limitations_on_public_access': profile.get('limitations_on_public_access'),
        'frequency_of_update': profile.get('frequency_of_update'),
        'conformity': profile.get('conformity'),
        # Curated per table (not per schema, unlike the fields above) in
        # table_overrides.yml, from confirmed official documentation only -
        # see metadata_record.schema.json. Most tables have neither: only
        # add an entry when a source's own documentation states one.
        'spatial_resolution': override.get('spatial_resolution'),
        'equivalent_scale': override.get('equivalent_scale'),
    }
    record['keywords'] = keywords_for(table, title, profile, override, columns)
    if not profile.get('source_url'):
        record['quality']['warnings'].append('No source URL is configured for this schema.')
    if not profile.get('licence_name'):
        record['quality']['warnings'].append('Licence has not yet been verified.')
    if profile.get('licence_scope') and 'verify' in profile['licence_scope'].lower():
        record['quality']['warnings'].append(profile['licence_scope'])
    if override.get('metadata_status'):
        record['quality']['metadata_status'] = override['metadata_status']
    if override.get('warnings') is not None:
        record['quality']['warnings'] = list(override['warnings'])
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


def _present(value):
    """True when value is neither None, an empty string, nor an empty list/dict."""
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return True


def gemini_compliance(record):
    """
    Scores a built record against UK GEMINI2 Tier 1/2/3 requirements (see
    Task 6). Returns (gemini_tier, missing_mandatory_fields):
      - gemini_tier: 3, 2, 1, or 0 for below Tier 1.
      - missing_mandatory_fields: the union of every unmet check across all
        three tiers (not just whichever tier is currently blocking), so it
        doubles as a full to-do list toward Tier 3, not just the next tier up.
    """
    publisher = record.get('publisher') or {}
    missing = []

    # Tier 1 (minimum). 'abstract' maps to record['description'] - this
    # codebase's own name for the same concept; there is no separate
    # 'abstract' field. 'access_constraints' accepts either
    # limitations_on_public_access or publisher.licence_name, per spec.
    tier1_checks = [
        ('title', _present(record.get('title'))),
        ('abstract', _present(record.get('description'))),
        ('keywords', len(record.get('keywords') or []) >= 3),
        ('responsible_organisation', _present(publisher.get('organisation'))),
        ('access_constraints', (
            _present(record.get('limitations_on_public_access'))
            or _present(publisher.get('licence_name'))
        )),
        ('licence_name', _present(publisher.get('licence_name'))),
        ('source_url', _present(publisher.get('source_url'))),
    ]
    missing.extend(name for name, ok in tier1_checks if not ok)
    tier1_ok = all(ok for _name, ok in tier1_checks)

    # Tier 2 (GEMINI compliant).
    tier2_checks = [
        ('topic_category', _present(record.get('topic_category'))),
        ('temporal_extent', _present(record.get('temporal_extent'))),
        ('dataset_reference_date', _present(record.get('dataset_reference_date'))),
        ('lineage', _present(record.get('lineage'))),
        ('use_constraints', _present(record.get('use_constraints'))),
        ('metadata_point_of_contact', _present(record.get('metadata_point_of_contact'))),
        ('conformity', _present(record.get('conformity'))),
    ]
    missing.extend(name for name, ok in tier2_checks if not ok)
    tier2_ok = tier1_ok and all(ok for _name, ok in tier2_checks)

    # Tier 3 (full quality). Spatial resolution / equivalent scale is skipped
    # for point geometries (per spec) and, by the same "no meaningful
    # resolution" reasoning, for tables with no geometry at all.
    no_placeholder_columns = not any(
        c.get('description') == PLACEHOLDER_COLUMN_DESCRIPTION for c in record.get('columns', [])
    )
    frequency_ok = _present(record.get('frequency_of_update'))
    geometry_type = (record.get('geometry', {}).get('type') or '').upper()
    resolution_applicable = bool(geometry_type) and geometry_type not in POINT_GEOMETRY_TYPES
    resolution_ok = (
        not resolution_applicable
        or _present(record.get('spatial_resolution'))
        or _present(record.get('equivalent_scale'))
    )
    if not no_placeholder_columns:
        missing.append('column_descriptions')
    if not frequency_ok:
        missing.append('frequency_of_update')
    if not resolution_ok:
        missing.append('spatial_resolution_or_equivalent_scale')
    tier3_ok = tier2_ok and no_placeholder_columns and frequency_ok and resolution_ok

    if tier3_ok:
        tier = 3
    elif tier2_ok:
        tier = 2
    elif tier1_ok:
        tier = 1
    else:
        # Not an integer 0 - metadata_record.schema.json's gemini_tier enum
        # is [1, 2, 3, null]; null means "does not meet even Tier 1".
        tier = None

    return tier, missing


def clean_record_for_output(record):
    """
    Trims the full internal record (built by build_record()) down to the
    {gemini, columns} shape written to output/metadata/*.json - the public/
    agent-facing contract. The full internal record - with 'publisher',
    'geometry', 'capabilities', 'quality', etc. - keeps being used for
    markdown_for(), index_entry() and gemini_compliance(); only the file
    written to disk is trimmed.

    'schema' and 'table' are kept inside 'gemini' even though they aren't
    part of the primary GEMINI field list, since a per-table record without
    them would be hard to identify at a glance; 'row_count'/'column_count'
    are dropped entirely rather than kept in some other subsection, since
    neither is in the GEMINI field list either.
    """
    publisher = record.get('publisher') or {}
    geometry = record.get('geometry') or {}
    dataset_reference_date = record.get('dataset_reference_date') or {}

    gemini = {
        'title': record.get('title'),
        'abstract': record.get('description'),
        'alternative_title': record.get('alternative_title'),
        'topic_category': record.get('topic_category'),
        'keywords': record.get('keywords') or [],
        'temporal_extent': record.get('temporal_extent'),
        'dataset_reference_date': dataset_reference_date.get('date'),
        'dataset_reference_date_type': dataset_reference_date.get('date_type'),
        'lineage': record.get('lineage'),
        'responsible_organisation': publisher.get('organisation'),
        'resource_locator': publisher.get('source_url'),
        'unique_identifier': record.get('identifier'),
        'schema': record.get('schema'),
        'table': record.get('table'),
        'bounding_box': geometry.get('bbox_wgs84'),
        'spatial_reference_system': geometry.get('crs'),
        'limitations_on_public_access': record.get('limitations_on_public_access'),
        'use_constraints': record.get('use_constraints'),
        'spatial_resolution': record.get('spatial_resolution'),
        'equivalent_scale': record.get('equivalent_scale'),
        'conformity': record.get('conformity'),
        'metadata_language': record.get('metadata_language'),
        'dataset_language': record.get('dataset_language'),
        'metadata_point_of_contact': record.get('metadata_point_of_contact'),
        'frequency_of_update': record.get('frequency_of_update'),
        'gemini_tier': record.get('gemini_tier'),
        'missing_mandatory_fields': record.get('missing_mandatory_fields') or [],
    }

    columns = []
    for column in record.get('columns', []):
        description = column.get('description')
        if not description or description == PLACEHOLDER_COLUMN_DESCRIPTION:
            description = None
        columns.append({
            'name': column.get('name'),
            'type': column.get('data_type'),
            'description': description,
        })

    return {'gemini': gemini, 'columns': columns}


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
    if record.get('official_dataset_url'):
        lines.append(f"- **Official dataset page:** {record['official_dataset_url']}")
    for source in record.get('documentation_sources', []):
        if source.get('role') == 'documentation':
            lines.append(f"- **Official documentation:** {source['url']}")
            break
    if record.get('local_dataset_version'):
        lines.append(f"- **Local dataset version:** {record['local_dataset_version']}")
    if record.get('official_dataset_updated'):
        lines.append(f"- **Official dataset last updated:** {record['official_dataset_updated']}")
    if publisher.get('licence_name'):
        licence = publisher['licence_name']
        if publisher.get('licence_url'):
            licence = f"[{licence}]({publisher['licence_url']})"
        lines.append(f"- **Licence:** {licence}")
    if record.get('geographic_coverage'):
        lines.append(f"- **Geographic coverage:** {record['geographic_coverage']}")
    bbox = geometry.get('bbox_wgs84') or {}
    if all(key in bbox for key in ('xmin', 'ymin', 'xmax', 'ymax')):
        lines.append(
            "- **WGS84 extent:** "
            f"`[{bbox['xmin']:.6f}, {bbox['ymin']:.6f}, "
            f"{bbox['xmax']:.6f}, {bbox['ymax']:.6f}]`"
        )
    # UK GEMINI2 fields (Tasks 1-6) - each shown only when present and not
    # null, per Task 3.
    if record.get('topic_category'):
        lines.append(f"- **Topic category:** {record['topic_category']}")
    temporal_extent = record.get('temporal_extent') or {}
    if temporal_extent.get('begin') or temporal_extent.get('end'):
        lines.append(
            "- **Temporal extent:** "
            f"{temporal_extent.get('begin') or '?'} to {temporal_extent.get('end') or '?'}"
        )
    dataset_reference_date = record.get('dataset_reference_date') or {}
    if dataset_reference_date.get('date'):
        lines.append(
            f"- **Dataset reference date:** {dataset_reference_date['date']} "
            f"({dataset_reference_date.get('date_type', 'unspecified')})"
        )
    if record.get('dataset_language'):
        lines.append(f"- **Dataset language:** {record['dataset_language']}")
    if record.get('metadata_language'):
        lines.append(f"- **Metadata language:** {record['metadata_language']}")
    if record.get('use_constraints'):
        lines.append(f"- **Use constraints:** {record['use_constraints']}")
    if record.get('limitations_on_public_access'):
        lines.append(f"- **Limitations on public access:** {record['limitations_on_public_access']}")
    if record.get('frequency_of_update'):
        lines.append(f"- **Frequency of update:** {record['frequency_of_update']}")
    if record.get('spatial_resolution'):
        lines.append(f"- **Spatial resolution:** {record['spatial_resolution']}")
    if record.get('equivalent_scale'):
        lines.append(f"- **Equivalent scale:** {record['equivalent_scale']}")
    if record.get('conformity'):
        lines.append(f"- **Conformity:** {record['conformity']}")
    if record.get('gemini_tier'):
        lines.append(f"- **UK GEMINI2 compliance tier:** {record['gemini_tier']}")
    if record.get('missing_mandatory_fields'):
        lines.append(
            f"- **Missing for full compliance:** {', '.join(record['missing_mandatory_fields'])}"
        )
    lines.extend([
        f"- **Schema:** `{record['schema']}`",
        f"- **Table:** `{record['table']}`",
        f"- **Geometry:** {geometry.get('type') or 'Non-spatial'}",
        f"- **CRS:** {geometry.get('crs') or 'Not applicable or unknown'}",
        f"- **Rows:** {record.get('row_count') if record.get('row_count') is not None else 'Unknown'}",
        f"- **Columns:** {record.get('column_count', len(record['columns']))}",
        f"- **Metadata status:** {record['quality']['metadata_status']}",
        '', '## Description', '', record['description'], '',
    ])
    if record.get('lineage'):
        lines.extend(['## Lineage', '', record['lineage'], ''])
    contact = record.get('metadata_point_of_contact') or {}
    if contact.get('organisation') or contact.get('email') or contact.get('role'):
        lines.extend(['## Metadata point of contact', ''])
        if contact.get('organisation'):
            lines.append(f"- **Organisation:** {contact['organisation']}")
        if contact.get('email'):
            lines.append(f"- **Email:** {contact['email']}")
        if contact.get('role'):
            lines.append(f"- **Role:** {contact['role']}")
        lines.append('')
    lines.extend([
        '## Columns', '',
        '| Column | Type | Description |',
        '|---|---|---|',
    ])
    for column in record['columns']:
        description = column.get('description')
        if not description or description == PLACEHOLDER_COLUMN_DESCRIPTION:
            description = ''
        else:
            description = str(description).replace('|', '\\|').replace('\n', ' ')
        lines.append(f"| `{column['name']}` | `{column['data_type']}` | {description} |")
    lines.append('')
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


def compliance_summary_text(compliance_counts):
    tier3 = compliance_counts.get(3, 0)
    tier2 = compliance_counts.get(2, 0)
    tier1 = compliance_counts.get(1, 0)
    below = compliance_counts.get(None, 0)
    total = tier3 + tier2 + tier1 + below
    return (
        '═══════════════════════════════════════════\n'
        ' UK GEMINI 2.2 Compliance Summary\n'
        '═══════════════════════════════════════════\n'
        f' Tier 3 — Full quality:         {tier3:>3} tables\n'
        f' Tier 2 — GEMINI compliant:     {tier2:>3} tables\n'
        f' Tier 1 — Minimum only:         {tier1:>3} tables\n'
        f' Below Tier 1 — Non-compliant:  {below:>3} tables\n'
        ' ───────────────────────────────────────────\n'
        f' Total:                         {total:>3} tables\n'
        '═══════════════════════════════════════════'
    )


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
    # WARNING: running without --schema replaces agent_index.json entirely.
    # Always use --schema for mock/dev testing to avoid overwriting
    # the production index. Restore with: git checkout metadata_builder/output/agent_index.json
    existing_index = read_json(INDEX_PATH, {}) if (args.schemas or args.retry_failed) else {}
    index = existing_index if isinstance(existing_index, dict) else {}
    results = []
    compliance_counts = Counter()

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
            gemini_tier, missing_mandatory_fields = gemini_compliance(record)
            record['gemini_tier'] = gemini_tier
            record['missing_mandatory_fields'] = missing_mandatory_fields
            previous = state['tables'].get(identifier, {})
            unchanged = (
                not args.full_rebuild and previous.get('fingerprint') == digest
                and metadata_path.exists() and markdown_path.exists()
            )
            if unchanged:
                # Not re-read from metadata_path: the file on disk only holds
                # the trimmed {gemini, columns} output (clean_record_for_output()),
                # not the full record that index_entry()/markdown_for() need.
                # build_record() is deterministic for identical inputs - which
                # is the whole premise fingerprinting relies on - so the record
                # already built above is equivalent to what's on disk; only the
                # write is skipped, not the computation.
                status = 'unchanged'
            else:
                write_json(metadata_path, clean_record_for_output(record))
                atomic_write(markdown_path, markdown_for(record))
                status = 'built'
            compliance_counts[gemini_tier] += 1
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
    summary = compliance_summary_text(compliance_counts)
    print(summary)
    atomic_write(OUTPUT_DIR / 'gemini_compliance_summary.txt', summary + '\n')
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
    # The compliance summary uses box-drawing/em-dash characters (Task 6).
    # Some terminals (e.g. Windows consoles on a legacy codepage) can't
    # encode them and raise UnicodeEncodeError on print(), which would
    # otherwise abort the whole run right at the final summary. Not needed
    # on Linux production (UTF-8 locale by default), but harmless there too.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            try:
                stream.reconfigure(encoding='utf-8')
            except (ValueError, OSError):
                pass
    try:
        return run(parse_args())
    except Exception as exc:
        print(f'FATAL: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
