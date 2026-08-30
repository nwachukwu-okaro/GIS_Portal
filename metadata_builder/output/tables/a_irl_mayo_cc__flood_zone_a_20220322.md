# Flood Zone A 20220322

## Overview

- **Identifier:** `a_irl_mayo_cc/flood_zone_a_20220322`
- **Source organisation:** Mayo County Council
- **Source:** https://data.gov.ie/organization/mayo-county-council
- **Geographic coverage:** County Mayo
- **WGS84 extent:** `[-10.259373, 53.471927, -8.589996, 54.368772]`
- **Schema:** `a_irl_mayo_cc`
- **Table:** `flood_zone_a_20220322`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29903
- **Rows:** 18466
- **Columns:** 23
- **Metadata status:** source_mapped

## Description

Flood Zone A 20220322 is an authoritative dataset published by Mayo County Council. It represents flood zone a 20220322 features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `fid` | `integer` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
| `object_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `goid` | `varchar` | Publisher-assigned goid for the record. | source_identifier | Yes | No | No |
| `ext_id` | `varchar` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `type_code` | `varchar` | Code assigned by the source dataset. | code | Yes | No | No |
| `rbd_code` | `varchar` | Code assigned by the source dataset. | code | Yes | No | No |
| `uom_code` | `integer` | Code assigned by the source dataset. | code | Yes | No | No |
| `model_code` | `varchar` | Code assigned by the source dataset. | code | Yes | No | No |
| `source_code` | `varchar` | Code assigned by the source dataset. | code | Yes | No | No |
| `aep` | `double precision` | Count or numeric value for aep in the represented area. | statistical_value | Yes | No | No |
| `scenario` | `varchar` | Publisher-supplied scenario for the represented feature or record. | source_attribute | Yes | No | No |
| `run_type` | `varchar` | Publisher-supplied run type for the represented feature or record. | source_attribute | Yes | No | No |
| `status` | `varchar` | Publisher-supplied status for the represented feature or record. | source_attribute | Yes | No | No |
| `fid_1` | `double precision` | Count or numeric value for fid 1 in the represented area. | statistical_value | Yes | No | No |
| `cat` | `integer` | Count or numeric value for cat in the represented area. | statistical_value | Yes | No | No |
| `value` | `double precision` | Count or numeric value for value in the represented area. | statistical_value | Yes | No | No |
| `layer` | `varchar` | Publisher-supplied layer for the represented feature or record. | source_attribute | Yes | No | No |
| `path` | `varchar` | Publisher-supplied path for the represented feature or record. | source_attribute | Yes | No | No |
| `source` | `varchar` | Publisher-supplied source for the represented feature or record. | source_attribute | Yes | No | No |
| `zone` | `varchar` | Publisher-supplied zone for the represented feature or record. | source_attribute | Yes | No | No |
| `cat_` | `integer` | Count or numeric value for cat in the represented area. | statistical_value | Yes | No | No |
| `probability_level` | `varchar` | Publisher-supplied probability level for the represented feature or record. | source_attribute | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

## Supported operations

- filter
- select
- reproject
- validate_geometry
- buffer
- clip
- intersect
- spatial_join
- export

## Operation requirements

- Intersect, clip and spatial-join inputs must use matching coordinate reference systems.
- Buffer operations require a suitable projected coordinate reference system.
- Reprojection is performed on working outputs; source tables remain unchanged.

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
