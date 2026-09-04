#!/usr/bin/env python
"""
monitor_new_tables.py

Compares the a_* schema tables currently in PostGIS against the tables the
metadata builder already knows about (metadata_builder/output/agent_index.json),
so newly added tables and tables needing a metadata review get flagged
automatically rather than silently sitting undocumented until someone notices.

For each table already known to the builder, the deeper GEMINI compliance
checks (gemini_tier, missing_mandatory_fields, staleness) are read from its
full metadata record (output/metadata/{schema}__{table}.json), not from
agent_index.json itself. agent_index.json is deliberately a compact retrieval
index (see metadata_builder/README.md) and does not carry gemini_tier or
missing_mandatory_fields - only the full per-table record does. It IS used
as the source of the "known tables" list, since that is exactly the list of
tables that a metadata record has been built for.

Usage:
    python metadata_builder/monitor_new_tables.py
    python metadata_builder/monitor_new_tables.py --mock       # print the email instead of sending it
    python metadata_builder/monitor_new_tables.py --new-only   # only detect/report/write new tables

If GIS_DB_USER is unset (e.g. on a dev laptop with no VPN access to the real
PostGIS server), the script automatically compares against a small synthetic
table list instead of failing outright - the same auto-fallback convention
used by scripts/ingest_authoritative.py. This is independent of --mock, which
controls only whether the email is sent or printed.
"""
import argparse
import json
import os
import smtplib
import sys
from datetime import datetime, timedelta, timezone
from email.mime.text import MIMEText
from pathlib import Path

from dotenv import load_dotenv

try:
    import psycopg2
except ImportError:  # pragma: no cover - dry-run/mock only works without this
    psycopg2 = None

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
OUTPUT_DIR = SCRIPT_DIR / 'output'
INDEX_PATH = OUTPUT_DIR / 'agent_index.json'
METADATA_DIR = OUTPUT_DIR / 'metadata'

load_dotenv(BASE_DIR / '.env', override=True)

SCHEMA_PREFIX = 'a_'
STALE_AFTER_DAYS = 90
RECIPIENT = 'pokaro@systra.com'

# Same env vars / defaults as extract_schema.py's DB_CONFIG.
DB_CONFIG = {
    'host': os.environ.get('GIS_DB_HOST', 'gisdb.systra.info'),
    'port': os.environ.get('GIS_DB_PORT', '5432'),
    'dbname': os.environ.get('GIS_DB_NAME', 'uk_irl'),
    'user': os.environ.get('GIS_DB_USER', ''),
    'password': os.environ.get('GIS_DB_PASSWORD', ''),
    'sslmode': os.environ.get('GIS_DB_SSLMODE', 'require'),
}

EMAIL_CONFIG = {
    'host': os.environ.get('EMAIL_HOST', ''),
    'port': int(os.environ.get('EMAIL_PORT', '587') or '587'),
    'user': os.environ.get('EMAIL_HOST_USER', ''),
    'password': os.environ.get('EMAIL_HOST_PASSWORD', ''),
    'use_tls': os.environ.get('EMAIL_USE_TLS', 'True').strip().lower() in ('1', 'true', 'yes'),
    'from_addr': os.environ.get('EMAIL_FROM', ''),
}

# Small synthetic scenario for the DB-unconfigured fallback: the tables
# already on record, plus one deliberately "new" table, so a --mock run on a
# dev laptop with no PostGIS access still exercises the new-table detection
# and email-formatting paths end to end. Not real data.
_SYNTHETIC_NEW_TABLE = ('a_demo_mock_schema', 'demo_new_table_for_testing')


def _is_db_unconfigured():
    # Same placeholder check as catalogue/views.py's _is_gis_db_mock().
    return not DB_CONFIG['user'] or DB_CONFIG['user'] == 'YOUR_DB_USER'


def _is_email_unconfigured():
    return not EMAIL_CONFIG['host'] or not EMAIL_CONFIG['user']


