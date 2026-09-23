# Land Use Zones Local Authority

## Overview

- **Identifier:** `a_irl_department_of_housing_lg_heritage/land_use_zones_local_authority`
- **Source organisation:** Department of Housing, Local Government and Heritage
- **Source:** https://www.gov.ie/en/organisation/department-of-housing-local-government-and-heritage/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.413342, 51.463662, -5.994535, 54.473025]`
- **Topic category:** boundaries
- **Temporal extent:** 2023-10-11 to 2026-06-18
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_department_of_housing_lg_heritage`
- **Table:** `land_use_zones_local_authority`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 85330
- **Columns:** 20
- **Metadata status:** source_mapped

## Description

Land Use Zones Local Authority is an authoritative dataset published by Department of Housing, Local Government and Heritage. It represents land use zones local authority features using multipolygon geometry.

## Lineage

Published by the Department of Housing, Local Government and Heritage as open data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `zone_gzt` | `varchar` |  |
| `zone_orig` | `varchar` |  |
| `zone_desc` | `varchar` |  |
| `zone_link` | `varchar` |  |
| `plan_from` | `date` |  |
| `plan_to` | `date` |  |
| `plan_name` | `varchar` | Name associated with the represented feature. |
| `colour` | `varchar` |  |
| `la_code` | `varchar` | Code assigned by the source dataset. |
| `gzt_desc` | `varchar` |  |
| `gzt_link` | `varchar` |  |
| `upload_date` | `date` | Date associated with the represented feature or source record. |
| `current_pl` | `integer` |  |
| `plan_level` | `varchar` |  |
| `szo` | `varchar` |  |
| `plan_id` | `varchar` | Identifier assigned by the source dataset. |
| `la_name` | `varchar` | Name associated with the represented feature. |
| `zone_desc_` | `varchar` |  |
| `luz_pk` | `integer` | Primary-key identifier for records in land_use_zones_local_authority. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
