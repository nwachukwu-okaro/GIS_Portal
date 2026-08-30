# Architectural Conservation Area

## Overview

- **Identifier:** `a_irl_meath_cc/architectural_conservation_area`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.167175, 53.418413, -6.238061, 53.792893]`
- **Schema:** `a_irl_meath_cc`
- **Table:** `architectural_conservation_area`
- **Geometry:** POLYGON
- **CRS:** EPSG:2157
- **Rows:** 23
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Architectural Conservation Area is an authoritative dataset published by Meath County Council. It represents architectural conservation area features using polygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `aca_pk` | `integer` | Count or numeric value for aca pk in the represented area. | statistical_value | Yes | No | No |
| `aca` | `varchar(100)` | Publisher-supplied aca for the represented feature or record. | source_attribute | Yes | No | No |
| `plan_name` | `varchar(120)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `map_label` | `varchar(100)` | Publisher-supplied map label for the represented feature or record. | source_attribute | Yes | No | No |
| `more_information` | `varchar(254)` | Publisher-supplied more information for the represented feature or record. | source_attribute | Yes | No | No |
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
