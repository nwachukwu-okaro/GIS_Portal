# Special Protection Areas

## Overview

- **Identifier:** `a_irl_spatial_data_exchange/special_protection_areas`
- **Source organisation:** Government of Ireland
- **Source:** https://data.gov.ie/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.687972, 51.447492, -5.947508, 55.449953]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_spatial_data_exchange`
- **Table:** `special_protection_areas`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 199
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Special Protection Areas is an authoritative dataset published by Government of Ireland. It represents special protection areas features using multipolygon geometry.

## Lineage

Published by the Government of Ireland as part of the national spatial data exchange. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `spa_pk` | `integer` | Count or numeric value for spa pk in the represented area. |
| `site_code` | `varchar(6)` | Code assigned by the source dataset. |
| `site_name` | `varchar(100)` | Name associated with the represented feature. |
| `version` | `double precision` | Count or numeric value for version in the represented area. |
| `county` | `varchar(50)` | Publisher-supplied county for the represented feature or record. |
| `ha` | `double precision` | Count or numeric value for ha in the represented area. |
| `source_crs` | `varchar(254)` | Publisher-supplied source crs for the represented feature or record. |
| `source_sale` | `varchar(50)` | Publisher-supplied source sale for the represented feature or record. |
| `url` | `varchar(50)` | Publisher-supplied url for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
