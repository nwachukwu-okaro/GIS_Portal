# Mile Post

## Overview

- **Identifier:** `a_irishrail/mile_post`
- **Source organisation:** Iarnrod Eireann / Irish Rail
- **Source:** https://www.irishrail.ie/travel-information/iarnrod-eireann-open-data
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.699179, 51.846434, -6.035095, 54.272267]`
- **Schema:** `a_irishrail`
- **Table:** `mile_post`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:29903
- **Rows:** 4282
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Mile Post is an authoritative dataset published by Iarnrod Eireann / Irish Rail. It represents mile post features using multipoint geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `mile_post_pk` | `integer` | Count or numeric value for mile post pk in the represented area. | statistical_value | Yes | No | No |
| `route` | `varchar` | Publisher-supplied route for the represented feature or record. | source_attribute | Yes | No | No |
| `mile` | `integer` | Count or numeric value for mile in the represented area. | statistical_value | Yes | No | No |
| `quarter` | `smallint` | Count or numeric value for quarter in the represented area. | statistical_value | Yes | No | No |
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
