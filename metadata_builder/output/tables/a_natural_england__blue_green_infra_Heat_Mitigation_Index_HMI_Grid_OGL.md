# Blue Green Infra Heat Mitigation Index Hmi Grid Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Heat_Mitigation_Index_HMI_Grid_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418746, 49.864551, 1.764598, 55.811556]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Heat_Mitigation_Index_HMI_Grid_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 2102902
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Blue Green Infra Heat Mitigation Index Hmi Grid Ogl is an authoritative dataset published by Natural England. It represents blue green infra heat mitigation index hmi grid ogl features using multipolygon geometry.

## Lineage

Published by Natural England as open environmental and conservation data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `urban` | `smallint` | Count or numeric value for urban in the represented area. |
| `orig_area` | `double precision` | Numeric orig area value recorded for the feature. |
| `mandmadearea` | `double precision` | Numeric mandmadearea value recorded for the feature. |
| `percmanmade` | `double precision` | Count or numeric value for percmanmade in the represented area. |
| `heatmiti` | `double precision` | Count or numeric value for heatmiti in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
