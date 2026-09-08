# Boundary Census Principal Status Csoed3

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_principal_status_csoed3`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.726726, 54.563349, 3.417194, 58.519873]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_principal_status_csoed3`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 3420
- **Columns:** 35
- **Metadata status:** source_mapped

## Description

Boundary Census Principal Status Csoed3 is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census principal status csoed3 features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `ed_english` | `text` | Publisher-supplied ed english for the represented feature or record. |
| `guid` | `text` | Publisher-assigned guid for the record. |
| `geogid` | `text` | Publisher-assigned geogid for the record. |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. |
| `at_work_males` | `bigint` | Count or numeric value for at work males in the represented area. |
| `looking_for_first_regular_job_males` | `bigint` | Count or numeric value for looking for first regular job males in the represented area. |
| `short_term_unemployed_males` | `bigint` | Count or numeric value for short term unemployed males in the represented area. |
| `long_term_unemployed_males` | `bigint` | Numeric long term unemployed males value recorded for the feature. |
| `student_males` | `bigint` | Count or numeric value for student males in the represented area. |
| `looking_after_homefamily_males` | `bigint` | Count or numeric value for looking after homefamily males in the represented area. |
| `retired_males` | `bigint` | Count or numeric value for retired males in the represented area. |
| `unable_to_work_due_to_permanent_sickness_or_disability_males` | `bigint` | Count or numeric value for unable to work due to permanent sickness or disability males in the represented area. |
| `other_males` | `bigint` | Count or numeric value for other males in the represented area. |
| `total_males` | `bigint` | Count or numeric value for total males in the represented area. |
| `at_work_females` | `bigint` | Count or numeric value for at work females in the represented area. |
| `looking_for_first_regular_job_females` | `bigint` | Count or numeric value for looking for first regular job females in the represented area. |
| `short_term_unemployed_females` | `bigint` | Count or numeric value for short term unemployed females in the represented area. |
| `long_term_unemployed_females` | `bigint` | Numeric long term unemployed females value recorded for the feature. |
| `student_females` | `bigint` | Count or numeric value for student females in the represented area. |
| `looking_after_homefamily_females` | `bigint` | Count or numeric value for looking after homefamily females in the represented area. |
| `retired_females` | `bigint` | Count or numeric value for retired females in the represented area. |
| `unable_to_work_due_to_permanent_sickness_or_disability_females` | `bigint` | Count or numeric value for unable to work due to permanent sickness or disability females in the represented area. |
| `other_females` | `bigint` | Count or numeric value for other females in the represented area. |
| `total_females` | `bigint` | Count or numeric value for total females in the represented area. |
| `at_work_total` | `bigint` | Count or numeric value for at work total in the represented area. |
| `looking_for_first_regular_job_total` | `bigint` | Count or numeric value for looking for first regular job total in the represented area. |
| `short_term_unemployed_total` | `bigint` | Count or numeric value for short term unemployed total in the represented area. |
| `long_term_unemployed_total` | `bigint` | Numeric long term unemployed total value recorded for the feature. |
| `student_total` | `bigint` | Count or numeric value for student total in the represented area. |
| `looking_after_homefamily_total` | `bigint` | Count or numeric value for looking after homefamily total in the represented area. |
| `retired_total` | `bigint` | Count or numeric value for retired total in the represented area. |
| `unable_to_work_due_to_permanent_sickness_or_disability_total` | `bigint` | Count or numeric value for unable to work due to permanent sickness or disability total in the represented area. |
| `other_total` | `bigint` | Count or numeric value for other total in the represented area. |
| `total` | `bigint` | Count or numeric value for total in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
