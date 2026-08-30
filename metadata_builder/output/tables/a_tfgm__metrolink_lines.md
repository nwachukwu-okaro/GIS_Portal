# Metrolink Lines

## Overview

- **Identifier:** `a_tfgm/metrolink_lines`
- **Source organisation:** Transport for Greater Manchester
- **Source:** https://developer.tfgm.com/
- **Geographic coverage:** Greater Manchester
- **WGS84 extent:** `[-2.348224, 53.365168, -2.088039, 53.617382]`
- **Schema:** `a_tfgm`
- **Table:** `metrolink_lines`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 20
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Metrolink Lines is an authoritative dataset published by Transport for Greater Manchester. It represents metrolink lines features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `tramline_pk` | `integer` | Count or numeric value for tramline pk in the represented area. | statistical_value | Yes | No | No |
| `description` | `varchar` | Publisher-supplied description for the represented feature or record. | source_attribute | Yes | No | No |
| `type` | `varchar` | Publisher-supplied type for the represented feature or record. | source_attribute | Yes | No | No |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `validfrom` | `timestamp` | Publisher-supplied validfrom for the represented feature or record. | source_attribute | Yes | No | No |
| `validto` | `timestamp` | Publisher-supplied validto for the represented feature or record. | source_attribute | Yes | No | No |
| `currentstatus` | `varchar` | Publisher-supplied currentstatus for the represented feature or record. | source_attribute | Yes | No | No |
| `comments` | `varchar` | Publisher-supplied comments for the represented feature or record. | source_attribute | Yes | No | No |
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
