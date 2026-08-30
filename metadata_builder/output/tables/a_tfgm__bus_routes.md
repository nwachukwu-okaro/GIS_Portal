# Bus Routes

## Overview

- **Identifier:** `a_tfgm/bus_routes`
- **Source organisation:** Transport for Greater Manchester
- **Source:** https://developer.tfgm.com/
- **Geographic coverage:** Greater Manchester
- **WGS84 extent:** `[-3.011828, 53.255054, -1.782201, 53.834496]`
- **Schema:** `a_tfgm`
- **Table:** `bus_routes`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 2852
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Bus Routes is an authoritative dataset published by Transport for Greater Manchester. It represents bus routes features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `service_pk` | `integer` | Count or numeric value for service pk in the represented area. | statistical_value | Yes | No | No |
| `service_id` | `varchar` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `service_no` | `varchar` | Publisher-supplied service number for the represented feature or record. | source_attribute | Yes | No | No |
| `suffix` | `varchar` | Publisher-supplied suffix for the represented feature or record. | source_attribute | Yes | No | No |
| `direction` | `varchar` | Publisher-supplied direction for the represented feature or record. | source_attribute | Yes | No | No |
| `day` | `varchar` | Publisher-supplied day for the represented feature or record. | source_attribute | Yes | No | No |
| `variation` | `varchar` | Publisher-supplied variation for the represented feature or record. | source_attribute | Yes | No | No |
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
