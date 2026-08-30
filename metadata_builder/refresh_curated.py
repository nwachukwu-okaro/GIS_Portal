"""Apply curated YAML metadata to existing canonical JSON without touching DB facts."""

from __future__ import annotations

import argparse
import re
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

import build


PLACEHOLDER = 'Source attribute; its precise meaning has not yet been documented.'


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def configured_column(name, schema, table_override, dictionary):
    lower = name.lower()
    return (
        table_override.get('columns', {}).get(lower),
        dictionary.get('schemas', {}).get(schema, {}).get('columns', {}).get(lower),
        dictionary.get('columns', {}).get(lower),
    )


def apply_column(column, schema, table_override, dictionary):
    before = column.get('description')
    table_value, schema_value, common_value = configured_column(
        column['name'], schema, table_override, dictionary,
    )
    selected = table_value or schema_value or common_value
    if not selected:
        return before, before

    column['description'] = selected['description']
    for key in (
        'semantic_role', 'identifier_system', 'entity_type', 'geography_type',
        'geography_version', 'unit', 'related_column', 'measure_concept',
        'population', 'statistic_type', 'reference_period', 'aggregation_method',
    ):
        if key in selected:
            column[key] = selected[key]
    if 'searchable' in selected:
        column['searchable'] = bool(selected['searchable'])
    if 'joinable' in selected:
        column['joinable'] = bool(selected['joinable'])
    column['provenance'] = (
        'table_override' if table_value else
        'schema_column_dictionary' if schema_value else 'column_dictionary'
    )
    column['confidence'] = 'curated'
    return before, column['description']


def apply_record(record, override, dictionary):
    original = deepcopy(record)
    for key in (
        'title', 'description', 'feature_concept', 'synonyms',
        'local_dataset_version', 'official_dataset_updated',
        'official_dataset_url', 'documentation_sources',
    ):
        if key in override:
            record[key] = override[key]

    if not record.get('local_dataset_version'):
        version_match = re.search(r'(?im)^Version:\s*(\d{8})\s*$', record.get('description', ''))
        if version_match:
            raw_version = version_match.group(1)
            parsed = datetime.strptime(raw_version, '%Y%m%d')
            record['local_dataset_version'] = (
                f"{raw_version} ({parsed.day} {parsed.strftime('%B %Y')})"
            )

    changes = []
    for column in record.get('columns', []):
        before, after = apply_column(column, record['schema'], override, dictionary)
        if before != after:
            changes.append((column['name'], before, after))

    record['column_count'] = len(record.get('columns', []))
    quality = record.setdefault('quality', {})
    if 'metadata_status' in override:
        quality['metadata_status'] = override['metadata_status']
    if 'warnings' in override:
        quality['warnings'] = list(override['warnings'])
    record.setdefault('provenance', {})['description'] = (
        'table_override' if 'description' in override
        else record.get('provenance', {}).get('description')
    )
    record['provenance']['description_confidence'] = (
        'curated' if 'description' in override
        else record['provenance'].get('description_confidence')
    )
    record.setdefault('build', {})['curated_at'] = utc_now()
    record['build']['builder_version'] = build.BUILDER_VERSION
    return original, record, changes


def refresh_schema(schema):
    overrides = build.read_yaml(build.CONFIG_DIR / 'table_overrides.yml')
    dictionary = build.read_yaml(build.CONFIG_DIR / 'column_dictionary.yml')
    pattern = f'{schema}__*.json'
    results = []
    index = build.read_json(build.INDEX_PATH, {})

    for metadata_path in sorted(build.METADATA_DIR.glob(pattern)):
        record = build.read_json(metadata_path)
        dotted = f"{record['schema']}.{record['table']}"
        override = overrides.get('tables', {}).get(dotted, {})
        _, record, changes = apply_record(record, override, dictionary)
        errors = build.validate_record(record)
        if errors:
            raise ValueError(f"{record['identifier']}: {'; '.join(errors)}")
        markdown_path = build.TABLES_DIR / f'{metadata_path.stem}.md'
        build.write_json(metadata_path, record)
        build.atomic_write(markdown_path, build.markdown_for(record))
        index[record['identifier']] = build.index_entry(record, metadata_path, markdown_path)
        unresolved = [
            c['name'] for c in record.get('columns', [])
            if c.get('description') == PLACEHOLDER
        ]
        results.append({
            'identifier': record['identifier'], 'changes': changes,
            'unresolved': unresolved,
        })
        print(
            f"    refreshed {record['identifier']} - "
            f"{len(changes)} descriptions changed, {len(unresolved)} unknown"
        )

    build.write_json(build.INDEX_PATH, dict(sorted(index.items())))
    return results


def append_audit(schema, results):
    audit_path = build.OUTPUT_DIR / 'enrichment_audit.md'
    existing = audit_path.read_text(encoding='utf-8') if audit_path.exists() else (
        '# Metadata Enrichment Audit\n\n'
    )
    improved = sum(len(result['changes']) for result in results)
    unknown = sum(len(result['unresolved']) for result in results)
    lines = [
        f"## {schema} — {utc_now()}", '',
        f"- Tables processed: {len(results)}",
        f"- Column descriptions changed: {improved}",
        f"- Columns still unknown: {unknown}", '',
    ]
    for result in results:
        lines.append(f"### `{result['identifier']}`")
        lines.append('')
        if result['changes']:
            for name, before, after in result['changes']:
                lines.append(f"- `{name}`: {after}")
        else:
            lines.append('- No column-description changes required.')
        if result['unresolved']:
            lines.append(f"- Still unknown: {', '.join(f'`{name}`' for name in result['unresolved'])}")
        lines.append('')
    build.atomic_write(audit_path, existing.rstrip() + '\n\n' + '\n'.join(lines))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--schema', required=True)
    args = parser.parse_args()
    results = refresh_schema(args.schema)
    append_audit(args.schema, results)
    print(
        f"Schema summary: {args.schema}; tables={len(results)}; "
        f"columns_improved={sum(len(r['changes']) for r in results)}; "
        f"columns_unknown={sum(len(r['unresolved']) for r in results)}"
    )


if __name__ == '__main__':
    main()
