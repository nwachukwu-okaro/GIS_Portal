# Boundary Census Health And Care Data 2021 Dz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_health_and_care_data_2021_dz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177484, 54.022725, -5.432790, 55.312985]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_health_and_care_data_2021_dz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 3780
- **Columns:** 20
- **Metadata status:** source_mapped

## Description

Boundary Census Health And Care Data 2021 Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census health and care data 2021 dz features using multipolygon geometry.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `year` | `bigint` | Count or numeric value for year in the represented area. |
| `general_health_bad` | `bigint` | Publisher-supplied general health bad for the represented feature or record. |
| `general_health_fair` | `bigint` | Publisher-supplied general health fair for the represented feature or record. |
| `general_health_good` | `bigint` | Publisher-supplied general health good for the represented feature or record. |
| `general_health_very_bad` | `bigint` | Publisher-supplied general health very bad for the represented feature or record. |
| `general_health_very_good` | `text` | Publisher-supplied general health very good for the represented feature or record. |
| `long_term_health_conditions_1_condition` | `bigint` | Publisher-supplied long term health conditions 1 condition for the represented feature or record. |
| `long_term_health_conditions_2_conditions` | `bigint` | Publisher-supplied long term health conditions 2 conditions for the represented feature or record. |
| `long_term_health_conditions_3_or_more_conditions` | `bigint` | Publisher-supplied long term health conditions 3 or more conditions for the represented feature or record. |
| `long_term_health_conditions_no_conditions` | `text` | Publisher-supplied long term health conditions number conditions for the represented feature or record. |
| `long_term_health_problem_or_disability_activities_not_limited` | `text` | Publisher-supplied long term health problem or disability activities not limited for the represented feature or record. |
| `long_term_health_problem_or_disability_limited_a_little` | `bigint` | Publisher-supplied long term health problem or disability limited a little for the represented feature or record. |
| `long_term_health_problem_or_disability_limited_a_lot` | `bigint` | Publisher-supplied long term health problem or disability limited a lot for the represented feature or record. |
| `unpaid_care_1_19_hours` | `bigint` | Publisher-supplied unpaid care 1 19 hours for the represented feature or record. |
| `unpaid_care_20_49_hours` | `bigint` | Publisher-supplied unpaid care 20 49 hours for the represented feature or record. |
| `unpaid_care_50_hours` | `bigint` | Publisher-supplied unpaid care 50 hours for the represented feature or record. |
| `unpaid_care_provides_no_unpaid_care` | `text` | Publisher-supplied unpaid care provides number unpaid care for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
