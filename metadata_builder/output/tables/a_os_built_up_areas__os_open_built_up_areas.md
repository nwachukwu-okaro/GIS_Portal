# OS Open Built Up Areas

## Overview

- **Identifier:** `a_os_built_up_areas/os_open_built_up_areas`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Built Up Areas
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-built-up-areas
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.509500, 49.910214, 1.763227, 60.480482]`
- **Schema:** `a_os_built_up_areas`
- **Table:** `os_open_built_up_areas`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 8716
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

OS Open Built Up Areas is part of OS Open Built Up Areas, published by Ordnance Survey. It represents built up area features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `gsscode` | `varchar` | Government Statistical Service code — unique identifier for administrative or statistical geographies. | geographic_identifier | Yes | No | Yes |
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
