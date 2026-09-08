# Drainage District Channels

## Overview

- **Identifier:** `a_irl_datagov_open_data/drainage_district_channels`
- **Source organisation:** Government of Ireland
- **Source:** https://data.gov.ie/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.091063, 51.535500, -6.200397, 55.219819]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_datagov_open_data`
- **Table:** `drainage_district_channels`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:29903
- **Rows:** 3255
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Drainage District Channels is an authoritative dataset published by Government of Ireland. It represents drainage district channels features using multilinestring geometry.

## Lineage

Published by the Government of Ireland as part of the national open data portal (data.gov.ie). Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `ddc_pk` | `integer` |  |
| `feature` | `varchar(50)` |  |
| `overall_id` | `bigint` | Identifier assigned by the source dataset. |
| `ref` | `varchar(50)` |  |
| `scheme` | `varchar(150)` |  |
| `sch_type` | `varchar(50)` |  |
| `source` | `varchar(255)` |  |
| `comments` | `varchar(43)` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
