# Greater Manchester Apib

## Overview

- **Identifier:** `a_greater_manchester_ecology_unit/greater_manchester_apib`
- **Source organisation:** Greater Manchester Ecology Unit
- **Source:** https://www.gmenvironment.org.uk/gmeu/
- **WGS84 extent:** `[-2.723911, 53.345913, -1.909622, 53.685117]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_greater_manchester_ecology_unit`
- **Table:** `greater_manchester_apib`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 2059
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Greater Manchester Apib is an authoritative dataset published by Greater Manchester Ecology Unit. It represents greater manchester apib features using multipolygon geometry.

## Lineage

Published by Greater Manchester Ecology Unit as open ecological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `lnrs_id` | `numeric` | Identifier assigned by the source dataset. |
| `apib_id` | `numeric` | Identifier assigned by the source dataset. |
| `apib_type` | `varchar(6)` | Type of area important for biodiversity, such as SAC, SPA, LWS or irreplaceable habitat. |
| `apib_name` | `varchar(60)` | Name associated with the represented feature. |
| `apib_site_` | `varchar(50)` | Source identifier of the biodiversity site represented by the feature. |
| `gmapib_pk` | `integer` | Internal primary-key value for the Greater Manchester APIB record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
