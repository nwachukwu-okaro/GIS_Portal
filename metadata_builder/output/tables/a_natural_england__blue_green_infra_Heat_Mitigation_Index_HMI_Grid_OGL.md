# Blue Green Infra Heat Mitigation Index Hmi Grid Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Heat_Mitigation_Index_HMI_Grid_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418746, 49.864551, 1.764598, 55.811556]`
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Heat_Mitigation_Index_HMI_Grid_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 2102902
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Blue Green Infra Heat Mitigation Index Hmi Grid Ogl is an authoritative dataset published by Natural England. It represents blue green infra heat mitigation index hmi grid ogl features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `urban` | `smallint` | Count or numeric value for urban in the represented area. | statistical_value | Yes | No | No |
| `orig_area` | `double precision` | Numeric orig area value recorded for the feature. | measure | Yes | No | No |
| `mandmadearea` | `double precision` | Numeric mandmadearea value recorded for the feature. | measure | Yes | No | No |
| `percmanmade` | `double precision` | Count or numeric value for percmanmade in the represented area. | statistical_value | Yes | No | No |
| `heatmiti` | `double precision` | Count or numeric value for heatmiti in the represented area. | statistical_value | Yes | No | No |
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
