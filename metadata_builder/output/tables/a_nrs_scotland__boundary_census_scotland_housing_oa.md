# Boundary Census Scotland Housing Oa

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_housing_oa`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.649996, 54.633220, -0.724450, 60.860787]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_census_scotland_housing_oa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 46363
- **Columns:** 83
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Housing Oa is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland housing oa features using geometry geometry.

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
| `all_people_in_households_accom_ppl` | `bigint` | Count or numeric value for all people in households accom ppl in the represented area. |
| `whole_house_or_bungalow_total_accom_ppl` | `double precision` | Count or numeric value for whole house or bungalow total accom ppl in the represented area. |
| `whole_house_or_bungalow_detached_accom_ppl` | `double precision` | Count or numeric value for whole house or bungalow detached accom ppl in the represented area. |
| `whole_house_or_bungalow_semi_detached_accom_ppl` | `double precision` | Count or numeric value for whole house or bungalow semi detached accom ppl in the represented area. |
| `house_terraced_accom_ppl` | `double precision` | Count or numeric value for house terraced accom ppl in the represented area. |
| `flat_maisonette_or_apartment_total_accom_ppl` | `double precision` | Numeric flat maisonette or apartment total accom ppl value recorded for the feature. |
| `flat_purpose_built_accom_ppl` | `double precision` | Numeric flat purpose built accom ppl value recorded for the feature. |
| `flat_converted_or_shared_accom_ppl` | `double precision` | Numeric flat converted or shared accom ppl value recorded for the feature. |
| `flat_commercial_accom_ppl` | `double precision` | Numeric flat commercial accom ppl value recorded for the feature. |
| `caravan_or_mobile_accom_ppl` | `double precision` | Count or numeric value for caravan or mobile accom ppl in the represented area. |
| `all_occupied_households_accom_hh` | `bigint` | Count or numeric value for all occupied households accom households in the represented area. |
| `whole_house_or_bungalow_total_accom_hh` | `double precision` | Count or numeric value for whole house or bungalow total accom households in the represented area. |
| `whole_house_or_bungalow_detached_accom_hh` | `double precision` | Count or numeric value for whole house or bungalow detached accom households in the represented area. |
| `whole_house_or_bungalow_semi_detached_accom_hh` | `double precision` | Count or numeric value for whole house or bungalow semi detached accom households in the represented area. |
| `house_terraced_accom_hh` | `double precision` | Count or numeric value for house terraced accom households in the represented area. |
| `flat_maisonette_or_apartment_total_accom_hh` | `double precision` | Numeric flat maisonette or apartment total accom households value recorded for the feature. |
| `flat_purpose_built_accom_hh` | `double precision` | Numeric flat purpose built accom households value recorded for the feature. |
| `flat_converted_or_shared_accom_hh` | `double precision` | Numeric flat converted or shared accom households value recorded for the feature. |
| `flat_commercial_accom_hh` | `double precision` | Numeric flat commercial accom households value recorded for the feature. |
| `caravan_or_other_mobile_or_temporary_structure_accom_hh` | `double precision` | Count or numeric value for caravan or other mobile or temporary structure accom households in the represented area. |
| `all_people_in_households_tenure_ppl` | `bigint` | Count or numeric value for all people in households tenure ppl in the represented area. |
| `owned_total_tenure_ppl` | `double precision` | Count or numeric value for owned total tenure ppl in the represented area. |
| `owned_owned_outright_tenure_ppl` | `double precision` | Count or numeric value for owned owned outright tenure ppl in the represented area. |
| `owned_owned_with_a_mortgage_or_loan_tenure_ppl` | `double precision` | Count or numeric value for owned owned with a mortgage or loan tenure ppl in the represented area. |
| `owned_shared_ownership_tenure_ppl` | `double precision` | Count or numeric value for owned shared ownership tenure ppl in the represented area. |
| `owned_shared_equity_e_g_lift_or_help_to_buy_tenure_ppl` | `double precision` | Count or numeric value for owned shared equity e g lift or help to buy tenure ppl in the represented area. |
| `social_rented_tenure_ppl` | `double precision` | Count or numeric value for social rented tenure ppl in the represented area. |
| `private_rented_total_tenure_ppl` | `double precision` | Count or numeric value for private rented total tenure ppl in the represented area. |
| `private_rented_landlord_tenure_ppl` | `double precision` | Count or numeric value for private rented landlord tenure ppl in the represented area. |
| `private_rented_other_tenure_ppl` | `double precision` | Count or numeric value for private rented other tenure ppl in the represented area. |
| `lives_rent_free_tenure_ppl` | `double precision` | Count or numeric value for lives rent free tenure ppl in the represented area. |
| `all_occupied_households_tenure_hh` | `bigint` | Count or numeric value for all occupied households tenure households in the represented area. |
| `owned_total_tenure_hh` | `double precision` | Count or numeric value for owned total tenure households in the represented area. |
| `owned_owned_outright_tenure_hh` | `double precision` | Count or numeric value for owned owned outright tenure households in the represented area. |
| `owned_owned_with_a_mortgage_or_loan_tenure_hh` | `double precision` | Count or numeric value for owned owned with a mortgage or loan tenure households in the represented area. |
| `owned_shared_ownership_tenure_hh` | `double precision` | Count or numeric value for owned shared ownership tenure households in the represented area. |
| `owned_shared_equity_e_g_lift_or_help_to_buy_tenure_hh` | `double precision` | Count or numeric value for owned shared equity e g lift or help to buy tenure households in the represented area. |
| `social_rented_tenure_hh` | `double precision` | Count or numeric value for social rented tenure households in the represented area. |
| `private_rented_total_tenure_hh` | `double precision` | Count or numeric value for private rented total tenure households in the represented area. |
| `private_rented_landlord_tenure_hh` | `double precision` | Count or numeric value for private rented landlord tenure households in the represented area. |
| `private_rented_other_tenure_hh` | `double precision` | Count or numeric value for private rented other tenure households in the represented area. |
| `lives_rent_free_tenure_hh` | `double precision` | Count or numeric value for lives rent free tenure households in the represented area. |
| `all_occupied_households_cars` | `bigint` | Count or numeric value for all occupied households cars in the represented area. |
| `number_of_cars_or_vans_in_household_no_cars_or_vans` | `double precision` | Count or numeric value for number of cars or vans in household number cars or vans in the represented area. |
| `number_of_cars_or_vans_in_household_one_car_or_van` | `bigint` | Count or numeric value for number of cars or vans in household one car or van in the represented area. |
| `number_of_cars_or_vans_in_household_two_cars_or_vans` | `double precision` | Count or numeric value for number of cars or vans in household two cars or vans in the represented area. |
| `number_of_cars_or_vans_in_household_three_cars_or_vans` | `double precision` | Count or numeric value for number of cars or vans in household three cars or vans in the represented area. |
| `four_plus_cars` | `double precision` | Count or numeric value for four plus cars in the represented area. |
| `all_occupied_household_spaces` | `bigint` | Count or numeric value for all occupied household spaces in the represented area. |
| `one_person` | `double precision` | Count or numeric value for one person in the represented area. |
| `two_people` | `double precision` | Count or numeric value for two people in the represented area. |
| `three_people` | `double precision` | Count or numeric value for three people in the represented area. |
| `four_people` | `double precision` | Count or numeric value for four people in the represented area. |
| `five_people` | `double precision` | Count or numeric value for five people in the represented area. |
| `six_people` | `double precision` | Count or numeric value for six people in the represented area. |
| `seven_people` | `double precision` | Count or numeric value for seven people in the represented area. |
| `eight_or_more_people` | `double precision` | Count or numeric value for eight or more people in the represented area. |
| `all_occupied_households_heating` | `bigint` | Count or numeric value for all occupied households heating in the represented area. |
| `no_central_heating` | `double precision` | Count or numeric value for number central heating in the represented area. |
| `gas_central_heating_total` | `double precision` | Count or numeric value for gas central heating total in the represented area. |
| `gas_central_heating_mains_gas` | `double precision` | Count or numeric value for gas central heating mains gas in the represented area. |
| `gas_heating_other` | `double precision` | Count or numeric value for gas heating other in the represented area. |
| `electric_including_storage_heaters_central_heating` | `double precision` | Count or numeric value for electric including storage heaters central heating in the represented area. |
| `oil_central_heating` | `double precision` | Count or numeric value for oil central heating in the represented area. |
| `solid_fuel_excluding_wood` | `double precision` | Count or numeric value for solid fuel excluding wood in the represented area. |
| `wood_biomass_heating` | `double precision` | Count or numeric value for wood biomass heating in the represented area. |
| `renewable_heating` | `double precision` | Count or numeric value for renewable heating in the represented area. |
| `district_or_communal_heat_system` | `double precision` | Count or numeric value for district or communal heat system in the represented area. |
| `other_central_heating` | `double precision` | Count or numeric value for other central heating in the represented area. |
| `two_or_more_types_of_central_heating` | `double precision` | Count or numeric value for two or more types of central heating in the represented area. |
| `all_occupied_households_bedrooms` | `bigint` | Count or numeric value for all occupied households bedrooms in the represented area. |
| `one_bedroom` | `double precision` | Count or numeric value for one bedroom in the represented area. |
| `two_bedrooms` | `double precision` | Count or numeric value for two bedrooms in the represented area. |
| `three_bedrooms` | `double precision` | Count or numeric value for three bedrooms in the represented area. |
| `four_bedrooms` | `double precision` | Count or numeric value for four bedrooms in the represented area. |
| `five_or_more_bedrooms` | `double precision` | Count or numeric value for five or more bedrooms in the represented area. |
| `all_occupied_households_occupancy` | `bigint` | Count or numeric value for all occupied households occupancy in the represented area. |
| `occupancy_rating_of_bedrooms_2_or_more` | `double precision` | Count or numeric value for occupancy rating of bedrooms 2 or more in the represented area. |
| `occupancy_rating_of_bedrooms_1` | `double precision` | Count or numeric value for occupancy rating of bedrooms 1 in the represented area. |
| `occupancy_rating_of_bedrooms_0` | `double precision` | Count or numeric value for occupancy rating of bedrooms 0 in the represented area. |
| `occupancy_rating_of_bedrooms_1_or_less` | `double precision` | Count or numeric value for occupancy rating of bedrooms 1 or less in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
