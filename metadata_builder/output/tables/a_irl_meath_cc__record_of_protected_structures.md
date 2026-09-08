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
| `rps_pk` | `integer` | Count or numeric value for rps pk in the represented area. |
| `la_rps_id` | `double precision` | Identifier assigned by the source dataset. |
| `niah_reg_n` | `double precision` | Count or numeric value for niah reg n in the represented area. |
| `municipal_` | `varchar(36)` | Publisher-supplied municipal for the represented feature or record. |
| `townland` | `varchar(58)` | Publisher-supplied townland for the represented feature or record. |
| `town` | `varchar(34)` | Publisher-supplied town for the represented feature or record. |
| `street_tow` | `varchar(90)` | Publisher-supplied street tow for the represented feature or record. |
| `cdp_settle` | `varchar(116)` | Publisher-supplied cdp settle for the represented feature or record. |
| `structure_` | `varchar(100)` | Publisher-supplied structure for the represented feature or record. |
| `structur00` | `varchar(18)` |  |
| `building_t` | `varchar(100)` | Publisher-supplied building t for the represented feature or record. |
| `description` | `varchar(254)` | Publisher-supplied description for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
