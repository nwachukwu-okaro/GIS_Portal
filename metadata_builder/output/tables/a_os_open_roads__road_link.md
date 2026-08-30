# Road Link

## Overview

- **Identifier:** `a_os_open_roads/road_link`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Roads
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-roads
- **Schema:** `a_os_open_roads`
- **Table:** `road_link`
- **Geometry:** LINESTRING
- **CRS:** EPSG:27700
- **Rows:** 3961077
- **Metadata status:** source_mapped

## Description

Road Link is part of OS Open Roads, published by Ordnance Survey. It represents road link features using linestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `fictitious` | `boolean` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `road_classification` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `road_function` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `form_of_way` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `road_classification_number` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `name_1` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `name_1_lang` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `name_2` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `name_2_lang` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `road_structure` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `length` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `length_uom` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `loop` | `boolean` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `primary_route` | `boolean` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `trunk_road` | `boolean` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `start_node` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `end_node` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `road_number_toid` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `road_name_toid` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
