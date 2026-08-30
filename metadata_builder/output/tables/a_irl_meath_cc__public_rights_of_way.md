# Public Rights Of Way

## Overview

- **Identifier:** `a_irl_meath_cc/public_rights_of_way`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Schema:** `a_irl_meath_cc`
- **Table:** `public_rights_of_way`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 24
- **Metadata status:** source_mapped

## Description

Public Rights Of Way is an authoritative dataset published by Meath County Council. It represents public rights of way features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `public_right_of_way` | `varchar(15)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `category` | `varchar(150)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `location` | `varchar(250)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `prow_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
