# Corine Land Cover 2018

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/corine_land_cover_2018`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-11.032268, 51.195129, -5.615331, 55.627838]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `corine_land_cover_2018`
- **Geometry:** POLYGON
- **CRS:** EPSG:29902
- **Rows:** 18882
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Corine Land Cover 2018 is an authoritative dataset published by Environmental Protection Agency Ireland. It represents corine land cover 2018 features using polygon geometry.

## Lineage

Published by the Environmental Protection Agency Ireland as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `clc18_pk` | `integer` | Count or numeric value for clc18 pk in the represented area. |
| `code_18` | `varchar(10)` | Publisher-supplied code 18 for the represented feature or record. |
| `class_description` | `varchar(200)` | Publisher-supplied class description for the represented feature or record. |
| `area_ha` | `double precision` | Area enclosed by the feature, measured in hectares. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
