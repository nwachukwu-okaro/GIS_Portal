# Road Link

## Overview

- **Identifier:** `a_os_open_roads/road_link`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Roads
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-roads
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.586180, 49.890912, 1.762311, 60.827676]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_open_roads`
- **Table:** `road_link`
- **Geometry:** LINESTRING
- **CRS:** EPSG:27700
- **Rows:** 3961077
- **Columns:** 22
- **Metadata status:** source_mapped

## Description

Road Link is part of OS Open Roads, published by Ordnance Survey. It represents road link features using linestring geometry.

## Lineage

Published by Ordnance Survey as part of OS Open Roads. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `text` |  |
| `fictitious` | `boolean` |  |
| `road_classification` | `text` |  |
| `road_function` | `text` |  |
| `form_of_way` | `text` |  |
| `road_classification_number` | `text` |  |
| `name_1` | `text` |  |
| `name_1_lang` | `text` |  |
| `name_2` | `text` |  |
| `name_2_lang` | `text` |  |
| `road_structure` | `text` |  |
| `length` | `double precision` |  |
| `length_uom` | `text` |  |
| `loop` | `boolean` |  |
| `primary_route` | `boolean` |  |
| `trunk_road` | `boolean` |  |
| `start_node` | `text` |  |
| `end_node` | `text` |  |
| `road_number_toid` | `text` |  |
| `road_name_toid` | `text` |  |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
