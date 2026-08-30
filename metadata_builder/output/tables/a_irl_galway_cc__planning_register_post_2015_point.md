# Planning Register Post 2015 Point

## Overview

- **Identifier:** `a_irl_galway_cc/planning_register_post_2015_point`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Schema:** `a_irl_galway_cc`
- **Table:** `planning_register_post_2015_point`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:2157
- **Rows:** 20572
- **Metadata status:** source_mapped

## Description

Planning Register Post 2015 Point is an authoritative dataset published by Galway County Council. It represents planning register post 2015 point features using multipoint geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `object_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `county` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `planning_authority` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `application_number` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `applicant_ame` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `received_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `application_type` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `application_status` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `location` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `description` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `decision` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `decision_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `decision_due_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `withdrawn_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `grant_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `expiry_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `appeal_notification_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `appeal_ref_num` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `appeal_decision` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `appeal_decision_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `itm_easting` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `itm_northing` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `more_info` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
