import argparse
import json
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = Path(__file__).resolve().parent / 'output'
TABLES_DIR = OUTPUT_DIR / 'tables'
INDEX_PATH = OUTPUT_DIR / 'agent_index.json'

FOOTER_RE = re.compile(r'<!--\s*agent_index_metadata:\s*(\{.*?\})\s*-->', re.DOTALL)
SECTION_RE = re.compile(r'^## (.+)$', re.MULTILINE)
H1_RE = re.compile(r'^# (.+)$', re.MULTILINE)
COLUMN_ROW_RE = re.compile(r'^\|\s*`?([A-Za-z0-9_]+)`?\s*\|', re.MULTILINE)
BULLET_RE = re.compile(r'^[-*]\s+(.*)$', re.MULTILINE)

STOPWORDS = {
    'the', 'a', 'an', 'of', 'to', 'in', 'and', 'or', 'is', 'are', 'this', 'that', 'for',
    'with', 'on', 'by', 'as', 'at', 'from', 'which', 'what', 'where', 'how', 'does', 'do',
    'be', 'was', 'were', 'it', 'its', 'their', 'each', 'per', 'into', 'used', 'use', 'via',
    'also', 'can', 'will', 'has', 'have', 'not', 'no', 'any', 'all', 'other', 'such', 'these',
    'those', 'than', 'within', 'across', 'between', 'about', 'based', 'typically', 'e.g',
    'i.e', 'dataset', 'data', 'table', 'column', 'row', 'value', 'values',
}


def _extract_footer(text):
    match = FOOTER_RE.search(text)
    if not match:
        return None
    return json.loads(match.group(1))


def _extract_section(text, heading):
    # Returns the body text between "## {heading}" and the next "## " (or end of doc).
    sections = {}
    matches = list(SECTION_RE.finditer(text))
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[m.group(1).strip().lower()] = text[start:end].strip()
    return sections.get(heading.lower())


def _fallback_identifier(md_path):
    schema, _, table = md_path.stem.partition('__')
    return {'identifier': f'{schema}/{table}', 'schema': schema, 'table': table}


def _fallback_field(text, label):
    # Handles both "**Label:** value" on one line and "**Label:**\nvalue" on the next,
    # since the LLM-authored docs use both forms inconsistently.
    m = re.search(rf'\*\*{re.escape(label)}:\*\*\s*\n*\s*([^\n]+)', text)
    return m.group(1).strip() if m else None


def _fallback_columns(text):
    columns_section = _extract_section(text, 'Columns')
    if not columns_section:
        return []
    rows = COLUMN_ROW_RE.findall(columns_section)
    # First match on each row is the column name cell; skip the "Column" header row itself.
    return [name for name in rows if name.lower() != 'column']


def _one_sentence_summary(text, title):
    description = _extract_section(text, 'Description')
    if description:
        # First sentence of the (whitespace-normalised) description paragraph.
        normalised = ' '.join(description.split())
        m = re.search(r'^(.*?[.!?])(\s|$)', normalised)
        if m:
            return m.group(1).strip()
        return normalised[:200].strip()
    return title or 'No summary available.'


def _keywords_from(description, spatial_questions_text, column_names, limit=25, max_column_keywords=12):
    words = re.findall(r"[A-Za-z][A-Za-z0-9']+", f'{description or ""} {spatial_questions_text or ""}')
    freq = {}
    for word in words:
        lw = word.lower()
        if len(lw) <= 3 or lw in STOPWORDS:
            continue
        freq[lw] = freq.get(lw, 0) + 1
    ranked = sorted(freq, key=lambda w: (-freq[w], w))

    keywords = []
    seen = set()
    # Column names first (and their snake_case parts) - precise, high-value search
    # terms for an agent doing schema lookups. Capped at max_column_keywords so that
    # wide tables (e.g. 26 columns) don't crowd out every prose-derived keyword from
    # the description / spatial questions text.
    for name in column_names:
        if len(keywords) >= max_column_keywords:
            break
        for token in [name, *name.split('_')]:
            token = token.lower()
            if token and token not in seen and len(token) > 2:
                seen.add(token)
                keywords.append(token)
                if len(keywords) >= max_column_keywords:
                    break
    for word in ranked:
        if word not in seen:
            seen.add(word)
            keywords.append(word)
        if len(keywords) >= limit:
            break
    return keywords[:limit]


