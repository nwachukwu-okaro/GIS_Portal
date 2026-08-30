# Landscape Sensitivity Ratings Cdp 2022 2028

## Overview

- **Identifier:** `a_irl_galway_cc/landscape_sensitivity_ratings_cdp_2022_2028`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.302290, 52.968151, -7.967334, 53.718912]`
- **Schema:** `a_irl_galway_cc`
- **Table:** `landscape_sensitivity_ratings_cdp_2022_2028`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 49
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Landscape Sensitivity Ratings Cdp 2022 2028 is an authoritative dataset published by Galway County Council. It represents landscape sensitivity ratings cdp 2022 2028 features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `object_id` | `smallint` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `unit` | `varchar` | Publisher-supplied unit for the represented feature or record. | source_attribute | Yes | No | No |
| `sensitivit` | `varchar` | Publisher-supplied sensitivit for the represented feature or record. | source_attribute | Yes | No | No |
| `value` | `smallint` | Count or numeric value for value in the represented area. | statistical_value | Yes | No | No |
| `urban_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `urban_source` | `varchar` | Publisher-supplied urban source for the represented feature or record. | source_attribute | Yes | No | No |
| `lsr_pk` | `integer` | Count or numeric value for lsr pk in the represented area. | statistical_value | Yes | No | No |
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
