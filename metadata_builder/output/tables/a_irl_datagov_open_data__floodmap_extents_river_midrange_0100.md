# Floodmap Extents River Midrange 0100

## Overview

- **Identifier:** `a_irl_datagov_open_data/floodmap_extents_river_midrange_0100`
- **Source organisation:** Government of Ireland
- **Source:** https://data.gov.ie/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.298086, 51.524676, -6.018716, 55.301938]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_datagov_open_data`
- **Table:** `floodmap_extents_river_midrange_0100`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29903
- **Rows:** 46802
- **Columns:** 21
- **Metadata status:** source_mapped

## Description

Floodmap Extents River Midrange 0100 is an authoritative dataset published by Government of Ireland. It represents floodmap extents river midrange 0100 features using multipolygon geometry.

## Lineage

Published by the Government of Ireland as part of the national open data portal (data.gov.ie). Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `uuid` | `varchar(50)` |  |
| `b` | `varchar(10)` |  |
| `sch` | `varchar(20)` |  |
| `ttt` | `varchar(10)` |  |
| `s` | `varchar(10)` |  |
| `c` | `varchar(10)` |  |
| `r` | `varchar(10)` |  |
| `pppp` | `varchar(10)` |  |
| `m` | `varchar(10)` |  |
| `stg` | `varchar(10)` |  |
| `a` | `varchar(10)` |  |
| `rn` | `varchar(10)` |  |
| `mc` | `varchar(20)` |  |
| `comments` | `varchar(300)` |  |
| `dm_uuid` | `varchar(50)` |  |
| `proj_name` | `varchar(200)` | Name associated with the represented feature. |
| `proj_type` | `varchar(200)` |  |
| `uploaded` | `date` |  |
| `version` | `varchar(50)` |  |
| `fm0100_pk` | `integer` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
