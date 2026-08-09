import argparse
import json
import os
import sys
import time
from pathlib import Path

import anthropic
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = Path(__file__).resolve().parent / 'output'
RAW_SCHEMA_PATH = OUTPUT_DIR / 'raw_schema.json'
TABLES_DIR = OUTPUT_DIR / 'tables'

# override=True: this sandboxed dev environment pre-defines ANTHROPIC_API_KEY as an
# empty string, and load_dotenv()'s default (override=False) would leave that empty
# value in place instead of picking up the real key from .env.
load_dotenv(BASE_DIR / '.env', override=True)

ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
MODEL = 'claude-sonnet-4-6'
# Wide tables (e.g. the 26-column BGS bedrock geology table) need more headroom for a
# complete per-column table than narrow ones - 2000 tokens was truncating them mid-document.
MAX_TOKENS_DEFAULT = 2000
MAX_TOKENS_WIDE = 4000
WIDE_TABLE_COLUMN_THRESHOLD = 20
API_DELAY_SECONDS = 1
WEB_SEARCH_MAX_USES = 5
MAX_PAUSE_TURN_RETRIES = 5

# Schema naming convention -> source organisation, as supplied for the GIS Portal project.
SOURCE_ORG_MAP = {
    'a_british_geological_survey': 'British Geological Survey (BGS)',
    'a_historic_england': 'Historic England',
    'a_os_built_up_areas': 'Ordnance Survey',
    'a_os_boundaryline': 'Ordnance Survey',
    'a_os_open_data': 'Ordnance Survey',
    'a_os_zoomstack': 'Ordnance Survey',
    'a_os_addressbase_core': 'Ordnance Survey',
    'a_os_addressbase_premium': 'Ordnance Survey',
    'a_os_open_greenspace': 'Ordnance Survey',
    'a_os_open_map_local': 'Ordnance Survey',
    'a_os_open_names': 'Ordnance Survey',
    'a_os_open_rivers': 'Ordnance Survey',
    'a_os_open_roads': 'Ordnance Survey',
    'a_os_open_terrain_50': 'Ordnance Survey',
    'a_os_codepoint': 'Ordnance Survey',
    'a_os_codepoint_polygon': 'Ordnance Survey',
    'a_environment_agency': 'Environment Agency',
    'a_natural_england': 'Natural England',
    'a_national_highways': 'National Highways',
    'a_network_rail': 'Network Rail',
    'a_ons_england_wales': 'Office for National Statistics',
    'a_ons_nrs_nirsa_census_data': 'Office for National Statistics',
    'a_hm_land_registry': 'HM Land Registry',
    'a_open_street_map': 'OpenStreetMap',
    'a_overture_maps': 'Overture Maps Foundation',
    'a_forestry_commission': 'Forestry Commission',
    'a_sport_england': 'Sport England',
    'a_sustrans': 'Sustrans',
    'a_national_lidar_programme': 'Defra / Environment Agency National LIDAR Programme',
    'a_department_for_education': 'Department for Education',
    'a_dft': 'Department for Transport',
    'a_greater_manchester_ecology_unit': 'Greater Manchester Ecology Unit',
    'a_tfgm': 'Transport for Greater Manchester',
    'a_oxfordshire_county_council': 'Oxfordshire County Council',
    'a_verisk_sample': 'Verisk',
    'a_ireland_cso': 'Central Statistics Office Ireland',
    'a_irishrail': 'Irish Rail',
    'a_irl_geological_survey': 'Geological Survey Ireland',
    'a_npws_ireland': 'National Parks and Wildlife Service Ireland',
    'a_nisra_nireland': 'NISRA Northern Ireland',
    'a_nrs_scotland': 'National Records of Scotland',
}

SYSTEM_PROMPT = """You are a GIS metadata specialist writing documentation for a spatial data catalogue used by \
planners, engineers and GIS analysts at an infrastructure consultancy.

For the dataset described in the user message, use the web_search tool to find its official documentation page, \
then write a single markdown document with exactly these sections, in this order:

# <Official dataset name>

## Overview
- **Source organisation:**
- **Official URL:** (the page you found via web search; write "Not found" if you could not find one - never \
invent a URL)
- **Licence:**
- **CRS:**
- **Scale / resolution:**
- **Geographic coverage:**
- **Version:** (if stated on the source page, else "Not stated")

## Citation
A formal citation for this dataset in a standard format.

## Description
A plain-English paragraph describing what the dataset contains and what it is typically used for.

## Columns
A markdown table with columns: `Column | Data Type | Meaning`. Include EVERY column supplied in the user \
message, in the order given - do not omit, merge, or summarise columns, even for tables with many columns.

## Spatial Questions
A bulleted list of spatial questions this dataset can help answer.

## Recommended Spatial Operations
A bulleted list of typical spatial operations (e.g. buffer, intersect, clip, spatial join, filter) used with \
this dataset, each with a one-line reason.

Ground factual claims (licence, CRS, coverage, official name, version) in what you find via web search rather \
than guessing. If you cannot verify a fact, write "Not stated" rather than inventing a value. Output only the \
markdown document itself - no preamble or commentary before or after it."""


