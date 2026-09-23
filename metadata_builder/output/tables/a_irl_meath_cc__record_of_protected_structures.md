# Record Of Protected Structures

## Overview

- **Identifier:** `a_irl_meath_cc/record_of_protected_structures`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.306272, 53.393003, -6.213299, 53.898268]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_irl_meath_cc`
- **Table:** `record_of_protected_structures`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 1410
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Record Of Protected Structures is an authoritative dataset published by Meath County Council. It represents record of protected structures features using point geometry.

## Lineage

Published by Meath County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `rps_pk` | `integer` | Primary-key identifier for records in record_of_protected_structures. |
| `la_rps_id` | `double precision` | Identifier assigned by the source dataset. |
| `niah_reg_n` | `double precision` |  |
| `municipal_` | `varchar(36)` |  |
| `townland` | `varchar(58)` |  |
| `town` | `varchar(34)` |  |
| `street_tow` | `varchar(90)` |  |
| `cdp_settle` | `varchar(116)` |  |
| `structure_` | `varchar(100)` |  |
| `structur00` | `varchar(18)` |  |
| `building_t` | `varchar(100)` |  |
| `description` | `varchar(254)` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
