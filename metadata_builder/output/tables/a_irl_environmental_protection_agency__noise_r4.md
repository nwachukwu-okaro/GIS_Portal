# Noise R4

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/noise_r4`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.787780, 51.579567, -5.939564, 55.126074]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `noise_r4`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29903
- **Rows:** 764
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Noise R4 is an authoritative dataset published by Environmental Protection Agency Ireland. It represents noise r4 features using multipolygon geometry.

## Lineage

Published by the Environmental Protection Agency Ireland as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `nr4_pk` | `integer` | Primary-key identifier for records in noise_r4. |
| `noise_round_type` | `varchar(20)` |  |
| `name` | `varchar(50)` | Official or publisher-assigned name of the represented feature. |
| `type` | `varchar(20)` |  |
| `report_period` | `varchar(10)` |  |
| `db_low` | `double precision` |  |
| `db_high` | `double precision` |  |
| `db_value` | `varchar(20)` |  |
| `time` | `varchar(20)` |  |
| `local_authority_name` | `varchar(50)` | Name associated with the represented feature. |
| `eden_code` | `varchar(10)` | Code assigned by the source dataset. |
| `url_text` | `varchar(30)` |  |
| `url` | `varchar(500)` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