def get_source_org(schema):
    if schema in SOURCE_ORG_MAP:
        return SOURCE_ORG_MAP[schema]
    if schema.startswith('a_irl_'):
        return 'Irish public bodies (CSO, EPA, OPW, local councils)'
    # Not in the supplied naming-convention list - best-effort guess, flagged as such
    # rather than silently presented as a confirmed mapping.
    guess = schema.removeprefix('a_').replace('_', ' ').title()
    return f'{guess} (unmapped schema - not in the supplied naming convention list)'


def _is_api_unconfigured():
    return not ANTHROPIC_API_KEY or ANTHROPIC_API_KEY == 'YOUR_ANTHROPIC_API_KEY'


def _build_user_prompt(table):
    schema, tbl = table['schema'], table['table']
    columns = table.get('columns', [])
    column_lines = '\n'.join(f"- {c['name']} ({c['data_type']})" for c in columns)

    sample_values = table.get('sample_values') or {}
    sample_lines = '\n'.join(
        f"- {col}: {', '.join(str(v) for v in vals)}" for col, vals in sample_values.items() if vals
    )

    return f"""Dataset to document:
- Schema: {schema}
- Table: {tbl}
- Likely source organisation (from internal naming convention): {get_source_org(schema)}
- Geometry type: {table.get('geometry_type') or 'n/a'}
- CRS: {table.get('crs') or 'n/a'}
- Row count: {table.get('row_count')}
- WGS84 bounding box: {table.get('bbox_wgs84')}
- Existing PostgreSQL table comment: {table.get('table_comment') or '(none)'}

Full column list ({len(columns)} columns total - the Columns table in your output must cover all {len(columns)}):
{column_lines}

Sample values captured from the database (if any):
{sample_lines or '(no sample values captured)'}

Search the web for this dataset's official documentation page from {get_source_org(schema)} (or the relevant \
government/open-data portal) and ground the metadata document in what you find. If you cannot find an official \
page, say so explicitly in the Official URL field rather than guessing one."""


def _max_tokens_for(table):
    return MAX_TOKENS_WIDE if len(table.get('columns', [])) > WIDE_TABLE_COLUMN_THRESHOLD else MAX_TOKENS_DEFAULT


def _call_claude(client, user_prompt, max_tokens):
    tools = [{'type': 'web_search_20260209', 'name': 'web_search', 'max_uses': WEB_SEARCH_MAX_USES}]
    system = [{'type': 'text', 'text': SYSTEM_PROMPT, 'cache_control': {'type': 'ephemeral'}}]
    messages = [{'role': 'user', 'content': user_prompt}]

    response = client.messages.create(model=MODEL, max_tokens=max_tokens, system=system, tools=tools, messages=messages)

    retries = 0
    while response.stop_reason == 'pause_turn' and retries < MAX_PAUSE_TURN_RETRIES:
        messages.append({'role': 'assistant', 'content': response.content})
        response = client.messages.create(model=MODEL, max_tokens=max_tokens, system=system, tools=tools, messages=messages)
        retries += 1

    return response


def _extract_text(response):
    # Claude interleaves short "thinking out loud" text blocks between web_search
    # tool calls (e.g. "Let me search for..."), followed by the actual markdown
    # document as the final text block(s) once tool use is done. Only keep the
    # trailing run of text blocks - i.e. everything after the last tool-related
    # block - so that intermediate commentary doesn't leak into the .md file.
    content = response.content
    last_tool_idx = -1
    for i, block in enumerate(content):
        if getattr(block, 'type', None) != 'text':
            last_tool_idx = i
    trailing = [block.text for block in content[last_tool_idx + 1:] if getattr(block, 'type', None) == 'text']
    text = '\n'.join(trailing).strip()

    # Belt-and-braces: even within that trailing run, Claude sometimes prefixes a
    # one-line intro ("Here is the completed document:") and/or a "---" divider
    # before the real content. The document always starts with an H1 title, so
    # jump to the first "# " line and drop anything before it.
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith('# '):
            return '\n'.join(lines[i:]).strip()
    return text


def _collect_urls(obj):
    # Walk the response structure looking for any "url" field, rather than pinning to
    # one exact citation/tool-result shape - keeps this robust to SDK/content-block
    # variations between web_search tool versions.
    urls = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'url' and isinstance(value, str):
                urls.append(value)
            else:
                urls.extend(_collect_urls(value))
    elif isinstance(obj, list):
        for item in obj:
            urls.extend(_collect_urls(item))
    return urls


