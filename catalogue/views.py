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

APP_DIR = Path(__file__).resolve().parent
MOCK_STAC_PATH = APP_DIR / 'mock_data' / 'sample_stac_response.json'
MOCK_TABLE_ROWS_PATH = APP_DIR / 'mock_data' / 'sample_table_rows.json'
MOCK_FILES_DIR = APP_DIR / 'mock_data' / 'files'

# Columns hidden from the PostGIS row preview — raw WKB isn't useful in a table.
GEOMETRY_COLUMNS = {'geom', 'geometry', 'the_geom', 'wkb_geometry', 'shape'}

IMAGE_FORMATS = {'image/png', 'image/jpeg', 'image/gif'}
PDF_FORMATS = {'application/pdf'}

# Matches ingest_minio.py.template's SKIP_BUCKETS — never offered as an upload target.
SKIP_BUCKETS = {'backups'}
MOCK_BUCKETS = ['surveys', 'reports', 'thumbnails', 'datasets']

# Matches ingest_postgis.py.template's SKIP_SCHEMAS — 'public' holds Django's own
# tables and 'pycsw' holds the catalogue itself, so neither is a valid upload target.
SKIP_SCHEMAS = {'pg_catalog', 'information_schema', 'pg_toast', 'pycsw', 'tiger', 'topology', 'public'}
MOCK_SCHEMAS = ['transport', 'planning', 'environment']

SPATIAL_WKT_COLUMNS = ('wkt', 'geometry', 'geom')
SPATIAL_LAT_COLUMNS = ('lat', 'latitude', 'y')
SPATIAL_LON_COLUMNS = ('lon', 'lng', 'longitude', 'x')


def _is_stac_mock():
    return settings.PYCSW_STAC_URL.strip().lower() == 'mock'


def _is_minio_mock():
    return not settings.MINIO_ACCESS_KEY or settings.MINIO_ACCESS_KEY == 'YOUR_MINIO_ACCESS_KEY'


def _is_gis_db_mock():
    user = settings.GIS_DB_CONFIG.get('user', '')
    return not user or user == 'YOUR_DB_USER'


def _minio_client():
    return boto3.client(
        's3',
        endpoint_url=settings.MINIO_ENDPOINT,
        aws_access_key_id=settings.MINIO_ACCESS_KEY,
        aws_secret_access_key=settings.MINIO_SECRET_KEY,
    )


def _load_mock_features():
    with open(MOCK_STAC_PATH, encoding='utf-8') as f:
        return json.load(f).get('features', [])


def _fetch_stac_features(query):
    """Return a list of STAC features, or None if the live search failed."""
    if _is_stac_mock():
        return _load_mock_features()

    stac_url = settings.PYCSW_STAC_URL.strip()
    try:
        response = requests.get(
            f"{stac_url.rstrip('/')}/search",
            params={'q': query, 'limit': 100} if query else {'limit': 100},
            timeout=10,
        )
        response.raise_for_status()
        return response.json().get('features', [])
    except (requests.RequestException, ValueError):
        return None


def _fetch_feature_by_id(identifier):
    """Return the single STAC feature matching identifier, or None."""
    if _is_stac_mock():
        for feature in _load_mock_features():
            if feature.get('id') == identifier:
                return feature
        return None

    stac_url = settings.PYCSW_STAC_URL.strip()
    try:
        response = requests.get(
            f"{stac_url.rstrip('/')}/search",
            params={'ids': identifier, 'limit': 1},
            timeout=10,
        )
        response.raise_for_status()
        features = response.json().get('features', [])
        return features[0] if features else None
    except (requests.RequestException, ValueError):
        return None


def _feature_source(feature):
    """MinIO items link with an http(s) href; PostGIS items with postgresql://."""
    href = feature.get('assets', {}).get('data', {}).get('href', '')
    if href.startswith('postgresql://'):
        return 'postgis'
    if href:
        return 'minio'
    return 'unknown'


