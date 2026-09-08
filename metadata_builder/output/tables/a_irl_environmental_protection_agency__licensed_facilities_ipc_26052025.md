# Licensed Facilities Ipc 26052025

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/licensed_facilities_ipc_26052025`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.239738, 51.688928, -6.111532, 55.064460]`
- **Topic category:** environment
- **Temporal extent:** 2015-11-27 to 2021-11-23
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `licensed_facilities_ipc_26052025`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:29903
- **Rows:** 166
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Licensed Facilities Ipc 26052025 is an authoritative dataset published by Environmental Protection Agency Ireland. It represents licensed facilities ipc 26052025 features using multipoint geometry.

## Lineage

Published by the Environmental Protection Agency Ireland as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `registration_code` | `varchar(50)` | Code assigned by the source dataset. |
| `name` | `varchar(250)` | Official or publisher-assigned name of the represented feature. |
| `date_from` | `date` | Publisher-supplied date from for the represented feature or record. |
| `sub_category` | `varchar(100)` | Publisher-supplied sub category for the represented feature or record. |
| `category` | `varchar(50)` | Publisher-supplied category for the represented feature or record. |
| `licence_status_type` | `varchar(100)` | Publisher-supplied licence status type for the represented feature or record. |
| `active_licence_number` | `varchar(50)` | Publisher-supplied active licence number for the represented feature or record. |
| `major_class_of_activity` | `varchar(50)` | Publisher-supplied major class of activity for the represented feature or record. |
| `licence_type_name` | `varchar(100)` | Name associated with the represented feature. |
| `address` | `varchar(250)` | Publisher-supplied address for the represented feature or record. |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `lfipc_pk` | `integer` | Count or numeric value for lfipc pk in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
