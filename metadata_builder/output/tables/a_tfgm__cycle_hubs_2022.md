# Cycle Hubs 2022

## Overview

- **Identifier:** `a_tfgm/cycle_hubs_2022`
- **Source organisation:** Transport for Greater Manchester
- **Source:** https://developer.tfgm.com/
- **Geographic coverage:** Greater Manchester
- **WGS84 extent:** `[-2.518667, 53.377326, -2.093716, 53.616457]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_tfgm`
- **Table:** `cycle_hubs_2022`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 20
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

version: 20220903
Source: https://www.data.gov.uk/dataset/e3236cd9-48c7-44c6-9c6e-efd76b67d8e5/gm-cycle-hubs

Attribution: Contains Transport for Greater Manchester data. Contains OS data © Crown copyright and database right 2022.

## Lineage

Published by Transport for Greater Manchester as open transport data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `bigint` | Count or numeric value for identifier in the represented area. |
| `hub_name` | `varchar(30)` | Name associated with the represented feature. |
| `easting` | `bigint` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `bigint` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `capacity` | `bigint` | Count or numeric value for capacity in the represented area. |
| `open_mon_f` | `varchar(20)` | Publisher-supplied open mon female for the represented feature or record. |
| `open_sat` | `varchar(20)` | Publisher-supplied open sat for the represented feature or record. |
| `open_sun` | `varchar(20)` | Publisher-supplied open sun for the represented feature or record. |
| `lockers` | `varchar(4)` | Publisher-supplied lockers for the represented feature or record. |
| `showers` | `varchar(4)` | Publisher-supplied showers for the represented feature or record. |
| `membership` | `varchar(10)` | Publisher-supplied membership for the represented feature or record. |
| `descriptio` | `varchar(200)` | Publisher-supplied descriptio for the represented feature or record. |
| `district` | `varchar(10)` | Publisher-supplied district for the represented feature or record. |
| `hotlink` | `varchar(200)` | Publisher-supplied hotlink for the represented feature or record. |
| `open` | `varchar(1)` | Publisher-supplied open for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `cycle_hubs_pk` | `integer` | Count or numeric value for cycle hubs pk in the represented area. |
