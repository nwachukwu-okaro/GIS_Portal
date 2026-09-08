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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
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
| `id` | `text` | Publisher-assigned identifier for the record. |
| `fictitious` | `boolean` | Publisher-supplied fictitious for the represented feature or record. |
| `road_classification` | `text` | Publisher-supplied road classification for the represented feature or record. |
| `road_function` | `text` | Publisher-supplied road function for the represented feature or record. |
| `form_of_way` | `text` | Publisher-supplied form of way for the represented feature or record. |
| `road_classification_number` | `text` | Publisher-supplied road classification number for the represented feature or record. |
| `name_1` | `text` | Publisher-supplied name 1 for the represented feature or record. |
| `name_1_lang` | `text` | Publisher-supplied name 1 lang for the represented feature or record. |
| `name_2` | `text` | Publisher-supplied name 2 for the represented feature or record. |
| `name_2_lang` | `text` | Publisher-supplied name 2 lang for the represented feature or record. |
| `road_structure` | `text` | Publisher-supplied road structure for the represented feature or record. |
| `length` | `double precision` | Numeric length value recorded for the feature. |
| `length_uom` | `text` | Publisher-supplied length uom for the represented feature or record. |
| `loop` | `boolean` | Publisher-supplied loop for the represented feature or record. |
| `primary_route` | `boolean` | Publisher-supplied primary route for the represented feature or record. |
| `trunk_road` | `boolean` | Publisher-supplied trunk road for the represented feature or record. |
| `start_node` | `text` | Publisher-supplied start node for the represented feature or record. |
| `end_node` | `text` | Publisher-supplied end node for the represented feature or record. |
| `road_number_toid` | `text` | Publisher-assigned road number toid for the record. |
| `road_name_toid` | `text` | Publisher-assigned road name toid for the record. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
