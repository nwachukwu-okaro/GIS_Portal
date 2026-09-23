# Tree Preservation Order

## Overview

- **Identifier:** `a_irl_meath_cc/tree_preservation_order`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-6.859796, 53.477875, -6.256054, 53.717973]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_irl_meath_cc`
- **Table:** `tree_preservation_order`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 8
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Tree Preservation Order is an authoritative dataset published by Meath County Council. It represents tree preservation order features using point geometry.

## Lineage

Published by Meath County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `tpo_pk` | `integer` | Primary-key identifier for records in tree_preservation_order. |
| `tpo_number` | `varchar(20)` |  |
| `tpo_location` | `varchar(100)` |  |
| `remarks` | `varchar(100)` |  |
| `settlement` | `bigint` |  |
| `settlement1` | `varchar(100)` |  |
| `plan_name` | `varchar(120)` | Name associated with the represented feature. |
| `map_label` | `varchar(100)` |  |
| `object_inf` | `varchar(20)` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
