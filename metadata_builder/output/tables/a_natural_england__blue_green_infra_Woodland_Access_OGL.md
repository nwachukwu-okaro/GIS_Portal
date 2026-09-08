# Blue Green Infra Woodland Access Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Woodland_Access_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.345669, 49.889357, 1.757345, 55.806479]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Woodland_Access_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 734072
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Blue Green Infra Woodland Access Ogl is an authoritative dataset published by Natural England. It represents blue green infra woodland access ogl features using multipolygon geometry.

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
| `accesslevel` | `varchar(255)` | Publisher-supplied accesslevel for the represented feature or record. |
| `area_ha` | `double precision` | Area enclosed by the feature, measured in hectares. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
