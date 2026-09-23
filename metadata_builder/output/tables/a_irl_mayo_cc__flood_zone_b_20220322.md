# Flood Zone B 20220322

## Overview

- **Identifier:** `a_irl_mayo_cc/flood_zone_b_20220322`
- **Source organisation:** Mayo County Council
- **Source:** https://data.gov.ie/organization/mayo-county-council
- **Geographic coverage:** County Mayo
- **WGS84 extent:** `[-10.258845, 53.472779, -8.593050, 54.368740]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_mayo_cc`
- **Table:** `flood_zone_b_20220322`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29903
- **Rows:** 70387
- **Columns:** 31
- **Metadata status:** source_mapped

## Description

Flood Zone B 20220322 is an authoritative dataset published by Mayo County Council. It represents flood zone b 20220322 features using multipolygon geometry.

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
| `object_id` | `double precision` | Identifier assigned by the source dataset. |
| `fid_fzb_cf` | `double precision` |  |
| `goid` | `varchar` |  |
| `ext_id` | `varchar` | Identifier assigned by the source dataset. |
| `type_code` | `varchar` | Code assigned by the source dataset. |
| `rbd_code` | `varchar` | Code assigned by the source dataset. |
| `uom_code` | `double precision` | Code assigned by the source dataset. |
| `source_code` | `varchar` | Code assigned by the source dataset. |
| `aep` | `double precision` |  |
| `scenario` | `varchar` |  |
| `run_type` | `varchar` |  |
| `status` | `varchar` |  |
| `fid_clip_e` | `double precision` |  |
| `goid_1` | `varchar` |  |
| `ext_id_1` | `varchar` |  |
| `type_code_1` | `varchar` |  |
| `rbd_code_1` | `varchar` |  |
| `uom_code_1` | `double precision` |  |
| `model_code` | `varchar` | Code assigned by the source dataset. |
| `source_co_1` | `varchar` |  |
| `aep_1` | `double precision` |  |
| `scenario_1` | `varchar` |  |
| `run_type_1` | `varchar` |  |
| `status_1` | `varchar` |  |
| `fid_1` | `double precision` |  |
| `cat` | `integer` |  |
| `value` | `double precision` |  |
| `layer` | `varchar` |  |
| `path` | `varchar` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
