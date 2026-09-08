# Lake Segment

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/lake_segment`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.425985, 51.453245, -6.049586, 55.353164]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `lake_segment`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29903
- **Rows:** 12217
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Lake Segment is an authoritative dataset published by Environmental Protection Agency Ireland. It represents lake segment features using multipolygon geometry.

## Lineage

Published by the Environmental Protection Agency Ireland as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `segment_code` | `varchar(24)` | Code assigned by the source dataset. |
| `name` | `varchar(100)` | Official or publisher-assigned name of the represented feature. |
| `area_in_km_square` | `double precision` | Numeric area in km square value recorded for the feature. |
| `area_in_hectares` | `double precision` | Numeric area in hectares value recorded for the feature. |
| `perimeter` | `double precision` | Count or numeric value for perimeter in the represented area. |
| `hydrometric_area` | `varchar(3)` | Publisher-supplied hydrometric area for the represented feature or record. |
| `order` | `double precision` | Count or numeric value for order in the represented area. |
| `os__layer` | `varchar(16)` | Publisher-supplied os layer for the represented feature or record. |
| `source` | `varchar(40)` | Publisher-supplied source for the represented feature or record. |
| `lake_water_body` | `varchar(3)` | Publisher-supplied lake water body for the represented feature or record. |
| `eden_lake_code` | `varchar(50)` | Code assigned by the source dataset. |
| `ls_pk` | `integer` | Count or numeric value for ls pk in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
