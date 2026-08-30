# Boundary Census Motor Car Pc Internet Access Province

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_motor_car_pc_internet_access_province`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.682125, 51.420091, -5.996278, 55.446936]`
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_motor_car_pc_internet_access_province`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 4
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

Boundary Census Motor Car Pc Internet Access Province is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census motor car pc internet access province features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `geogid` | `text` | Publisher-assigned geogid for the record. | source_identifier | Yes | No | No |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `no_motor_car` | `bigint` | Count or numeric value for number motor car in the represented area. | statistical_value | Yes | No | No |
| `t_1_motor_car` | `bigint` | Count or numeric value for t 1 motor car in the represented area. | statistical_value | Yes | No | No |
| `t_2_motor_cars` | `bigint` | Count or numeric value for t 2 motor cars in the represented area. | statistical_value | Yes | No | No |
| `t_3_motor_cars` | `bigint` | Count or numeric value for t 3 motor cars in the represented area. | statistical_value | Yes | No | No |
| `t_4_or_more_motor_cars` | `bigint` | Count or numeric value for t 4 or more motor cars in the represented area. | statistical_value | Yes | No | No |
| `not_stated` | `bigint` | Count or numeric value for not stated in the represented area. | statistical_value | Yes | No | No |
| `total` | `bigint` | Count or numeric value for total in the represented area. | statistical_value | Yes | No | No |
| `broadband` | `bigint` | Count or numeric value for broadband in the represented area. | statistical_value | Yes | No | No |
| `other_internet_connection` | `bigint` | Count or numeric value for other internet connection in the represented area. | statistical_value | Yes | No | No |
| `no_internet_connection` | `bigint` | Count or numeric value for number internet connection in the represented area. | statistical_value | Yes | No | No |
| `type_of_internet_connection_not_stated` | `bigint` | Count or numeric value for type of internet connection not stated in the represented area. | statistical_value | Yes | No | No |
| `all_internet_connections` | `bigint` | Count or numeric value for all internet connections in the represented area. | statistical_value | Yes | No | No |
| `area` | `double precision` | Numeric area value recorded for the feature. | measure | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

## Supported operations

- filter
- select
- reproject
- validate_geometry
- buffer
- clip
- intersect
- spatial_join
- export

## Operation requirements

- Intersect, clip and spatial-join inputs must use matching coordinate reference systems.
- Buffer operations require a suitable projected coordinate reference system.
- Reprojection is performed on working outputs; source tables remain unchanged.

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