def _feature_to_result(feature):
    props = feature.get('properties', {})

    return {
        'identifier': feature.get('id', ''),
        'title': props.get('title') or feature.get('id', 'Untitled'),
        'abstract': props.get('abstract', ''),
        'type': props.get('type', 'dataset'),
        'format': props.get('format', ''),
        'organisation': props.get('organisation', ''),
        'contact': props.get('contact', ''),
        'access': props.get('access', 'internal'),
        'keywords': props.get('keywords') or [],
        'size': props.get('file_size') or props.get('table_size', ''),
        'source': _feature_source(feature),
        'href': feature.get('assets', {}).get('data', {}).get('href', ''),
        'date_modified': props.get('date_modified', ''),
    }


def _feature_to_detail(feature):
    props = feature.get('properties', {})
    identifier = feature.get('id', '')
    source = _feature_source(feature)

    detail = {
        'identifier': identifier,
        'title': props.get('title') or identifier,
        'abstract': props.get('abstract', ''),
        'type': props.get('type', 'dataset'),
        'format': props.get('format', ''),
        'organisation': props.get('organisation', ''),
        'team': props.get('team', ''),
        'contact': props.get('contact', ''),
        'project': props.get('project', ''),
        'access': props.get('access', 'internal'),
        'keywords': props.get('keywords') or [],
        'size': props.get('file_size') or props.get('table_size', ''),
        'date_modified': props.get('date_modified', ''),
        'source': source,
    }

    if source == 'minio':
        mime_type = props.get('format', '')
        detail.update({
            'mime_type': mime_type,
            'is_image': mime_type in IMAGE_FORMATS,
            'is_pdf': mime_type in PDF_FORMATS,
            'mock_asset': props.get('mock_asset', ''),
        })
    elif source == 'postgis':
        detail.update({
            'schema': props.get('schema', ''),
            'table': props.get('table', ''),
            'crs': props.get('crs', ''),
            'geometry_type': props.get('geometry_type', ''),
            'row_count': props.get('row_count'),
        })

    return detail


def _matches_query(result, query):
    if not query:
        return True
    q = query.lower()
    return (
        q in result['title'].lower()
        or q in result['abstract'].lower()
        or any(q in keyword.lower() for keyword in result['keywords'])
    )


def search(request):
    query = request.GET.get('q', '').strip()
    type_filter = request.GET.get('type', '')
    source_filter = request.GET.get('source', '')
    access_filter = request.GET.get('access', '')

    features = _fetch_stac_features(query)
    error = None
    results = []

    if features is None:
        error = 'Could not reach the catalogue search service. Please try again later.'
    else:
        results = [_feature_to_result(feature) for feature in features]
        results = [r for r in results if _matches_query(r, query)]

        if type_filter:
            results = [r for r in results if r['type'].lower() == type_filter.lower()]
        if source_filter:
            results = [r for r in results if r['source'] == source_filter]
        if access_filter:
            results = [r for r in results if r['access'].lower() == access_filter.lower()]

    context = {
        'query': query,
        'results': results,
        'result_count': len(results),
        'error': error,
        'type_filter': type_filter,
        'source_filter': source_filter,
        'access_filter': access_filter,
        'using_mock': _is_stac_mock(),
    }
    return render(request, 'catalogue/search.html', context)


def _visible_columns(columns):
    return [i for i, col in enumerate(columns) if col.lower() not in GEOMETRY_COLUMNS]


def _load_mock_table_rows(identifier):
    with open(MOCK_TABLE_ROWS_PATH, encoding='utf-8') as f:
        tables = json.load(f)

    table = tables.get(identifier)
    if not table:
        return {'error': 'No sample rows are bundled for this table.'}

    visible = _visible_columns(table['columns'])
    return {
        'columns': [table['columns'][i] for i in visible],
        'rows': [[row[i] for i in visible] for row in table['rows']],
    }


def _fetch_table_preview(item):
    if _is_gis_db_mock():
        return _load_mock_table_rows(item['identifier'])

    schema, table = item.get('schema', ''), item.get('table', '')
    if not schema or not table:
        return {'error': 'This record is missing schema/table metadata.'}

    try:
        conn = psycopg2.connect(**settings.GIS_DB_CONFIG)
        try:
            with conn.cursor() as cur:
                query = sql.SQL('SELECT * FROM {}.{} LIMIT 100').format(
                    sql.Identifier(schema), sql.Identifier(table)
                )
                cur.execute(query)
                columns = [desc[0] for desc in cur.description]
                rows = cur.fetchall()
        finally:
            conn.close()
    except psycopg2.Error:
        return {'error': 'Could not connect to the database to preview this table.'}

    visible = _visible_columns(columns)
    return {
        'columns': [columns[i] for i in visible],
        'rows': [[row[i] for i in visible] for row in rows],
    }


