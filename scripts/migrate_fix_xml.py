#!/usr/bin/env python
"""
migrate_fix_xml.py

One-time migration: fixes any p_pycsw.records row whose xml column holds
JSON (from before ingest_authoritative.py / ingest_minio.py /
ingest_postgis.py were updated to generate real CSW XML - see those
scripts' build_csw_xml() functions) instead of a valid OGC CSW 2.0.2
Dublin Core (csw:Record) document. This JSON-instead-of-XML content is
what caused QGIS MetaSearch's "record serialization failed: list index out
of range" error - pycsw's ISO metadata parser tries to parse this column as
XML, gets an empty result back from unparseable JSON text, and then
unconditionally indexes it with [0].

Detects affected rows with "xml LIKE '{%'" (a JSON object), then
double-checks each one actually fails to parse as XML in Python before
touching it - so a row that happens to start with '{' but is still valid
XML for some other reason is never overwritten. Only rebuilds the xml
column; every other column is left untouched. Safe to run more than once -
once a row's xml is valid, later runs will no longer match it.

Reads only the columns still known to exist on p_pycsw.records (see the
"Fix views.py for dropped columns" work): identifier, title, abstract,
keywords, type, format, publisher, organization, wkt_geometry, mdsource.

Unlike this project's other migration scripts, --dry-run here still needs a
live database connection (read-only, no writes) - there is no local file
this migration can preview against instead, since its whole job is
inspecting existing database rows.

Usage:
    python scripts/migrate_fix_xml.py --dry-run   # list affected records, no DB writes
    python scripts/migrate_fix_xml.py             # fix them for real
"""
import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from dotenv import load_dotenv
import os

try:
    import psycopg2
except ImportError:  # pragma: no cover - this script cannot do anything without it
    psycopg2 = None

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent

load_dotenv(BASE_DIR / '.env', override=True)

# Same env vars / defaults as the rest of this project's DB-connecting scripts.
DB_CONFIG = {
    'host': os.environ.get('GIS_DB_HOST', 'gisdb.systra.info'),
    'port': os.environ.get('GIS_DB_PORT', '5432'),
    'dbname': os.environ.get('GIS_DB_NAME', 'uk_irl'),
    'user': os.environ.get('GIS_DB_USER', ''),
    'password': os.environ.get('GIS_DB_PASSWORD', ''),
    'sslmode': os.environ.get('GIS_DB_SSLMODE', 'require'),
}

CSW_NAMESPACES = {
    'csw': 'http://www.opengis.net/cat/csw/2.0.2',
    'dc':  'http://purl.org/dc/elements/1.1/',
    'dct': 'http://purl.org/dc/terms/',
    'ows': 'http://www.opengis.net/ows',
}
for _prefix, _uri in CSW_NAMESPACES.items():
    ET.register_namespace(_prefix, _uri)


def _is_db_unconfigured():
    # Same placeholder check as catalogue/views.py's _is_gis_db_mock().
    return not DB_CONFIG['user'] or DB_CONFIG['user'] == 'YOUR_DB_USER'


def is_valid_xml(value):
    """True when value is non-empty and parses as well-formed XML."""
    if not value:
        return False
    try:
        ET.fromstring(value)
        return True
    except ET.ParseError:
        return False


def wkt_to_bbox(wkt):
    """Extracts [xmin, ymin, xmax, ymax] from a WKT POLYGON string, or None."""
    if not wkt or 'POLYGON' not in wkt.upper():
        return None
    try:
        start = wkt.index('((') + 2
        end = wkt.index('))')
        points = [
            tuple(map(float, pair.strip().split()))
            for pair in wkt[start:end].split(',')
        ]
        xs = [point[0] for point in points]
        ys = [point[1] for point in points]
        return [min(xs), min(ys), max(xs), max(ys)]
    except (ValueError, IndexError):
        return None


def parse_keywords(keywords_raw):
    """Splits a stored keyword string on whichever separator it uses."""
    if not keywords_raw:
        return []
    for sep in ('/', '|', ';', ','):
        if sep in keywords_raw:
            return [k.strip() for k in keywords_raw.split(sep) if k.strip()]
    return [keywords_raw.strip()] if keywords_raw.strip() else []


