#!/usr/bin/env python
"""Repair only pycsw 2.6.2 links. Run with --dry-run before applying.

Reads all non-null links: a total comma count misses JSON and malformed
individual entries in a multi-link value. Only a_*/table
identifiers without a file extension are repaired. Other identifiers are
left untouched. Each failed record is rolled back and warned about without
undoing successful records or stopping subsequent repairs. No XML is changed.
"""
import argparse
import json
import logging
import re

LOGGER = logging.getLogger(__name__)


def is_postgis_identifier(identifier):
    """Conservative deployment-specific heuristic, not catalogue source metadata."""
    return isinstance(identifier, str) and bool(
        re.fullmatch(r'a_[^/\s]+/[^/.\s]+', identifier)
    )


def _url(value):
    return isinstance(value, str) and bool(re.match(r'^[A-Za-z][A-Za-z0-9+.-]*://\S+$', value))


def _encode(name, description, protocol, url):
    if not _url(url):
        raise ValueError('Link has no valid absolute URL')
    fields = [str(value or '').replace(',', ' ').replace('^', ' ')
              for value in (name, description, protocol)]
    return ','.join(fields + [url.replace(',', '%2C').replace('^', '%5E')])


def normalize_links(value):
    """Convert bare URLs/STAC JSON; preserve correct legacy links verbatim."""
    if value is None:
        return None
    raw = value.strip()
    if not raw:
        return None
    if raw.startswith(('[', '{')):
        entries = json.loads(raw)
        if isinstance(entries, dict):
            entries = [entries]
        if not isinstance(entries, list):
            raise ValueError('Expected a JSON link list')
        result = []
        for entry in entries:
            if not isinstance(entry, dict):
                raise ValueError('Expected JSON link objects')
            result.append(_encode(entry.get('name') or entry.get('title') or 'Dataset',
                                  entry.get('description') or 'Resource',
                                  entry.get('protocol') or 'WWW:LINK',
                                  entry.get('href') or entry.get('url')))
        return '^'.join(result) or None
    result = []
    for entry in raw.split('^'):
        if _url(entry):
            result.append(_encode('Dataset', 'Publisher resource', 'WWW:LINK', entry))
            continue
        fields = entry.split(',')
        if len(fields) != 4 or not fields[2] or not _url(fields[3]):
            raise ValueError('Expected name,description,protocol,url or an absolute URL')
        result.append(entry)
    return '^'.join(result)


def repair_links(conn, dry_run=False):
    """Commit each successful repair; a bad record cannot abort later repairs."""
    changed = unchanged = skipped = failed = 0
    try:
        with conn.cursor() as cur:
            cur.execute('SELECT identifier, links FROM p_pycsw.records WHERE links IS NOT NULL ORDER BY identifier')
            rows = cur.fetchall()
            for identifier, old in rows:
                if not is_postgis_identifier(identifier):
                    skipped += 1
                    LOGGER.warning('%s: skipped (not an a_ schema table); links unchanged', identifier)
                    continue
                try:
                    new = normalize_links(old)
                    if new == old:
                        unchanged += 1
                        continue
                    if not dry_run:
                        cur.execute('UPDATE p_pycsw.records SET links = %s WHERE identifier = %s AND links IS NOT DISTINCT FROM %s',
                                    (new, identifier, old))
                        if cur.rowcount != 1:
                            raise RuntimeError('Concurrently changed; retry migration')
                        conn.commit()
                    changed += 1
                    print(f'{identifier}: {"would fix" if dry_run else "fixed"} links')
                except Exception as exc:
                    conn.rollback()
                    failed += 1
                    LOGGER.warning('%s: skipped after error; links unchanged: %s', identifier, exc)
        # Close any remaining read-only transaction (also used by dry-run).
        conn.rollback()
    except Exception:
        conn.rollback()
        raise
    print(f'Links: {changed} {"would change" if dry_run else "changed"}, '
          f'{unchanged} unchanged, {skipped} skipped, {failed} failed.')
    return changed


def main():
    import os
    from pathlib import Path
    import psycopg2
    from dotenv import load_dotenv

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    load_dotenv(Path(__file__).resolve().parent.parent / '.env', override=True)
    user = os.environ.get('GIS_DB_USER', '')
    if not user or user == 'YOUR_DB_USER':
        parser.error('Configure GIS_DB_* in .env; even --dry-run requires database access.')
    conn = psycopg2.connect(host=os.environ.get('GIS_DB_HOST', 'gisdb.systra.info'),
                            port=os.environ.get('GIS_DB_PORT', '5432'),
                            dbname=os.environ.get('GIS_DB_NAME', 'uk_irl'), user=user,
                            password=os.environ.get('GIS_DB_PASSWORD', ''),
                            sslmode=os.environ.get('GIS_DB_SSLMODE', 'require'))
    try:
        conn.set_session(readonly=args.dry_run)
        repair_links(conn, args.dry_run)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
