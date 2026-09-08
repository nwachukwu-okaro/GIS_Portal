# Trees To Be Protected

## Overview

- **Identifier:** `a_irl_meath_cc/trees_to_be_protected`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.166354, 53.411316, -6.231530, 53.851763]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_irl_meath_cc`
- **Table:** `trees_to_be_protected`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 911
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Trees To Be Protected is an authoritative dataset published by Meath County Council. It represents trees to be protected features using point geometry.

## Lineage

Published by Meath County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `tp_pk` | `integer` | Count or numeric value for tp pk in the represented area. |
| `settlement` | `double precision` | Count or numeric value for settlement in the represented area. |
| `settlement2` | `varchar(60)` |  |
| `objective` | `varchar(250)` | Publisher-supplied objective for the represented feature or record. |
| `plan_name` | `varchar(120)` | Name associated with the represented feature. |
| `map_label` | `varchar(100)` | Publisher-supplied map label for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
