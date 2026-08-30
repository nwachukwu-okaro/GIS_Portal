# Smr Zone

## Overview

- **Identifier:** `a_irl_national_built_heritage_service/smr_zone`
- **Source organisation:** National Built Heritage Service
- **Source:** https://www.buildingsofireland.ie/
- **Schema:** `a_irl_national_built_heritage_service`
- **Table:** `smr_zone`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 82731
- **Metadata status:** source_mapped

## Description

Smr Zone is an authoritative dataset published by National Built Heritage Service. It represents smr zone features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `zone_id` | `varchar` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `smrz_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
