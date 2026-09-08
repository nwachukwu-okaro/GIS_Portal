# Floodmap Extents Coastal Midrange 0200

## Overview

- **Identifier:** `a_irl_datagov_open_data/floodmap_extents_coastal_midrange_0200`
- **Source organisation:** Government of Ireland
- **Source:** https://data.gov.ie/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.376779, 51.600703, -6.021117, 55.331676]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_datagov_open_data`
- **Table:** `floodmap_extents_coastal_midrange_0200`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29903
- **Rows:** 18895
- **Columns:** 21
- **Metadata status:** source_mapped

## Description

Floodmap Extents Coastal Midrange 0200 is an authoritative dataset published by Government of Ireland. It represents floodmap extents coastal midrange 0200 features using multipolygon geometry.

## Lineage

Published by the Government of Ireland as part of the national open data portal (data.gov.ie). Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `uuid` | `varchar(36)` |  |
| `b` | `varchar(1)` |  |
| `sch` | `varchar(6)` |  |
| `ttt` | `varchar(3)` |  |
| `s` | `varchar(1)` |  |
| `c` | `varchar(1)` |  |
| `r` | `varchar(1)` |  |
| `pppp` | `varchar(4)` |  |
| `m` | `varchar(1)` |  |
| `stg` | `varchar(2)` |  |
| `a` | `varchar(1)` |  |
| `rn` | `varchar(2)` |  |
| `mc` | `varchar(6)` |  |
| `comments` | `varchar(255)` |  |
| `dm_uuid` | `varchar(36)` |  |
| `proj_name` | `varchar(120)` | Name associated with the represented feature. |
| `proj_type` | `varchar(120)` |  |
| `uploaded` | `date` |  |
| `version` | `varchar(20)` |  |
| `cm0200_pk` | `integer` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
