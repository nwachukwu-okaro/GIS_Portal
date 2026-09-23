# Boundary Census Principal Status Bua

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_principal_status_bua`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.426272, 54.617106, 3.355468, 58.377636]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_principal_status_bua`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 867
- **Columns:** 34
- **Metadata status:** source_mapped

## Description

Boundary Census Principal Status Bua is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census principal status bua features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `guid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `geogid` | `text` | Code identifying the geographical area represented by the row. |
| `geogdesc` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `at_work_males` | `bigint` |  |
| `looking_for_first_regular_job_males` | `bigint` |  |
| `short_term_unemployed_males` | `bigint` |  |
| `long_term_unemployed_males` | `bigint` |  |
| `student_males` | `bigint` |  |
| `looking_after_homefamily_males` | `bigint` |  |
| `retired_males` | `bigint` |  |
| `unable_to_work_due_to_permanent_sickness_or_disability_males` | `bigint` |  |
| `other_males` | `bigint` |  |
| `total_males` | `bigint` | Census total for males in the represented geographical area; measurement unit requires the table documentation. |
| `at_work_females` | `bigint` |  |
| `looking_for_first_regular_job_females` | `bigint` |  |
| `short_term_unemployed_females` | `bigint` |  |
| `long_term_unemployed_females` | `bigint` |  |
| `student_females` | `bigint` |  |
| `looking_after_homefamily_females` | `bigint` |  |
| `retired_females` | `bigint` |  |
| `unable_to_work_due_to_permanent_sickness_or_disability_females` | `bigint` |  |
| `other_females` | `bigint` |  |
| `total_females` | `bigint` | Census total for females in the represented geographical area; measurement unit requires the table documentation. |
| `at_work_total` | `bigint` |  |
| `looking_for_first_regular_job_total` | `bigint` |  |
| `short_term_unemployed_total` | `bigint` |  |
| `long_term_unemployed_total` | `bigint` |  |
| `student_total` | `bigint` |  |
| `looking_after_homefamily_total` | `bigint` |  |
| `retired_total` | `bigint` |  |
| `unable_to_work_due_to_permanent_sickness_or_disability_total` | `bigint` |  |
| `other_total` | `bigint` |  |
| `total` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
