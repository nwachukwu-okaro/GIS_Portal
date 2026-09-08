# Blue Green Infra Prow Higher Rights Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_PRoW_Higher_Rights_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.710662, 49.960143, 1.751415, 55.805063]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_PRoW_Higher_Rights_OGL`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 83882
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Blue Green Infra Prow Higher Rights Ogl is an authoritative dataset published by Natural England. It represents blue green infra prow higher rights ogl features using multilinestring geometry.

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
| `name` | `varchar(254)` | Official or publisher-assigned name of the represented feature. |
| `folderpath` | `varchar(254)` | Publisher-supplied folderpath for the represented feature or record. |
| `type` | `varchar(254)` | Publisher-supplied type for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
