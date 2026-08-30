# Noise R4

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/noise_r4`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.787780, 51.579567, -5.939564, 55.126074]`
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `noise_r4`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29903
- **Rows:** 764
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Noise R4 is an authoritative dataset published by Environmental Protection Agency Ireland. It represents noise r4 features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `nr4_pk` | `integer` | Count or numeric value for nr4 pk in the represented area. | statistical_value | Yes | No | No |
| `noise_round_type` | `varchar(20)` | Publisher-supplied noise round type for the represented feature or record. | source_attribute | Yes | No | No |
| `name` | `varchar(50)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `type` | `varchar(20)` | Publisher-supplied type for the represented feature or record. | source_attribute | Yes | No | No |
| `report_period` | `varchar(10)` | Publisher-supplied report period for the represented feature or record. | source_attribute | Yes | No | No |
| `db_low` | `double precision` | Count or numeric value for db low in the represented area. | statistical_value | Yes | No | No |
| `db_high` | `double precision` | Count or numeric value for db high in the represented area. | statistical_value | Yes | No | No |
| `db_value` | `varchar(20)` | Publisher-supplied db value for the represented feature or record. | source_attribute | Yes | No | No |
| `time` | `varchar(20)` | Publisher-supplied time for the represented feature or record. | source_attribute | Yes | No | No |
| `local_authority_name` | `varchar(50)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `eden_code` | `varchar(10)` | Code assigned by the source dataset. | code | Yes | No | No |
| `url_text` | `varchar(30)` | Publisher-supplied url text for the represented feature or record. | source_attribute | Yes | No | No |
| `url` | `varchar(500)` | Publisher-supplied url for the represented feature or record. | source_attribute | Yes | No | No |
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
