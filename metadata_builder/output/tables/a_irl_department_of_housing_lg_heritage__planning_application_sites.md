# Planning Application Sites

## Overview

- **Identifier:** `a_irl_department_of_housing_lg_heritage/planning_application_sites`
- **Source organisation:** Department of Housing, Local Government and Heritage
- **Source:** https://www.gov.ie/en/organisation/department-of-housing-local-government-and-heritage/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.467412, 51.430656, -5.993860, 55.378429]`
- **Schema:** `a_irl_department_of_housing_lg_heritage`
- **Table:** `planning_application_sites`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:3857
- **Rows:** 501124
- **Columns:** 34
- **Metadata status:** source_mapped

## Description

Planning Application Sites is an authoritative dataset published by Department of Housing, Local Government and Heritage. It represents planning application sites features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `pas_pk` | `integer` | Count or numeric value for pas pk in the represented area. | statistical_value | Yes | No | No |
| `planning_authority` | `varchar(100)` | Publisher-supplied planning authority for the represented feature or record. | source_attribute | Yes | No | No |
| `application_number` | `varchar(50)` | Publisher-supplied application number for the represented feature or record. | source_attribute | Yes | No | No |
| `development_description` | `varchar(12500)` | Publisher-supplied development description for the represented feature or record. | source_attribute | Yes | No | No |
| `development_address` | `varchar(7500)` | Publisher-supplied development address for the represented feature or record. | source_attribute | Yes | No | No |
| `development_postcode` | `varchar(50)` | Publisher-assigned development postcode for the record. | source_identifier | Yes | No | No |
| `itm_easting` | `double precision` | Numeric itm easting value recorded for the feature. | measure | Yes | No | No |
| `itm_northing` | `double precision` | Numeric itm northing value recorded for the feature. | measure | Yes | No | No |
| `application_status` | `varchar(4500)` | Publisher-supplied application status for the represented feature or record. | source_attribute | Yes | No | No |
| `application_type` | `varchar(150)` | Publisher-supplied application type for the represented feature or record. | source_attribute | Yes | No | No |
| `decision` | `varchar(12500)` | Publisher-supplied decision for the represented feature or record. | source_attribute | Yes | No | No |
| `land_use_code` | `varchar(100)` | Code assigned by the source dataset. | code | Yes | No | No |
| `area_of_site` | `double precision` | Numeric area of site value recorded for the feature. | measure | Yes | No | No |
| `num_residential_units` | `integer` | Count or numeric value for num residential units in the represented area. | statistical_value | Yes | No | No |
| `one_off_house` | `varchar(50)` | Publisher-supplied one off house for the represented feature or record. | source_attribute | Yes | No | No |
| `floor_area` | `double precision` | Numeric floor area value recorded for the feature. | measure | Yes | No | No |
| `received_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `withdrawn_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `decision_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `decision_due_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `grant_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `expiry_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `appeal_ref_number` | `varchar(80)` | Publisher-supplied appeal reference number for the represented feature or record. | source_attribute | Yes | No | No |
| `appeal_status` | `varchar(3500)` | Publisher-supplied appeal status for the represented feature or record. | source_attribute | Yes | No | No |
| `appeal_decision` | `varchar(3500)` | Publisher-supplied appeal decision for the represented feature or record. | source_attribute | Yes | No | No |
| `appeal_decision_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `appeal_submitted_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `fi_request_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `fi_rec_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `link_app_details` | `varchar(200)` | Publisher-supplied link app details for the represented feature or record. | source_attribute | Yes | No | No |
| `one_off_kpi` | `varchar(50)` | Publisher-supplied one off kpi for the represented feature or record. | source_attribute | Yes | No | No |
| `etl_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `site_id` | `varchar(100)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

## Supported operations

- filter
- select
- reproject
- validate_geometry
- buffer
- clip
- intersect
- spatial_join
- export

## Operation requirements

- Intersect, clip and spatial-join inputs must use matching coordinate reference systems.
- Buffer operations require a suitable projected coordinate reference system.
- Reprojection is performed on working outputs; source tables remain unchanged.

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
