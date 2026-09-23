# Blue Green Infra OS Sports Provision Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_OS_Sports_Provision_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.333381, 49.912104, 1.758236, 55.788363]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_OS_Sports_Provision_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 74573
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Blue Green Infra OS Sports Provision Ogl is an authoritative dataset published by Natural England. It represents blue green infra os sports provision ogl features using multipolygon geometry.

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
| `dataset` | `varchar(255)` |  |
| `accessible` | `varchar(255)` |  |
| `angst` | `varchar(255)` |  |
| `naturalness` | `integer` |  |
| `typologytitle` | `varchar(255)` |  |
| `license` | `varchar(255)` |  |
| `greenspacetopology` | `integer` |  |
| `habitat` | `integer` |  |
| `designation` | `integer` |  |
| `attribute` | `varchar(8000)` |  |
| `typologycode` | `varchar(255)` |  |
| `orig_area` | `double precision` |  |
| `perc_manmade` | `double precision` |  |
| `vxcount` | `integer` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
