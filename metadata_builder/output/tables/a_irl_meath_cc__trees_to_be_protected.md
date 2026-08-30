# Trees To Be Protected

## Overview

- **Identifier:** `a_irl_meath_cc/trees_to_be_protected`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.166354, 53.411316, -6.231530, 53.851763]`
- **Schema:** `a_irl_meath_cc`
- **Table:** `trees_to_be_protected`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 911
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Trees To Be Protected is an authoritative dataset published by Meath County Council. It represents trees to be protected features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `tp_pk` | `integer` | Count or numeric value for tp pk in the represented area. | statistical_value | Yes | No | No |
| `settlement` | `double precision` | Count or numeric value for settlement in the represented area. | statistical_value | Yes | No | No |
| `settlement2` | `varchar(60)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `objective` | `varchar(250)` | Publisher-supplied objective for the represented feature or record. | source_attribute | Yes | No | No |
| `plan_name` | `varchar(120)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
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
