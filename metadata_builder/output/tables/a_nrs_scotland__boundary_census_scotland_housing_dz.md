# Boundary Census Scotland Housing Dz

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_housing_dz`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.650007, 54.633240, -0.724609, 60.860766]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_census_scotland_housing_dz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 7392
- **Columns:** 83
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Housing Dz is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland housing dz features using multipolygon geometry.

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
| `uv401_all_people_in_households` | `bigint` |  |
| `uv401_whole_house_or_bungalow_total` | `bigint` |  |
| `uv401_whole_house_or_bungalow_detached` | `double precision` |  |
| `uv401_whole_house_or_bungalow_semi_detached` | `double precision` |  |
| `uv401_whole_house_or_bungalow_terraced_incl_end_terrace` | `double precision` |  |
| `uv401_flat_maisonette_or_apartment_total` | `double precision` |  |
| `uv401_flat_maisonette_or_apartment_purpose_built_block_of_flats` | `double precision` |  |
| `uv401_flat_maisonette_or_apartment_part_of_a_converted_or_share` | `double precision` |  |
| `uv401_flat_maisonette_or_apartment_in_a_commercial_building` | `double precision` |  |
| `uv401_caravan_or_other_mobile_or_temporary_structure` | `double precision` |  |
| `uv402_all_occupied_households` | `bigint` |  |
| `uv402_whole_house_or_bungalow_total` | `bigint` |  |
| `uv402_whole_house_or_bungalow_detached` | `double precision` |  |
| `uv402_whole_house_or_bungalow_semi_detached` | `double precision` |  |
| `uv402_whole_house_or_bungalow_terraced_incl_end_terrace` | `double precision` |  |
| `uv402_flat_maisonette_or_apartment_total` | `double precision` |  |
| `uv402_flat_maisonette_or_apartment_purpose_built_block_of_flats` | `double precision` |  |
| `uv402_flat_maisonette_or_apartment_part_of_a_converted_or_share` | `double precision` |  |
| `uv402_flat_maisonette_or_apartment_in_a_commercial_building` | `double precision` |  |
| `uv402_caravan_or_other_mobile_or_temporary_structure` | `double precision` |  |
| `uv403_all_people_in_households` | `bigint` |  |
| `uv403_owned_total` | `bigint` |  |
| `uv403_owned_owned_outright` | `bigint` |  |
| `uv403_owned_owned_with_a_mortgage_or_loan` | `bigint` |  |
| `uv403_owned_shared_ownership_part_owned_and_part_rented` | `double precision` |  |
| `uv403_owned_shared_equity_e_g_lift_or_help_to_buy` | `double precision` |  |
| `uv403_social_rented_council_la_or_housing_association_registere` | `double precision` |  |
| `uv403_private_rented_total` | `double precision` |  |
| `uv403_private_rented_private_landlord_or_letting_agency` | `double precision` |  |
| `uv403_private_rented_other` | `double precision` |  |
| `uv403_lives_rent_free` | `double precision` |  |
| `uv404_all_occupied_households` | `bigint` |  |
| `uv404_owned_total` | `bigint` |  |
| `uv404_owned_owned_outright` | `bigint` |  |
| `uv404_owned_owned_with_a_mortgage_or_loan` | `bigint` |  |
| `uv404_owned_shared_ownership_part_owned_and_part_rented` | `double precision` |  |
| `uv404_owned_shared_equity_e_g_lift_or_help_to_buy` | `double precision` |  |
| `uv404_social_rented_council_la_or_housing_association_registere` | `double precision` |  |
| `uv404_private_rented_total` | `double precision` |  |
| `uv404_private_rented_private_landlord_or_letting_agency` | `double precision` |  |
| `uv404_private_rented_other` | `double precision` |  |
| `uv404_lives_rent_free` | `double precision` |  |
| `uv405_all_occupied_households` | `bigint` |  |
| `number_of_cars_or_vans_in_hh_no_cars_or_vans` | `double precision` |  |
| `number_of_cars_or_vans_in_household_one_car_or_van` | `bigint` |  |
| `number_of_cars_or_vans_in_hh_two_cars_or_vans` | `bigint` |  |
| `number_of_cars_or_vans_in_hh_three_cars_or_vans` | `double precision` |  |
| `number_of_cars_or_vans_in_hh_four_plus_cars_or_vans` | `double precision` |  |
| `all_occupied_household_spaces` | `bigint` |  |
| `one_person` | `bigint` |  |
| `two_people` | `bigint` |  |
| `three_people` | `bigint` |  |
| `four_people` | `double precision` |  |
| `five_people` | `double precision` |  |
| `six_people` | `double precision` |  |
| `seven_people` | `double precision` |  |
| `eight_or_more_people` | `double precision` |  |
| `uv407_all_occupied_households` | `bigint` |  |
| `no_central_heating` | `double precision` |  |
| `gas_central_heating_total` | `double precision` |  |
| `gas_central_heating_mains_gas` | `double precision` |  |
| `gas_central_heating_other_gas_incl_liquid_petroleum_gas_and_bio` | `double precision` |  |
| `electric_including_storage_heaters_central_heating` | `double precision` |  |
| `oil_central_heating` | `double precision` |  |
| `solid_fuel_excluding_wood` | `double precision` |  |
| `wood_or_biomass_incl_logs_pellets_chippings_central_heating` | `double precision` |  |
| `other_renewable_energy_source_incl_electric_and_air_heat_pump_s` | `double precision` |  |
| `district_or_communal_heat_system` | `double precision` |  |
| `other_central_heating` | `double precision` |  |
| `two_or_more_types_of_central_heating` | `double precision` |  |
| `uv408_all_occupied_households` | `bigint` |  |
| `one_bedroom` | `double precision` |  |
| `two_bedrooms` | `double precision` |  |
| `three_bedrooms` | `bigint` |  |
| `four_bedrooms` | `double precision` |  |
| `five_or_more_bedrooms` | `double precision` |  |
| `uv415_all_occupied_households` | `bigint` |  |
| `occupancy_rating_of_bedrooms_2_or_more` | `double precision` |  |
| `occupancy_rating_of_bedrooms_1` | `bigint` |  |
| `occupancy_rating_of_bedrooms_0` | `bigint` |  |
| `occupancy_rating_of_bedrooms_1_or_less` | `double precision` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
