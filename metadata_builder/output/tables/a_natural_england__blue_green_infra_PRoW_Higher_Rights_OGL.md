# Blue Green Infra Prow Higher Rights Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_PRoW_Higher_Rights_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.710662, 49.960143, 1.751415, 55.805063]`
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_PRoW_Higher_Rights_OGL`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 83882
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Blue Green Infra Prow Higher Rights Ogl is an authoritative dataset published by Natural England. It represents blue green infra prow higher rights ogl features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `name` | `varchar(254)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `folderpath` | `varchar(254)` | Publisher-supplied folderpath for the represented feature or record. | source_attribute | Yes | No | No |
| `type` | `varchar(254)` | Publisher-supplied type for the represented feature or record. | source_attribute | Yes | No | No |
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
