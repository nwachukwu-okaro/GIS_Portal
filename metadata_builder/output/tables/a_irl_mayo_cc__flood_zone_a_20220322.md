# Flood Zone A 20220322

## Overview

- **Identifier:** `a_irl_mayo_cc/flood_zone_a_20220322`
- **Source organisation:** Mayo County Council
- **Source:** https://data.gov.ie/organization/mayo-county-council
- **Geographic coverage:** County Mayo
- **WGS84 extent:** `[-10.259373, 53.471927, -8.589996, 54.368772]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_mayo_cc`
- **Table:** `flood_zone_a_20220322`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29903
- **Rows:** 18466
- **Columns:** 23
- **Metadata status:** source_mapped

## Description

Flood Zone A 20220322 is an authoritative dataset published by Mayo County Council. It represents flood zone a 20220322 features using multipolygon geometry.

## Lineage

Published by Mayo County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `fid` | `integer` | Feature identifier assigned by the source or import process. |
| `object_id` | `integer` | Identifier assigned by the source dataset. |
| `goid` | `varchar` |  |
| `ext_id` | `varchar` | Identifier assigned by the source dataset. |
| `type_code` | `varchar` | Code assigned by the source dataset. |
| `rbd_code` | `varchar` | Code assigned by the source dataset. |
| `uom_code` | `integer` | Code assigned by the source dataset. |
| `model_code` | `varchar` | Code assigned by the source dataset. |
| `source_code` | `varchar` | Code assigned by the source dataset. |
| `aep` | `double precision` |  |
| `scenario` | `varchar` |  |
| `run_type` | `varchar` |  |
| `status` | `varchar` |  |
| `fid_1` | `double precision` |  |
| `cat` | `integer` |  |
| `value` | `double precision` |  |
| `layer` | `varchar` |  |
| `path` | `varchar` |  |
| `source` | `varchar` |  |
| `zone` | `varchar` |  |
| `cat_` | `integer` |  |
| `probability_level` | `varchar` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
