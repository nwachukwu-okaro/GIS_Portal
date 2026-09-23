# Blue Green Infra All Gi Bi Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_All_GI_BI_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418945, 49.864637, 1.768950, 55.811668]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_All_GI_BI_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1765624
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Blue Green Infra All Gi Bi Ogl is an authoritative dataset published by Natural England. It represents blue green infra all gi bi ogl features using multipolygon geometry.

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
| `parent_id` | `varchar(254)` | Identifier assigned by the source dataset. |
| `dataset` | `varchar(255)` |  |
| `accessible` | `varchar(255)` |  |
| `angst` | `varchar(255)` |  |
| `naturalness` | `integer` |  |
| `typologytitle` | `varchar(255)` |  |
| `likely_cricket` | `varchar(255)` |  |
| `license` | `varchar(255)` |  |
| `typologycode` | `varchar(255)` |  |
| `perc_manmade` | `double precision` |  |
| `join_id` | `integer` | Identifier assigned by the source dataset. |
| `attribute` | `varchar(255)` |  |
| `shape_length` | `double precision` |  |
| `shape_area` | `double precision` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
