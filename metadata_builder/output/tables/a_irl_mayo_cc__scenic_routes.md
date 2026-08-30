# Scenic Routes

## Overview

- **Identifier:** `a_irl_mayo_cc/scenic_routes`
- **Source organisation:** Mayo County Council
- **Source:** https://data.gov.ie/organization/mayo-county-council
- **Schema:** `a_irl_mayo_cc`
- **Table:** `scenic_routes`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:3857
- **Rows:** 54
- **Metadata status:** source_mapped

## Description

Scenic Routes is an authoritative dataset published by Mayo County Council. It represents scenic routes features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `fid` | `integer` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
| `id` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sr_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
