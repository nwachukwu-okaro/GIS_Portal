# Blue Green Infra Prow Experiential Terrain Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_PRoW_Experiential_Terrain_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.715763, 49.959198, 1.760872, 55.810765]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_PRoW_Experiential_Terrain_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 3196113
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Blue Green Infra Prow Experiential Terrain Ogl is an authoritative dataset published by Natural England. It represents blue green infra prow experiential terrain ogl features using multipolygon geometry.

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
| `type` | `varchar(50)` | Publisher-supplied type for the represented feature or record. |
| `experiential_terrain_class` | `varchar(255)` | Publisher-supplied experiential terrain class for the represented feature or record. |
| `phys_desc` | `varchar(50)` | Publisher-supplied phys description for the represented feature or record. |
| `lform_desc` | `varchar(50)` | Publisher-supplied lform description for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
