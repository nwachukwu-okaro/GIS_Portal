# Recorded Registered And National Monuments

## Overview

- **Identifier:** `a_irl_meath_cc/recorded_registered_and_national_monuments`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.327602, 53.346681, -6.213423, 53.915137]`
- **Schema:** `a_irl_meath_cc`
- **Table:** `recorded_registered_and_national_monuments`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 4284
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Recorded Registered And National Monuments is an authoritative dataset published by Meath County Council. It represents recorded registered and national monuments features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `rrnm_pk` | `integer` | Count or numeric value for rrnm pk in the represented area. | statistical_value | Yes | No | No |
| `entity_id` | `varchar(7)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `class_code` | `varchar(4)` | Code assigned by the source dataset. | code | Yes | No | No |
| `class_description` | `varchar(60)` | Publisher-supplied class description for the represented feature or record. | source_attribute | Yes | No | No |
| `smrs` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `townland` | `varchar(254)` | Publisher-supplied townland for the represented feature or record. | source_attribute | Yes | No | No |
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
