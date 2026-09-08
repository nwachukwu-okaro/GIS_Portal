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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
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
| `goid` | `varchar` | Publisher-assigned goid for the record. |
| `ext_id` | `varchar` | Identifier assigned by the source dataset. |
| `type_code` | `varchar` | Code assigned by the source dataset. |
| `rbd_code` | `varchar` | Code assigned by the source dataset. |
| `uom_code` | `integer` | Code assigned by the source dataset. |
| `model_code` | `varchar` | Code assigned by the source dataset. |
| `source_code` | `varchar` | Code assigned by the source dataset. |
| `aep` | `double precision` | Count or numeric value for aep in the represented area. |
| `scenario` | `varchar` | Publisher-supplied scenario for the represented feature or record. |
| `run_type` | `varchar` | Publisher-supplied run type for the represented feature or record. |
| `status` | `varchar` | Publisher-supplied status for the represented feature or record. |
| `fid_1` | `double precision` | Count or numeric value for fid 1 in the represented area. |
| `cat` | `integer` | Count or numeric value for cat in the represented area. |
| `value` | `double precision` | Count or numeric value for value in the represented area. |
| `layer` | `varchar` | Publisher-supplied layer for the represented feature or record. |
| `path` | `varchar` | Publisher-supplied path for the represented feature or record. |
| `source` | `varchar` | Publisher-supplied source for the represented feature or record. |
| `zone` | `varchar` | Publisher-supplied zone for the represented feature or record. |
| `cat_` | `integer` | Count or numeric value for cat in the represented area. |
| `probability_level` | `varchar` | Publisher-supplied probability level for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
