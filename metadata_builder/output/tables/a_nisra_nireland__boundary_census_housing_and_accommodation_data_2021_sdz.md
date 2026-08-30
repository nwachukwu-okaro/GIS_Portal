# Boundary Census Housing And Accommodation Data 2021 Sdz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_housing_and_accommodation_data_2021_sdz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177484, 54.022725, -5.432790, 55.312985]`
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_housing_and_accommodation_data_2021_sdz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 850
- **Columns:** 28
- **Metadata status:** source_mapped

## Description

Boundary Census Housing And Accommodation Data 2021 Sdz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census housing and accommodation data 2021 sdz features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `population` | `text` | Publisher-supplied population for the represented feature or record. | source_attribute | Yes | No | No |
| `accommodation_type_caravan_or_other_mobile_or_temporary_structu` | `bigint` | Count or numeric value for accommodation type caravan or other mobile or temporary structu in the represented area. | statistical_value | Yes | No | No |
| `accommodation_type_detached` | `text` | Publisher-supplied accommodation type detached for the represented feature or record. | source_attribute | Yes | No | No |
| `accommodation_type_flat_maisonette_or_apartment` | `text` | Publisher-supplied accommodation type flat maisonette or apartment for the represented feature or record. | source_attribute | Yes | No | No |
| `accommodation_type_semi_detached` | `text` | Publisher-supplied accommodation type semi detached for the represented feature or record. | source_attribute | Yes | No | No |
| `accommodation_type_terraced` | `bigint` | Publisher-supplied accommodation type terraced for the represented feature or record. | source_attribute | Yes | No | No |
| `car_or_van_availability_1_car_or_van` | `bigint` | Publisher-supplied car or van availability 1 car or van for the represented feature or record. | source_attribute | Yes | No | No |
| `car_or_van_availability_2_cars_or_vans` | `bigint` | Publisher-supplied car or van availability 2 cars or vans for the represented feature or record. | source_attribute | Yes | No | No |
| `car_or_van_availability_3_cars_or_vans` | `bigint` | Publisher-supplied car or van availability 3 cars or vans for the represented feature or record. | source_attribute | Yes | No | No |
| `car_or_van_availability_4_cars_or_vans` | `bigint` | Count or numeric value for car or van availability 4 cars or vans in the represented area. | statistical_value | Yes | No | No |
| `car_or_van_availability_5_or_more_cars_or_vans` | `bigint` | Count or numeric value for car or van availability 5 or more cars or vans in the represented area. | statistical_value | Yes | No | No |
| `car_or_van_availability_no_cars_or_vans` | `bigint` | Publisher-supplied car or van availability number cars or vans for the represented feature or record. | source_attribute | Yes | No | No |
| `central_heating_gas_only_note_1` | `bigint` | Publisher-supplied central heating gas only note 1 for the represented feature or record. | source_attribute | Yes | No | No |
| `central_heating_oil_only` | `text` | Publisher-supplied central heating oil only for the represented feature or record. | source_attribute | Yes | No | No |
| `central_heating_other` | `bigint` | Publisher-supplied central heating other for the represented feature or record. | source_attribute | Yes | No | No |
| `household_adaptations_not_designed_or_adapted` | `text` | Publisher-supplied household adaptations not designed or adapted for the represented feature or record. | source_attribute | Yes | No | No |
| `household_adaptations_one` | `bigint` | Publisher-supplied household adaptations one for the represented feature or record. | source_attribute | Yes | No | No |
| `household_adaptations_two_or_more` | `bigint` | Publisher-supplied household adaptations two or more for the represented feature or record. | source_attribute | Yes | No | No |
| `household_tenure_lives_rent_free` | `bigint` | Count or numeric value for household tenure lives rent free in the represented area. | statistical_value | Yes | No | No |
| `household_tenure_owns_inc_shared_ownership` | `text` | Publisher-supplied household tenure owns inc shared ownership for the represented feature or record. | source_attribute | Yes | No | No |
| `household_tenure_private_rented` | `bigint` | Publisher-supplied household tenure private rented for the represented feature or record. | source_attribute | Yes | No | No |
| `household_tenure_social_rented` | `bigint` | Publisher-supplied household tenure social rented for the represented feature or record. | source_attribute | Yes | No | No |
| `renewable_energy_systems_any_renewable_energy_systems` | `bigint` | Publisher-supplied renewable energy systems any renewable energy systems for the represented feature or record. | source_attribute | Yes | No | No |
| `renewable_energy_systems_no_renewable_energy_systems` | `text` | Publisher-supplied renewable energy systems number renewable energy systems for the represented feature or record. | source_attribute | Yes | No | No |
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
