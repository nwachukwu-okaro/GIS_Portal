# Blue Green Infra Woodland Access Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Woodland_Access_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.345669, 49.889357, 1.757345, 55.806479]`
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Woodland_Access_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 734072
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Blue Green Infra Woodland Access Ogl is an authoritative dataset published by Natural England. It represents blue green infra woodland access ogl features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `accesslevel` | `varchar(255)` | Publisher-supplied accesslevel for the represented feature or record. | source_attribute | Yes | No | No |
| `area_ha` | `double precision` | Area enclosed by the feature, measured in hectares. | area | Yes | No | No |
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
