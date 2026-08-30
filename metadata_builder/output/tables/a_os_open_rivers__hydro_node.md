# Hydro Node

## Overview

- **Identifier:** `a_os_open_rivers/hydro_node`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Rivers
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-rivers
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.524879, 49.974616, 1.756276, 60.825228]`
- **Schema:** `a_os_open_rivers`
- **Table:** `hydro_node`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 197734
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Hydro Node is part of OS Open Rivers, published by Ordnance Survey. It represents hydro node features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `hydro_node_category` | `varchar` | Publisher-supplied hydro node category for the represented feature or record. | source_attribute | Yes | No | No |
| `fid` | `integer` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
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
