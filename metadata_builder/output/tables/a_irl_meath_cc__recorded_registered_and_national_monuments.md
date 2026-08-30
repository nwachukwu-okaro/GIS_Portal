# Recorded Registered And National Monuments

## Overview

- **Identifier:** `a_irl_meath_cc/recorded_registered_and_national_monuments`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Schema:** `a_irl_meath_cc`
- **Table:** `recorded_registered_and_national_monuments`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 4284
- **Metadata status:** source_mapped

## Description

Recorded Registered And National Monuments is an authoritative dataset published by Meath County Council. It represents recorded registered and national monuments features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `rrnm_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `entity_id` | `varchar(7)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `class_code` | `varchar(4)` | Code assigned by the source dataset. | code | Yes | No | No |
| `class_description` | `varchar(60)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `smrs` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `townland` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `map_label` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
