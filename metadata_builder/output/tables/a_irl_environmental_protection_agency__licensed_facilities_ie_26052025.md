# Licensed Facilities Ie 26052025

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/licensed_facilities_ie_26052025`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.777210, 51.608037, -6.050323, 55.061859]`
- **Topic category:** environment
- **Temporal extent:** 2015-11-27 to 2024-05-30
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `licensed_facilities_ie_26052025`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:29903
- **Rows:** 725
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Licensed Facilities Ie 26052025 is an authoritative dataset published by Environmental Protection Agency Ireland. It represents licensed facilities ie 26052025 features using multipoint geometry.

## Lineage

Published by the Environmental Protection Agency Ireland as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `lfie_pk` | `integer` | Primary-key identifier for records in licensed_facilities_ie_26052025. |
| `registration_code` | `varchar(50)` | Code assigned by the source dataset. |
| `name` | `varchar(250)` | Official or publisher-assigned name of the represented feature. |
| `date_from` | `date` |  |
| `sub_category` | `varchar(100)` |  |
| `category` | `varchar(50)` |  |
| `licence_status_type` | `varchar(100)` |  |
| `active_licence_number` | `varchar(50)` |  |
| `major_class_of_activity` | `varchar(50)` |  |
| `licence_type_name` | `varchar(100)` | Name associated with the represented feature. |
| `address` | `varchar(250)` |  |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
