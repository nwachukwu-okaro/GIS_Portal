# OS Open Non Built Up Extents

## Overview

- **Identifier:** `a_os_built_up_areas/os_open_non_built_up_extents`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Built Up Areas
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-built-up-areas
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.506172, 49.910887, 1.758406, 60.462597]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_built_up_areas`
- **Table:** `os_open_non_built_up_extents`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 8258
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

OS Open Non Built Up Extents is part of OS Open Built Up Areas, published by Ordnance Survey. It represents non built up extents features using multipolygon geometry.

## Lineage

Published by Ordnance Survey as part of OS Open Built Up Areas. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `relatedtogsscode` | `varchar` | Publisher-assigned relatedtogsscode for the record. |
| `name1_text` | `varchar` | Primary place name or feature name. |
| `name1_language` | `varchar` | Language of the primary name (for example ENG for English or CYM for Welsh). |
| `name2_text` | `varchar` | Secondary or alternative place name. |
| `name2_language` | `varchar` | Language of the secondary name. |
| `areahectares` | `double precision` | Area of the polygon feature in hectares. |
| `geometry_area_m` | `double precision` | Area of the polygon feature in square metres. |
| `fid` | `bigint` | Feature identifier — unique integer ID assigned to each feature in the dataset. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
