# Offshore Special Areas Of Conservation

## Overview

- **Identifier:** `a_irl_spatial_data_exchange/offshore_special_areas_of_conservation`
- **Source organisation:** Government of Ireland
- **Source:** https://data.gov.ie/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-15.357778, 48.180188, -9.408948, 56.383759]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_spatial_data_exchange`
- **Table:** `offshore_special_areas_of_conservation`
- **Geometry:** POLYGON
- **CRS:** EPSG:4326
- **Rows:** 8
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Offshore Special Areas Of Conservation is an authoritative dataset published by Government of Ireland. It represents offshore special areas of conservation features using polygon geometry.

## Lineage

Published by the Government of Ireland as part of the national spatial data exchange. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `osac_pk` | `integer` | Primary-key identifier for records in offshore_special_areas_of_conservation. |
| `site_name` | `varchar(50)` | Name associated with the represented feature. |
| `site_code` | `varchar(6)` | Code assigned by the source dataset. |
| `centroid_x` | `double precision` | X coordinate of the feature centroid; units and reference system are not confirmed for this attribute. |
| `centroid_y` | `double precision` | Y coordinate of the feature centroid; units and reference system are not confirmed for this attribute. |
| `laea_area` | `double precision` |  |
| `url` | `varchar(50)` | Web address associated with the record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
