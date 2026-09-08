# Planning Part 8

## Overview

- **Identifier:** `a_irl_galway_cc/planning_part_8`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.219259, 52.980785, -8.063640, 53.706012]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_galway_cc`
- **Table:** `planning_part_8`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 569
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Planning Part 8 is an authoritative dataset published by Galway County Council. It represents planning part 8 features using multipolygon geometry.

## Lineage

Published by Galway County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `double precision` | Publisher-assigned identifier for the record. |
| `plan_id` | `varchar` | Identifier assigned by the source dataset. |
| `desc_` | `varchar` | Publisher-supplied description for the represented feature or record. |
| `global_id` | `varchar` | Identifier assigned by the source dataset. |
| `object_id` | `integer` | Identifier assigned by the source dataset. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
