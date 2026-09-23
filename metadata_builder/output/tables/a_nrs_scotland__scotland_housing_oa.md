# Scotland Housing Oa

## Overview

- **Identifier:** `a_nrs_scotland/scotland_housing_oa`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `scotland_housing_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 46363
- **Columns:** 82
- **Metadata status:** source_mapped

## Description

Scotland Housing Oa is an authoritative dataset published by National Records of Scotland. It contains records relating to scotland housing oa.

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
| `all_people_in_households_accom_ppl` | `bigint` | Recorded census measure for the category "all people in households accom ppl" in the represented area. Units and population base require the source table. |
| `whole_house_or_bungalow_total_accom_ppl` | `double precision` |  |
| `whole_house_or_bungalow_detached_accom_ppl` | `double precision` |  |
| `whole_house_or_bungalow_semi_detached_accom_ppl` | `double precision` |  |
| `house_terraced_accom_ppl` | `double precision` |  |
| `flat_maisonette_or_apartment_total_accom_ppl` | `double precision` |  |
| `flat_purpose_built_accom_ppl` | `double precision` |  |
| `flat_converted_or_shared_accom_ppl` | `double precision` |  |
| `flat_commercial_accom_ppl` | `double precision` |  |
| `caravan_or_mobile_accom_ppl` | `double precision` |  |
| `all_occupied_households_accom_hh` | `bigint` | Recorded census measure for the category "all occupied households accom hh" in the represented area. Units and population base require the source table. |
| `whole_house_or_bungalow_total_accom_hh` | `double precision` |  |
| `whole_house_or_bungalow_detached_accom_hh` | `double precision` |  |
| `whole_house_or_bungalow_semi_detached_accom_hh` | `double precision` |  |
| `house_terraced_accom_hh` | `double precision` |  |
| `flat_maisonette_or_apartment_total_accom_hh` | `double precision` |  |
| `flat_purpose_built_accom_hh` | `double precision` |  |
| `flat_converted_or_shared_accom_hh` | `double precision` |  |
| `flat_commercial_accom_hh` | `double precision` |  |
| `caravan_or_other_mobile_or_temporary_structure_accom_hh` | `double precision` |  |
| `all_people_in_households_tenure_ppl` | `bigint` | Recorded census measure for the category "all people in households tenure ppl" in the represented area. Units and population base require the source table. |
| `owned_total_tenure_ppl` | `double precision` |  |
| `owned_owned_outright_tenure_ppl` | `double precision` |  |
| `owned_owned_with_a_mortgage_or_loan_tenure_ppl` | `double precision` |  |
| `owned_shared_ownership_tenure_ppl` | `double precision` |  |
| `owned_shared_equity_e_g_lift_or_help_to_buy_tenure_ppl` | `double precision` |  |
| `social_rented_tenure_ppl` | `double precision` |  |
| `private_rented_total_tenure_ppl` | `double precision` |  |
| `private_rented_landlord_tenure_ppl` | `double precision` |  |
| `private_rented_other_tenure_ppl` | `double precision` |  |
| `lives_rent_free_tenure_ppl` | `double precision` |  |
| `all_occupied_households_tenure_hh` | `bigint` | Recorded census measure for the category "all occupied households tenure hh" in the represented area. Units and population base require the source table. |
| `owned_total_tenure_hh` | `double precision` |  |
| `owned_owned_outright_tenure_hh` | `double precision` |  |
| `owned_owned_with_a_mortgage_or_loan_tenure_hh` | `double precision` |  |
| `owned_shared_ownership_tenure_hh` | `double precision` |  |
| `owned_shared_equity_e_g_lift_or_help_to_buy_tenure_hh` | `double precision` |  |
| `social_rented_tenure_hh` | `double precision` |  |
| `private_rented_total_tenure_hh` | `double precision` |  |
| `private_rented_landlord_tenure_hh` | `double precision` |  |
| `private_rented_other_tenure_hh` | `double precision` |  |
| `lives_rent_free_tenure_hh` | `double precision` |  |
| `all_occupied_households_cars` | `bigint` | Recorded census measure for the category "all occupied households cars" in the represented area. Units and population base require the source table. |
| `number_of_cars_or_vans_in_household_no_cars_or_vans` | `double precision` |  |
| `number_of_cars_or_vans_in_household_one_car_or_van` | `bigint` |  |
| `number_of_cars_or_vans_in_household_two_cars_or_vans` | `double precision` |  |
| `number_of_cars_or_vans_in_household_three_cars_or_vans` | `double precision` |  |
| `four_plus_cars` | `double precision` |  |
| `all_occupied_household_spaces` | `bigint` |  |
| `one_person` | `double precision` |  |
| `two_people` | `double precision` |  |
| `three_people` | `double precision` |  |
| `four_people` | `double precision` |  |
| `five_people` | `double precision` |  |
| `six_people` | `double precision` |  |
| `seven_people` | `double precision` |  |
| `eight_or_more_people` | `double precision` |  |
| `all_occupied_households_heating` | `bigint` | Recorded census measure for the category "all occupied households heating" in the represented area. Units and population base require the source table. |
| `no_central_heating` | `double precision` |  |
| `gas_central_heating_total` | `double precision` |  |
| `gas_central_heating_mains_gas` | `double precision` |  |
| `gas_heating_other` | `double precision` |  |
| `electric_including_storage_heaters_central_heating` | `double precision` |  |
| `oil_central_heating` | `double precision` |  |
| `solid_fuel_excluding_wood` | `double precision` |  |
| `wood_biomass_heating` | `double precision` |  |
| `renewable_heating` | `double precision` |  |
| `district_or_communal_heat_system` | `double precision` |  |
| `other_central_heating` | `double precision` |  |
| `two_or_more_types_of_central_heating` | `double precision` |  |
| `all_occupied_households_bedrooms` | `bigint` | Recorded census measure for the category "all occupied households bedrooms" in the represented area. Units and population base require the source table. |
| `one_bedroom` | `double precision` |  |
| `two_bedrooms` | `double precision` |  |
| `three_bedrooms` | `double precision` |  |
| `four_bedrooms` | `double precision` |  |
| `five_or_more_bedrooms` | `double precision` |  |
| `all_occupied_households_occupancy` | `bigint` | Recorded census measure for the category "all occupied households occupancy" in the represented area. Units and population base require the source table. |
| `occupancy_rating_of_bedrooms_2_or_more` | `double precision` |  |
| `occupancy_rating_of_bedrooms_1` | `double precision` |  |
| `occupancy_rating_of_bedrooms_0` | `double precision` |  |
| `occupancy_rating_of_bedrooms_1_or_less` | `double precision` |  |
