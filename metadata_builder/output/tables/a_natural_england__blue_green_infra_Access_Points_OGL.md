# Blue Green Infra Access Points Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Access_Points_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.351368, 49.893298, 1.758079, 55.787125]`
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Access_Points_OGL`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 333676
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Blue Green Infra Access Points Ogl is an authoritative dataset published by Natural England. It represents blue green infra access points ogl features using multipoint geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
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
