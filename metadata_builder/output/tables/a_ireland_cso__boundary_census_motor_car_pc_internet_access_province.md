# Boundary Census Motor Car Pc Internet Access Province

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_motor_car_pc_internet_access_province`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.682125, 51.420091, -5.996278, 55.446936]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_motor_car_pc_internet_access_province`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 4
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

Boundary Census Motor Car Pc Internet Access Province is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census motor car pc internet access province features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. |
| `geogid` | `text` | Publisher-assigned geogid for the record. |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. |
| `no_motor_car` | `bigint` | Count or numeric value for number motor car in the represented area. |
| `t_1_motor_car` | `bigint` | Count or numeric value for t 1 motor car in the represented area. |
| `t_2_motor_cars` | `bigint` | Count or numeric value for t 2 motor cars in the represented area. |
| `t_3_motor_cars` | `bigint` | Count or numeric value for t 3 motor cars in the represented area. |
| `t_4_or_more_motor_cars` | `bigint` | Count or numeric value for t 4 or more motor cars in the represented area. |
| `not_stated` | `bigint` | Count or numeric value for not stated in the represented area. |
| `total` | `bigint` | Count or numeric value for total in the represented area. |
| `broadband` | `bigint` | Count or numeric value for broadband in the represented area. |
| `other_internet_connection` | `bigint` | Count or numeric value for other internet connection in the represented area. |
| `no_internet_connection` | `bigint` | Count or numeric value for number internet connection in the represented area. |
| `type_of_internet_connection_not_stated` | `bigint` | Count or numeric value for type of internet connection not stated in the represented area. |
| `all_internet_connections` | `bigint` | Count or numeric value for all internet connections in the represented area. |
| `area` | `double precision` | Numeric area value recorded for the feature. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
