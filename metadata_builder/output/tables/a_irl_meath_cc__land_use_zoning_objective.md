# Land Use Zoning Objective

## Overview

- **Identifier:** `a_irl_meath_cc/land_use_zoning_objective`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.343668, 53.381919, -6.212613, 53.917668]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_meath_cc`
- **Table:** `land_use_zoning_objective`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 2201
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Land Use Zoning Objective is an authoritative dataset published by Meath County Council. It represents land use zoning objective features using multipolygon geometry.

## Lineage

Published by Meath County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `luzo_pk` | `integer` | Primary-key identifier for records in land_use_zoning_objective. |
| `guid` | `double precision` |  |
| `site_code` | `varchar(100)` | Code assigned by the source dataset. |
| `zoning_code` | `varchar(6)` | Code assigned by the source dataset. |
| `zoning_description` | `varchar(100)` |  |
| `zoning_objective` | `varchar(254)` |  |
| `area_acres` | `real` |  |
| `area_hectares` | `real` |  |
| `residential` | `varchar(100)` |  |
| `settlement` | `double precision` |  |
| `settlement_01` | `varchar(100)` |  |
| `plan_name` | `varchar(120)` | Name associated with the represented feature. |
| `lifetime` | `varchar(25)` |  |
| `more_info` | `varchar(250)` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
