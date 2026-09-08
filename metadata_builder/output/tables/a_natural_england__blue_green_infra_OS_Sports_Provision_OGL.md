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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
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
| `dataset` | `varchar(255)` | Publisher-supplied dataset for the represented feature or record. |
| `accessible` | `varchar(255)` | Publisher-supplied accessible for the represented feature or record. |
| `angst` | `varchar(255)` | Publisher-supplied angst for the represented feature or record. |
| `naturalness` | `integer` | Count or numeric value for naturalness in the represented area. |
| `typologytitle` | `varchar(255)` | Publisher-supplied typologytitle for the represented feature or record. |
| `license` | `varchar(255)` | Publisher-supplied license for the represented feature or record. |
| `greenspacetopology` | `integer` | Count or numeric value for greenspacetopology in the represented area. |
| `habitat` | `integer` | Count or numeric value for habitat in the represented area. |
| `designation` | `integer` | Count or numeric value for designation in the represented area. |
| `attribute` | `varchar(8000)` | Publisher-supplied attribute for the represented feature or record. |
| `typologycode` | `varchar(255)` | Publisher-assigned typologycode for the record. |
| `orig_area` | `double precision` | Numeric orig area value recorded for the feature. |
| `perc_manmade` | `double precision` | Count or numeric value for perc manmade in the represented area. |
| `vxcount` | `integer` | Count or numeric value for vxcount in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