def load_known_index():
    """
    The list of tables the metadata builder already knows about, keyed by
    identifier ('schema/table'). Each value is the agent_index.json entry,
    which includes 'metadata_path' - used to load the full record for the
    deeper compliance checks.
    """
    if not INDEX_PATH.exists():
        print(
            f'{INDEX_PATH} does not exist - run metadata_builder/build.py at least once first.',
            file=sys.stderr,
        )
        sys.exit(1)
    return json.loads(INDEX_PATH.read_text(encoding='utf-8'))


def load_full_record(entry):
    """Loads a table's full metadata record (not just its agent_index.json summary)."""
    metadata_path = entry.get('metadata_path')
    if not metadata_path:
        return None
    path = BASE_DIR / metadata_path
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        return None


def get_current_tables():
    """
    Returns a sorted list of (schema, table) tuples for every table in every
    a_* schema currently in PostGIS. Falls back to a synthetic list when
    GIS_DB_USER is not configured, same auto-fallback convention as
    scripts/ingest_authoritative.py.
    """
    if _is_db_unconfigured():
        print(
            'GIS_DB_USER is not configured (still the YOUR_DB_USER placeholder or unset) - '
            'comparing against a small synthetic table list instead of the real database. '
            'Set GIS_DB_HOST/PORT/NAME/USER/PASSWORD in .env and ensure VPN/network access '
            'to the real PostGIS server for a live run.\n'
        )
        known = load_known_index()
        synthetic = {(entry['schema'], entry['table']) for entry in known.values()}
        synthetic.add(_SYNTHETIC_NEW_TABLE)
        return sorted(synthetic)

    if psycopg2 is None:
        raise RuntimeError(
            'psycopg2 is required for a live run. Install the project requirements first.'
        )
    conn = psycopg2.connect(**DB_CONFIG)
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT table_schema, table_name FROM information_schema.tables "
                "WHERE table_schema ~ '^a_' AND table_type = 'BASE TABLE' "
                "ORDER BY table_schema, table_name"
            )
            return cur.fetchall()
    finally:
        conn.close()


def detect_new_tables(current_tables, known_index):
    known_identifiers = {f"{entry['schema']}/{entry['table']}" for entry in known_index.values()}
    return [
        (schema, table) for schema, table in current_tables
        if f'{schema}/{table}' not in known_identifiers
    ]


def _days_since(iso_timestamp):
    if not iso_timestamp:
        return None
    try:
        built_at = datetime.fromisoformat(iso_timestamp)
    except ValueError:
        return None
    if built_at.tzinfo is None:
        built_at = built_at.replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - built_at).days


def review_summary(known_index):
    """
    Classifies every already-known table by reading its full metadata record.
    Returns (tier1_tables, incomplete_tables, stale_tables, tier_counts) -
    each of the first three is a list of 'schema/table' identifiers;
    tier_counts is {1: n, 2: n, 3: n, 'below_tier_1': n, 'unscored': n}.

    'unscored' and 'below_tier_1' are deliberately distinct: build.py's
    gemini_compliance() (Task 6) stores gemini_tier as an explicit null for
    a table that has been scored and found not to meet even Tier 1 - that is
    NOT the same as a record built before Task 6 existed, which has no
    gemini_tier key at all. record.get('gemini_tier') returns None for both
    cases, so the key's presence is checked separately to tell them apart.
    """
    tier1_tables = []
    incomplete_tables = []
    stale_tables = []
    tier_counts = {1: 0, 2: 0, 3: 0, 'below_tier_1': 0, 'unscored': 0}

    for identifier, entry in known_index.items():
        record = load_full_record(entry)
        if record is None or 'gemini_tier' not in record:
            tier_counts['unscored'] += 1
        else:
            tier = record['gemini_tier']
            tier_counts[tier if tier in (1, 2, 3) else 'below_tier_1'] += 1
            if tier == 1:
                tier1_tables.append(identifier)

        if record is None:
            continue

        missing_fields = record.get('missing_mandatory_fields')
        if missing_fields:
            incomplete_tables.append(identifier)

        days_old = _days_since(record.get('build', {}).get('generated_at'))
        if days_old is not None and days_old > STALE_AFTER_DAYS:
            stale_tables.append(identifier)

    return tier1_tables, incomplete_tables, stale_tables, tier_counts