def build_csw_xml(identifier, title, keywords, record_type, record_format,
                   organisation, abstract, source_url, bbox):
    """
    Renders a minimal, valid OGC CSW 2.0.2 Dublin Core (csw:Record) XML
    document. See scripts/ingest_authoritative.py's build_csw_xml() for the
    original fix and full explanation of the bug this addresses.

    Built with ElementTree (not string formatting), so titles/abstracts
    containing '&', '<', '>' etc. can never produce malformed XML.
    """
    root = ET.Element(f"{{{CSW_NAMESPACES['csw']}}}Record")

    def add(prefix, tag, text):
        if text is None or text == '':
            return None
        element = ET.SubElement(root, f'{{{CSW_NAMESPACES[prefix]}}}{tag}')
        element.text = str(text)
        return element

    add('dc', 'identifier', identifier)
    add('dc', 'title', title)
    add('dc', 'type', record_type)
    add('dc', 'format', record_format)
    for keyword in (keywords or [])[:20]:
        add('dc', 'subject', keyword)
    add('dc', 'publisher', organisation)
    add('dct', 'abstract', abstract)
    references = add('dct', 'references', source_url)
    if references is not None:
        references.set('scheme', 'WWW:LINK')

    if bbox and len(bbox) == 4:
        xmin, ymin, xmax, ymax = bbox
        bbox_element = ET.SubElement(root, f"{{{CSW_NAMESPACES['ows']}}}BoundingBox")
        bbox_element.set('crs', 'urn:ogc:def:crs:EPSG::4326')
        # y x order (lat lon), matching pycsw's own convention - see
        # catalogue/views.py's _csw_record_to_feature().
        lower = ET.SubElement(bbox_element, f"{{{CSW_NAMESPACES['ows']}}}LowerCorner")
        lower.text = f"{ymin} {xmin}"
        upper = ET.SubElement(bbox_element, f"{{{CSW_NAMESPACES['ows']}}}UpperCorner")
        upper.text = f"{ymax} {xmax}"

    return ET.tostring(root, encoding='unicode')


SELECT_CANDIDATES_SQL = """
    SELECT identifier, title, abstract, keywords, type, format,
           publisher, organization, wkt_geometry, mdsource, xml
    FROM p_pycsw.records
    WHERE xml LIKE '{%%'
    ORDER BY identifier
"""

UPDATE_SQL = "UPDATE p_pycsw.records SET xml = %s WHERE identifier = %s"


def run(dry_run):
    conn = psycopg2.connect(**DB_CONFIG)
    fixed = already_valid = failed = 0
    try:
        with conn.cursor() as cur:
            cur.execute(SELECT_CANDIDATES_SQL)
            rows = cur.fetchall()
            print(f"Found {len(rows)} record(s) with 'xml LIKE \\'{{%'\" (JSON-shaped xml column).\n")

            for i, (
                identifier, title, abstract, keywords_raw, record_type,
                record_format, publisher, organization, wkt_geometry,
                mdsource, current_xml,
            ) in enumerate(rows, 1):
                # Double-check even though the SQL filter already matched -
                # a row that happens to start with '{' but is somehow still
                # valid XML (extremely unlikely) is left untouched.
                if is_valid_xml(current_xml):
                    already_valid += 1
                    print(f'  [{i}/{len(rows)}] {identifier}: already valid XML - skipped')
                    continue

                organisation = organization or publisher or ''
                keywords = parse_keywords(keywords_raw)
                bbox = wkt_to_bbox(wkt_geometry)
                new_xml = build_csw_xml(
                    identifier, title, keywords, record_type, record_format,
                    organisation, abstract, mdsource, bbox,
                )

                if dry_run:
                    print(f'  [{i}/{len(rows)}] {identifier}: would fix ({len(new_xml)} bytes)')
                    if i == 1:
                        print(f'\n    Sample generated XML for {identifier}:\n    {new_xml}\n')
                    continue

                try:
                    cur.execute(UPDATE_SQL, (new_xml, identifier))
                    conn.commit()
                    fixed += 1
                    print(f'  [{i}/{len(rows)}] {identifier}: OK - fixed')
                except Exception as exc:
                    conn.rollback()
                    failed += 1
                    print(f'  [{i}/{len(rows)}] {identifier}: FAILED - {exc}')
    finally:
        conn.close()

    print()
    if dry_run:
        print(
            f'DRY-RUN complete: {len(rows) - already_valid} record(s) would be fixed, '
            f'{already_valid} already valid. No database writes were made.'
        )
    else:
        print(f'Migration complete: {fixed} fixed, {already_valid} already valid, {failed} failed.')
    return 1 if failed else 0


def main():
    parser = argparse.ArgumentParser(
        description="Fix p_pycsw.records rows whose xml column holds JSON instead of valid CSW XML."
    )
    parser.add_argument(
        '--dry-run', action='store_true',
        help='List affected records and preview the XML that would be written, without updating the database.',
    )
    args = parser.parse_args()

    if psycopg2 is None:
        print('psycopg2 is required. Install the project requirements first.', file=sys.stderr)
        sys.exit(1)

    # No offline dry-run fallback here (unlike this project's other migration
    # scripts): this migration's whole job is inspecting existing database
    # rows, so even --dry-run needs a real connection to read them.
    if _is_db_unconfigured():
        print(
            'GIS_DB_USER is not configured (still the YOUR_DB_USER placeholder or unset). '
            'This migration reads existing p_pycsw.records rows, so it needs a real database '
            'connection even for --dry-run. Set GIS_DB_HOST/PORT/NAME/USER/PASSWORD in .env '
            'and ensure VPN/network access to the real PostGIS server.',
            file=sys.stderr,
        )
        sys.exit(1)

    sys.exit(run(args.dry_run))


if __name__ == '__main__':
    main()
