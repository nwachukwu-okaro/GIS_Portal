"""
catalogue/views.py
==================
Core view logic for the Systra GIS Data Portal.

This module handles all user-facing functionality:
  - Searching the catalogue (via direct DB query or CSW fallback)
  - Viewing dataset detail pages with previews and downloads
  - Streaming MinIO files securely through Django
  - Uploading files to MinIO with mandatory metadata tagging
  - Uploading spatial data to PostGIS with structured table comments

Architecture decisions:
  - Direct PostgreSQL query on p_pycsw.records is the primary search path.
    It is faster, supports ILIKE full-text search, and returns all custom
    columns (distancevalue for size, distanceuom for geometry type, crs)
    that the CSW Dublin Core response does not expose.
  - CSW is the fallback when the database is not reachable.
  - Mock mode is active when credentials are absent from .env — all views
    return bundled sample data so the UI can be developed and tested
    without a live server connection.
  - The asset view streams MinIO files through Django rather than exposing
    direct MinIO URLs, so private buckets remain secure.

Sections:
  1.  Imports and constants
  2.  Mock / live detection helpers
  3.  MinIO client helper
  4.  Direct DB helpers — record fetch, search, identifier parsing
  5.  CSW fallback helpers
  6.  Result normalisation helpers
  7.  Search view  ← homepage: shows latest 10 when no query is given
  8.  PostGIS table preview helpers
  9.  PostGIS download views (CSV and GeoPackage)
  10. Detail view
  11. MinIO asset streaming view
  12. MinIO file upload
  13. PostGIS spatial data upload
"""

# ── 1. Imports and constants ──────────────────────────────────────────────────

import csv
import json
import re
import tempfile
from pathlib import Path
from urllib.parse import quote_plus

import boto3
import pandas as pd
import psycopg2
import requests
from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse, StreamingHttpResponse
from django.shortcuts import redirect, render
from django.utils.text import get_valid_filename
from django.views.decorators.clickjacking import xframe_options_sameorigin
from psycopg2 import sql
from shapely import wkt as shapely_wkt
from shapely.geometry import Point

from .forms import SpatialUploadForm, UploadForm

# ── Paths to bundled mock data ────────────────────────────────────
# Used when the server is unreachable (e.g. working from home without VPN).
APP_DIR              = Path(__file__).resolve().parent
MOCK_STAC_PATH       = APP_DIR / 'mock_data' / 'sample_stac_response.json'
MOCK_TABLE_ROWS_PATH = APP_DIR / 'mock_data' / 'sample_table_rows.json'
MOCK_FILES_DIR       = APP_DIR / 'mock_data' / 'files'

# ── Column exclusion ──────────────────────────────────────────────
# Geometry columns contain raw WKB hex — not useful to display in the
# table preview and would break column width layout.
GEOMETRY_COLUMNS = {'geom', 'geometry', 'the_geom', 'wkb_geometry', 'shape'}

# ── MIME type sets for preview routing ───────────────────────────
# Used by the detail view to decide which preview widget to render.
IMAGE_FORMATS = {'image/png', 'image/jpeg', 'image/gif', 'image/tiff'}
PDF_FORMATS   = {'application/pdf'}

# ── Upload exclusion lists ────────────────────────────────────────
# Buckets and schemas that are never offered as upload destinations.
# These mirror the exclusions in the ingestion scripts.
SKIP_BUCKETS = {'backups'}
MOCK_BUCKETS = ['surveys', 'reports', 'thumbnails', 'datasets']

SKIP_SCHEMAS = {
    'pg_catalog', 'information_schema', 'pg_toast',
    'pycsw', 'p_pycsw', 'tiger', 'topology', 'public',
}
MOCK_SCHEMAS = ['transport', 'planning', 'environment']

# ── CSV geometry column detection ────────────────────────────────
# When a user uploads a CSV, these column name patterns are checked
# (in order) to locate geometry or coordinate data.
SPATIAL_WKT_COLUMNS = ('wkt', 'geometry', 'geom')
SPATIAL_LAT_COLUMNS = ('lat', 'latitude', 'y')
SPATIAL_LON_COLUMNS = ('lon', 'lng', 'longitude', 'x')

# ── MIME type map for file extension → content type ──────────────
# Used by the asset streaming view to set the correct Content-Type header.
MIME_MAP = {
    '.png':     'image/png',
    '.jpg':     'image/jpeg',
    '.jpeg':    'image/jpeg',
    '.gif':     'image/gif',
    '.pdf':     'application/pdf',
    '.tif':     'image/tiff',
    '.tiff':    'image/tiff',
    '.gpkg':    'application/geopackage+sqlite3',
    '.zip':     'application/zip',
    '.geojson': 'application/geo+json',
    '.nc':      'application/x-netcdf',
    '.las':     'application/vnd.las',
    '.laz':     'application/vnd.laszip',
}

# ── Homepage display limit ────────────────────────────────────────
# When the search page is loaded with no query and no filters, only
# the most recently modified datasets are shown. This keeps the
# homepage fast and focused rather than dumping the entire catalogue.
HOMEPAGE_LATEST_COUNT = 10


# ── 2. Mock / live detection helpers ─────────────────────────────────────────

def _is_stac_mock():
    """
    Returns True when PYCSW_STAC_URL is set to 'mock' in .env.
    In mock mode, catalogue searches return bundled sample data from
    catalogue/mock_data/sample_stac_response.json.
    """
    return settings.PYCSW_STAC_URL.strip().lower() == 'mock'


def _is_minio_mock():
    """
    Returns True when MinIO credentials are absent or placeholder values.
    In mock mode, file uploads are simulated and previews use bundled
    sample files from catalogue/mock_data/files/.
    """
    key = settings.MINIO_ACCESS_KEY or ''
    return not key or key in ('', 'YOUR_MINIO_ACCESS_KEY')


def _is_gis_db_mock():
    """
    Returns True when PostGIS credentials are absent or placeholder values.
    In mock mode, table previews use bundled sample rows and uploads are
    simulated without touching the real database.
    """
    user = settings.GIS_DB_CONFIG.get('user', '')
    return not user or user in ('', 'YOUR_DB_USER')


# ── 3. MinIO client helper ────────────────────────────────────────────────────

def _minio_client():
    """
    Returns a boto3 S3 client pointed at the MinIO endpoint.
    MinIO is S3-compatible so the standard boto3 client works with a
    custom endpoint_url pointing to our internal MinIO server.
    """
    return boto3.client(
        's3',
        endpoint_url=settings.MINIO_ENDPOINT,
        aws_access_key_id=settings.MINIO_ACCESS_KEY,
        aws_secret_access_key=settings.MINIO_SECRET_KEY,
    )


