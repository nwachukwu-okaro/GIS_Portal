import json
from pathlib import Path

import requests
from django.conf import settings
from django.shortcuts import render

MOCK_STAC_PATH = Path(__file__).resolve().parent / 'mock_data' / 'sample_stac_response.json'


def _load_mock_features():
    with open(MOCK_STAC_PATH, encoding='utf-8') as f:
        return json.load(f).get('features', [])


def _fetch_stac_features(query):
    """Return a list of STAC features, or None if the live search failed."""
    stac_url = settings.PYCSW_STAC_URL.strip()

    if stac_url.lower() == 'mock':
        return _load_mock_features()

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
        'using_mock': settings.PYCSW_STAC_URL.strip().lower() == 'mock',
    }
    return render(request, 'catalogue/search.html', context)
