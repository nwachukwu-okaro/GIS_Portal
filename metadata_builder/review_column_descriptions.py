"""Apply conservative column rules to existing local JSON/Markdown only.

Run without --apply for a preview. Audit keeps every replaced description.
No APIs, database connections, ingestion, commits or paid services are used.
"""
import argparse
from collections import Counter
import json
from pathlib import Path

from contextual_columns import enrich_record

ROOT = Path(__file__).resolve().parent


def update_markdown(text, columns):
    by_name = {c['name']: c.get('description') or '' for c in columns}
    lines = text.splitlines(keepends=True)
    in_columns = False
    for i, line in enumerate(lines):
        if line.startswith('## '):
            in_columns = line.strip() == '## Columns'
        if in_columns and line.startswith('| `'):
            name = line.split('`', 2)[1]
            if name in by_name:
                # Preserve column name/type and all other document sections.
                parts = line.split('|', 3)
                if len(parts) == 4:
                    desc = by_name[name].replace('|', '\\|').replace('\n', ' ')
                    lines[i] = '|'.join(parts[:3]) + f'| {desc} |\n'
    return ''.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--pass-number', type=int, choices=[1, 2], default=2)
    args = parser.parse_args()
    suffix = '' if args.pass_number == 1 else '_pass2'
    audit = ROOT / f'output/column_description_review{suffix}.json'
    if args.apply and audit.exists():
        raise RuntimeError('Audit already exists; preserve it before another apply run. Preview remains available.')
    totals = Counter()
    changes = []
    for path in sorted((ROOT / 'output/metadata').glob('*.json')):
        record = json.loads(path.read_text(encoding='utf-8'))
        totals['tables_scanned'] += 1
        totals['columns_scanned'] += len(record.get('columns', []))
        changed = enrich_record(record)
        totals['remaining_empty'] += sum(not c.get('description') for c in record.get('columns', []))
        for c in record.get('columns', []):
            if c.get('description_review'):
                totals[f"final_{c['provenance']}_{c['confidence']}"] += 1
        if not changed:
            continue
        totals['tables_changed'] += 1
        totals['columns_reviewed'] += len(changed)
        for entry in changed:
            totals[entry['basis']] += 1
            changes.append({'identifier': record['identifier'], **entry})
        if args.apply:
            path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            markdown = ROOT / 'output/tables' / (path.stem + '.md')
            if markdown.exists():
                text = markdown.read_text(encoding='utf-8')
                updated = update_markdown(text, record['columns'])
                if text != updated:
                    markdown.write_text(updated, encoding='utf-8')
    totals['descriptions_added_or_improved'] = sum(bool(c['after']) and c['before'] != c['after'] for c in changes)
    totals['boilerplate_cleared'] = sum(bool(c['before']) and not c['after'] for c in changes)
    print(json.dumps(totals, indent=2))
    if args.apply and changes:
        audit.write_text(json.dumps({'summary': dict(totals), 'changes': changes}, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        report = [f'# Column description review — pass {args.pass_number}', '',
                  'Specific existing descriptions were preserved, not independently reverified.',
                  'Only blank descriptions and recognized generic boilerplate were reconsidered.',
                  'No production data, table descriptions, licences, types or column order were changed.', '',
                  '## Summary', '']
        report += [f'- {key}: {value}' for key, value in totals.items()]
        report += ['', '## Sources', '',
                   '- https://www.gov.uk/government/publications/open-standards-for-government/identifying-property-and-street-information',
                   '- https://docs.os.uk/os-downloads/products/addresses-and-names-portfolio/addressbase-fundamentals/code-lists-and-enumerations/logicalstatuscode',
                   '- Local exported primary keys, geometry declarations, names and sample values.', '',
                   'The JSON audit retains every previous description and the basis for each replacement.',
                   'Unknown abbreviations, unnamed fields and ambiguous census measures remain empty.', '']
        (ROOT / f'output/column_description_review{suffix}.md').write_text('\n'.join(report), encoding='utf-8')


if __name__ == '__main__':
    main()
