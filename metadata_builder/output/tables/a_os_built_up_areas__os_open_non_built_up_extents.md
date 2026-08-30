# OS Open Non Built Up Extents

## Overview

- **Identifier:** `a_os_built_up_areas/os_open_non_built_up_extents`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Built Up Areas
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-built-up-areas
- **Schema:** `a_os_built_up_areas`
- **Table:** `os_open_non_built_up_extents`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 8258
- **Metadata status:** source_mapped

## Description

OS Open Non Built Up Extents is part of OS Open Built Up Areas, published by Ordnance Survey. It represents non built up extents features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `relatedtogsscode` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `name1_text` | `varchar` | Primary place name or feature name. | feature_name | Yes | Yes | No |
| `name1_language` | `varchar` | Language of the primary name (for example ENG for English or CYM for Welsh). | language_code | Yes | No | No |
| `name2_text` | `varchar` | Secondary or alternative place name. | alternative_name | Yes | Yes | No |
| `name2_language` | `varchar` | Language of the secondary name. | language_code | Yes | No | No |
| `areahectares` | `double precision` | Area of the polygon feature in hectares. | area | Yes | No | No |
| `geometry_area_m` | `double precision` | Area of the polygon feature in square metres. | area | Yes | No | No |
| `fid` | `bigint` | Feature identifier — unique integer ID assigned to each feature in the dataset. | record_identifier | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
