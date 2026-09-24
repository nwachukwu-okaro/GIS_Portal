from django.urls import path

from . import views

app_name = 'catalogue'

urlpatterns = [
    path('', views.search, name='search'),
    path('tiles/osm/<int:z>/<int:x>/<int:y>.png', views.osm_tile_proxy, name='osm_tile_proxy'),
    path('spatial-analysis/', views.spatial_analysis, name='spatial_analysis'),
    path('spatial-analysis/api/schemas/', views.spatial_schemas_api, name='spatial_schemas_api'),
    path('spatial-analysis/api/tables/', views.spatial_tables_api, name='spatial_tables_api'),
    path('spatial-analysis/api/table-data/', views.spatial_table_data_api, name='spatial_table_data_api'),
    path('spatial-analysis/api/table-columns/', views.spatial_table_columns_api, name='spatial_table_columns_api'),
    path('spatial-analysis/api/run-operation/', views.spatial_run_operation_api, name='spatial_run_operation_api'),
    path('spatial-analysis/api/saved-results/', views.spatial_saved_results_api, name='spatial_saved_results_api'),
    path('spatial-analysis/api/download-result/', views.spatial_download_result_api, name='spatial_download_result_api'),
    path('item/<path:identifier>/geojson/', views.postgis_geojson, name='postgis_geojson'),
    path('item/<path:identifier>/download.csv', views.postgis_download_csv, name='postgis_download_csv'),
    path('item/<path:identifier>/download.gpkg', views.postgis_download_gpkg, name='postgis_download_gpkg'),
    path('item/<path:identifier>/', views.detail, name='detail'),
    path('asset/<path:identifier>/', views.asset, name='asset'),
    path('upload/', views.upload, name='upload'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('upload/spatial/', views.spatial_upload, name='spatial_upload'),
    path('upload/spatial/success/', views.spatial_upload_success, name='spatial_upload_success'),
]
