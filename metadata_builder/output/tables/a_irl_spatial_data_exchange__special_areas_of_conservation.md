# Special Areas Of Conservation

## Overview

- **Identifier:** `a_irl_spatial_data_exchange/special_areas_of_conservation`
- **Source organisation:** Government of Ireland
- **Source:** https://data.gov.ie/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.691667, 51.410000, -5.591380, 55.471236]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_spatial_data_exchange`
- **Table:** `special_areas_of_conservation`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 433
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Special Areas Of Conservation is an authoritative dataset published by Government of Ireland. It represents special areas of conservation features using multipolygon geometry.

## Lineage

Published by the Government of Ireland as part of the national spatial data exchange. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `sac_pk` | `integer` | Primary-key identifier for records in special_areas_of_conservation. |
| `site_code` | `varchar(6)` | Code assigned by the source dataset. |
| `site_name` | `varchar(100)` | Name associated with the represented feature. |
| `version` | `double precision` |  |
| `county` | `varchar(50)` |  |
| `ha` | `double precision` |  |
| `source_crs` | `varchar(254)` |  |
| `source_sale` | `varchar(50)` |  |
| `url` | `varchar(50)` | Web address associated with the record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
