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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
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
| `area_in_km_square` | `double precision` |  |
| `area_in_hectares` | `double precision` |  |
| `perimeter` | `double precision` |  |
| `hydrometric_area` | `varchar(3)` |  |
| `order` | `double precision` |  |
| `os__layer` | `varchar(16)` |  |
| `source` | `varchar(40)` |  |
| `lake_water_body` | `varchar(3)` |  |
| `eden_lake_code` | `varchar(50)` | Code assigned by the source dataset. |
| `ls_pk` | `integer` | Primary-key identifier for records in lake_segment. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
