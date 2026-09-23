# Boundary Census Housing And Accommodation Data 2021 Dz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_housing_and_accommodation_data_2021_dz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177484, 54.022725, -5.432790, 55.312985]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_housing_and_accommodation_data_2021_dz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 3780
- **Columns:** 28
- **Metadata status:** source_mapped

## Description

Boundary Census Housing And Accommodation Data 2021 Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census housing and accommodation data 2021 dz features using multipolygon geometry.

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
| `population` | `text` |  |
| `accommodation_type_caravan_or_other_mobile_or_temporary_structu` | `bigint` |  |
| `accommodation_type_detached` | `bigint` |  |
| `accommodation_type_flat_maisonette_or_apartment` | `bigint` |  |
| `accommodation_type_semi_detached` | `bigint` |  |
| `accommodation_type_terraced` | `bigint` |  |
| `car_or_van_availability_1_car_or_van` | `bigint` |  |
| `car_or_van_availability_2_cars_or_vans` | `bigint` |  |
| `car_or_van_availability_3_cars_or_vans` | `bigint` |  |
| `car_or_van_availability_4_cars_or_vans` | `bigint` |  |
| `car_or_van_availability_5_or_more_cars_or_vans` | `bigint` |  |
| `car_or_van_availability_no_cars_or_vans` | `bigint` |  |
| `central_heating_gas_only_note_1` | `bigint` |  |
| `central_heating_oil_only` | `bigint` |  |
| `central_heating_other` | `bigint` |  |
| `household_adaptations_not_designed_or_adapted` | `bigint` |  |
| `household_adaptations_one` | `bigint` |  |
| `household_adaptations_two_or_more` | `bigint` |  |
| `household_tenure_lives_rent_free` | `bigint` |  |
| `household_tenure_owns_inc_shared_ownership` | `bigint` |  |
| `household_tenure_private_rented` | `bigint` |  |
| `household_tenure_social_rented` | `bigint` |  |
| `renewable_energy_systems_any_renewable_energy_systems` | `bigint` |  |
| `renewable_energy_systems_no_renewable_energy_systems` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
