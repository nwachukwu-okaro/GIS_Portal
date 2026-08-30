# Blue Green Infra Prow Network Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_PRoW_Network_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.716482, 49.959104, 1.760685, 55.810713]`
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_PRoW_Network_OGL`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 448195
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Blue Green Infra Prow Network Ogl is an authoritative dataset published by Natural England. It represents blue green infra prow network ogl features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `name` | `varchar(254)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `folderpath` | `varchar(254)` | Publisher-supplied folderpath for the represented feature or record. | source_attribute | Yes | No | No |
| `accesstype` | `varchar(255)` | Publisher-supplied accesstype for the represented feature or record. | source_attribute | Yes | No | No |
| `accessible_for` | `varchar(255)` | Publisher-supplied accessible for for the represented feature or record. | source_attribute | Yes | No | No |
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
