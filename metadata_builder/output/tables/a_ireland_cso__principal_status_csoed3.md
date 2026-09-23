# Principal Status Csoed3

## Overview

- **Identifier:** `a_ireland_cso/principal_status_csoed3`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_ireland_cso`
- **Table:** `principal_status_csoed3`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3421
- **Columns:** 33
- **Metadata status:** source_mapped

## Description

Principal Status Csoed3 is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to principal status csoed3.

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
