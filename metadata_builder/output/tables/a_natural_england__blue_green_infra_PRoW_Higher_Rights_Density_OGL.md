# Blue Green Infra Prow Higher Rights Density Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_PRoW_Higher_Rights_Density_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418557, 49.864685, 1.763546, 55.811072]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_PRoW_Higher_Rights_Density_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 131369
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Blue Green Infra Prow Higher Rights Density Ogl is an authoritative dataset published by Natural England. It represents blue green infra prow higher rights density ogl features using multipolygon geometry.

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
| `boat_length_m` | `integer` | Numeric boat length male value recorded for the feature. |
| `restricted_byway_length_m` | `integer` | Numeric restricted byway length male value recorded for the feature. |
| `bridleway_length_m` | `integer` | Numeric bridleway length male value recorded for the feature. |
| `higher_rights_m` | `double precision` | Count or numeric value for higher rights male in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
