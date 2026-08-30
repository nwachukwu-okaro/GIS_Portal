# Motorway Junction

## Overview

- **Identifier:** `a_os_open_roads/motorway_junction`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Roads
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-roads
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-4.556252, 50.680518, 1.155486, 56.384512]`
- **Schema:** `a_os_open_roads`
- **Table:** `motorway_junction`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 669
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Motorway Junction is part of OS Open Roads, published by Ordnance Survey. It represents motorway junction features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `junction_number` | `varchar` | Publisher-supplied junction number for the represented feature or record. | source_attribute | Yes | No | No |
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
