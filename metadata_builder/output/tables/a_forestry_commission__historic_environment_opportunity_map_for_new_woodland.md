# Historic Environment Opportunity Map For New Woodland

## Overview

- **Identifier:** `a_forestry_commission/historic_environment_opportunity_map_for_new_woodland`
- **Source organisation:** Forestry Commission
- **Source:** https://www.forestresearch.gov.uk/tools-and-resources/national-forest-inventory/
- **WGS84 extent:** `[-6.418877, 49.864767, 1.769120, 55.811664]`
- **Topic category:** biota
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_forestry_commission`
- **Table:** `historic_environment_opportunity_map_for_new_woodland`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 552503
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

version: 20250408
Source: https://environment.data.gov.uk/dataset/00354b01-c138-4aca-b2a1-4504dc40be5c

Attribution: © Forestry Commission copyright and/or database right 2025. All rights reserved.

## Lineage

Published by Forestry Commission as part of the National Forest Inventory. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `opportunit` | `varchar(32)` | Suitability class for woodland creation based on historic-environment constraints, such as Favourable, Neutral or Unsuitable. |
| `area_ha` | `double precision` | Area enclosed by the feature, measured in hectares. |
| `fcid` | `integer` | Forestry Commission identifier assigned to the mapped opportunity feature. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
