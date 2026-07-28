from django.urls import path

from . import views

app_name = 'catalogue'

urlpatterns = [
    path('', views.search, name='search'),
    path('item/<path:identifier>/', views.detail, name='detail'),
    path('asset/<path:identifier>/', views.asset, name='asset'),
    path('item/<path:identifier>/download.csv', views.postgis_download_csv, name='postgis_download_csv'),
    path('item/<path:identifier>/download.gpkg', views.postgis_download_gpkg, name='postgis_download_gpkg'),
    path('upload/', views.upload, name='upload'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('upload/spatial/', views.spatial_upload, name='spatial_upload'),
    path('upload/spatial/success/', views.spatial_upload_success, name='spatial_upload_success'),
]
