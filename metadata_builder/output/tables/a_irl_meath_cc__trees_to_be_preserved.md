# Trees To Be Preserved

## Overview

- **Identifier:** `a_irl_meath_cc/trees_to_be_preserved`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Schema:** `a_irl_meath_cc`
- **Table:** `trees_to_be_preserved`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 9
- **Metadata status:** source_mapped

## Description

Trees To Be Preserved is an authoritative dataset published by Meath County Council. It represents trees to be preserved features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `ttbp_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `reference` | `varchar(5)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `location_se` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `settlement` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `plan_name` | `varchar(120)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `map_label` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `object_inf` | `varchar(20)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
