# Railway Track

## Overview

- **Identifier:** `a_os_open_map_local/railway_track`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Map Local
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-map-local
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-6.145539, 50.120798, 1.749664, 60.424421]`
- **Schema:** `a_os_open_map_local`
- **Table:** `railway_track`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 113560
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Contains OS data © Crown copyright and database right 2026

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `classification` | `varchar` | Publisher-supplied classification for the represented feature or record. | source_attribute | Yes | No | No |
| `feature_code` | `integer` | Code assigned by the source dataset. | code | Yes | No | No |
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
