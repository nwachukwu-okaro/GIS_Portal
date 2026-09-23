# Air Quality Sites

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/air_quality_sites`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.240986, 51.855000, -6.122076, 55.358472]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `air_quality_sites`
- **Geometry:** POINT
- **CRS:** EPSG:29902
- **Rows:** 43
- **Columns:** 24
- **Metadata status:** source_mapped

## Description

Air Quality Sites is an authoritative dataset published by Environmental Protection Agency Ireland. It represents air quality sites features using point geometry.

## Lineage

Published by the Environmental Protection Agency Ireland as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `aqih_pk` | `integer` | Primary-key identifier for records in air_quality_sites. |
| `name` | `varchar(254)` | Official or publisher-assigned name of the represented feature. |
| `code` | `varchar(254)` |  |
| `location` | `varchar(254)` |  |
| `status` | `varchar(254)` |  |
| `url` | `varchar(254)` | Web address associated with the record. |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `address1` | `varchar(254)` |  |
| `address2` | `varchar(254)` |  |
| `region` | `varchar(20)` |  |
| `coverage` | `varchar(254)` |  |
| `operator` | `varchar(254)` |  |
| `eio_net_code` | `varchar(20)` | Code assigned by the source dataset. |
| `para_1` | `varchar(254)` |  |
| `para_2` | `varchar(254)` |  |
| `para_3` | `varchar(254)` |  |
| `para_4` | `varchar(254)` |  |
| `para_5` | `varchar(254)` |  |
| `para_6` | `varchar(254)` |  |
| `para_7` | `varchar(254)` |  |
| `para_8` | `varchar(254)` |  |
| `operational` | `integer` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