METADATA_TABLE_DDL = """
    CREATE SCHEMA IF NOT EXISTS p_pycsw;
    CREATE TABLE IF NOT EXISTS p_pycsw.metadata (
        id              SERIAL PRIMARY KEY,
        schema_name     VARCHAR NOT NULL,
        table_name      VARCHAR NOT NULL,
        detected_at     TIMESTAMP NOT NULL DEFAULT NOW(),
        metadata_status VARCHAR,
        gemini_tier     INTEGER,
        missing_fields  TEXT,
        last_reviewed   TIMESTAMP
    )
"""


def write_new_tables_to_db(new_tables, dry_run):
    """
    Records newly detected tables in p_pycsw.metadata, creating the table
    first if it does not exist. Skips tables already logged there from a
    previous run (matched on schema_name + table_name) so a nightly
    --new-only run does not re-insert the same undetected table every night
    until it is actually built.
    """
    if not new_tables:
        return 0
    if dry_run:
        print('DRY-RUN: would ensure p_pycsw.metadata exists and insert:')
        for schema, table in new_tables:
            print(f'    {schema}.{table}')
        return len(new_tables)

    conn = psycopg2.connect(**DB_CONFIG)
    written = 0
    try:
        with conn.cursor() as cur:
            cur.execute(METADATA_TABLE_DDL)
            for schema, table in new_tables:
                cur.execute(
                    'SELECT 1 FROM p_pycsw.metadata WHERE schema_name = %s AND table_name = %s',
                    (schema, table),
                )
                if cur.fetchone():
                    continue
                cur.execute(
                    'INSERT INTO p_pycsw.metadata '
                    '(schema_name, table_name, metadata_status) VALUES (%s, %s, %s)',
                    (schema, table, 'new_undocumented'),
                )
                written += 1
        conn.commit()
    finally:
        conn.close()
    return written


def _recommended_commands(new_tables, tier1_tables, incomplete_tables):
    commands = []
    new_schemas = sorted({schema for schema, _table in new_tables})
    for schema in new_schemas:
        commands.append(f'python metadata_builder/build.py --schema {schema}')
    review_schemas = sorted({identifier.split('/', 1)[0] for identifier in tier1_tables + incomplete_tables})
    for schema in review_schemas:
        if schema not in new_schemas:
            commands.append(f'python metadata_builder/build.py --schema {schema} --full-rebuild')
    return commands


def build_email(new_tables, tier1_tables, incomplete_tables, stale_tables, tier_counts, new_only):
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    subject = f'GIS Portal — Metadata Status Report — {today}'

    lines = [f'GIS Portal metadata status report — {today}', '']

    if new_tables:
        lines.append(f'New tables detected ({len(new_tables)}):')
        lines.extend(f'  - {schema}/{table}' for schema, table in new_tables)
    else:
        lines.append('New tables detected: none')
    lines.append('')

    if not new_only:
        needing_review = sorted(set(tier1_tables) | set(incomplete_tables) | set(stale_tables))
        lines.append(f'Tables needing review ({len(needing_review)}):')
        if needing_review:
            for identifier in needing_review:
                reasons = []
                if identifier in tier1_tables:
                    reasons.append('Tier 1 (minimum only)')
                if identifier in incomplete_tables:
                    reasons.append('missing mandatory fields')
                if identifier in stale_tables:
                    reasons.append(f'not rebuilt in {STALE_AFTER_DAYS}+ days')
                lines.append(f'  - {identifier} ({", ".join(reasons)})')
        else:
            lines.append('  none')
        lines.append('')

        compliant = tier_counts[2] + tier_counts[3]
        lines.append(f'Fully GEMINI-compliant tables (Tier 2 or 3): {compliant}')
        lines.append('Tables by compliance tier:')
        lines.append(f'  Tier 3 — Full quality:         {tier_counts[3]}')
        lines.append(f'  Tier 2 — GEMINI compliant:     {tier_counts[2]}')
        lines.append(f'  Tier 1 — Minimum only:         {tier_counts[1]}')
        lines.append(f'  Below Tier 1 — Non-compliant:  {tier_counts["below_tier_1"]}')
        lines.append(f'  Not yet scored:                {tier_counts["unscored"]}')
        lines.append('')

    commands = _recommended_commands(new_tables, tier1_tables, incomplete_tables)
    if commands:
        lines.append('Recommended action:')
        lines.extend(f'  {cmd}' for cmd in commands)
    else:
        lines.append('Recommended action: none — nothing new or flagged for review.')

    return subject, '\n'.join(lines)


