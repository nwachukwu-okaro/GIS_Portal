# Boundary Census Health And Care Data 2021 Dz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_health_and_care_data_2021_dz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177484, 54.022725, -5.432790, 55.312985]`
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_health_and_care_data_2021_dz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 3780
- **Columns:** 20
- **Metadata status:** source_mapped

## Description

Boundary Census Health And Care Data 2021 Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census health and care data 2021 dz features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `general_health_bad` | `bigint` | Publisher-supplied general health bad for the represented feature or record. | source_attribute | Yes | No | No |
| `general_health_fair` | `bigint` | Publisher-supplied general health fair for the represented feature or record. | source_attribute | Yes | No | No |
| `general_health_good` | `bigint` | Publisher-supplied general health good for the represented feature or record. | source_attribute | Yes | No | No |
| `general_health_very_bad` | `bigint` | Publisher-supplied general health very bad for the represented feature or record. | source_attribute | Yes | No | No |
| `general_health_very_good` | `text` | Publisher-supplied general health very good for the represented feature or record. | source_attribute | Yes | No | No |
| `long_term_health_conditions_1_condition` | `bigint` | Publisher-supplied long term health conditions 1 condition for the represented feature or record. | source_attribute | Yes | No | No |
| `long_term_health_conditions_2_conditions` | `bigint` | Publisher-supplied long term health conditions 2 conditions for the represented feature or record. | source_attribute | Yes | No | No |
| `long_term_health_conditions_3_or_more_conditions` | `bigint` | Publisher-supplied long term health conditions 3 or more conditions for the represented feature or record. | source_attribute | Yes | No | No |
| `long_term_health_conditions_no_conditions` | `text` | Publisher-supplied long term health conditions number conditions for the represented feature or record. | source_attribute | Yes | No | No |
| `long_term_health_problem_or_disability_activities_not_limited` | `text` | Publisher-supplied long term health problem or disability activities not limited for the represented feature or record. | source_attribute | Yes | No | No |
| `long_term_health_problem_or_disability_limited_a_little` | `bigint` | Publisher-supplied long term health problem or disability limited a little for the represented feature or record. | source_attribute | Yes | No | No |
| `long_term_health_problem_or_disability_limited_a_lot` | `bigint` | Publisher-supplied long term health problem or disability limited a lot for the represented feature or record. | source_attribute | Yes | No | No |
| `unpaid_care_1_19_hours` | `bigint` | Publisher-supplied unpaid care 1 19 hours for the represented feature or record. | source_attribute | Yes | No | No |
| `unpaid_care_20_49_hours` | `bigint` | Publisher-supplied unpaid care 20 49 hours for the represented feature or record. | source_attribute | Yes | No | No |
| `unpaid_care_50_hours` | `bigint` | Publisher-supplied unpaid care 50 hours for the represented feature or record. | source_attribute | Yes | No | No |
| `unpaid_care_provides_no_unpaid_care` | `text` | Publisher-supplied unpaid care provides number unpaid care for the represented feature or record. | source_attribute | Yes | No | No |
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
