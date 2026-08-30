# Athenry Lap Zoning 2024 2030

## Overview

- **Identifier:** `a_irl_galway_cc/athenry_lap_zoning_2024_2030`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-8.781623, 53.284632, -8.723046, 53.315870]`
- **Schema:** `a_irl_galway_cc`
- **Table:** `athenry_lap_zoning_2024_2030`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 583
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Athenry Lap Zoning 2024 2030 is an authoritative dataset published by Galway County Council. It represents athenry lap zoning 2024 2030 features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `object_id` | `smallint` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `zoning_abb` | `varchar` | Publisher-supplied zoning abb for the represented feature or record. | source_attribute | Yes | No | No |
| `zoning` | `varchar` | Publisher-supplied zoning for the represented feature or record. | source_attribute | Yes | No | No |
| `status` | `varchar` | Publisher-supplied status for the represented feature or record. | source_attribute | Yes | No | No |
| `town` | `varchar` | Publisher-supplied town for the represented feature or record. | source_attribute | Yes | No | No |
| `plan_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `opportunit` | `varchar` | Publisher-supplied opportunit for the represented feature or record. | source_attribute | Yes | No | No |
| `policy_obj` | `varchar` | Publisher-supplied policy obj for the represented feature or record. | source_attribute | Yes | No | No |
| `policy_o_1` | `varchar` | Publisher-supplied policy o 1 for the represented feature or record. | source_attribute | Yes | No | No |
| `globabl_id` | `varchar` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `myplan_gzt` | `varchar` | Publisher-supplied myplan gzt for the represented feature or record. | source_attribute | Yes | No | No |
| `luz_pk` | `integer` | Count or numeric value for luz pk in the represented area. | statistical_value | Yes | No | No |
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