def send_email(subject, body, mock):
    if mock:
        print('=' * 72)
        print('MOCK MODE — email would be sent, printed instead:')
        print('=' * 72)
        print(f'From:    {EMAIL_CONFIG["from_addr"] or "(EMAIL_FROM not set)"}')
        print(f'To:      {RECIPIENT}')
        print(f'Subject: {subject}')
        print('-' * 72)
        print(body)
        print('=' * 72)
        return

    if _is_email_unconfigured():
        print(
            'EMAIL_HOST / EMAIL_HOST_USER are not configured in .env - printing the '
            'email instead of sending it. Set EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, '
            'EMAIL_HOST_PASSWORD, EMAIL_USE_TLS and EMAIL_FROM to send for real.\n',
            file=sys.stderr,
        )
        send_email(subject, body, mock=True)
        return

    message = MIMEText(body, 'plain', 'utf-8')
    message['Subject'] = subject
    message['From'] = EMAIL_CONFIG['from_addr'] or EMAIL_CONFIG['user']
    message['To'] = RECIPIENT

    with smtplib.SMTP(EMAIL_CONFIG['host'], EMAIL_CONFIG['port']) as server:
        if EMAIL_CONFIG['use_tls']:
            server.starttls()
        if EMAIL_CONFIG['user']:
            server.login(EMAIL_CONFIG['user'], EMAIL_CONFIG['password'])
        server.sendmail(message['From'], [RECIPIENT], message.as_string())

    print(f'Email sent to {RECIPIENT}.')


def main():
    parser = argparse.ArgumentParser(
        description='Compare PostGIS a_* tables against the metadata builder\'s known tables '
                     'and email a status report.'
    )
    parser.add_argument(
        '--mock', action='store_true',
        help='Print the email to the console instead of sending it, for testing.',
    )
    parser.add_argument(
        '--new-only', action='store_true',
        help='Only detect, report and write new tables; skip the compliance review counts.',
    )
    args = parser.parse_args()

    known_index = load_known_index()
    current_tables = get_current_tables()
    new_tables = detect_new_tables(current_tables, known_index)

    if args.new_only:
        tier1_tables, incomplete_tables, stale_tables, tier_counts = [], [], [], {1: 0, 2: 0, 3: 0, 'below_tier_1': 0, 'unscored': 0}
    else:
        tier1_tables, incomplete_tables, stale_tables, tier_counts = review_summary(known_index)

    written = write_new_tables_to_db(new_tables, dry_run=_is_db_unconfigured())

    subject, body = build_email(
        new_tables, tier1_tables, incomplete_tables, stale_tables, tier_counts, args.new_only,
    )
    send_email(subject, body, mock=args.mock)

    print(f'\n{len(current_tables)} table(s) checked, {len(new_tables)} new, {written} written to p_pycsw.metadata.')
    if not args.new_only:
        print(
            f'Review: {len(tier1_tables)} at Tier 1, {len(incomplete_tables)} with missing '
            f'mandatory fields, {len(stale_tables)} stale (>{STALE_AFTER_DAYS} days).'
        )


if __name__ == '__main__':
    main()
