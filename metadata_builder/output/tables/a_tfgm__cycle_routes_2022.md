# Cycle Routes 2022

## Overview

- **Identifier:** `a_tfgm/cycle_routes_2022`
- **Source organisation:** Transport for Greater Manchester
- **Source:** https://developer.tfgm.com/
- **Geographic coverage:** Greater Manchester
- **WGS84 extent:** `[-2.729156, 53.316610, -1.909767, 53.698304]`
- **Topic category:** transportation
- **Temporal extent:** 2020-05-26 to 2022-06-30
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_tfgm`
- **Table:** `cycle_routes_2022`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 3573
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Cycle Routes 2022 is an authoritative dataset published by Transport for Greater Manchester. It represents cycle routes 2022 features using multilinestring geometry.

## Lineage

Published by Transport for Greater Manchester as open transport data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `cr_pk` | `integer` | Count or numeric value for cr pk in the represented area. |
| `routetype` | `bigint` | Count or numeric value for routetype in the represented area. |
| `routestatu` | `bigint` | Count or numeric value for routestatu in the represented area. |
| `routesurfa` | `bigint` | Count or numeric value for routesurfa in the represented area. |
| `ncnroute` | `bigint` | Count or numeric value for ncnroute in the represented area. |
| `ncnroutenu` | `bigint` | Count or numeric value for ncnroutenu in the represented area. |
| `notes` | `varchar(100)` | Publisher-supplied notes for the represented feature or record. |
| `date_updat` | `date` | Publisher-supplied date updat for the represented feature or record. |
| `strategic_` | `bigint` | Count or numeric value for strategic in the represented area. |
| `mand_advis` | `varchar(1)` | Publisher-supplied mand advis for the represented feature or record. |
| `recovery_s` | `varchar(4)` | Publisher-supplied recovery s for the represented feature or record. |
| `reduce_hgw` | `varchar(1)` | Publisher-supplied reduce hgw for the represented feature or record. |
| `reduce_ftw` | `varchar(1)` | Publisher-supplied reduce ftw for the represented feature or record. |
| `tranche` | `integer` | Count or numeric value for tranche in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
