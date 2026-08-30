# Motor Car Pc Internet Access Province

## Overview

- **Identifier:** `a_ireland_cso/motor_car_pc_internet_access_province`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Schema:** `a_ireland_cso`
- **Table:** `motor_car_pc_internet_access_province`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 5
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Motor Car Pc Internet Access Province is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to motor car pc internet access province.

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

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
