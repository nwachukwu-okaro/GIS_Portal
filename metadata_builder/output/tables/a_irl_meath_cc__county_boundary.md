# County Boundary

## Overview

- **Identifier:** `a_irl_meath_cc/county_boundary`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.343668, 53.381919, -6.212613, 53.917668]`
- **Schema:** `a_irl_meath_cc`
- **Table:** `county_boundary`
- **Geometry:** POLYGON
- **CRS:** EPSG:2157
- **Rows:** 1
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

County Boundary is an authoritative dataset published by Meath County Council. It represents county boundary features using polygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `county` | `varchar(25)` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
| `cb_pk` | `integer` | Count or numeric value for cb pk in the represented area. | statistical_value | Yes | No | No |
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