def _relative_md_path(md_path):
    try:
        return str(md_path.relative_to(BASE_DIR)).replace('\\', '/')
    except ValueError:
        return str(md_path)


def build_entry(md_path):
    text = md_path.read_text(encoding='utf-8')
    footer = _extract_footer(text)

    if footer:
        identifier = footer.get('identifier')
        schema = footer.get('schema')
        table = footer.get('table')
        source_org = footer.get('source_organisation')
        official_url = footer.get('official_url')
        geometry_type = footer.get('geometry_type')
        crs = footer.get('crs')
        row_count = footer.get('row_count')
        bbox_wgs84 = footer.get('bbox_wgs84')
        columns = footer.get('columns') or _fallback_columns(text)
        status = footer.get('enrichment_status', 'unknown')
    else:
        # No footer (e.g. a hand-edited or pre-Script-3-fix .md file) - fall back to
        # best-effort parsing of the document body rather than skipping the file.
        print(f'    note    {md_path.name}: no agent_index_metadata footer, falling back to prose parsing', file=sys.stderr)
        ids = _fallback_identifier(md_path)
        identifier, schema, table = ids['identifier'], ids['schema'], ids['table']
        source_org = _fallback_field(text, 'Source organisation')
        official_url = _fallback_field(text, 'Official URL')
        geometry_type = None
        crs = _fallback_field(text, 'CRS')
        row_count = None
        bbox_wgs84 = None
        columns = _fallback_columns(text)
        # Heuristic: a complete document ends with its final section; if that section
        # heading is missing entirely, the generation likely got cut off.
        status = 'complete' if 'Recommended Spatial Operations' in text else 'truncated (heuristic)'

    title_match = H1_RE.search(text)
    title = title_match.group(1).strip() if title_match else table

    description = _extract_section(text, 'Description')
    spatial_questions = _extract_section(text, 'Spatial Questions')
    summary = _one_sentence_summary(text, title)
    keywords = _keywords_from(description, spatial_questions, columns)

    return {
        'identifier': identifier,
        'schema': schema,
        'table': table,
        'title': title,
        'source_organisation': source_org,
        'official_url': official_url,
        'geometry_type': geometry_type,
        'crs': crs,
        'row_count': row_count,
        'bbox_wgs84': bbox_wgs84,
        'columns': columns,
        'keywords': keywords,
        'summary': summary,
        'md_path': _relative_md_path(md_path),
        'status': status,
    }


def build_index():
    if not TABLES_DIR.exists():
        print(f'{TABLES_DIR} does not exist - run enrich_metadata.py first.', file=sys.stderr)
        sys.exit(1)

    md_files = sorted(TABLES_DIR.glob('*.md'))
    if not md_files:
        print(f'No .md files found in {TABLES_DIR} - run enrich_metadata.py first.', file=sys.stderr)
        sys.exit(1)

    index = {}
    succeeded, failed = [], []

    for i, md_path in enumerate(md_files, 1):
        print(f'[{i}/{len(md_files)}] {md_path.name}')
        try:
            entry = build_entry(md_path)
            index[entry['identifier']] = entry
            print(f"    ok      {entry['identifier']}  ({len(entry['columns'])} columns, {len(entry['keywords'])} keywords, status={entry['status']})")
            succeeded.append(entry['identifier'])
        except Exception as exc:
            print(f'    FAILED  {md_path.name} - {exc}', file=sys.stderr)
            failed.append({'file': md_path.name, 'error': str(exc)})

    return index, succeeded, failed


def main():
    parser = argparse.ArgumentParser(description='Build a searchable agent index from enriched table markdown files.')
    parser.add_argument(
        '--mock',
        action='store_true',
        help='Accepted for symmetry with the other scripts; this script always reads whatever .md files exist in output/tables/.',
    )
    args = parser.parse_args()
    if args.mock:
        print('--mock has no effect here: indexing whatever .md files already exist in output/tables/.')

    index, succeeded, failed = build_index()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(index, indent=2, default=str), encoding='utf-8')

    print(f'\nWrote {len(index)} entr{"y" if len(index) == 1 else "ies"} to {INDEX_PATH}')
    if failed:
        print(f'{len(failed)} file(s) failed indexing:')
        for f in failed:
            print(f"  FAILED  {f['file']} - {f['error']}")


if __name__ == '__main__':
    main()
