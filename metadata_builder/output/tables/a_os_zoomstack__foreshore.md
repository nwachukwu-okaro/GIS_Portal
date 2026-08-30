# Foreshore

## Overview

- **Identifier:** `a_os_zoomstack/foreshore`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Zoomstack
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-zoomstack
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.648511, 49.863142, 1.763537, 60.860837]`
- **Schema:** `a_os_zoomstack`
- **Table:** `foreshore`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 35677
- **Columns:** 2
- **Metadata status:** source_mapped

## Description

Foreshore is part of OS Open Zoomstack, published by Ordnance Survey. It represents foreshore features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
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
