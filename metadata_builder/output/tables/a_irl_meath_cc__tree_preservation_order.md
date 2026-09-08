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
| `tpo_pk` | `integer` | Count or numeric value for tpo pk in the represented area. |
| `tpo_number` | `varchar(20)` | Publisher-supplied tpo number for the represented feature or record. |
| `tpo_location` | `varchar(100)` | Publisher-supplied tpo location for the represented feature or record. |
| `remarks` | `varchar(100)` | Publisher-supplied remarks for the represented feature or record. |
| `settlement` | `bigint` | Count or numeric value for settlement in the represented area. |
| `settlement1` | `varchar(100)` |  |
| `plan_name` | `varchar(120)` | Name associated with the represented feature. |
| `map_label` | `varchar(100)` | Publisher-supplied map label for the represented feature or record. |
| `object_inf` | `varchar(20)` | Publisher-supplied object inf for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
