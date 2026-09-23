# Planning Application Sites

## Overview

- **Identifier:** `a_irl_department_of_housing_lg_heritage/planning_application_sites`
- **Source organisation:** Department of Housing, Local Government and Heritage
- **Source:** https://www.gov.ie/en/organisation/department-of-housing-local-government-and-heritage/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.467412, 51.430656, -5.993860, 55.378429]`
- **Topic category:** boundaries
- **Temporal extent:** 1991-03-05T00:00:00 to 2026-07-31T00:00:00
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_department_of_housing_lg_heritage`
- **Table:** `planning_application_sites`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:3857
- **Rows:** 501124
- **Columns:** 34
- **Metadata status:** source_mapped

## Description

Planning Application Sites is an authoritative dataset published by Department of Housing, Local Government and Heritage. It represents planning application sites features using multipolygon geometry.

## Lineage

Published by the Department of Housing, Local Government and Heritage as open data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `pas_pk` | `integer` | Primary-key identifier for records in planning_application_sites. |
| `planning_authority` | `varchar(100)` |  |
| `application_number` | `varchar(50)` |  |
| `development_description` | `varchar(12500)` |  |
| `development_address` | `varchar(7500)` |  |
| `development_postcode` | `varchar(50)` |  |
| `itm_easting` | `double precision` |  |
| `itm_northing` | `double precision` |  |
| `application_status` | `varchar(4500)` |  |
| `application_type` | `varchar(150)` |  |
| `decision` | `varchar(12500)` |  |
| `land_use_code` | `varchar(100)` | Code assigned by the source dataset. |
| `area_of_site` | `double precision` |  |
| `num_residential_units` | `integer` |  |
| `one_off_house` | `varchar(50)` |  |
| `floor_area` | `double precision` |  |
| `received_date` | `timestamp` | Date associated with the represented feature or source record. |
| `withdrawn_date` | `timestamp` | Date associated with the represented feature or source record. |
| `decision_date` | `timestamp` | Date associated with the represented feature or source record. |
| `decision_due_date` | `timestamp` | Date associated with the represented feature or source record. |
| `grant_date` | `timestamp` | Date associated with the represented feature or source record. |
| `expiry_date` | `timestamp` | Date associated with the represented feature or source record. |
| `appeal_ref_number` | `varchar(80)` |  |
| `appeal_status` | `varchar(3500)` |  |
| `appeal_decision` | `varchar(3500)` |  |
| `appeal_decision_date` | `timestamp` | Date associated with the represented feature or source record. |
| `appeal_submitted_date` | `timestamp` | Date associated with the represented feature or source record. |
| `fi_request_date` | `timestamp` | Date associated with the represented feature or source record. |
| `fi_rec_date` | `timestamp` | Date associated with the represented feature or source record. |
| `link_app_details` | `varchar(200)` |  |
| `one_off_kpi` | `varchar(50)` |  |
| `etl_date` | `timestamp` | Date associated with the represented feature or source record. |
| `site_id` | `varchar(100)` | Identifier assigned by the source dataset. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
