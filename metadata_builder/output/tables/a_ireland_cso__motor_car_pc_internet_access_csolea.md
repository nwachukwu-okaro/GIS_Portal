# Motor Car Pc Internet Access Csolea

## Overview

- **Identifier:** `a_ireland_cso/motor_car_pc_internet_access_csolea`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_ireland_cso`
- **Table:** `motor_car_pc_internet_access_csolea`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 167
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Motor Car Pc Internet Access Csolea is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to motor car pc internet access csolea.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `guid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `geogid` | `text` | Code identifying the geographical area represented by the row. |
| `geogdesc` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `no_motor_car` | `bigint` |  |
| `t_1_motor_car` | `bigint` |  |
| `t_2_motor_cars` | `bigint` |  |
| `t_3_motor_cars` | `bigint` |  |
| `t_4_or_more_motor_cars` | `bigint` |  |
| `not_stated` | `bigint` |  |
| `total` | `bigint` |  |
| `broadband` | `bigint` |  |
| `other_internet_connection` | `bigint` |  |
| `no_internet_connection` | `bigint` |  |
| `type_of_internet_connection_not_stated` | `bigint` |  |
| `all_internet_connections` | `bigint` |  |
