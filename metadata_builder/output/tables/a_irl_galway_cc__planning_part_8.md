# Planning Part 8

## Overview

- **Identifier:** `a_irl_galway_cc/planning_part_8`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.219259, 52.980785, -8.063640, 53.706012]`
- **Schema:** `a_irl_galway_cc`
- **Table:** `planning_part_8`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 569
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Planning Part 8 is an authoritative dataset published by Galway County Council. It represents planning part 8 features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `double precision` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `plan_id` | `varchar` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `desc_` | `varchar` | Publisher-supplied description for the represented feature or record. | source_attribute | Yes | No | No |
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
