# Wfd River Water Body Catchments Cycle 3

## Overview

- **Identifier:** `a_environment_agency/wfd_river_water_body_catchments_cycle_3`
- **Source organisation:** Environment Agency
- **Source:** https://environment.data.gov.uk/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.691935, 49.994087, 1.749815, 55.749186]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_environment_agency`
- **Table:** `wfd_river_water_body_catchments_cycle_3`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 3824
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Wfd River Water Body Catchments Cycle 3 is an authoritative dataset published by Environment Agency. It represents wfd river water body catchments cycle 3 features using multipolygon geometry.

## Lineage

Published by Environment Agency as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `wb_cat` | `varchar` |  |
| `rbd_id` | `varchar` | Identifier assigned by the source dataset. |
| `mncat_name` | `varchar` | Name associated with the represented feature. |
| `rbd_name` | `varchar` | Name associated with the represented feature. |
| `opcat_id` | `varchar` | Identifier assigned by the source dataset. |
| `hydromorph` | `varchar` |  |
| `mancat_id` | `varchar` | Identifier assigned by the source dataset. |
| `url` | `varchar` |  |
| `opcat_name` | `varchar` | Name associated with the represented feature. |
| `wb_id` | `varchar` | Identifier assigned by the source dataset. |
| `version` | `varchar` |  |
| `wb_name` | `varchar` | Name associated with the represented feature. |
| `rwbcc_pk` | `integer` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
