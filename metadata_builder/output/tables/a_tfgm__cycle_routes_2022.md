# Cycle Routes 2022

## Overview

- **Identifier:** `a_tfgm/cycle_routes_2022`
- **Source organisation:** Transport for Greater Manchester
- **Source:** https://developer.tfgm.com/
- **Geographic coverage:** Greater Manchester
- **WGS84 extent:** `[-2.729156, 53.316610, -1.909767, 53.698304]`
- **Schema:** `a_tfgm`
- **Table:** `cycle_routes_2022`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 3573
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Cycle Routes 2022 is an authoritative dataset published by Transport for Greater Manchester. It represents cycle routes 2022 features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `cr_pk` | `integer` | Count or numeric value for cr pk in the represented area. | statistical_value | Yes | No | No |
| `routetype` | `bigint` | Count or numeric value for routetype in the represented area. | statistical_value | Yes | No | No |
| `routestatu` | `bigint` | Count or numeric value for routestatu in the represented area. | statistical_value | Yes | No | No |
| `routesurfa` | `bigint` | Count or numeric value for routesurfa in the represented area. | statistical_value | Yes | No | No |
| `ncnroute` | `bigint` | Count or numeric value for ncnroute in the represented area. | statistical_value | Yes | No | No |
| `ncnroutenu` | `bigint` | Count or numeric value for ncnroutenu in the represented area. | statistical_value | Yes | No | No |
| `notes` | `varchar(100)` | Publisher-supplied notes for the represented feature or record. | source_attribute | Yes | No | No |
| `date_updat` | `date` | Publisher-supplied date updat for the represented feature or record. | source_attribute | Yes | No | No |
| `strategic_` | `bigint` | Count or numeric value for strategic in the represented area. | statistical_value | Yes | No | No |
| `mand_advis` | `varchar(1)` | Publisher-supplied mand advis for the represented feature or record. | source_attribute | Yes | No | No |
| `recovery_s` | `varchar(4)` | Publisher-supplied recovery s for the represented feature or record. | source_attribute | Yes | No | No |
| `reduce_hgw` | `varchar(1)` | Publisher-supplied reduce hgw for the represented feature or record. | source_attribute | Yes | No | No |
| `reduce_ftw` | `varchar(1)` | Publisher-supplied reduce ftw for the represented feature or record. | source_attribute | Yes | No | No |
| `tranche` | `integer` | Count or numeric value for tranche in the represented area. | statistical_value | Yes | No | No |
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
