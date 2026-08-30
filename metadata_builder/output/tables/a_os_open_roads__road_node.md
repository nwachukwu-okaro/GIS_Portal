# Road Node

## Overview

- **Identifier:** `a_os_open_roads/road_node`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Roads
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-roads
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.584537, 49.891062, 1.762169, 60.827676]`
- **Schema:** `a_os_open_roads`
- **Table:** `road_node`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 3346499
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Road Node is part of OS Open Roads, published by Ordnance Survey. It represents road node features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `text` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `form_of_road_node` | `text` | Publisher-supplied form of road node for the represented feature or record. | source_attribute | Yes | No | No |
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
