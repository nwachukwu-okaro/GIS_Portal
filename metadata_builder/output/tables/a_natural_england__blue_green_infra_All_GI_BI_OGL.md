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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
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
| `dataset` | `varchar(255)` | Publisher-supplied dataset for the represented feature or record. |
| `accessible` | `varchar(255)` | Publisher-supplied accessible for the represented feature or record. |
| `angst` | `varchar(255)` | Publisher-supplied angst for the represented feature or record. |
| `naturalness` | `integer` | Count or numeric value for naturalness in the represented area. |
| `typologytitle` | `varchar(255)` | Publisher-supplied typologytitle for the represented feature or record. |
| `likely_cricket` | `varchar(255)` | Publisher-supplied likely cricket for the represented feature or record. |
| `license` | `varchar(255)` | Publisher-supplied license for the represented feature or record. |
| `typologycode` | `varchar(255)` | Publisher-assigned typologycode for the record. |
| `perc_manmade` | `double precision` | Count or numeric value for perc manmade in the represented area. |
| `join_id` | `integer` | Identifier assigned by the source dataset. |
| `attribute` | `varchar(255)` | Publisher-supplied attribute for the represented feature or record. |
| `shape_length` | `double precision` | Numeric shape length value recorded for the feature. |
| `shape_area` | `double precision` | Numeric shape area value recorded for the feature. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
