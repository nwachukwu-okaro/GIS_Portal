# Blue Green Infra Prow Experiential Terrain Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_PRoW_Experiential_Terrain_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.715763, 49.959198, 1.760872, 55.810765]`
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_PRoW_Experiential_Terrain_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 3196113
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Blue Green Infra Prow Experiential Terrain Ogl is an authoritative dataset published by Natural England. It represents blue green infra prow experiential terrain ogl features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `type` | `varchar(50)` | Publisher-supplied type for the represented feature or record. | source_attribute | Yes | No | No |
| `experiential_terrain_class` | `varchar(255)` | Publisher-supplied experiential terrain class for the represented feature or record. | source_attribute | Yes | No | No |
| `phys_desc` | `varchar(50)` | Publisher-supplied phys description for the represented feature or record. | source_attribute | Yes | No | No |
| `lform_desc` | `varchar(50)` | Publisher-supplied lform description for the represented feature or record. | source_attribute | Yes | No | No |
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
