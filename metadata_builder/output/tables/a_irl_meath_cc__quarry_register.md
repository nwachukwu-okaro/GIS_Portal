# Quarry Register

## Overview

- **Identifier:** `a_irl_meath_cc/quarry_register`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.294228, 53.385624, -6.218810, 53.901445]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_irl_meath_cc`
- **Table:** `quarry_register`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 318
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Quarry Register is an authoritative dataset published by Meath County Council. It represents quarry register features using point geometry.

## Lineage

Published by Meath County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `qr_pk` | `integer` |  |
| `ref_no` | `varchar(10)` |  |
| `location_o` | `varchar(104)` |  |
| `townland` | `varchar(50)` |  |
| `municipal_` | `varchar(40)` |  |
| `more_info` | `varchar(254)` |  |
| `map_label` | `varchar(100)` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
