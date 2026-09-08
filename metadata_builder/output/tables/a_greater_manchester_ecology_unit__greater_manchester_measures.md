# Greater Manchester Measures

## Overview

- **Identifier:** `a_greater_manchester_ecology_unit/greater_manchester_measures`
- **Source organisation:** Greater Manchester Ecology Unit
- **Source:** https://www.gmenvironment.org.uk/gmeu/
- **WGS84 extent:** `[-2.727031, 53.327182, -1.909622, 53.685720]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_greater_manchester_ecology_unit`
- **Table:** `greater_manchester_measures`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 175773
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Greater Manchester Measures is an authoritative dataset published by Greater Manchester Ecology Unit. It represents greater manchester measures features using multipolygon geometry.

## Lineage

Published by Greater Manchester Ecology Unit as open ecological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `gmm_pk` | `integer` | Internal primary-key value for the Greater Manchester ecological measure. |
| `lnrs_id` | `numeric` | Identifier assigned by the source dataset. |
| `pm_loc_id` | `numeric` | Identifier assigned by the source dataset. |
| `pm_id` | `numeric` | Identifier assigned by the source dataset. |
| `pm_desc` | `varchar(250)` | Description of the proposed ecological measure or habitat intervention. |
| `priority_1` | `varchar(250)` | Primary nature-recovery priority associated with the proposed measure. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
