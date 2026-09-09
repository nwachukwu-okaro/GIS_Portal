#!/usr/bin/env python
"""
migrate_fix_xml.py

One-time migration: fixes any p_pycsw.records row that isn't correctly set
up for pycsw's apiso profile (pycsw/config/pycsw.cfg.example has
profiles=apiso). Two things have to both be right:

  1. typename must be exactly 'gmd:MD_Metadata' - pycsw's apiso plugin
     (pycsw/plugins/profiles/apiso/apiso.py) decides whether to treat a
     record as ISO 19139 with "typename == 'gmd:MD_Metadata'". Its only
     fallback checks whether the raw xml string startswith the literal text
     '<gmd:MD_Metadata>' with NO attributes - impossible for valid
     namespaced XML, which must declare xmlns: on its root element. So a
     record can have perfect ISO XML and still be mis-served if typename is
     wrong.
  2. xml must actually be a valid ISO 19139 gmd:MD_Metadata document -
     earlier versions of this project's ingestion scripts stored
     json.dumps(item) (before the first fix) or a Dublin Core csw:Record
     document (before this fix) in that column. Either one makes owslib's
     ISO parser (used once typename routes a record to it) end up with an
     empty gmd:identificationInfo/gmd:MD_DataIdentification list, which is
     then indexed unconditionally with [0] - "record serialization failed:
     list index out of range".

Detects affected rows with "typename IS DISTINCT FROM 'gmd:MD_Metadata' OR
xml LIKE '{%'" - the first half catches records already fixed to valid-but-
wrong-schema XML by an earlier version of this migration, not just the
original JSON-holding rows. Each candidate is regenerated regardless of
which half matched, since typename and xml must always change together.
Safe to run more than once - once a row is correctly typed and has valid
ISO XML, later runs no longer match it.

Reads only the columns still known to exist on p_pycsw.records (see the
"Fix views.py for dropped columns" work): identifier, title, abstract,
keywords, publisher, organization, wkt_geometry, topicategory, time_begin.

Unlike this project's other migration scripts, --dry-run here still needs a
live database connection (read-only, no writes) - there is no local file
this migration can preview against instead, since its whole job is
inspecting existing database rows.

Usage:
    python scripts/migrate_fix_xml.py --dry-run   # list affected records, no DB writes
    python scripts/migrate_fix_xml.py             # fix them for real

After the XML pass, independently repairs legacy links using the same
normalizer as migrate_fix_links.py (including records whose XML is already
correct). --dry-run previews both passes. For links-only repair, prefer
migrate_fix_links.py; it leaves all XML and typename values untouched.
"""
import argparse
from migrate_fix_links import repair_links
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
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

# See scripts/ingest_authoritative.py's build_iso19139_xml() for the
# original fix and full explanation - this mirrors it for existing rows.
RECORD_TYPENAME = 'gmd:MD_Metadata'
RECORD_SCHEMA = 'http://www.isotc211.org/2005/gmd'

ISO_NAMESPACES = {
    'gmd': 'http://www.isotc211.org/2005/gmd',
    'gco': 'http://www.isotc211.org/2005/gco',
}
for _prefix, _uri in ISO_NAMESPACES.items():
    ET.register_namespace(_prefix, _uri)

ISO_CONTACT_ORGANISATION = 'Systra GIS Team'
ISO_CONTACT_EMAIL = 'gis_uk@systra.com'

_ISO_CODELIST_BASE = (
    'http://standards.iso.org/ittf/PubliclyAvailableStandards/'
    'ISO_19139_Schemas/resources/codelist/gmxCodelists.xml'
)
ISO_CHARACTER_SET_CODELIST = f'{_ISO_CODELIST_BASE}#MD_CharacterSetCode'
ISO_SCOPE_CODELIST = f'{_ISO_CODELIST_BASE}#MD_ScopeCode'
ISO_ROLE_CODELIST = f'{_ISO_CODELIST_BASE}#CI_RoleCode'


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


def _gmd(tag):
    return f"{{{ISO_NAMESPACES['gmd']}}}{tag}"


def _gco(tag):
    return f"{{{ISO_NAMESPACES['gco']}}}{tag}"


def _iso_char_string(parent, tag, text):
    """<gmd:{tag}><gco:CharacterString>{text}</gco:CharacterString></gmd:{tag}>"""
    if text is None or text == '':
        return None
    element = ET.SubElement(parent, _gmd(tag))
    char_string = ET.SubElement(element, _gco('CharacterString'))
    char_string.text = str(text)
    return element