def _dedupe(items):
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def _build_footer(table, official_url, response, max_tokens):
    # Structured, machine-readable footer appended to each .md file as an HTML comment
    # (invisible when the markdown is rendered). build_index.py (Script 3) reads this
    # instead of regex-parsing the AI-written prose for fields like geometry type, row
    # count and bounding box, which never appear in the document's free-text sections
    # and would otherwise be unreliable to extract.
    payload = {
        'identifier': table.get('identifier', f"{table['schema']}/{table['table']}"),
        'schema': table['schema'],
        'table': table['table'],
        'source_organisation': get_source_org(table['schema']),
        'official_url': official_url,
        'geometry_type': table.get('geometry_type'),
        'srid': table.get('srid'),
        'crs': table.get('crs'),
        'row_count': table.get('row_count'),
        'bbox_wgs84': table.get('bbox_wgs84'),
        'columns': [c['name'] for c in table.get('columns', [])],
        'enrichment_status': 'truncated' if response.stop_reason == 'max_tokens' else 'complete',
        'stop_reason': response.stop_reason,
        'model': MODEL,
        'max_tokens': max_tokens,
    }
    return f'\n\n<!-- agent_index_metadata: {json.dumps(payload)} -->\n'


def enrich(tables, client):
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    succeeded, skipped, failed = [], [], []

    for i, table in enumerate(tables, 1):
        schema, tbl = table['schema'], table['table']
        label = f'{schema}.{tbl}'
        out_path = TABLES_DIR / f'{schema}__{tbl}.md'
        print(f'[{i}/{len(tables)}] {label}')

        if out_path.exists():
            print(f'    skip    {out_path.name} already exists')
            skipped.append(label)
            continue

        try:
            max_tokens = _max_tokens_for(table)
            response = _call_claude(client, _build_user_prompt(table), max_tokens)
            markdown_text = _extract_text(response)
            if not markdown_text:
                raise RuntimeError(f'empty response text (stop_reason={response.stop_reason})')

            urls = _dedupe(_collect_urls(response.model_dump()))
            official_url = urls[0] if urls else None
            if urls:
                print(f'    docs    found ({len(urls)} url(s)), e.g. {urls[0]}')
            else:
                print('    docs    no cited URL found in response')

            if response.stop_reason == 'max_tokens':
                print(f'    WARNING output may be truncated (stop_reason=max_tokens, max_tokens={max_tokens})', file=sys.stderr)

            footer = _build_footer(table, official_url, response, max_tokens)
            out_path.write_text(markdown_text + footer, encoding='utf-8')
            print(f'    ok      wrote {out_path.name} (max_tokens={max_tokens})')
            succeeded.append(label)
        except Exception as exc:
            print(f'    FAILED  {label} - {exc}', file=sys.stderr)
            failed.append({'table': label, 'error': str(exc)})
        finally:
            time.sleep(API_DELAY_SECONDS)

    return {'succeeded': succeeded, 'skipped': skipped, 'failed': failed}


def main():
    parser = argparse.ArgumentParser(description='Enrich raw PostGIS schema metadata with AI-generated documentation.')
    parser.add_argument(
        '--mock',
        action='store_true',
        help=(
            'Accepted for symmetry with the other scripts (run_metadata_build.sh passes it through). '
            'This script always reads output/raw_schema.json and always makes live Anthropic API + '
            'web search calls, in both --mock and live mode.'
        ),
    )
    args = parser.parse_args()

    if args.mock:
        print('--mock has no effect here: reading whatever output/raw_schema.json already contains, and making live API calls.')

    if not RAW_SCHEMA_PATH.exists():
        print(f'{RAW_SCHEMA_PATH} does not exist - run extract_schema.py first.', file=sys.stderr)
        sys.exit(1)

    if _is_api_unconfigured():
        print(
            'ANTHROPIC_API_KEY is not set in .env (still the YOUR_ANTHROPIC_API_KEY placeholder).\n'
            'Set a real key before running - this script always makes live Anthropic API + web search calls.',
            file=sys.stderr,
        )
        sys.exit(1)

    raw = json.loads(RAW_SCHEMA_PATH.read_text(encoding='utf-8'))
    tables = raw.get('tables', [])
    print(f"Loaded {len(tables)} table(s) from {RAW_SCHEMA_PATH} (produced in '{raw.get('mode')}' mode).\n")

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    results = enrich(tables, client)

    print(f"\nDone: {len(results['succeeded'])} succeeded, {len(results['skipped'])} skipped, {len(results['failed'])} failed.")
    if results['failed']:
        for f in results['failed']:
            print(f"  FAILED  {f['table']} - {f['error']}")


if __name__ == '__main__':
    main()
