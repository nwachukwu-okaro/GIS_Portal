# Planning Part 6

## Overview

- **Identifier:** `a_irl_galway_cc/planning_part_6`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-8.780426, 53.287029, -8.780426, 53.287029]`
- **Schema:** `a_irl_galway_cc`
- **Table:** `planning_part_6`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:2157
- **Rows:** 1
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Planning Part 6 is an authoritative dataset published by Galway County Council. It represents planning part 6 features using multipoint geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `ref` | `varchar` | Publisher-assigned reference for the record. | source_identifier | Yes | No | No |
| `description` | `varchar` | Publisher-supplied description for the represented feature or record. | source_attribute | Yes | No | No |
| `global_id` | `varchar` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `object_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
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