def build_iso19139_xml(identifier, title, abstract, keywords, topic_category,
                        dataset_reference_date, bbox, language='eng'):
    """
    Renders a minimal, valid ISO 19139 gmd:MD_Metadata XML document. See
    scripts/ingest_authoritative.py's build_iso19139_xml() for the original
    fix and full explanation of the bug this addresses (verified against
    both pycsw's apiso.py and OWSLib's iso.py source).

    Built with ElementTree (not string formatting), so titles/abstracts
    containing '&', '<', '>' etc. can never produce malformed XML.
    """
    root = ET.Element(_gmd('MD_Metadata'))

    _iso_char_string(root, 'fileIdentifier', identifier)
    _iso_char_string(root, 'language', language)

    character_set = ET.SubElement(root, _gmd('characterSet'))
    character_set_code = ET.SubElement(character_set, _gmd('MD_CharacterSetCode'))
    character_set_code.set('codeList', ISO_CHARACTER_SET_CODELIST)
    character_set_code.set('codeListValue', 'utf8')
    character_set_code.text = 'utf8'

    hierarchy_level = ET.SubElement(root, _gmd('hierarchyLevel'))
    hierarchy_level_code = ET.SubElement(hierarchy_level, _gmd('MD_ScopeCode'))
    hierarchy_level_code.set('codeList', ISO_SCOPE_CODELIST)
    hierarchy_level_code.set('codeListValue', 'dataset')
    hierarchy_level_code.text = 'dataset'

    contact = ET.SubElement(root, _gmd('contact'))
    responsible_party = ET.SubElement(contact, _gmd('CI_ResponsibleParty'))
    _iso_char_string(responsible_party, 'organisationName', ISO_CONTACT_ORGANISATION)
    contact_info = ET.SubElement(responsible_party, _gmd('contactInfo'))
    ci_contact = ET.SubElement(contact_info, _gmd('CI_Contact'))
    address_wrapper = ET.SubElement(ci_contact, _gmd('address'))
    ci_address = ET.SubElement(address_wrapper, _gmd('CI_Address'))
    _iso_char_string(ci_address, 'electronicMailAddress', ISO_CONTACT_EMAIL)
    role = ET.SubElement(responsible_party, _gmd('role'))
    role_code = ET.SubElement(role, _gmd('CI_RoleCode'))
    role_code.set('codeList', ISO_ROLE_CODELIST)
    role_code.set('codeListValue', 'pointOfContact')
    role_code.text = 'pointOfContact'

    date_stamp = ET.SubElement(root, _gmd('dateStamp'))
    date_stamp_value = ET.SubElement(date_stamp, _gco('Date'))
    date_stamp_value.text = dataset_reference_date or datetime.now(timezone.utc).date().isoformat()

    identification_info = ET.SubElement(root, _gmd('identificationInfo'))
    data_identification = ET.SubElement(identification_info, _gmd('MD_DataIdentification'))

    citation = ET.SubElement(data_identification, _gmd('citation'))
    ci_citation = ET.SubElement(citation, _gmd('CI_Citation'))
    _iso_char_string(ci_citation, 'title', title)
    if dataset_reference_date:
        citation_date = ET.SubElement(ci_citation, _gmd('date'))
        ci_date = ET.SubElement(citation_date, _gmd('CI_Date'))
        date_element = ET.SubElement(ci_date, _gmd('date'))
        ET.SubElement(date_element, _gco('Date')).text = dataset_reference_date
        date_type = ET.SubElement(ci_date, _gmd('dateType'))
        # migrate_fix_xml.py only has time_begin (temporal_extent, a
        # different GEMINI concept from dataset_reference_date) available
        # among existing columns - not a real publication/revision/creation
        # date type, so this is deliberately left generic.
        date_type_code = ET.SubElement(date_type, _gmd('CI_DateTypeCode'))
        date_type_code.set('codeListValue', 'publication')
        date_type_code.text = 'publication'

    _iso_char_string(data_identification, 'abstract', abstract)

    if keywords:
        descriptive_keywords = ET.SubElement(data_identification, _gmd('descriptiveKeywords'))
        md_keywords = ET.SubElement(descriptive_keywords, _gmd('MD_Keywords'))
        for keyword in keywords[:20]:
            _iso_char_string(md_keywords, 'keyword', keyword)

    _iso_char_string(data_identification, 'language', language)

    if topic_category:
        topic_category_el = ET.SubElement(data_identification, _gmd('topicCategory'))
        ET.SubElement(topic_category_el, _gmd('MD_TopicCategoryCode')).text = topic_category

    if bbox and len(bbox) == 4:
        xmin, ymin, xmax, ymax = bbox
        extent = ET.SubElement(data_identification, _gmd('extent'))
        ex_extent = ET.SubElement(extent, _gmd('EX_Extent'))
        geographic_element = ET.SubElement(ex_extent, _gmd('geographicElement'))
        geographic_bbox = ET.SubElement(geographic_element, _gmd('EX_GeographicBoundingBox'))
        for tag, value in (
            ('westBoundLongitude', xmin), ('eastBoundLongitude', xmax),
            ('southBoundLatitude', ymin), ('northBoundLatitude', ymax),
        ):
            bound_element = ET.SubElement(geographic_bbox, _gmd(tag))
            ET.SubElement(bound_element, _gco('Decimal')).text = str(value)

    return ET.tostring(root, encoding='unicode')


