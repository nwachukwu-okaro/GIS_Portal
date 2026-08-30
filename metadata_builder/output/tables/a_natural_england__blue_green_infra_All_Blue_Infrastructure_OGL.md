# Blue Green Infra All Blue Infrastructure Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_All_Blue_Infrastructure_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_All_Blue_Infrastructure_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 942940
- **Metadata status:** source_mapped

## Description

Blue Green Infra All Blue Infrastructure Ogl is an authoritative dataset published by Natural England. It represents blue green infra all blue infrastructure ogl features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system object identifier. | identifier | Yes | No | No |
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
