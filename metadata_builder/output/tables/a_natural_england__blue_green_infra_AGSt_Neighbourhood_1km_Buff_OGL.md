# Blue Green Infra Agst Neighbourhood 1km Buff Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_AGSt_Neighbourhood_1km_Buff_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.731004, 49.949980, 1.772636, 55.664544]`
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_AGSt_Neighbourhood_1km_Buff_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1212
- **Columns:** 2
- **Metadata status:** source_mapped

## Description

Blue Green Infra Agst Neighbourhood 1km Buff Ogl is an authoritative dataset published by Natural England. It represents blue green infra agst neighbourhood 1km buff ogl features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
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