# ── 4. Direct DB helpers ──────────────────────────────────────────────────────

def _db_connect():
    """
    Opens a psycopg2 connection to the GIS database using credentials
    from GIS_DB_CONFIG (populated from .env by settings.py).
    All database queries in this module use this helper so credentials
    are never hardcoded in view logic.
    """
    return psycopg2.connect(**settings.GIS_DB_CONFIG)


def _fetch_record_from_db(identifier):
    """
    Fetches a single record's full metadata directly from p_pycsw.records.

    The CSW Dublin Core response only returns a subset of fields. Many
    important columns — distancevalue (file/table size), distanceuom
    (geometry type), crs, team, organisation — are stored in the database
    but not exposed by the CSW protocol. This function queries them directly
    so the detail page can show complete information.

    Returns a dict of field values, or {} if the record is not found
    or the database is unavailable.
    """
    if _is_gis_db_mock():
        return {}

    try:
        conn = _db_connect()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT
                        distancevalue,      -- file size (MinIO) or table size (PostGIS)
                        distanceuom,        -- geometry type for PostGIS tables
                        crs,                -- coordinate reference system
                        keywords,           -- slash-separated keyword string
                        abstract,           -- human-readable description
                        publisher,          -- contact email
                        creator,            -- team / department
                        organization,       -- organisation name
                        accessconstraints,  -- internal / restricted / public
                        anytext,            -- full-text search blob
                        title,              -- dataset title
                        type,               -- Map / dataset / Report / service
                        format,             -- MIME type or PostGIS/POINT etc.
                        date_modified,      -- last modified timestamp
                        source              -- project name
                    FROM p_pycsw.records
                    WHERE identifier = %s
                    LIMIT 1
                """, (identifier,))
                row = cur.fetchone()
                if not row:
                    return {}
                return {
                    'size':          row[0] or '',
                    'geom_type':     row[1] or '',
                    'crs':           row[2] or '',
                    'keywords_raw':  row[3] or '',
                    'abstract':      row[4] or '',
                    'contact':       row[5] or '',
                    'team':          row[6] or '',
                    'organisation':  row[7] or '',
                    'access':        row[8] or '',
                    'anytext':       row[9] or '',
                    'title':         row[10] or '',
                    'type':          row[11] or '',
                    'format':        row[12] or '',
                    'date_modified': str(row[13]) if row[13] else '',
                    'project':       row[14] or '',
                }
        finally:
            conn.close()
    except psycopg2.Error:
        return {}


def _parse_keywords(keywords_raw):
    """
    Splits a raw keyword string into a clean list.

    Keywords are stored with a slash separator (e.g. 'hospitals/Medway/NHS')
    because commas are not reliable in MinIO tags. This function also handles
    pipe, semicolon, and comma separators for robustness.
    """
    if not keywords_raw:
        return []
    for sep in ['/', '|', ';', ',']:
        if sep in keywords_raw:
            return [k.strip() for k in keywords_raw.split(sep) if k.strip()]
    return [keywords_raw.strip()]


def _identifier_to_source(identifier):
    """
    Parses a record identifier into (source, schema, table, href).

    Identifier format conventions:
      MinIO:   'bucket-name/filename.ext'   → source = 'minio'
      PostGIS: 'schema_name/table_name'     → source = 'postgis'
               (no file extension in the table name part)

    The href is constructed from the identifier so asset links and
    PostGIS connection strings are always consistent.
    """
    parts = identifier.split('/')
    if len(parts) == 2 and '.' not in parts[-1]:
        # PostGIS table — schema/table with no file extension
        schema = parts[0]
        table  = parts[1]
        href   = (
            f"postgresql://{settings.GIS_DB_CONFIG['host']}:"
            f"{settings.GIS_DB_CONFIG['port']}/"
            f"{settings.GIS_DB_CONFIG['dbname']}/{schema}/{table}"
        )
        return 'postgis', schema, table, href
    else:
        # MinIO file — bucket/key (may have multiple path segments)
        bucket = parts[0] if parts else ''
        key    = '/'.join(parts[1:]) if len(parts) > 1 else ''
        base   = settings.MINIO_ENDPOINT.rstrip('/')
        href   = f"{base}/{bucket}/{key}" if bucket and key else ''
        return 'minio', '', '', href


def _row_to_feature(row):
    """
    Converts a single p_pycsw.records database row into a normalised
    feature dict that matches the shape used throughout the portal.

    This internal format is intentionally similar to STAC Items so that
    mock data (real STAC JSON) and live DB data can be processed by the
    same downstream functions without branching.
    """
    identifier   = row[0] or ''
    title        = row[1] or identifier
    abstract     = row[2] or ''
    keywords_raw = row[3] or ''
    rtype        = row[4] or 'dataset'
    fmt          = row[5] or ''
    contact      = row[6] or ''
    team         = row[7] or ''
    org          = row[8] or ''
    access       = row[9] or 'internal'
    size         = row[10] or ''
    geom_type    = row[11] or ''
    crs          = row[12] or ''
    modified     = str(row[13]) if row[13] else ''
    project      = row[14] or ''

    keywords               = _parse_keywords(keywords_raw)
    source, schema, table, href = _identifier_to_source(identifier)

    return {
        'id': identifier,
        'properties': {
            'title':         title,
            'abstract':      abstract,
            'format':        fmt,
            'type':          rtype,
            'contact':       contact,
            'organisation':  org,
            'team':          team,
            'access':        access,
            'project':       project,
            'keywords':      keywords,
            'file_size':     size,
            'table_size':    size,
            'date_modified': modified,
            'schema':        schema,
            'table':         table,
            'crs':           crs,
            'geometry_type': geom_type,
            'row_count':     None,
        },
        'assets': {'data': {'href': href}},
        'bbox':    [-180, -90, 180, 90],
        '_source': source,
    }


def _search_db_directly(query, type_filter, source_filter, access_filter):
    """
    Searches p_pycsw.records using ILIKE on the anytext column.

    anytext is a pre-built full-text blob containing title, abstract,
    keywords, organisation, team, project, AOI, file size, and more.
    ILIKE is case-insensitive so users can search 'Medway' or 'medway'.

    This is the primary search path. It is preferred over CSW because:
      - It returns all columns including size, CRS, and geometry type
      - It supports partial keyword matching
      - It is faster (single SQL query vs HTTP round-trip to pycsw)

    Returns a list of normalised feature dicts, or None if the DB
    is unavailable (which triggers the CSW fallback in search()).
    """
    if _is_gis_db_mock():
        return None  # Signal to caller to use mock / CSW path

    try:
        conn = _db_connect()
        try:
            with conn.cursor() as cur:
                conditions = []
                params     = []

                # Full-text keyword search on the anytext blob
                if query:
                    conditions.append("anytext ILIKE %s")
                    params.append(f'%{query}%')

                # Optional type filter (Map, dataset, Report, service)
                if type_filter:
                    conditions.append("type ILIKE %s")
                    params.append(type_filter)

                # Optional access level filter
                if access_filter:
                    conditions.append("accessconstraints ILIKE %s")
                    params.append(access_filter)

                where_clause = ('WHERE ' + ' AND '.join(conditions)) if conditions else ''

                cur.execute(f"""
                    SELECT
                        identifier,
                        title,
                        abstract,
                        keywords,
                        type,
                        format,
                        publisher,      -- contact email
                        creator,        -- team
                        organization,
                        accessconstraints,
                        distancevalue,  -- size
                        distanceuom,    -- geometry type
                        crs,
                        date_modified,
                        source          -- project name
                    FROM p_pycsw.records
                    {where_clause}
                    ORDER BY
                        COALESCE(date_modified, insert_date) DESC
                    LIMIT 200
                """, params)

                rows = cur.fetchall()
        finally:
            conn.close()
    except psycopg2.Error:
        return None  # DB unreachable — caller will fall back to CSW

    features = []
    for row in rows:
        feature = _row_to_feature(row)
        # Source filter cannot be done in SQL (source is derived from
        # identifier pattern, not stored as a column), so we apply it here.
        if source_filter and feature['_source'] != source_filter:
            continue
        features.append(feature)

    return features


# ── 5. CSW fallback helpers ───────────────────────────────────────────────────

def _load_mock_features():
    """
    Loads the bundled STAC feature collection from mock_data/.
    Used when PYCSW_STAC_URL=mock in .env (offline development).
    """
    with open(MOCK_STAC_PATH, encoding='utf-8') as f:
        return json.load(f).get('features', [])


def _csw_record_to_feature(record):
    """
    Converts a single CSW JSON record dict into the normalised feature format.

    pycsw returns CSW records as JSON when outputformat=application/json
    is requested. The field names use Dublin Core prefixes (dc:, dct:, ows:).
    This function maps those to our internal format so downstream code
    works identically whether data came from the DB or from CSW.

    Note: CSW Dublin Core does not expose distancevalue, distanceuom, or crs.
    Those fields will be empty here — the detail view fetches them directly
    from the DB when needed.
    """
    identifier = record.get('dc:identifier', '')
    title      = record.get('dc:title', identifier)
    abstract   = record.get('dct:abstract', '')
    fmt        = record.get('dc:format', '')
    rtype      = record.get('dc:type', 'dataset')
    contact    = record.get('dc:publisher', '')
    org        = record.get('dc:creator', '')
    access     = record.get('dc:rights', 'internal')
    project    = record.get('dc:source', '')
    modified   = record.get('dct:modified', '')

    keywords = record.get('dc:subject', [])
    if isinstance(keywords, str):
        keywords = [keywords]

    # BoundingBox arrives as "lat lon" pairs (y x order) — swap to lng/lat
    bbox_elem = record.get('ows:BoundingBox', {})
    lower     = bbox_elem.get('ows:LowerCorner', '-90 -180').split()
    upper     = bbox_elem.get('ows:UpperCorner', '90 180').split()
    try:
        bbox = [float(lower[1]), float(lower[0]), float(upper[1]), float(upper[0])]
    except (IndexError, ValueError):
        bbox = [-180, -90, 180, 90]

    source, schema, table, href = _identifier_to_source(identifier)

    return {
        'id': identifier,
        'properties': {
            'title':         title,
            'abstract':      abstract,
            'format':        fmt,
            'type':          rtype,
            'contact':       contact,
            'organisation':  org,
            'team':          '',
            'access':        access,
            'project':       project,
            'keywords':      keywords,
            'file_size':     '',   # not in CSW Dublin Core response
            'table_size':    '',   # not in CSW Dublin Core response
            'date_modified': modified,
            'schema':        schema,
            'table':         table,
            'crs':           '',   # not in CSW Dublin Core response
            'geometry_type': '',   # not in CSW Dublin Core response
            'row_count':     None,
        },
        'assets': {'data': {'href': href}},
        'bbox':    bbox,
        '_source': source,
    }


def _fetch_stac_features(query):
    """
    Queries the pycsw CSW endpoint with JSON output as a fallback search.

    This is used when the direct DB connection is unavailable. The CSW
    GetRecords request with outputformat=application/json returns a JSON
    envelope containing Dublin Core records.

    Returns a list of normalised features, or None if the request fails
    (which the caller interprets as a service unavailable error).
    """
    if _is_stac_mock():
        return _load_mock_features()

    params = {
        'service':        'CSW',
        'version':        '2.0.2',
        'request':        'GetRecords',
        'typenames':      'csw:Record',
        'outputformat':   'application/json',
        'elementsetname': 'full',
        'resulttype':     'results',
        'maxrecords':     '100',
        'outputSchema':   'http://www.opengis.net/cat/csw/2.0.2',
    }

    # Add keyword constraint when a search term is provided
    if query:
        params['constraintlanguage'] = 'CQL_TEXT'
        params['constraint']         = f"AnyText like '%{query}%'"

    try:
        response = requests.get(
            settings.PYCSW_STAC_URL.strip(),
            params=params,
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError):
        return None

    records = (
        data
        .get('csw:GetRecordsResponse', {})
        .get('csw:SearchResults', {})
        .get('csw:Record', [])
    )
    # pycsw returns a dict (not a list) when exactly one record matches
    if isinstance(records, dict):
        records = [records]

    return [_csw_record_to_feature(r) for r in records]


def _fetch_feature_by_id(identifier):
    """
    Returns a single normalised feature by identifier.

    Search order:
      1. Direct DB lookup (fastest, returns all fields)
      2. CSW search (fallback, missing custom fields)
      3. Mock data (offline development)

    Returns None if the record cannot be found by any method.
    """
    # Direct DB lookup first
    db = _fetch_record_from_db(identifier)
    if db:
        source, schema, table, href = _identifier_to_source(identifier)
        return {
            'id': identifier,
            'properties': {
                'title':         db.get('title', identifier),
                'abstract':      db.get('abstract', ''),
                'format':        db.get('format', ''),
                'type':          db.get('type', 'dataset'),
                'contact':       db.get('contact', ''),
                'organisation':  db.get('organisation', ''),
                'team':          db.get('team', ''),
                'access':        db.get('access', 'internal'),
                'project':       db.get('project', ''),
                'keywords':      _parse_keywords(db.get('keywords_raw', '')),
                'file_size':     db.get('size', ''),
                'table_size':    db.get('size', ''),
                'date_modified': db.get('date_modified', ''),
                'schema':        schema,
                'table':         table,
                'crs':           db.get('crs', ''),
                'geometry_type': db.get('geom_type', ''),
                'row_count':     None,
            },
            'assets': {'data': {'href': href}},
            'bbox':    [-180, -90, 180, 90],
            '_source': source,
        }

    # CSW fallback — fetch all and find by id
    if _is_stac_mock():
        for f in _load_mock_features():
            if f.get('id') == identifier:
                return f
        return None

    features = _fetch_stac_features('')
    if features:
        for f in features:
            if f.get('id') == identifier:
                return f
    return None


# ── 6. Result normalisation helpers ──────────────────────────────────────────

def _feature_source(feature):
    """
    Returns the source string ('minio' or 'postgis') for a feature.

    Checks the _source key first (set by _row_to_feature and
    _csw_record_to_feature), then falls back to inspecting the asset href.
    """
    if '_source' in feature:
        return feature['_source']
    href = feature.get('assets', {}).get('data', {}).get('href', '')
    if href.startswith('postgresql://'):
        return 'postgis'
    if href:
        return 'minio'
    return 'unknown'


def _feature_to_result(feature):
    """
    Flattens a feature into a simple dict suitable for the search results list.
    Only includes the fields needed for the result card — not the full detail.
    """
    props = feature.get('properties', {})
    return {
        'identifier':    feature.get('id', ''),
        'title':         props.get('title') or feature.get('id', 'Untitled'),
        'abstract':      props.get('abstract', ''),
        'type':          props.get('type', 'dataset'),
        'format':        props.get('format', ''),
        'organisation':  props.get('organisation', ''),
        'contact':       props.get('contact', ''),
        'access':        props.get('access', 'internal'),
        'keywords':      props.get('keywords') or [],
        'size':          props.get('file_size') or props.get('table_size', ''),
        'source':        _feature_source(feature),
        'href':          feature.get('assets', {}).get('data', {}).get('href', ''),
        'date_modified': props.get('date_modified', ''),
    }


def _feature_to_detail(feature):
    """
    Flattens a feature into a richer dict for the detail page.
    Includes source-specific fields: MIME type info for MinIO records,
    schema/table/CRS/geometry type for PostGIS records.
    """
    props      = feature.get('properties', {})
    identifier = feature.get('id', '')
    source     = _feature_source(feature)

    detail = {
        'identifier':    identifier,
        'title':         props.get('title') or identifier,
        'abstract':      props.get('abstract', ''),
        'type':          props.get('type', 'dataset'),
        'format':        props.get('format', ''),
        'organisation':  props.get('organisation', ''),
        'team':          props.get('team', ''),
        'contact':       props.get('contact', ''),
        'project':       props.get('project', ''),
        'access':        props.get('access', 'internal'),
        'keywords':      props.get('keywords') or [],
        'size':          props.get('file_size') or props.get('table_size', ''),
        'date_modified': props.get('date_modified', ''),
        'source':        source,
    }

    if source == 'minio':
        # MinIO-specific: determine which preview widget to use
        mime_type = props.get('format', '')
        detail.update({
            'mime_type':  mime_type,
            'is_image':   mime_type in IMAGE_FORMATS,
            'is_pdf':     mime_type in PDF_FORMATS,
            'mock_asset': props.get('mock_asset', ''),
        })

    elif source == 'postgis':
        # PostGIS-specific: parse schema/table from identifier if not in props
        parts  = identifier.split('/')
        schema = props.get('schema') or (parts[0] if len(parts) == 2 else '')
        table  = props.get('table')  or (parts[1] if len(parts) == 2 else '')
        detail.update({
            'schema':        schema,
            'table':         table,
            'crs':           props.get('crs', ''),
            'geometry_type': props.get('geometry_type', ''),
            'row_count':     props.get('row_count'),
        })

    return detail


def _matches_query(result, query):
    """
    Client-side keyword filter applied after results are retrieved.
    Used when the CSW fallback is active (DB-side filtering is not available).
    Checks title, abstract, and keywords case-insensitively.
    """
    if not query:
        return True
    q = query.lower()
    return (
        q in result['title'].lower()
        or q in result['abstract'].lower()
        or any(q in kw.lower() for kw in result['keywords'])
    )


# ── 7. Search view ────────────────────────────────────────────────────────────

def search(request):
    """
    Main search and homepage view.

    Homepage behaviour (no query, no filters):
      Shows the HOMEPAGE_LATEST_COUNT most recently modified datasets.
      This keeps the homepage fast and informative without dumping the
      entire catalogue. A banner explains that the list is filtered by
      recency and prompts the user to search for specific data.

    Search behaviour (query or filters present):
      Queries p_pycsw.records directly using ILIKE on the anytext column.
      Falls back to CSW if the database is unavailable.
      Applies source and access filters in Python after retrieval
      (these cannot easily be done in CSW queries).
    """
    query         = request.GET.get('q', '').strip()
    type_filter   = request.GET.get('type', '')
    source_filter = request.GET.get('source', '')
    access_filter = request.GET.get('access', '')

    error          = None
    results        = []
    showing_latest = False  # Controls the homepage banner message

    # ── Primary path: direct DB search ──────────────────────────
    features = _search_db_directly(query, type_filter, source_filter, access_filter)

    if features is None:
        # ── Fallback path: CSW endpoint ──────────────────────────
        features = _fetch_stac_features(query)
        if features is None:
            error = (
                'Could not reach the catalogue search service. '
                'Please try again later.'
            )
        else:
            results = [_feature_to_result(f) for f in features]
            results = [r for r in results if _matches_query(r, query)]
            if type_filter:
                results = [r for r in results if r['type'].lower() == type_filter.lower()]
            if source_filter:
                results = [r for r in results if r['source'] == source_filter]
            if access_filter:
                results = [r for r in results if r['access'].lower() == access_filter.lower()]
    else:
        results = [_feature_to_result(f) for f in features]

    # ── Homepage: show latest N when no search terms are present ─
    # If the user has not typed anything and not selected any filters,
    # limit the results to the most recently modified datasets and sort
    # them newest-first. This makes the homepage a useful "what's new"
    # summary rather than an overwhelming full dump of the catalogue.
    is_homepage = not query and not type_filter and not source_filter and not access_filter
    if is_homepage and not error:
        results = sorted(
            results,
            key=lambda r: r.get('date_modified') or '',
            reverse=True
        )[:HOMEPAGE_LATEST_COUNT]
        showing_latest = True

    context = {
        'query':          query,
        'results':        results,
        'result_count':   len(results),
        'error':          error,
        'type_filter':    type_filter,
        'source_filter':  source_filter,
        'access_filter':  access_filter,
        'using_mock':     _is_stac_mock() and _is_gis_db_mock(),
        'showing_latest': showing_latest,
        'latest_count':   HOMEPAGE_LATEST_COUNT,
    }
    return render(request, 'catalogue/search.html', context)


# ── 8. PostGIS table preview helpers ─────────────────────────────────────────

def _visible_columns(columns):
    """
    Returns column indices that are not geometry columns.
    Geometry columns contain raw WKB hex strings which are not useful
    to display in a table preview and would break the column layout.
    """
    return [i for i, col in enumerate(columns) if col.lower() not in GEOMETRY_COLUMNS]


def _load_mock_table_rows(identifier):
    """
    Loads bundled sample table rows for a PostGIS record in mock mode.
    Sample data lives in catalogue/mock_data/sample_table_rows.json,
    keyed by identifier (schema/table_name).
    """
    with open(MOCK_TABLE_ROWS_PATH, encoding='utf-8') as f:
        tables = json.load(f)
    table = tables.get(identifier)
    if not table:
        return {'error': 'No sample rows are bundled for this table.'}
    visible = _visible_columns(table['columns'])
    return {
        'columns': [table['columns'][i] for i in visible],
        'rows':    [[row[i] for i in visible] for row in table['rows']],
    }


def _fetch_table_preview(item):
    """
    Returns a dict with 'columns' and 'rows' (first 100) for the
    PostGIS table preview on the detail page.

    Uses a parameterised query with psycopg2.sql.Identifier to prevent
    SQL injection — table and schema names are quoted identifiers,
    not string interpolation.
    """
    if _is_gis_db_mock():
        return _load_mock_table_rows(item['identifier'])

    schema = item.get('schema', '')
    table  = item.get('table', '')
    if not schema or not table:
        return {'error': 'This record is missing schema/table metadata.'}

    try:
        conn = _db_connect()
        try:
            with conn.cursor() as cur:
                query = sql.SQL('SELECT * FROM {}.{} LIMIT 100').format(
                    sql.Identifier(schema), sql.Identifier(table)
                )
                cur.execute(query)
                columns = [desc[0] for desc in cur.description]
                rows    = cur.fetchall()
        finally:
            conn.close()
    except psycopg2.Error:
        return {'error': 'Could not connect to the database to preview this table.'}

    visible = _visible_columns(columns)
    return {
        'columns': [columns[i] for i in visible],
        'rows':    [[row[i] for i in visible] for row in rows],
    }


# ── 9. PostGIS download views ─────────────────────────────────────────────────

class _Echo:
    """
    Minimal write-only file object used by csv.writer inside a
    StreamingHttpResponse. Returns each row as a string rather than
    writing to a buffer, which allows Django to stream rows to the
    client as they are fetched from the database.
    """
    def write(self, value):
        return value


def _download_postgis_csv(item, table_name):
    """
    Streams all rows from a PostGIS table as a CSV download.

    Uses a server-side named cursor to fetch rows in batches of 1000
    rather than loading the entire table into memory. This makes large
    table exports memory-safe.

    Geometry columns are excluded — raw WKB hex is not useful in CSV.
    Falls back to the mock sample rows when PostGIS is not configured.
    """
    if _is_gis_db_mock():
        table = _load_mock_table_rows(item['identifier'])
        if table.get('error'):
            raise Http404(table['error'])
        columns, rows = table['columns'], table['rows']
        writer = csv.writer(_Echo())

        def generate():
            yield writer.writerow(columns)
            for row in rows:
                yield writer.writerow(row)

        response = StreamingHttpResponse(generate(), content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{table_name}.csv"'
        return response

    schema   = item.get('schema', '')
    table_id = item.get('table', '')
    if not schema or not table_id:
        raise Http404('This record is missing schema/table metadata.')

    try:
        conn = _db_connect()
    except psycopg2.Error:
        raise Http404('Could not connect to the database.')

    # Named server-side cursor: rows are fetched in batches, not all at once
    cur   = conn.cursor(name='catalogue_csv_export')
    query = sql.SQL('SELECT * FROM {}.{}').format(
        sql.Identifier(schema), sql.Identifier(table_id)
    )
    cur.execute(query)
    columns = [desc[0] for desc in cur.description]
    visible = _visible_columns(columns)
    writer  = csv.writer(_Echo())

    def generate():
        try:
            yield writer.writerow([columns[i] for i in visible])
            while True:
                batch = cur.fetchmany(1000)
                if not batch:
                    break
                for row in batch:
                    yield writer.writerow([row[i] for i in visible])
        finally:
            cur.close()
            conn.close()

    response = StreamingHttpResponse(generate(), content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{table_name}.csv"'
    return response


def _download_postgis_gpkg(item, table_name):
    """
    Exports a PostGIS table as a GeoPackage (.gpkg) file.

    Uses geopandas.read_postgis() to load the full table including
    geometry and then writes a GeoPackage using the fiona engine.
    The CRS is preserved from the original table.

    Note: this loads the entire table into memory. For very large tables
    (> ~500k rows) a chunked export strategy would be needed.

    Falls back to CSV when PostGIS is not configured (no real geometry
    is available in mock mode).
    """
    if _is_gis_db_mock():
        # No real geometry in mock mode — fall back to CSV
        return _download_postgis_csv(item, table_name)

    import geopandas as gpd  # Deferred import: heavy GDAL dependency

    schema   = item.get('schema', '')
    table_id = item.get('table', '')
    if not schema or not table_id:
        raise Http404('This record is missing schema/table metadata.')

    try:
        conn = _db_connect()
        try:
            query = sql.SQL('SELECT * FROM {}.{}').format(
                sql.Identifier(schema), sql.Identifier(table_id)
            )
            gdf = gpd.read_postgis(
                query.as_string(conn),
                conn,
                geom_col='geom',
                crs=item.get('crs') or None,
            )
        finally:
            conn.close()
    except Exception:
        raise Http404('Could not export this table as a GeoPackage.')

    with tempfile.TemporaryDirectory() as tmp_dir:
        gpkg_path = Path(tmp_dir) / f'{table_name}.gpkg'
        gdf.to_file(gpkg_path, driver='GPKG', engine='fiona')
        data = gpkg_path.read_bytes()

    response = HttpResponse(data, content_type='application/geopackage+sqlite3')
    response['Content-Disposition'] = f'attachment; filename="{table_name}.gpkg"'
    return response


def postgis_download_csv(request, identifier):
    """URL-facing view: validates the record then delegates to _download_postgis_csv."""
    feature = _fetch_feature_by_id(identifier)
    if feature is None:
        raise Http404('Record not found.')
    item = _feature_to_detail(feature)
    if item['source'] != 'postgis':
        raise Http404('This record is not a PostGIS table.')
    table_name = item.get('table') or identifier.rsplit('/', 1)[-1]
    return _download_postgis_csv(item, table_name)


def postgis_download_gpkg(request, identifier):
    """URL-facing view: validates the record then delegates to _download_postgis_gpkg."""
    feature = _fetch_feature_by_id(identifier)
    if feature is None:
        raise Http404('Record not found.')
    item = _feature_to_detail(feature)
    if item['source'] != 'postgis':
        raise Http404('This record is not a PostGIS table.')
    table_name = item.get('table') or identifier.rsplit('/', 1)[-1]
    return _download_postgis_gpkg(item, table_name)


# ── 10. Detail view ───────────────────────────────────────────────────────────

def detail(request, identifier):
    """
    Detail page for a single catalogue record.

    Fetches the record by identifier (DB first, then CSW, then mock).
    For PostGIS records, also fetches the first 100 table rows for preview.
    The template renders different widgets depending on the source:
      - MinIO image: <img> tag via the asset streaming view
      - MinIO PDF: <iframe> via the asset streaming view
      - MinIO other: download-only with no preview
      - PostGIS: scrollable data table with GeoPackage and CSV download buttons
    """
    feature = _fetch_feature_by_id(identifier)
    if feature is None:
        raise Http404('Record not found in the catalogue.')

    item = _feature_to_detail(feature)

    context = {
        'item':               item,
        'using_minio_mock':   _is_minio_mock(),
        'using_gis_db_mock':  _is_gis_db_mock(),
    }

    if item['source'] == 'postgis':
        context['table_data'] = _fetch_table_preview(item)

    return render(request, 'catalogue/detail.html', context)


# ── 11. MinIO asset streaming view ────────────────────────────────────────────

@xframe_options_sameorigin
def asset(request, identifier):
    """
    Streams a MinIO file to the browser using Systra credentials.

    Why stream through Django rather than linking directly to MinIO?
      - The MinIO buckets are private (Access Denied on direct URLs).
      - Streaming through Django keeps credentials server-side.
      - The xframe_options_sameorigin decorator allows the PDF iframe
        to embed the file without a clickjacking block.

    The identifier is split on the first slash to get bucket and key.
    No record lookup is needed — we have everything required from the URL.

    ?download=1 query parameter triggers Content-Disposition: attachment
    which forces the browser to download rather than display inline.
    """
    as_attachment = bool(request.GET.get('download'))

    if '/' not in identifier:
        raise Http404('Invalid file identifier.')

    # Split on first slash only — key may contain further slashes
    bucket, key = identifier.split('/', 1)
    filename    = key.rsplit('/', 1)[-1]
    ext         = Path(filename).suffix.lower()
    mime_type   = MIME_MAP.get(ext, 'application/octet-stream')

    if _is_minio_mock():
        # Serve a bundled sample file in mock mode
        feature = _fetch_feature_by_id(identifier)
        if feature is None:
            raise Http404('Record not found in mock data.')
        item      = _feature_to_detail(feature)
        mock_file = item.get('mock_asset', '')
        file_path = MOCK_FILES_DIR / mock_file if mock_file else None
        if not mock_file or not file_path.exists():
            raise Http404('No sample file bundled for this mock record.')
        return FileResponse(
            open(file_path, 'rb'),
            content_type=mime_type,
            as_attachment=as_attachment,
            filename=filename,
        )

    # Live mode: fetch from MinIO using credentials and stream to browser
    try:
        s3  = _minio_client()
        obj = s3.get_object(Bucket=bucket, Key=key)
    except Exception as exc:
        raise Http404(f'Could not retrieve file from MinIO: {exc}')

    response = FileResponse(
        obj['Body'],
        content_type=obj.get('ContentType') or mime_type,
        as_attachment=as_attachment,
        filename=filename,
    )
    if 'ContentLength' in obj:
        response['Content-Length'] = obj['ContentLength']
    return response


# ── 12. MinIO file upload ─────────────────────────────────────────────────────

class UploadError(Exception):
    """
    Raised when an upload step fails.
    The message is surfaced to the user as a form-level error.
    """
    pass


def _list_buckets():
    """
    Returns available MinIO bucket names for the upload form dropdown.
    Excludes buckets listed in SKIP_BUCKETS (e.g. 'backups').
    Returns a mock list when MinIO credentials are not configured.
    """
    if _is_minio_mock():
        return MOCK_BUCKETS
    try:
        response = _minio_client().list_buckets()
    except Exception:
        return []
    return [b['Name'] for b in response.get('Buckets', []) if b['Name'] not in SKIP_BUCKETS]


def _convert_keywords(raw):
    """
    Converts comma-separated form input to slash-separated storage format.

    The upload form accepts commas for user convenience (e.g. "roads, Medway").
    The ingestion scripts and search system split on slash, pipe, or semicolon.
    This conversion ensures the stored value is always parseable.
    Example: "roads, transport, survey" → "roads/transport/survey"
    """
    return '/'.join(k.strip() for k in raw.split(',') if k.strip())


def _perform_upload(data):
    """
    Uploads a file to MinIO and writes all metadata as object tags.

    MinIO object tags are key-value pairs attached to the object.
    The ingestion scripts (ingest_minio.py) read these tags to populate
    the catalogue record. This is why completing all metadata fields
    before upload is enforced — without them, the catalogue record will
    be empty and the file will not be discoverable.

    Tag values are capped at 256 characters (S3/MinIO API limit).
    In mock mode, the upload is simulated without touching MinIO.
    """
    uploaded_file = data['file']
    bucket        = data['bucket']
    filename      = get_valid_filename(uploaded_file.name)

    # Build the tag set from form data
    tags = {k: str(data.get(k, ''))[:256] for k in [
        'title', 'abstract', 'keywords', 'aoi', 'type',
        'organisation', 'team', 'access', 'project', 'contact',
    ]}
    # Convert comma-separated keywords to slash-separated for storage
    tags['keywords'] = _convert_keywords(tags['keywords'])

    mock = _is_minio_mock()

    if not mock:
        try:
            s3 = _minio_client()
            # Upload the file object
            s3.put_object(
                Bucket=bucket,
                Key=filename,
                Body=uploaded_file,
                ContentType=uploaded_file.content_type or 'application/octet-stream',
            )
            # Write metadata tags separately (S3 API design)
            s3.put_object_tagging(
                Bucket=bucket,
                Key=filename,
                Tagging={'TagSet': [{'Key': k, 'Value': v} for k, v in tags.items()]},
            )
        except Exception as exc:
            raise UploadError(str(exc)) from exc

    return {
        'filename': filename,
        'bucket':   bucket,
        'tags':     tags,
        'size':     uploaded_file.size,
        'mock':     mock,
    }


def upload(request):
    """
    MinIO file upload form.

    The form enforces completion of all 10 required metadata fields
    before submission is allowed. This is the primary data governance
    control for MinIO uploads — without it, files would be stored
    without the metadata needed to make them discoverable.

    On successful upload, the result is stored in the session and the
    user is redirected to the success page. Session-based redirect
    prevents form resubmission on page refresh.
    """
    buckets      = _list_buckets()
    bucket_error = None if buckets or _is_minio_mock() else (
        'Could not reach MinIO to list available buckets. Please try again later.'
    )

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES, buckets=buckets)
        if form.is_valid():
            try:
                result = _perform_upload(form.cleaned_data)
            except UploadError as exc:
                form.add_error(None, f'Upload failed: {exc}')
            else:
                request.session['upload_result'] = result
                return redirect('catalogue:upload_success')
    else:
        form = UploadForm(buckets=buckets)

    return render(request, 'catalogue/upload.html', {
        'form':             form,
        'bucket_error':     bucket_error,
        'using_minio_mock': _is_minio_mock(),
    })


def upload_success(request):
    """
    Success confirmation page after a MinIO upload.

    Pops the result from the session so that refreshing the page
    redirects back to the upload form rather than showing stale data.
    This prevents the confusing "already uploaded" impression.
    """
    result = request.session.pop('upload_result', None)
    if result is None:
        return redirect('catalogue:upload')
    return render(request, 'catalogue/upload_success.html', {'result': result})


# ── 13. PostGIS spatial data upload ──────────────────────────────────────────

def _list_schemas():
    """
    Returns available PostGIS schema names for the spatial upload form.
    Excludes system schemas and the pycsw catalogue schema.
    Returns a mock list when PostGIS credentials are not configured.
    """
    if _is_gis_db_mock():
        return MOCK_SCHEMAS
    try:
        conn = _db_connect()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    'SELECT schema_name FROM information_schema.schemata '
                    'WHERE schema_name != ALL(%s) ORDER BY schema_name',
                    (list(SKIP_SCHEMAS),),
                )
                return [row[0] for row in cur.fetchall()]
        finally:
            conn.close()
    except psycopg2.Error:
        return []


def _generate_table_name(filename):
    """
    Creates a valid PostgreSQL table name from an uploaded filename.

    Rules applied:
      - Strip the file extension
      - Replace non-alphanumeric characters with underscores
      - Collapse multiple underscores
      - Ensure the name starts with a letter (prefix 'tbl_' if not)
      - Truncate to 63 characters (PostgreSQL identifier limit)
    """
    stem = Path(filename).stem
    name = re.sub(r'[^a-zA-Z0-9]+', '_', stem).strip('_').lower()
    name = re.sub(r'_+', '_', name)
    if not name or not name[0].isalpha():
        name = f'tbl_{name}' if name else 'uploaded_table'
    return name[:63]


def _unique_table_name(schema, base_name):
    """
    Ensures the generated table name does not already exist in the schema.
    Appends _2, _3, etc. until a unique name is found.
    """
    conn = _db_connect()
    try:
        with conn.cursor() as cur:
            cur.execute(
                'SELECT table_name FROM information_schema.tables WHERE table_schema = %s',
                (schema,),
            )
            existing = {row[0] for row in cur.fetchall()}
    finally:
        conn.close()

    if base_name not in existing:
        return base_name
    n = 2
    while f'{base_name}_{n}' in existing:
        n += 1
    return f'{base_name}_{n}'


def _geodataframe_from_csv(uploaded_file):
    """
    Reads a CSV file and constructs a GeoDataFrame.

    Geometry detection order:
      1. A column named 'wkt', 'geometry', or 'geom' containing WKT strings
      2. Separate lat/lon columns for point data creation

    Raises UploadError if no geometry can be found or parsed.
    """
    import geopandas as gpd  # Deferred import: heavy GDAL dependency

    df         = pd.read_csv(uploaded_file)
    lower_cols = {c.lower(): c for c in df.columns}

    # Try WKT column first
    wkt_col = next((lower_cols[n] for n in SPATIAL_WKT_COLUMNS if n in lower_cols), None)
    if wkt_col:
        try:
            geometry = df[wkt_col].apply(shapely_wkt.loads)
        except Exception as exc:
            raise UploadError(f"Could not parse WKT in column '{wkt_col}': {exc}") from exc
        return gpd.GeoDataFrame(df.drop(columns=[wkt_col]), geometry=geometry, crs='EPSG:4326')

    # Try lat/lon columns for point data
    lat_col = next((lower_cols[n] for n in SPATIAL_LAT_COLUMNS if n in lower_cols), None)
    lon_col = next((lower_cols[n] for n in SPATIAL_LON_COLUMNS if n in lower_cols), None)
    if lat_col and lon_col:
        try:
            geometry = [Point(xy) for xy in zip(df[lon_col], df[lat_col])]
        except Exception as exc:
            raise UploadError(f'Could not build geometry from columns: {exc}') from exc
        return gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')

    raise UploadError(
        "Could not find a geometry column or latitude/longitude columns in the CSV."
    )


def _read_spatial_file(uploaded_file):
    """
    Reads a GeoPackage, GeoJSON, or CSV upload into a GeoDataFrame.

    GeoPackage and GeoJSON require a real file path (fiona cannot read
    from an in-memory buffer), so they are written to a temp directory
    first. CSV is handled by _geodataframe_from_csv which reads from
    the in-memory upload directly.
    """
    import geopandas as gpd  # Deferred import: heavy GDAL dependency

    ext = Path(uploaded_file.name).suffix.lower()

    if ext == '.csv':
        return _geodataframe_from_csv(uploaded_file)

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir) / uploaded_file.name
        with open(tmp_path, 'wb') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)
        try:
            gdf = gpd.read_file(tmp_path, engine='fiona')
        except Exception as exc:
            raise UploadError(f'Could not read file as spatial data: {exc}') from exc

    if gdf.crs is None:
        raise UploadError('The uploaded file has no CRS defined.')
    return gdf


def _geometry_type_string(gdf):
    """Returns a single geometry type string for the GeoDataFrame."""
    types = gdf.geom_type.dropna().unique()
    return types[0].upper() if len(types) == 1 else 'GEOMETRY'


def _crs_string(gdf):
    """Returns EPSG:XXXX string or the CRS WKT if no EPSG code is available."""
    if gdf.crs is None:
        return ''
    epsg = gdf.crs.to_epsg()
    return f'EPSG:{epsg}' if epsg else gdf.crs.to_string()


def _write_geodataframe_to_postgis(gdf, schema, table_name):
    """
    Writes a GeoDataFrame to PostGIS using SQLAlchemy + geopandas.to_postgis().

    The fiona PostgreSQL driver is not compiled into the bundled GDAL wheel
    on Linux, so geopandas.to_postgis() (which uses SQLAlchemy) is the
    only reliable write path. Credentials are URL-encoded to handle the
    pokaro@systra.info username which contains a special character.
    """
    from sqlalchemy import create_engine

    cfg = settings.GIS_DB_CONFIG
    url = (
        f"postgresql+psycopg2://{quote_plus(cfg['user'])}:{quote_plus(cfg['password'])}"
        f"@{cfg['host']}:{cfg['port']}/{cfg['dbname']}?sslmode={cfg['sslmode']}"
    )
    engine = create_engine(url)
    try:
        gdf.to_postgis(table_name, engine, schema=schema, if_exists='fail', index=False)
    finally:
        engine.dispose()


def _write_table_comment(schema, table_name, comment_text):
    """
    Writes the structured metadata comment to the PostgreSQL table.

    The comment format (key: value lines) matches exactly what
    parse_comment() in ingest_postgis.py reads. This ensures that
    a table uploaded via the web portal is automatically picked up
    and catalogued on the next scheduled ingestion run.
    """
    conn = _db_connect()
    try:
        with conn.cursor() as cur:
            query = sql.SQL('COMMENT ON TABLE {}.{} IS %s').format(
                sql.Identifier(schema), sql.Identifier(table_name)
            )
            cur.execute(query, (comment_text,))
        conn.commit()
    finally:
        conn.close()


def _comment_safe(value):
    """
    Collapses multi-line or multi-space values to a single line.
    parse_comment() reads one key: value per line, so values must not
    contain newlines.
    """
    return ' '.join(value.split())


def _perform_spatial_upload(data):
    """
    Reads the uploaded spatial file, writes it to PostGIS, and applies
    the structured metadata comment so the ingestion script catalogues it.

    Steps:
      1. Read the file into a GeoDataFrame (auto-detects CRS and geometry type)
      2. Generate a unique table name from the filename
      3. Write the GeoDataFrame to the target schema in PostGIS
      4. Write the structured comment so ingest_postgis.py finds this table
      5. Return a result dict for the success page

    In mock mode, steps 3 and 4 are skipped but the file is still parsed
    so accurate stats (row count, CRS, geometry type) are shown.
    """
    uploaded_file   = data['file']
    schema          = data['schema']
    base_table_name = _generate_table_name(uploaded_file.name)

    gdf = _read_spatial_file(uploaded_file)
    if gdf.empty:
        raise UploadError('The uploaded file contains no rows.')

    row_count     = len(gdf)
    geometry_type = _geometry_type_string(gdf)
    crs           = _crs_string(gdf)

    # Build the structured comment in the exact format parse_comment() expects.
    # Each line is "key: value" — one per metadata field.
    metadata = {k: _comment_safe(str(data.get(k, ''))) for k in [
        'title', 'abstract', 'type', 'access',
        'organisation', 'project', 'contact', 'aoi', 'team',
    ]}
    metadata['keywords'] = _comment_safe(_convert_keywords(data.get('keywords', '')))
    comment_text = '\n'.join(f'{k}: {v}' for k, v in metadata.items())

    mock = _is_gis_db_mock()

    if mock:
        table_name = base_table_name
    else:
        try:
            table_name = _unique_table_name(schema, base_table_name)
            _write_geodataframe_to_postgis(gdf, schema, table_name)
            _write_table_comment(schema, table_name, comment_text)
        except UploadError:
            raise
        except Exception as exc:
            raise UploadError(str(exc)) from exc

    return {
        'schema':        schema,
        'table_name':    table_name,
        'row_count':     row_count,
        'crs':           crs,
        'geometry_type': geometry_type,
        'metadata':      metadata,
        'comment':       comment_text,
        'mock':          mock,
    }


def spatial_upload(request):
    """
    PostGIS spatial data upload form.

    Accepts GeoPackage (.gpkg), GeoJSON (.geojson), and CSV files
    with WKT or lat/lon columns. All 10 metadata fields must be
    completed before submission is allowed — the form enforces this
    at the Django form validation level.

    On success, stores the result in the session and redirects to
    the success page. The structured comment written to the PostGIS
    table ensures the next scheduled ingest run catalogues the upload
    automatically without any manual intervention.
    """
    schemas      = _list_schemas()
    schema_error = None if schemas or _is_gis_db_mock() else (
        'Could not reach PostGIS to list available schemas. Please try again later.'
    )

    if request.method == 'POST':
        form = SpatialUploadForm(request.POST, request.FILES, schemas=schemas)
        if form.is_valid():
            try:
                result = _perform_spatial_upload(form.cleaned_data)
            except UploadError as exc:
                form.add_error(None, f'Upload failed: {exc}')
            else:
                request.session['spatial_upload_result'] = result
                return redirect('catalogue:spatial_upload_success')
    else:
        form = SpatialUploadForm(schemas=schemas)

    return render(request, 'catalogue/upload_spatial.html', {
        'form':              form,
        'schema_error':      schema_error,
        'using_gis_db_mock': _is_gis_db_mock(),
    })


def spatial_upload_success(request):
    """
    Success confirmation page after a PostGIS spatial upload.
    Pops the session result to prevent stale data on refresh.
    """
    result = request.session.pop('spatial_upload_result', None)
    if result is None:
        return redirect('catalogue:spatial_upload')
    return render(request, 'catalogue/upload_spatial_success.html', {'result': result})