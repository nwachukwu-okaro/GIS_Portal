# Scenic Routes

## Overview

- **Identifier:** `a_irl_galway_cc/scenic_routes`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.174339, 53.055206, -8.222288, 53.614337]`
- **Schema:** `a_irl_galway_cc`
- **Table:** `scenic_routes`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:2157
- **Rows:** 8
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Scenic Routes is an authoritative dataset published by Galway County Council. It represents scenic routes features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `object_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `route_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `route` | `varchar` | Publisher-supplied route for the represented feature or record. | source_attribute | Yes | No | No |
| `shape__length` | `double precision` | Numeric shape length value recorded for the feature. | measure | Yes | No | No |
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
