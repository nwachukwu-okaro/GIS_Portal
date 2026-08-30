# Road Link

## Overview

- **Identifier:** `a_os_open_roads/road_link`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Roads
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-roads
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.586180, 49.890912, 1.762311, 60.827676]`
- **Schema:** `a_os_open_roads`
- **Table:** `road_link`
- **Geometry:** LINESTRING
- **CRS:** EPSG:27700
- **Rows:** 3961077
- **Columns:** 22
- **Metadata status:** source_mapped

## Description

Road Link is part of OS Open Roads, published by Ordnance Survey. It represents road link features using linestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `text` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `fictitious` | `boolean` | Publisher-supplied fictitious for the represented feature or record. | source_attribute | Yes | No | No |
| `road_classification` | `text` | Publisher-supplied road classification for the represented feature or record. | source_attribute | Yes | No | No |
| `road_function` | `text` | Publisher-supplied road function for the represented feature or record. | source_attribute | Yes | No | No |
| `form_of_way` | `text` | Publisher-supplied form of way for the represented feature or record. | source_attribute | Yes | No | No |
| `road_classification_number` | `text` | Publisher-supplied road classification number for the represented feature or record. | source_attribute | Yes | No | No |
| `name_1` | `text` | Publisher-supplied name 1 for the represented feature or record. | source_attribute | Yes | No | No |
| `name_1_lang` | `text` | Publisher-supplied name 1 lang for the represented feature or record. | source_attribute | Yes | No | No |
| `name_2` | `text` | Publisher-supplied name 2 for the represented feature or record. | source_attribute | Yes | No | No |
| `name_2_lang` | `text` | Publisher-supplied name 2 lang for the represented feature or record. | source_attribute | Yes | No | No |
| `road_structure` | `text` | Publisher-supplied road structure for the represented feature or record. | source_attribute | Yes | No | No |
| `length` | `double precision` | Numeric length value recorded for the feature. | measure | Yes | No | No |
| `length_uom` | `text` | Publisher-supplied length uom for the represented feature or record. | source_attribute | Yes | No | No |
| `loop` | `boolean` | Publisher-supplied loop for the represented feature or record. | source_attribute | Yes | No | No |
| `primary_route` | `boolean` | Publisher-supplied primary route for the represented feature or record. | source_attribute | Yes | No | No |
| `trunk_road` | `boolean` | Publisher-supplied trunk road for the represented feature or record. | source_attribute | Yes | No | No |
| `start_node` | `text` | Publisher-supplied start node for the represented feature or record. | source_attribute | Yes | No | No |
| `end_node` | `text` | Publisher-supplied end node for the represented feature or record. | source_attribute | Yes | No | No |
| `road_number_toid` | `text` | Publisher-assigned road number toid for the record. | source_identifier | Yes | No | No |
| `road_name_toid` | `text` | Publisher-assigned road name toid for the record. | source_identifier | Yes | No | No |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
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
