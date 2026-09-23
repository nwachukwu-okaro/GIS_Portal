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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
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
| `id` | `bigint` |  |
| `hub_name` | `varchar(30)` | Name associated with the represented feature. |
| `easting` | `bigint` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `bigint` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `capacity` | `bigint` | Capacity recorded for the cycle hub; the capacity unit has not been confirmed. |
| `open_mon_f` | `varchar(20)` | Cycle-hub opening hours from Monday to Friday. |
| `open_sat` | `varchar(20)` | Cycle-hub opening hours on Saturday. |
| `open_sun` | `varchar(20)` | Cycle-hub opening hours on Sunday. |
| `lockers` | `varchar(4)` | Indicates whether lockers are available at the cycle hub (Y=yes; N=no). |
| `showers` | `varchar(4)` | Indicates whether showers are available at the cycle hub (Y=yes; N=no). |
| `membership` | `varchar(10)` |  |
| `descriptio` | `varchar(200)` |  |
| `district` | `varchar(10)` |  |
| `hotlink` | `varchar(200)` |  |
| `open` | `varchar(1)` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `cycle_hubs_pk` | `integer` | Primary-key identifier for records in cycle_hubs_2022. |
