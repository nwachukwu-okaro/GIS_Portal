# Quarry Register

## Overview

- **Identifier:** `a_irl_meath_cc/quarry_register`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.294228, 53.385624, -6.218810, 53.901445]`
- **Schema:** `a_irl_meath_cc`
- **Table:** `quarry_register`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 318
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Quarry Register is an authoritative dataset published by Meath County Council. It represents quarry register features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `qr_pk` | `integer` | Count or numeric value for qr pk in the represented area. | statistical_value | Yes | No | No |
| `ref_no` | `varchar(10)` | Publisher-supplied reference number for the represented feature or record. | source_attribute | Yes | No | No |
| `location_o` | `varchar(104)` | Publisher-supplied location o for the represented feature or record. | source_attribute | Yes | No | No |
| `townland` | `varchar(50)` | Publisher-supplied townland for the represented feature or record. | source_attribute | Yes | No | No |
| `municipal_` | `varchar(40)` | Publisher-supplied municipal for the represented feature or record. | source_attribute | Yes | No | No |
| `more_info` | `varchar(254)` | Publisher-supplied more info for the represented feature or record. | source_attribute | Yes | No | No |
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
