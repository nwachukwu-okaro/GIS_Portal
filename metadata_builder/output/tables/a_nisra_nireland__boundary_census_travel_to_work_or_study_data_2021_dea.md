# Boundary Census Travel To Work Or Study Data 2021 Dea

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_travel_to_work_or_study_data_2021_dea`
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
- **Table:** `boundary_census_travel_to_work_or_study_data_2021_dea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 80
- **Columns:** 28
- **Metadata status:** source_mapped

## Description

Boundary Census Travel To Work Or Study Data 2021 Dea is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census travel to work or study data 2021 dea features using multipolygon geometry.

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
| `distance_travelled_to_study_20km_and_over` | `text` |  |
| `distance_travelled_to_study_5km_20km` | `text` |  |
| `distance_travelled_to_study_less_than_5km` | `text` |  |
| `distance_travelled_to_study_mainly_at_or_from_home` | `text` |  |
| `distance_travelled_to_study_no_fixed_place` | `bigint` |  |
| `distance_travelled_to_study_outside_northern_ireland` | `bigint` |  |
| `distance_travelled_to_work_20km_and_over` | `text` |  |
| `distance_travelled_to_work_5km_20km` | `text` |  |
| `distance_travelled_to_work_less_than_5km` | `text` |  |
| `distance_travelled_to_work_mainly_at_or_from_home` | `text` |  |
| `distance_travelled_to_work_no_fixed_place` | `text` |  |
| `distance_travelled_to_work_outside_northern_ireland` | `text` |  |
| `method_of_travel_to_study_bus_or_train` | `text` |  |
| `method_of_travel_to_study_driving_a_car_or_van` | `text` |  |
| `method_of_travel_to_study_mainly_at_or_from_home` | `text` |  |
| `method_of_travel_to_study_other` | `bigint` |  |
| `method_of_travel_to_study_passenger_in_a_car_or_van` | `text` |  |
| `method_of_travel_to_study_walking_or_cycling` | `text` |  |
| `method_of_travel_to_work_bus_or_train` | `text` |  |
| `method_of_travel_to_work_driving_a_car_or_van` | `text` |  |
| `method_of_travel_to_work_mainly_at_or_from_home` | `text` |  |
| `method_of_travel_to_work_other` | `bigint` |  |
| `method_of_travel_to_work_passenger_in_a_car_or_van` | `text` |  |
| `method_of_travel_to_work_walking_or_cycling` | `text` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
