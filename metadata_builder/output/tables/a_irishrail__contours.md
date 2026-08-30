# Contours

## Overview

- **Identifier:** `a_irishrail/contours`
- **Source organisation:** Iarnrod Eireann / Irish Rail
- **Source:** https://www.irishrail.ie/travel-information/iarnrod-eireann-open-data
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.706042, 51.846086, -6.034629, 54.274006]`
- **Schema:** `a_irishrail`
- **Table:** `contours`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:29903
- **Rows:** 365055
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Contours is an authoritative dataset published by Iarnrod Eireann / Irish Rail. It represents contours features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `contour_pk` | `integer` | Count or numeric value for contour pk in the represented area. | statistical_value | Yes | No | No |
| `contour_type` | `varchar(5)` | Publisher-supplied contour type for the represented feature or record. | source_attribute | Yes | No | No |
| `z` | `real` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