class _Echo:
    """A file-like object that hands back whatever csv.writer sends it, for streaming."""

    def write(self, value):
        return value


def _download_postgis_csv(item, table_name):
    """Streams every row of the table as CSV, geometry columns excluded."""
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

    schema, table_id = item.get('schema', ''), item.get('table', '')
    if not schema or not table_id:
        raise Http404('This record is missing schema/table metadata.')

    try:
        conn = psycopg2.connect(**settings.GIS_DB_CONFIG)
    except psycopg2.Error:
        raise Http404('Could not connect to the database to export this table.')

    cur = conn.cursor(name='catalogue_csv_export')  # server-side cursor: streams instead of loading all rows
    query = sql.SQL('SELECT * FROM {}.{}').format(sql.Identifier(schema), sql.Identifier(table_id))
    cur.execute(query)
    columns = [desc[0] for desc in cur.description]
    visible = _visible_columns(columns)

    writer = csv.writer(_Echo())

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
    """Exports every row, including geometry, as a GeoPackage preserving CRS."""
    if _is_gis_db_mock():
        # No real geometry available offline — fall back to the CSV export.
        return _download_postgis_csv(item, table_name)

    import geopandas as gpd  # deferred: heavy GDAL-backed import, only needed on this path

    schema, table_id = item.get('schema', ''), item.get('table', '')
    if not schema or not table_id:
        raise Http404('This record is missing schema/table metadata.')

    try:
        conn = psycopg2.connect(**settings.GIS_DB_CONFIG)
        try:
            query = sql.SQL('SELECT * FROM {}.{}').format(
                sql.Identifier(schema), sql.Identifier(table_id)
            )
            gdf = gpd.read_postgis(
                query.as_string(conn), conn, geom_col='geom', crs=item.get('crs') or None
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
    feature = _fetch_feature_by_id(identifier)
    if feature is None:
        raise Http404('Record not found in the catalogue.')

    item = _feature_to_detail(feature)
    if item['source'] != 'postgis':
        raise Http404('This record is not a PostGIS table.')

    table_name = item.get('table') or identifier.rsplit('/', 1)[-1]
    return _download_postgis_csv(item, table_name)


def postgis_download_gpkg(request, identifier):
    feature = _fetch_feature_by_id(identifier)
    if feature is None:
        raise Http404('Record not found in the catalogue.')

    item = _feature_to_detail(feature)
    if item['source'] != 'postgis':
        raise Http404('This record is not a PostGIS table.')

    table_name = item.get('table') or identifier.rsplit('/', 1)[-1]
    return _download_postgis_gpkg(item, table_name)


def detail(request, identifier):
    feature = _fetch_feature_by_id(identifier)
    if feature is None:
        raise Http404('Record not found in the catalogue.')

    item = _feature_to_detail(feature)
    context = {
        'item': item,
        'using_minio_mock': _is_minio_mock(),
        'using_gis_db_mock': _is_gis_db_mock(),
    }

    if item['source'] == 'postgis':
        context['table_data'] = _fetch_table_preview(item)

    return render(request, 'catalogue/detail.html', context)


@xframe_options_sameorigin
def asset(request, identifier):
    """Streams a MinIO file inline (for preview) or as an attachment (?download=1)."""
    feature = _fetch_feature_by_id(identifier)
    if feature is None:
        raise Http404('Record not found in the catalogue.')

    item = _feature_to_detail(feature)
    if item['source'] != 'minio':
        raise Http404('This record has no downloadable file.')

    as_attachment = bool(request.GET.get('download'))
    filename = identifier.rsplit('/', 1)[-1]
    mime_type = item.get('mime_type') or 'application/octet-stream'

    if _is_minio_mock():
        mock_filename = item.get('mock_asset', '')
        file_path = MOCK_FILES_DIR / mock_filename if mock_filename else None
        if not mock_filename or not file_path.exists():
            raise Http404('No sample file bundled for this mock record.')
        return FileResponse(
            open(file_path, 'rb'),
            content_type=mime_type,
            as_attachment=as_attachment,
            filename=filename,
        )

    bucket, _, key = identifier.partition('/')
    try:
        obj = _minio_client().get_object(Bucket=bucket, Key=key)
    except Exception:
        raise Http404('Could not retrieve the file from MinIO.')

    response = FileResponse(
        obj['Body'],
        content_type=obj.get('ContentType') or mime_type,
        as_attachment=as_attachment,
        filename=filename,
    )
    if 'ContentLength' in obj:
        response['Content-Length'] = obj['ContentLength']
    return response


class UploadError(Exception):
    pass


def _list_buckets():
    if _is_minio_mock():
        return MOCK_BUCKETS

    try:
        response = _minio_client().list_buckets()
    except Exception:
        return []

    return [b['Name'] for b in response.get('Buckets', []) if b['Name'] not in SKIP_BUCKETS]


def _convert_keywords(raw):
    """Form input is comma-separated; ingest scripts split on '/', '|', or ';'."""
    return '/'.join(k.strip() for k in raw.split(',') if k.strip())


def _perform_upload(data):
    uploaded_file = data['file']
    bucket = data['bucket']
    filename = get_valid_filename(uploaded_file.name)

    tags = {
        'title': data['title'],
        'abstract': data['abstract'],
        'keywords': _convert_keywords(data['keywords']),
        'aoi': data['aoi'],
        'type': data['type'],
        'organisation': data['organisation'],
        'team': data['team'],
        'access': data['access'],
        'project': data['project'],
        'contact': data['contact'],
    }
    # MinIO/S3 object tag values are capped at 256 characters.
    tags = {key: value[:256] for key, value in tags.items()}

    mock = _is_minio_mock()

    if not mock:
        try:
            s3 = _minio_client()
            s3.put_object(
                Bucket=bucket,
                Key=filename,
                Body=uploaded_file,
                ContentType=uploaded_file.content_type or 'application/octet-stream',
            )
            s3.put_object_tagging(
                Bucket=bucket,
                Key=filename,
                Tagging={'TagSet': [{'Key': k, 'Value': v} for k, v in tags.items()]},
            )
        except Exception as exc:
            raise UploadError(str(exc)) from exc

    return {
        'filename': filename,
        'bucket': bucket,
        'tags': tags,
        'size': uploaded_file.size,
        'mock': mock,
    }


def upload(request):
    buckets = _list_buckets()
    bucket_error = None
    if not buckets and not _is_minio_mock():
        bucket_error = 'Could not reach MinIO to list available buckets. Please try again later.'

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

    context = {
        'form': form,
        'bucket_error': bucket_error,
        'using_minio_mock': _is_minio_mock(),
    }
    return render(request, 'catalogue/upload.html', context)


def upload_success(request):
    result = request.session.pop('upload_result', None)
    if result is None:
        return redirect('catalogue:upload')
    return render(request, 'catalogue/upload_success.html', {'result': result})


def _list_schemas():
    if _is_gis_db_mock():
        return MOCK_SCHEMAS

    try:
        conn = psycopg2.connect(**settings.GIS_DB_CONFIG)
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
    stem = Path(filename).stem
    name = re.sub(r'[^a-zA-Z0-9]+', '_', stem).strip('_').lower()
    name = re.sub(r'_+', '_', name)
    if not name or not name[0].isalpha():
        name = f'tbl_{name}' if name else 'uploaded_table'
    return name[:63]


def _unique_table_name(schema, base_name):
    conn = psycopg2.connect(**settings.GIS_DB_CONFIG)
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
    import geopandas as gpd  # deferred: heavy GDAL-backed import

    df = pd.read_csv(uploaded_file)
    lower_cols = {c.lower(): c for c in df.columns}

    wkt_col = next((lower_cols[name] for name in SPATIAL_WKT_COLUMNS if name in lower_cols), None)
    if wkt_col:
        try:
            geometry = df[wkt_col].apply(shapely_wkt.loads)
        except Exception as exc:
            raise UploadError(f"Could not parse WKT geometry in column '{wkt_col}': {exc}") from exc
        return gpd.GeoDataFrame(df.drop(columns=[wkt_col]), geometry=geometry, crs='EPSG:4326')

    lat_col = next((lower_cols[name] for name in SPATIAL_LAT_COLUMNS if name in lower_cols), None)
    lon_col = next((lower_cols[name] for name in SPATIAL_LON_COLUMNS if name in lower_cols), None)
    if lat_col and lon_col:
        try:
            geometry = [Point(xy) for xy in zip(df[lon_col], df[lat_col])]
        except Exception as exc:
            raise UploadError(f'Could not build point geometry from {lon_col}/{lat_col}: {exc}') from exc
        return gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')

    raise UploadError(
        "Could not find a 'wkt'/'geometry' column or latitude/longitude columns in the CSV."
    )


def _read_spatial_file(uploaded_file):
    import geopandas as gpd  # deferred: heavy GDAL-backed import

    ext = Path(uploaded_file.name).suffix.lower()

    if ext == '.csv':
        return _geodataframe_from_csv(uploaded_file)

    # GeoPackage / GeoJSON: geopandas reads geometry + CRS natively via fiona.
    # fiona needs a real file on disk, not an in-memory upload.
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir) / uploaded_file.name
        with open(tmp_path, 'wb') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)
        try:
            gdf = gpd.read_file(tmp_path, engine='fiona')
        except Exception as exc:
            raise UploadError(f'Could not read the uploaded file as spatial data: {exc}') from exc

    if gdf.crs is None:
        raise UploadError('The uploaded file has no coordinate reference system (CRS) defined.')

    return gdf


