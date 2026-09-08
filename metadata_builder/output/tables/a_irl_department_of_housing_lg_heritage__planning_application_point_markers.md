# Planning Application Point Markers

## Overview

- **Identifier:** `a_irl_department_of_housing_lg_heritage/planning_application_point_markers`
- **Source organisation:** Department of Housing, Local Government and Heritage
- **Source:** https://www.gov.ie/en/organisation/department-of-housing-local-government-and-heritage/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.465199, 51.431126, -6.013037, 55.378307]`
- **Topic category:** boundaries
- **Temporal extent:** 1991-03-05T00:00:00 to 2026-07-31T00:00:00
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_irl_department_of_housing_lg_heritage`
- **Table:** `planning_application_point_markers`
- **Geometry:** POINT
- **CRS:** EPSG:3857
- **Rows:** 501303
- **Columns:** 38
- **Metadata status:** source_mapped

## Description

Planning Application Point Markers is an authoritative dataset published by Department of Housing, Local Government and Heritage. It represents planning application point markers features using point geometry.

## Lineage

Published by the Department of Housing, Local Government and Heritage as open data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `papm_pk` | `integer` | Count or numeric value for papm pk in the represented area. |
| `planning_authority` | `varchar(100)` | Publisher-supplied planning authority for the represented feature or record. |
| `application_number` | `varchar(50)` | Publisher-supplied application number for the represented feature or record. |
| `development_description` | `varchar(12500)` | Publisher-supplied development description for the represented feature or record. |
| `development_address` | `varchar(7500)` | Publisher-supplied development address for the represented feature or record. |
| `development_postcode` | `varchar(50)` | Publisher-assigned development postcode for the record. |
| `itm_easting` | `double precision` | Numeric itm easting value recorded for the feature. |
| `itm_northing` | `double precision` | Numeric itm northing value recorded for the feature. |
| `application_status` | `varchar(4500)` | Publisher-supplied application status for the represented feature or record. |
| `application_type` | `varchar(150)` | Publisher-supplied application type for the represented feature or record. |
| `applicant_forename` | `varchar(2500)` | Publisher-supplied applicant forename for the represented feature or record. |
| `applicant_surname` | `varchar(2500)` | Publisher-supplied applicant surname for the represented feature or record. |
| `applicant_address` | `varchar(2500)` | Publisher-supplied applicant address for the represented feature or record. |
| `decision` | `varchar(12500)` | Publisher-supplied decision for the represented feature or record. |
| `land_use_code` | `varchar(100)` | Code assigned by the source dataset. |
| `area_of_site` | `double precision` | Numeric area of site value recorded for the feature. |
| `num_residential_units` | `integer` | Count or numeric value for num residential units in the represented area. |
| `one_off_house` | `varchar(50)` | Publisher-supplied one off house for the represented feature or record. |
| `floor_area` | `double precision` | Numeric floor area value recorded for the feature. |
| `received_date` | `timestamp` | Date associated with the represented feature or source record. |
| `withdrawn_date` | `timestamp` | Date associated with the represented feature or source record. |
| `decision_date` | `timestamp` | Date associated with the represented feature or source record. |
| `decision_due_date` | `timestamp` | Date associated with the represented feature or source record. |
| `grant_date` | `timestamp` | Date associated with the represented feature or source record. |
| `expiry_date` | `timestamp` | Date associated with the represented feature or source record. |
| `appeal_ref_number` | `varchar(80)` | Publisher-supplied appeal reference number for the represented feature or record. |
| `appeal_status` | `varchar(3500)` | Publisher-supplied appeal status for the represented feature or record. |
| `appeal_decision` | `varchar(3500)` | Publisher-supplied appeal decision for the represented feature or record. |
| `appeal_decision_date` | `timestamp` | Date associated with the represented feature or source record. |
| `appeal_submitted_date` | `timestamp` | Date associated with the represented feature or source record. |
| `fi_request_date` | `timestamp` | Date associated with the represented feature or source record. |
| `fi_rec_date` | `timestamp` | Date associated with the represented feature or source record. |
| `link_app_details` | `varchar(200)` | Publisher-supplied link app details for the represented feature or record. |
| `one_off_kpi` | `varchar(50)` | Publisher-supplied one off kpi for the represented feature or record. |
| `etl_date` | `timestamp` | Date associated with the represented feature or source record. |
| `site_id` | `varchar(100)` | Identifier assigned by the source dataset. |
| `orig_fid` | `integer` | Count or numeric value for orig fid in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
