# Boundary Census Scotland Housing Intzones

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_housing_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.650007, 54.633238, -0.724609, 60.860766]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_census_scotland_housing_intzones`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1280
- **Columns:** 73
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Housing Intzones is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland housing intzones features using multipolygon geometry.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. |
| `geography_name` | `text` | Name associated with the represented feature. |
| `accom_hh_all_occupied_hhs` | `bigint` |  |
| `accom_hh_house_bungalow_total` | `bigint` |  |
| `accom_hh_house_detached` | `bigint` |  |
| `accom_hh_house_semi_detached` | `bigint` |  |
| `accom_hh_house_terraced` | `bigint` |  |
| `accom_hh_flat_total` | `bigint` |  |
| `accom_hh_flat_purpose_built` | `bigint` |  |
| `accom_hh_flat_converted_or_shared` | `bigint` |  |
| `accom_hh_flat_commercial_building` | `bigint` |  |
| `accom_hh_caravan_or_temporary` | `bigint` |  |
| `all_people_in_hhs` | `bigint` | Recorded census measure for the category "all people in hhs" in the represented area. Units and population base require the source table. |
| `accom_people_house_bungalow_total` | `bigint` |  |
| `accom_people_house_detached` | `bigint` |  |
| `accom_people_house_semi_detached` | `bigint` |  |
| `accom_people_house_terraced` | `bigint` |  |
| `accom_people_flat_total` | `bigint` |  |
| `accom_people_flat_purpose_built` | `bigint` |  |
| `accom_people_flat_converted_or_shared` | `bigint` |  |
| `accom_people_flat_commercial_building` | `bigint` |  |
| `accom_people_caravan_or_temporary` | `bigint` |  |
| `central_heating_all_occupied_hhs` | `bigint` |  |
| `no_heating` | `bigint` |  |
| `gas_heating_total` | `bigint` |  |
| `gas_heating_mains` | `bigint` |  |
| `gas_heating_other` | `bigint` |  |
| `electric_heating` | `bigint` |  |
| `oil_heating` | `bigint` |  |
| `solid_fuel_heating` | `bigint` |  |
| `wood_biomass_heating` | `bigint` |  |
| `renewable_heating` | `bigint` |  |
| `district_communal_heating` | `bigint` |  |
| `other_heating` | `bigint` |  |
| `two_plus_heating_types` | `bigint` |  |
| `num_bedrooms_all_occupied_hhs` | `bigint` |  |
| `one_bedroom` | `bigint` |  |
| `two_bedrooms` | `bigint` |  |
| `three_bedrooms` | `bigint` |  |
| `four_bedrooms` | `bigint` |  |
| `t_5plus_bedrooms` | `bigint` |  |
| `all_occupied_hh_spaces` | `bigint` |  |
| `one_person` | `bigint` |  |
| `two_people` | `bigint` |  |
| `three_people` | `bigint` |  |
| `four_people` | `bigint` |  |
| `five_people` | `bigint` |  |
| `six_people` | `bigint` |  |
| `seven_people` | `bigint` |  |
| `t_8plus_people` | `bigint` |  |
| `occupancy_all_occupied_hhs` | `bigint` |  |
| `occupancy_2plus` | `bigint` |  |
| `occupancy_plus1` | `bigint` |  |
| `occupancy_0` | `bigint` |  |
| `occupancy_minus1_or_less` | `bigint` |  |
| `tenure_all_occupied_hhs` | `bigint` |  |
| `owned_total` | `bigint` |  |
| `owned_outright` | `bigint` |  |
| `owned_mortgage_or_loan` | `bigint` |  |
| `owned_shared_ownership` | `bigint` |  |
| `owned_shared_equity` | `bigint` |  |
| `social_rented` | `bigint` |  |
| `private_rented_total` | `bigint` |  |
| `private_rented_landlord` | `bigint` |  |
| `private_rented_other` | `bigint` |  |
| `rent_free` | `bigint` |  |
| `cars_vans_all_occupied_hhs` | `bigint` |  |
| `no_cars_or_vans` | `bigint` |  |
| `one_car_or_van` | `bigint` |  |
| `two_cars_or_vans` | `bigint` |  |
| `three_cars_or_vans` | `bigint` |  |
| `four_plus_cars_or_vans` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
