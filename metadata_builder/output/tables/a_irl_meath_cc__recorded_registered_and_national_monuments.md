# Recorded Registered And National Monuments

## Overview

- **Identifier:** `a_irl_meath_cc/recorded_registered_and_national_monuments`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.327602, 53.346681, -6.213423, 53.915137]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_irl_meath_cc`
- **Table:** `recorded_registered_and_national_monuments`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 4284
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Recorded Registered And National Monuments is an authoritative dataset published by Meath County Council. It represents recorded registered and national monuments features using point geometry.

## Lineage

Published by Meath County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `rrnm_pk` | `integer` | Count or numeric value for rrnm pk in the represented area. |
| `entity_id` | `varchar(7)` | Identifier assigned by the source dataset. |
| `class_code` | `varchar(4)` | Code assigned by the source dataset. |
| `class_description` | `varchar(60)` | Publisher-supplied class description for the represented feature or record. |
| `smrs` | `varchar(100)` |  |
| `townland` | `varchar(254)` | Publisher-supplied townland for the represented feature or record. |
| `map_label` | `varchar(100)` | Publisher-supplied map label for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
