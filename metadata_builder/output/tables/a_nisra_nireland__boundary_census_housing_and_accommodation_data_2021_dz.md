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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
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
| `geocode` | `text` | Publisher-assigned geocode for the record. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `year` | `bigint` | Count or numeric value for year in the represented area. |
| `population` | `text` | Publisher-supplied population for the represented feature or record. |
| `accommodation_type_caravan_or_other_mobile_or_temporary_structu` | `bigint` | Count or numeric value for accommodation type caravan or other mobile or temporary structu in the represented area. |
| `accommodation_type_detached` | `bigint` | Publisher-supplied accommodation type detached for the represented feature or record. |
| `accommodation_type_flat_maisonette_or_apartment` | `bigint` | Publisher-supplied accommodation type flat maisonette or apartment for the represented feature or record. |
| `accommodation_type_semi_detached` | `bigint` | Publisher-supplied accommodation type semi detached for the represented feature or record. |
| `accommodation_type_terraced` | `bigint` | Publisher-supplied accommodation type terraced for the represented feature or record. |
| `car_or_van_availability_1_car_or_van` | `bigint` | Publisher-supplied car or van availability 1 car or van for the represented feature or record. |
| `car_or_van_availability_2_cars_or_vans` | `bigint` | Publisher-supplied car or van availability 2 cars or vans for the represented feature or record. |
| `car_or_van_availability_3_cars_or_vans` | `bigint` | Publisher-supplied car or van availability 3 cars or vans for the represented feature or record. |
| `car_or_van_availability_4_cars_or_vans` | `bigint` | Count or numeric value for car or van availability 4 cars or vans in the represented area. |
| `car_or_van_availability_5_or_more_cars_or_vans` | `bigint` | Count or numeric value for car or van availability 5 or more cars or vans in the represented area. |
| `car_or_van_availability_no_cars_or_vans` | `bigint` | Publisher-supplied car or van availability number cars or vans for the represented feature or record. |
| `central_heating_gas_only_note_1` | `bigint` | Publisher-supplied central heating gas only note 1 for the represented feature or record. |
| `central_heating_oil_only` | `bigint` | Publisher-supplied central heating oil only for the represented feature or record. |
| `central_heating_other` | `bigint` | Publisher-supplied central heating other for the represented feature or record. |
| `household_adaptations_not_designed_or_adapted` | `bigint` | Publisher-supplied household adaptations not designed or adapted for the represented feature or record. |
| `household_adaptations_one` | `bigint` | Publisher-supplied household adaptations one for the represented feature or record. |
| `household_adaptations_two_or_more` | `bigint` | Publisher-supplied household adaptations two or more for the represented feature or record. |
| `household_tenure_lives_rent_free` | `bigint` | Count or numeric value for household tenure lives rent free in the represented area. |
| `household_tenure_owns_inc_shared_ownership` | `bigint` | Publisher-supplied household tenure owns inc shared ownership for the represented feature or record. |
| `household_tenure_private_rented` | `bigint` | Publisher-supplied household tenure private rented for the represented feature or record. |
| `household_tenure_social_rented` | `bigint` | Publisher-supplied household tenure social rented for the represented feature or record. |
| `renewable_energy_systems_any_renewable_energy_systems` | `bigint` | Publisher-supplied renewable energy systems any renewable energy systems for the represented feature or record. |
| `renewable_energy_systems_no_renewable_energy_systems` | `bigint` | Publisher-supplied renewable energy systems number renewable energy systems for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
