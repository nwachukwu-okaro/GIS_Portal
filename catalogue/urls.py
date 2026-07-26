from django.urls import path

from . import views

app_name = 'catalogue'

urlpatterns = [
    path('', views.search, name='search'),
    path('item/<path:identifier>/', views.detail, name='detail'),
    path('asset/<path:identifier>/', views.asset, name='asset'),
    path('item/<path:identifier>/download.csv', views.postgis_download_csv, name='postgis_download_csv'),
    path('item/<path:identifier>/download.gpkg', views.postgis_download_gpkg, name='postgis_download_gpkg'),
]
