# Blue Green Infra Accessible Waterside Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Accessible_Waterside_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.714067, 49.963839, 1.757875, 55.803013]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Accessible_Waterside_OGL`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 451956
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Blue Green Infra Accessible Waterside Ogl is an authoritative dataset published by Natural England. It represents blue green infra accessible waterside ogl features using multilinestring geometry.

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
| `left_fid` | `integer` | Count or numeric value for left fid in the represented area. |
| `right_fid` | `integer` | Count or numeric value for right fid in the represented area. |
| `id` | `varchar(38)` | Publisher-assigned identifier for the record. |
| `featcode` | `integer` | Count or numeric value for featcode in the represented area. |
| `shape_length` | `double precision` | Numeric shape length value recorded for the feature. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
