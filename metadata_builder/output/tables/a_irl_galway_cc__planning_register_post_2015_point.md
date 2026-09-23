# Planning Register Post 2015 Point

## Overview

- **Identifier:** `a_irl_galway_cc/planning_register_post_2015_point`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.234705, 52.978936, -7.994424, 53.713605]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_irl_galway_cc`
- **Table:** `planning_register_post_2015_point`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:2157
- **Rows:** 20572
- **Columns:** 25
- **Metadata status:** source_mapped

## Description

Planning Register Post 2015 Point is an authoritative dataset published by Galway County Council. It represents planning register post 2015 point features using multipoint geometry.

## Lineage

Published by Galway County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `object_id` | `integer` | Identifier assigned by the source dataset. |
| `county` | `varchar` |  |
| `planning_authority` | `varchar` |  |
| `application_number` | `varchar` |  |
| `applicant_ame` | `varchar` |  |
| `received_date` | `varchar` | Date associated with the represented feature or source record. |
| `application_type` | `varchar` |  |
| `application_status` | `varchar` |  |
| `location` | `varchar` |  |
| `description` | `varchar` |  |
| `decision` | `varchar` |  |
| `decision_date` | `varchar` | Date associated with the represented feature or source record. |
| `decision_due_date` | `varchar` | Date associated with the represented feature or source record. |
| `withdrawn_date` | `varchar` | Date associated with the represented feature or source record. |
| `grant_date` | `varchar` | Date associated with the represented feature or source record. |
| `expiry_date` | `varchar` | Date associated with the represented feature or source record. |
| `appeal_notification_date` | `varchar` | Date associated with the represented feature or source record. |
| `appeal_ref_num` | `varchar` |  |
| `appeal_decision` | `varchar` |  |
| `appeal_decision_date` | `varchar` | Date associated with the represented feature or source record. |
| `itm_easting` | `double precision` |  |
| `itm_northing` | `double precision` |  |
| `more_info` | `varchar` |  |
| `global_id` | `varchar` | Identifier assigned by the source dataset. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
