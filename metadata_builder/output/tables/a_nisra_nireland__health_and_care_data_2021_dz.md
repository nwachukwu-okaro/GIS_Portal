# Health And Care Data 2021 Dz

## Overview

- **Identifier:** `a_nisra_nireland/health_and_care_data_2021_dz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nisra_nireland`
- **Table:** `health_and_care_data_2021_dz`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3780
- **Columns:** 19
- **Metadata status:** source_mapped

## Description

Health And Care Data 2021 Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to health and care data 2021 dz.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geocode` | `text` | Code identifying the geographical area represented by the row. |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `year` | `bigint` | Reference year recorded for the statistical observation. |
| `general_health_bad` | `bigint` |  |
| `general_health_fair` | `bigint` |  |
| `general_health_good` | `bigint` |  |
| `general_health_very_bad` | `bigint` |  |
| `general_health_very_good` | `text` |  |
| `long_term_health_conditions_1_condition` | `bigint` |  |
| `long_term_health_conditions_2_conditions` | `bigint` |  |
| `long_term_health_conditions_3_or_more_conditions` | `bigint` |  |
| `long_term_health_conditions_no_conditions` | `text` |  |
| `long_term_health_problem_or_disability_activities_not_limited` | `text` |  |
| `long_term_health_problem_or_disability_limited_a_little` | `bigint` |  |
| `long_term_health_problem_or_disability_limited_a_lot` | `bigint` |  |
| `unpaid_care_1_19_hours` | `bigint` |  |
| `unpaid_care_20_49_hours` | `bigint` |  |
| `unpaid_care_50_hours` | `bigint` |  |
| `unpaid_care_provides_no_unpaid_care` | `text` |  |
