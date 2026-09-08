# Planning Part 6

## Overview

- **Identifier:** `a_irl_galway_cc/planning_part_6`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-8.780426, 53.287029, -8.780426, 53.287029]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_irl_galway_cc`
- **Table:** `planning_part_6`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:2157
- **Rows:** 1
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Planning Part 6 is an authoritative dataset published by Galway County Council. It represents planning part 6 features using multipoint geometry.

## Lineage

Published by Galway County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `ref` | `varchar` | Publisher-assigned reference for the record. |
| `description` | `varchar` | Publisher-supplied description for the represented feature or record. |
| `global_id` | `varchar` | Identifier assigned by the source dataset. |
| `object_id` | `integer` | Identifier assigned by the source dataset. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
