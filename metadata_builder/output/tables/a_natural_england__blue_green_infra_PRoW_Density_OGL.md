# Blue Green Infra Prow Density Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_PRoW_Density_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418557, 49.864685, 1.763546, 55.811072]`
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_PRoW_Density_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 131369
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Blue Green Infra Prow Density Ogl is an authoritative dataset published by Natural England. It represents blue green infra prow density ogl features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `total_prow_m` | `double precision` | Count or numeric value for total prow male in the represented area. | statistical_value | Yes | No | No |
| `footpath_length_m` | `integer` | Numeric footpath length male value recorded for the feature. | measure | Yes | No | No |
| `boat_length_m` | `integer` | Numeric boat length male value recorded for the feature. | measure | Yes | No | No |
| `restricted_byway_length_m` | `integer` | Numeric restricted byway length male value recorded for the feature. | measure | Yes | No | No |
| `bridleway_length_m` | `integer` | Numeric bridleway length male value recorded for the feature. | measure | Yes | No | No |
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
