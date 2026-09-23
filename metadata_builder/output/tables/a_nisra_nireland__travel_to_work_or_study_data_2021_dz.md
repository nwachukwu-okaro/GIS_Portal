# Travel To Work Or Study Data 2021 Dz

## Overview

- **Identifier:** `a_nisra_nireland/travel_to_work_or_study_data_2021_dz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nisra_nireland`
- **Table:** `travel_to_work_or_study_data_2021_dz`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3780
- **Columns:** 27
- **Metadata status:** source_mapped

## Description

Travel To Work Or Study Data 2021 Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to travel to work or study data 2021 dz.

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
| `distance_travelled_to_study_20km_and_over` | `bigint` |  |
| `distance_travelled_to_study_5km_20km` | `bigint` |  |
| `distance_travelled_to_study_less_than_5km` | `text` |  |
| `distance_travelled_to_study_mainly_at_or_from_home` | `bigint` |  |
| `distance_travelled_to_study_no_fixed_place` | `bigint` |  |
| `distance_travelled_to_study_outside_northern_ireland` | `bigint` |  |
| `distance_travelled_to_work_20km_and_over` | `bigint` |  |
| `distance_travelled_to_work_5km_20km` | `bigint` |  |
| `distance_travelled_to_work_less_than_5km` | `bigint` |  |
| `distance_travelled_to_work_mainly_at_or_from_home` | `bigint` |  |
| `distance_travelled_to_work_no_fixed_place` | `bigint` |  |
| `distance_travelled_to_work_outside_northern_ireland` | `bigint` |  |
| `method_of_travel_to_study_bus_or_train` | `bigint` |  |
| `method_of_travel_to_study_driving_a_car_or_van` | `bigint` |  |
| `method_of_travel_to_study_mainly_at_or_from_home` | `bigint` |  |
| `method_of_travel_to_study_other` | `bigint` |  |
| `method_of_travel_to_study_passenger_in_a_car_or_van` | `bigint` |  |
| `method_of_travel_to_study_walking_or_cycling` | `text` |  |
| `method_of_travel_to_work_bus_or_train` | `bigint` |  |
| `method_of_travel_to_work_driving_a_car_or_van` | `bigint` |  |
| `method_of_travel_to_work_mainly_at_or_from_home` | `bigint` |  |
| `method_of_travel_to_work_other` | `bigint` |  |
| `method_of_travel_to_work_passenger_in_a_car_or_van` | `bigint` |  |
| `method_of_travel_to_work_walking_or_cycling` | `bigint` |  |
