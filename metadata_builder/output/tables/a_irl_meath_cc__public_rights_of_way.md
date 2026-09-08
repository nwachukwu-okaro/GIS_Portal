# Public Rights Of Way

## Overview

- **Identifier:** `a_irl_meath_cc/public_rights_of_way`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.118596, 53.504532, -6.212613, 53.747896]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_meath_cc`
- **Table:** `public_rights_of_way`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 24
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Public Rights Of Way is an authoritative dataset published by Meath County Council. It represents public rights of way features using multipolygon geometry.

## Lineage

Published by Meath County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `public_right_of_way` | `varchar(15)` | Publisher-supplied public right of way for the represented feature or record. |
| `category` | `varchar(150)` | Publisher-supplied category for the represented feature or record. |
| `location` | `varchar(250)` | Publisher-supplied location for the represented feature or record. |
| `prow_pk` | `integer` | Count or numeric value for prow pk in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
