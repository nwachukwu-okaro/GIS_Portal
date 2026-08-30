# Land Water Boundary

## Overview

- **Identifier:** `a_os_open_terrain_50/land_water_boundary`
- **Source organisation:** Ordnance Survey
- **Product:** OS Terrain 50
- **Source:** https://www.ordnancesurvey.co.uk/products/os-terrain-50
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.649928, 49.863142, 1.763537, 60.860836]`
- **Schema:** `a_os_open_terrain_50`
- **Table:** `land_water_boundary`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 71307
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Contains OS data © Crown copyright and database right 2026

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `property_value` | `double precision` | Count or numeric value for property value in the represented area. | statistical_value | Yes | No | No |
| `water_level_category` | `varchar` | Publisher-supplied water level category for the represented feature or record. | source_attribute | Yes | No | No |
| `fid` | `integer` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