def _geometry_type_string(gdf):
    types = gdf.geom_type.dropna().unique()
    if len(types) == 1:
        return types[0].upper()
    return 'GEOMETRY'


def _crs_string(gdf):
    if gdf.crs is None:
        return ''
    epsg = gdf.crs.to_epsg()
    return f'EPSG:{epsg}' if epsg else gdf.crs.to_string()


def _write_geodataframe_to_postgis(gdf, schema, table_name):
    # fiona's PostgreSQL/OGR driver isn't compiled into the bundled GDAL wheel, so
    # geopandas needs SQLAlchemy + GeoAlchemy2 (its documented alternative) to write.
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
    conn = psycopg2.connect(**settings.GIS_DB_CONFIG)
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
    """Keeps a value to one physical line — parse_comment() reads one 'key: value' per line."""
    return ' '.join(value.split())


def _perform_spatial_upload(data):
    uploaded_file = data['file']
    schema = data['schema']
    base_table_name = _generate_table_name(uploaded_file.name)

    gdf = _read_spatial_file(uploaded_file)
    if gdf.empty:
        raise UploadError('The uploaded file contains no rows.')

    row_count = len(gdf)
    geometry_type = _geometry_type_string(gdf)
    crs = _crs_string(gdf)

    metadata = {
        'title': _comment_safe(data['title']),
        'abstract': _comment_safe(data['abstract']),
        'keywords': _comment_safe(_convert_keywords(data['keywords'])),
        'type': _comment_safe(data['type']),
        'access': _comment_safe(data['access']),
        'organisation': _comment_safe(data['organisation']),
        'project': _comment_safe(data['project']),
        'contact': _comment_safe(data['contact']),
        'aoi': _comment_safe(data['aoi']),
        'team': _comment_safe(data['team']),
    }
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
        'schema': schema,
        'table_name': table_name,
        'row_count': row_count,
        'crs': crs,
        'geometry_type': geometry_type,
        'metadata': metadata,
        'comment': comment_text,
        'mock': mock,
    }


def spatial_upload(request):
    schemas = _list_schemas()
    schema_error = None
    if not schemas and not _is_gis_db_mock():
        schema_error = 'Could not reach PostGIS to list available schemas. Please try again later.'

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

    context = {
        'form': form,
        'schema_error': schema_error,
        'using_gis_db_mock': _is_gis_db_mock(),
    }
    return render(request, 'catalogue/upload_spatial.html', context)


def spatial_upload_success(request):
    result = request.session.pop('spatial_upload_result', None)
    if result is None:
        return redirect('catalogue:spatial_upload')
    return render(request, 'catalogue/upload_spatial_success.html', {'result': result})
