# Boundary Census Principal Status County

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_principal_status_county`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.746471, 54.563349, 3.417194, 58.520162]`
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_principal_status_county`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 31
- **Columns:** 35
- **Metadata status:** source_mapped

## Description

Boundary Census Principal Status County is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census principal status county features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `geogid` | `text` | Publisher-assigned geogid for the record. | source_identifier | Yes | No | No |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `at_work_males` | `bigint` | Count or numeric value for at work males in the represented area. | statistical_value | Yes | No | No |
| `looking_for_first_regular_job_males` | `bigint` | Count or numeric value for looking for first regular job males in the represented area. | statistical_value | Yes | No | No |
| `short_term_unemployed_males` | `bigint` | Count or numeric value for short term unemployed males in the represented area. | statistical_value | Yes | No | No |
| `long_term_unemployed_males` | `bigint` | Numeric long term unemployed males value recorded for the feature. | measure | Yes | No | No |
| `student_males` | `bigint` | Count or numeric value for student males in the represented area. | statistical_value | Yes | No | No |
| `looking_after_homefamily_males` | `bigint` | Count or numeric value for looking after homefamily males in the represented area. | statistical_value | Yes | No | No |
| `retired_males` | `bigint` | Count or numeric value for retired males in the represented area. | statistical_value | Yes | No | No |
| `unable_to_work_due_to_permanent_sickness_or_disability_males` | `bigint` | Count or numeric value for unable to work due to permanent sickness or disability males in the represented area. | statistical_value | Yes | No | No |
| `other_males` | `bigint` | Count or numeric value for other males in the represented area. | statistical_value | Yes | No | No |
| `total_males` | `bigint` | Count or numeric value for total males in the represented area. | statistical_value | Yes | No | No |
| `at_work_females` | `bigint` | Count or numeric value for at work females in the represented area. | statistical_value | Yes | No | No |
| `looking_for_first_regular_job_females` | `bigint` | Count or numeric value for looking for first regular job females in the represented area. | statistical_value | Yes | No | No |
| `short_term_unemployed_females` | `bigint` | Count or numeric value for short term unemployed females in the represented area. | statistical_value | Yes | No | No |
| `long_term_unemployed_females` | `bigint` | Numeric long term unemployed females value recorded for the feature. | measure | Yes | No | No |
| `student_females` | `bigint` | Count or numeric value for student females in the represented area. | statistical_value | Yes | No | No |
| `looking_after_homefamily_females` | `bigint` | Count or numeric value for looking after homefamily females in the represented area. | statistical_value | Yes | No | No |
| `retired_females` | `bigint` | Count or numeric value for retired females in the represented area. | statistical_value | Yes | No | No |
| `unable_to_work_due_to_permanent_sickness_or_disability_females` | `bigint` | Count or numeric value for unable to work due to permanent sickness or disability females in the represented area. | statistical_value | Yes | No | No |
| `other_females` | `bigint` | Count or numeric value for other females in the represented area. | statistical_value | Yes | No | No |
| `total_females` | `bigint` | Count or numeric value for total females in the represented area. | statistical_value | Yes | No | No |
| `at_work_total` | `bigint` | Count or numeric value for at work total in the represented area. | statistical_value | Yes | No | No |
| `looking_for_first_regular_job_total` | `bigint` | Count or numeric value for looking for first regular job total in the represented area. | statistical_value | Yes | No | No |
| `short_term_unemployed_total` | `bigint` | Count or numeric value for short term unemployed total in the represented area. | statistical_value | Yes | No | No |
| `long_term_unemployed_total` | `bigint` | Numeric long term unemployed total value recorded for the feature. | measure | Yes | No | No |
| `student_total` | `bigint` | Count or numeric value for student total in the represented area. | statistical_value | Yes | No | No |
| `looking_after_homefamily_total` | `bigint` | Count or numeric value for looking after homefamily total in the represented area. | statistical_value | Yes | No | No |
| `retired_total` | `bigint` | Count or numeric value for retired total in the represented area. | statistical_value | Yes | No | No |
| `unable_to_work_due_to_permanent_sickness_or_disability_total` | `bigint` | Count or numeric value for unable to work due to permanent sickness or disability total in the represented area. | statistical_value | Yes | No | No |
| `other_total` | `bigint` | Count or numeric value for other total in the represented area. | statistical_value | Yes | No | No |
| `total` | `bigint` | Count or numeric value for total in the represented area. | statistical_value | Yes | No | No |
| `area` | `double precision` | Numeric area value recorded for the feature. | measure | Yes | No | No |
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
