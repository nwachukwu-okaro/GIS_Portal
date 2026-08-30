# Protected View And Prospect

## Overview

- **Identifier:** `a_irl_meath_cc/protected_view_and_prospect`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-6.960533, 53.396144, -6.229006, 53.853611]`
- **Schema:** `a_irl_meath_cc`
- **Table:** `protected_view_and_prospect`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 77
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

Protected View And Prospect is an authoritative dataset published by Meath County Council. It represents protected view and prospect features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `pvp_pk` | `integer` | Count or numeric value for pvp pk in the represented area. | statistical_value | Yes | No | No |
| `map_label` | `varchar(100)` | Publisher-supplied map label for the represented feature or record. | source_attribute | Yes | No | No |
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
