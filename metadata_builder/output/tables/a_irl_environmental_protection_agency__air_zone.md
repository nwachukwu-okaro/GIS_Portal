# Air Zone

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/air_zone`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.621856, 51.388882, -5.996275, 55.384383]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `air_zone`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 27
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Air Zone is an authoritative dataset published by Environmental Protection Agency Ireland. It represents air zone features using multipolygon geometry.

## Lineage

Published by the Environmental Protection Agency Ireland as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `az_pk` | `integer` | Count or numeric value for az pk in the represented area. |
| `air_zone` | `varchar(35)` | Publisher-supplied air zone for the represented feature or record. |
| `name` | `varchar(30)` | Official or publisher-assigned name of the represented feature. |
| `location` | `varchar(50)` | Publisher-supplied location for the represented feature or record. |
| `global_id` | `varchar(38)` | Identifier assigned by the source dataset. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
