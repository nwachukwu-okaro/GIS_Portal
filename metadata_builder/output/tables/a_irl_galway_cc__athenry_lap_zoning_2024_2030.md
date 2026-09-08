# Athenry Lap Zoning 2024 2030

## Overview

- **Identifier:** `a_irl_galway_cc/athenry_lap_zoning_2024_2030`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-8.781623, 53.284632, -8.723046, 53.315870]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_galway_cc`
- **Table:** `athenry_lap_zoning_2024_2030`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 583
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Athenry Lap Zoning 2024 2030 is an authoritative dataset published by Galway County Council. It represents athenry lap zoning 2024 2030 features using multipolygon geometry.

## Lineage

Published by Galway County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `object_id` | `smallint` | Identifier assigned by the source dataset. |
| `zoning_abb` | `varchar` | Publisher-supplied zoning abb for the represented feature or record. |
| `zoning` | `varchar` | Publisher-supplied zoning for the represented feature or record. |
| `status` | `varchar` | Publisher-supplied status for the represented feature or record. |
| `town` | `varchar` | Publisher-supplied town for the represented feature or record. |
| `plan_name` | `varchar` | Name associated with the represented feature. |
| `opportunit` | `varchar` | Publisher-supplied opportunit for the represented feature or record. |
| `policy_obj` | `varchar` | Publisher-supplied policy obj for the represented feature or record. |
| `policy_o_1` | `varchar` | Publisher-supplied policy o 1 for the represented feature or record. |
| `globabl_id` | `varchar` | Identifier assigned by the source dataset. |
| `myplan_gzt` | `varchar` | Publisher-supplied myplan gzt for the represented feature or record. |
| `luz_pk` | `integer` | Count or numeric value for luz pk in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
