# Boundary Census Health And Care Data 2021 Dea

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_health_and_care_data_2021_dea`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177502, 54.022724, -5.432789, 55.312984]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_health_and_care_data_2021_dea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 160
- **Columns:** 24
- **Metadata status:** source_mapped

## Description

Boundary Census Health And Care Data 2021 Dea is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census health and care data 2021 dea features using multipolygon geometry.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `finalr_dea` | `varchar` |  |
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geocode` | `text` | Code identifying the geographical area represented by the row. |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `year` | `bigint` | Reference year recorded for the statistical observation. |
| `population` | `text` |  |
| `general_health_bad` | `text` |  |
| `general_health_fair` | `text` |  |
| `general_health_good` | `text` |  |
| `general_health_very_bad` | `text` |  |
| `general_health_very_good` | `text` |  |
| `long_term_health_conditions_1_condition` | `text` |  |
| `long_term_health_conditions_2_conditions` | `text` |  |
| `long_term_health_conditions_3_or_more_conditions` | `text` |  |
| `long_term_health_conditions_no_conditions` | `text` |  |
| `long_term_health_problem_or_disability_activities_not_limited` | `text` |  |
| `long_term_health_problem_or_disability_limited_a_little` | `text` |  |
| `long_term_health_problem_or_disability_limited_a_lot` | `text` |  |
| `unpaid_care_1_19_hours` | `text` |  |
| `unpaid_care_20_49_hours` | `text` |  |
| `unpaid_care_50_hours` | `text` |  |
| `unpaid_care_provides_no_unpaid_care` | `text` |  |
