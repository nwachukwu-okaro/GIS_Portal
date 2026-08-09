#!/usr/bin/env bash
# Runs the full metadata_builder pipeline (extract -> enrich -> index) in sequence
# and writes a run report summarising what happened. Pass --mock to run every
# stage against the bundled sample data / existing raw_schema.json instead of a
# live (VPN-gated) PostGIS connection.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
OUTPUT_DIR="$SCRIPT_DIR/output"
LOG_DIR="$OUTPUT_DIR/logs"
REPORT_PATH="$OUTPUT_DIR/run_report.txt"

MOCK_FLAG=""
if [[ "${1:-}" == "--mock" ]]; then
    MOCK_FLAG="--mock"
fi
MODE_LABEL="live"
if [[ -n "$MOCK_FLAG" ]]; then
    MODE_LABEL="mock"
fi

# Prefer the project's own venv (same one the scripts were developed/tested against),
# fall back to whatever python3/python is on PATH.
if [[ -x "$PROJECT_DIR/venv/Scripts/python.exe" ]]; then
    PYTHON="$PROJECT_DIR/venv/Scripts/python.exe"
elif [[ -x "$PROJECT_DIR/venv/bin/python" ]]; then
    PYTHON="$PROJECT_DIR/venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON="python3"
else
    PYTHON="python"
fi

mkdir -p "$LOG_DIR"

START_TIME="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
START_EPOCH="$(date +%s)"

echo "======================================================="
echo " Systra GIS Portal - metadata_builder pipeline"
echo " mode: $MODE_LABEL"
echo " started: $START_TIME"
echo "======================================================="

echo
echo "[1/3] extract_schema.py $MOCK_FLAG"
"$PYTHON" "$SCRIPT_DIR/extract_schema.py" $MOCK_FLAG 2>&1 | tee "$LOG_DIR/extract_schema.log"
EXTRACT_EXIT=${PIPESTATUS[0]}
echo "      -> exit code $EXTRACT_EXIT"

echo
echo "[2/3] enrich_metadata.py $MOCK_FLAG"
"$PYTHON" "$SCRIPT_DIR/enrich_metadata.py" $MOCK_FLAG 2>&1 | tee "$LOG_DIR/enrich_metadata.log"
ENRICH_EXIT=${PIPESTATUS[0]}
echo "      -> exit code $ENRICH_EXIT"

echo
echo "[3/3] build_index.py $MOCK_FLAG"
"$PYTHON" "$SCRIPT_DIR/build_index.py" $MOCK_FLAG 2>&1 | tee "$LOG_DIR/build_index.log"
INDEX_EXIT=${PIPESTATUS[0]}
echo "      -> exit code $INDEX_EXIT"

END_TIME="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
END_EPOCH="$(date +%s)"
DURATION=$((END_EPOCH - START_EPOCH))

echo
echo "======================================================="
echo " Building run report..."
echo "======================================================="

"$PYTHON" - "$OUTPUT_DIR" "$START_TIME" "$END_TIME" "$DURATION" "$EXTRACT_EXIT" "$ENRICH_EXIT" "$INDEX_EXIT" "$MODE_LABEL" <<'PYEOF'
import json
import re
import sys
from pathlib import Path

output_dir = Path(sys.argv[1])
start_time, end_time, duration = sys.argv[2], sys.argv[3], sys.argv[4]
extract_exit, enrich_exit, index_exit = sys.argv[5], sys.argv[6], sys.argv[7]
mode = sys.argv[8]

raw_schema_path = output_dir / 'raw_schema.json'
tables_dir = output_dir / 'tables'
index_path = output_dir / 'agent_index.json'
enrich_log_path = output_dir / 'logs' / 'enrich_metadata.log'
report_path = output_dir / 'run_report.txt'

raw = {}
if raw_schema_path.exists():
    raw = json.loads(raw_schema_path.read_text(encoding='utf-8'))
tables = raw.get('tables', [])
extract_errors = raw.get('errors', [])

enrich_log = enrich_log_path.read_text(encoding='utf-8') if enrich_log_path.exists() else ''
# "    FAILED  schema.table - reason" - written by enrich_metadata.py's per-table
# try/except logging.
failed_reasons = dict(re.findall(r'FAILED\s+(\S+)\s*-\s*(.+)', enrich_log))

by_schema = {}
failed_tables = []
for t in tables:
    schema, table = t['schema'], t['table']
    label = f'{schema}.{table}'
    md_path = tables_dir / f'{schema}__{table}.md'
    entry = by_schema.setdefault(schema, {'found': 0, 'enriched': 0, 'failed': 0})
    entry['found'] += 1
    if md_path.exists():
        entry['enriched'] += 1
    else:
        entry['failed'] += 1
        reason = failed_reasons.get(label, 'unknown - see output/logs/enrich_metadata.log')
        failed_tables.append((label, reason))

index_count = 0
if index_path.exists():
    index_count = len(json.loads(index_path.read_text(encoding='utf-8')))

total_found = sum(v['found'] for v in by_schema.values())
total_enriched = sum(v['enriched'] for v in by_schema.values())
total_failed = sum(v['failed'] for v in by_schema.values())

lines = []
lines.append('=' * 60)
lines.append('Systra GIS Portal - Metadata Build Report')
lines.append('=' * 60)
lines.append(f'Mode:      {mode}')
lines.append(f'Started:   {start_time}')
lines.append(f'Finished:  {end_time}')
lines.append(f'Duration:  {duration}s')
lines.append('')
lines.append('Stage exit codes:')
lines.append(f'  1. extract_schema.py   exit={extract_exit}')
lines.append(f'  2. enrich_metadata.py  exit={enrich_exit}')
lines.append(f'  3. build_index.py      exit={index_exit}')
lines.append('')
lines.append('Per-schema breakdown:')
if by_schema:
    for schema in sorted(by_schema):
        v = by_schema[schema]
        lines.append(f'  {schema}')
        lines.append(f'      found: {v["found"]}   enriched: {v["enriched"]}   failed: {v["failed"]}')
else:
    lines.append('  (no tables found - check output/logs/extract_schema.log)')
lines.append('')
lines.append('Failed tables:')
if failed_tables:
    for label, reason in failed_tables:
        lines.append(f'  {label} - {reason}')
else:
    lines.append('  (none)')
if extract_errors:
    lines.append('')
    lines.append('Extraction errors (from raw_schema.json):')
    for e in extract_errors:
        lines.append(f"  {e.get('schema')}.{e.get('table')} - {e.get('error')}")
lines.append('')
lines.append('Totals:')
lines.append(f'  schemas:              {len(by_schema)}')
lines.append(f'  tables found:         {total_found}')
lines.append(f'  tables enriched:      {total_enriched}')
lines.append(f'  tables failed:        {total_failed}')
lines.append(f'  agent_index entries:  {index_count}')
lines.append('')
lines.append('Output files:')
lines.append(f'  {raw_schema_path}')
lines.append(f'  {tables_dir}/*.md  ({total_enriched} file(s))')
lines.append(f'  {index_path}')
lines.append(f'  {report_path}  (this report)')
lines.append('=' * 60)

report_text = '\n'.join(lines) + '\n'
report_path.write_text(report_text, encoding='utf-8')
print(report_text)
PYEOF

echo "Report saved to: $REPORT_PATH"

if [[ "$EXTRACT_EXIT" -ne 0 || "$ENRICH_EXIT" -ne 0 || "$INDEX_EXIT" -ne 0 ]]; then
    exit 1
fi
exit 0