SELECT_CANDIDATES_SQL = """
    SELECT identifier, title, abstract, keywords,
           publisher, organization, wkt_geometry, topicategory, time_begin,
           typename, xml
    FROM p_pycsw.records
    WHERE typename IS DISTINCT FROM %(typename)s OR xml LIKE '{%%'
    ORDER BY identifier
"""

UPDATE_SQL = """
    UPDATE p_pycsw.records
    SET typename = %(typename)s, schema = %(schema)s, xml = %(xml)s
    WHERE identifier = %(identifier)s
"""


def run(dry_run):
    conn = psycopg2.connect(**DB_CONFIG)
    fixed = already_ok = failed = 0
    try:
        with conn.cursor() as cur:
            cur.execute(SELECT_CANDIDATES_SQL, {'typename': RECORD_TYPENAME})
            rows = cur.fetchall()
            print(
                f"Found {len(rows)} record(s) not yet typename = '{RECORD_TYPENAME}' "
                f"or with JSON-shaped xml.\n"
            )

            for i, (
                identifier, title, abstract, keywords_raw,
                publisher, organization, wkt_geometry, topic_category, time_begin,
                current_typename, current_xml,
            ) in enumerate(rows, 1):
                # Double-check even though the SQL filter already matched -
                # a row with the correct typename AND already-valid ISO XML
                # (extremely unlikely to reach here at all) is left untouched.
                if current_typename == RECORD_TYPENAME and is_valid_xml(current_xml):
                    already_ok += 1
                    print(f'  [{i}/{len(rows)}] {identifier}: already correct - skipped')
                    continue

                organisation = organization or publisher or ''
                keywords = parse_keywords(keywords_raw)
                bbox = wkt_to_bbox(wkt_geometry)
                reference_date = time_begin.date().isoformat() if hasattr(time_begin, 'date') else None
                new_xml = build_iso19139_xml(
                    identifier, title, abstract, keywords, topic_category,
                    reference_date, bbox,
                )

                if dry_run:
                    print(f'  [{i}/{len(rows)}] {identifier}: would fix ({len(new_xml)} bytes)')
                    if i == 1:
                        print(f'\n    Sample generated XML for {identifier}:\n    {new_xml}\n')
                    continue

                try:
                    cur.execute(UPDATE_SQL, {
                        'typename': RECORD_TYPENAME, 'schema': RECORD_SCHEMA,
                        'xml': new_xml, 'identifier': identifier,
                    })
                    conn.commit()
                    fixed += 1
                    print(f'  [{i}/{len(rows)}] {identifier}: OK - fixed')
                except Exception as exc:
                    conn.rollback()
                    failed += 1
                    print(f'  [{i}/{len(rows)}] {identifier}: FAILED - {exc}')
        # Scan links independently: correctly typed XML can still have bad links.
        repair_links(conn, dry_run=dry_run)
    finally:
        conn.close()

    print()
    if dry_run:
        print(
            f'DRY-RUN complete: {len(rows) - already_ok} record(s) would be fixed, '
            f'{already_ok} already correct. No database writes were made.'
        )
    else:
        print(f'Migration complete: {fixed} fixed, {already_ok} already correct, {failed} failed.')
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
