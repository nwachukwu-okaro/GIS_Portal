# Planning Register Pts 16

## Overview

- **Identifier:** `a_irl_galway_cc/planning_register_pts_16`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.234705, 52.978936, -7.994424, 53.713605]`
- **Schema:** `a_irl_galway_cc`
- **Table:** `planning_register_pts_16`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:2157
- **Rows:** 20430
- **Columns:** 25
- **Metadata status:** source_mapped

## Description

Planning Register Pts 16 is an authoritative dataset published by Galway County Council. It represents planning register pts 16 features using multipoint geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `object_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `county` | `varchar` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
| `planning_authority` | `varchar` | Publisher-supplied planning authority for the represented feature or record. | source_attribute | Yes | No | No |
| `application_number` | `varchar` | Publisher-supplied application number for the represented feature or record. | source_attribute | Yes | No | No |
| `applicant_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `received_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `application_type` | `varchar` | Publisher-supplied application type for the represented feature or record. | source_attribute | Yes | No | No |
| `application_status` | `varchar` | Publisher-supplied application status for the represented feature or record. | source_attribute | Yes | No | No |
| `location` | `varchar` | Publisher-supplied location for the represented feature or record. | source_attribute | Yes | No | No |
| `description` | `varchar` | Publisher-supplied description for the represented feature or record. | source_attribute | Yes | No | No |
| `decision` | `varchar` | Publisher-supplied decision for the represented feature or record. | source_attribute | Yes | No | No |
| `decision_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `decision_due_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `withdrawn_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `grant_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `expiry_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `appeal_notification_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `appeal_ref_num` | `varchar` | Publisher-supplied appeal reference num for the represented feature or record. | source_attribute | Yes | No | No |
| `appeal_decision` | `varchar` | Publisher-supplied appeal decision for the represented feature or record. | source_attribute | Yes | No | No |
| `appeal_decision_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `itm_easting` | `double precision` | Numeric itm easting value recorded for the feature. | measure | Yes | No | No |
| `itm_northing` | `double precision` | Numeric itm northing value recorded for the feature. | measure | Yes | No | No |
| `more_info` | `varchar` | Publisher-supplied more info for the represented feature or record. | source_attribute | Yes | No | No |
| `global_id` | `varchar` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
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
