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
| `aqih_pk` | `integer` | Count or numeric value for aqih pk in the represented area. |
| `name` | `varchar(254)` | Official or publisher-assigned name of the represented feature. |
| `code` | `varchar(254)` | Publisher-assigned code for the record. |
| `location` | `varchar(254)` | Publisher-supplied location for the represented feature or record. |
| `status` | `varchar(254)` | Publisher-supplied status for the represented feature or record. |
| `url` | `varchar(254)` | Publisher-supplied url for the represented feature or record. |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `address1` | `varchar(254)` |  |
| `address2` | `varchar(254)` |  |
| `region` | `varchar(20)` | Publisher-supplied region for the represented feature or record. |
| `coverage` | `varchar(254)` | Publisher-supplied coverage for the represented feature or record. |
| `operator` | `varchar(254)` | Publisher-supplied operator for the represented feature or record. |
| `eio_net_code` | `varchar(20)` | Code assigned by the source dataset. |
| `para_1` | `varchar(254)` | Publisher-supplied para 1 for the represented feature or record. |
| `para_2` | `varchar(254)` | Publisher-supplied para 2 for the represented feature or record. |
| `para_3` | `varchar(254)` | Publisher-supplied para 3 for the represented feature or record. |
| `para_4` | `varchar(254)` | Publisher-supplied para 4 for the represented feature or record. |
| `para_5` | `varchar(254)` | Publisher-supplied para 5 for the represented feature or record. |
| `para_6` | `varchar(254)` | Publisher-supplied para 6 for the represented feature or record. |
| `para_7` | `varchar(254)` | Publisher-supplied para 7 for the represented feature or record. |
| `para_8` | `varchar(254)` | Publisher-supplied para 8 for the represented feature or record. |
| `operational` | `integer` | Count or numeric value for operational in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
