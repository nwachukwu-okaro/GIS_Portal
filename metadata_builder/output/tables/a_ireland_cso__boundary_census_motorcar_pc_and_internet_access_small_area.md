# Boundary Census Motorcar Pc And Internet Access Small Area

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_motorcar_pc_and_internet_access_small_area`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.726726, 54.563349, 3.417194, 58.519873]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_motorcar_pc_and_internet_access_small_area`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 18919
- **Columns:** 18
- **Metadata status:** source_mapped

## Description

Boundary Census Motorcar Pc And Internet Access Small Area is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census motorcar pc and internet access small area features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `guid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `geogid` | `text` | Code identifying the geographical area represented by the row. |
| `geogdesc` | `text` |  |
| `ur_category` | `double precision` |  |
| `ur_category_desc` | `text` |  |
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
