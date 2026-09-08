# Protected View And Prospect

## Overview

- **Identifier:** `a_irl_meath_cc/protected_view_and_prospect`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-6.960533, 53.396144, -6.229006, 53.853611]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_irl_meath_cc`
- **Table:** `protected_view_and_prospect`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 77
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

Protected View And Prospect is an authoritative dataset published by Meath County Council. It represents protected view and prospect features using point geometry.

## Lineage

Published by Meath County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `pvp_pk` | `integer` | Count or numeric value for pvp pk in the represented area. |
| `map_label` | `varchar(100)` | Publisher-supplied map label for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
