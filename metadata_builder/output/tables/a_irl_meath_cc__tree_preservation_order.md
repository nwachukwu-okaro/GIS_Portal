# Tree Preservation Order

## Overview

- **Identifier:** `a_irl_meath_cc/tree_preservation_order`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-6.859796, 53.477875, -6.256054, 53.717973]`
- **Schema:** `a_irl_meath_cc`
- **Table:** `tree_preservation_order`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 8
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Tree Preservation Order is an authoritative dataset published by Meath County Council. It represents tree preservation order features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `tpo_pk` | `integer` | Count or numeric value for tpo pk in the represented area. | statistical_value | Yes | No | No |
| `tpo_number` | `varchar(20)` | Publisher-supplied tpo number for the represented feature or record. | source_attribute | Yes | No | No |
| `tpo_location` | `varchar(100)` | Publisher-supplied tpo location for the represented feature or record. | source_attribute | Yes | No | No |
| `remarks` | `varchar(100)` | Publisher-supplied remarks for the represented feature or record. | source_attribute | Yes | No | No |
| `settlement` | `bigint` | Count or numeric value for settlement in the represented area. | statistical_value | Yes | No | No |
| `settlement1` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `plan_name` | `varchar(120)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `map_label` | `varchar(100)` | Publisher-supplied map label for the represented feature or record. | source_attribute | Yes | No | No |
| `object_inf` | `varchar(20)` | Publisher-supplied object inf for the represented feature or record. | source_attribute | Yes | No | No |
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
