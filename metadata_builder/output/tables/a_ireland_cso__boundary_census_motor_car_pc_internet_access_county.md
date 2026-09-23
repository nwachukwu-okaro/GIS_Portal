# Boundary Census Motor Car Pc Internet Access County

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_motor_car_pc_internet_access_county`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.746471, 54.563349, 3.417194, 58.520162]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_motor_car_pc_internet_access_county`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 31
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

Boundary Census Motor Car Pc Internet Access County is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census motor car pc internet access county features using geometry geometry.

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
| `area` | `double precision` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
