# Housing Ltla

## Overview

- **Identifier:** `a_ons_england_wales/housing_ltla`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update
- **Schema:** `a_ons_england_wales`
- **Table:** `housing_ltla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 331
- **Columns:** 140
- **Metadata status:** source_mapped

## Description

Housing Ltla is an authoritative dataset published by Office for National Statistics. It contains records relating to housing ltla.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` |  |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `accommodation_type_total` | `bigint` |  |
| `detached` | `bigint` |  |
| `semi_detached` | `bigint` |  |
| `terraced` | `bigint` |  |
| `in_a_purpose_built_block_of_flats_or_tenement` | `bigint` |  |
| `converted_or_shared_house_incl_bedsits` | `bigint` |  |
| `converted_bldg_eg_school_church_warehouse` | `bigint` |  |
| `commercial_bldg_eg_office_hotel_shop` | `bigint` |  |
| `a_caravan_or_other_mobile_or_temporary_structure` | `bigint` |  |
| `num_cars_or_vans_total` | `bigint` |  |
| `no_cars_or_vans_in_household` | `bigint` |  |
| `t_1_car_or_van_in_household` | `bigint` |  |
| `t_2_cars_or_vans_in_household` | `bigint` |  |
| `t_3_or_more_cars_or_vans_in_household` | `bigint` |  |
| `central_heating_total` | `bigint` |  |
| `no_central_heating` | `bigint` |  |
| `mains_gas_only` | `bigint` |  |
| `tank_or_bottled_gas_only` | `bigint` |  |
| `electric_only` | `bigint` |  |
| `oil_only` | `bigint` |  |
| `wood_only` | `bigint` |  |
| `solid_fuel_only` | `bigint` |  |
| `renewable_energy_only` | `bigint` |  |
| `district_or_communal_heat_networks_only` | `bigint` |  |
| `other_central_heating_only` | `bigint` |  |
| `two_or_more_types_of_central_heating` | `bigint` |  |
| `two_or_more_types_of_central_heating_2` | `bigint` |  |
| `communal_estab_position_total` | `bigint` |  |
| `resident` | `bigint` |  |
| `resident_male` | `bigint` |  |
| `resident_male_aged_0_to_15_years` | `bigint` |  |
| `resident_male_aged_16_to_24_years` | `bigint` |  |
| `resident_male_aged_25_to_34_years` | `bigint` |  |
| `resident_male_aged_35_to_49_years` | `bigint` |  |
| `resident_male_aged_50_to_64_years` | `bigint` |  |
| `resident_male_aged_65_to_74_years` | `bigint` |  |
| `resident_male_aged_75_to_84_years` | `bigint` |  |
| `resident_male_aged_85_years_and_over` | `bigint` |  |
| `resident_female` | `bigint` |  |
| `resident_female_aged_0_to_15_years` | `bigint` |  |
| `resident_female_aged_16_to_24_years` | `bigint` |  |
| `resident_female_aged_25_to_34_years` | `bigint` |  |
| `resident_female_aged_35_to_49_years` | `bigint` |  |
| `resident_female_aged_50_to_64_years` | `bigint` |  |
| `resident_female_aged_65_to_74_years` | `bigint` |  |
| `resident_female_aged_75_to_84_years` | `bigint` |  |
| `resident_female_aged_85_years_and_over` | `bigint` |  |
| `staff_or_owner` | `bigint` |  |
| `family_member_or_partner_of_staff_or_owner` | `bigint` |  |
| `staying_temporarily` | `bigint` |  |
| `communal_estab_mgmt_total` | `bigint` |  |
| `medical_and_care_establishment` | `bigint` |  |
| `medical_and_care_establishment_nhs` | `bigint` |  |
| `med_care_estab_nhs_general_hospital` | `bigint` |  |
| `med_care_estab_nhs_mental_health_hospital_or_unit` | `bigint` |  |
| `medical_and_care_establishment_nhs_other_hospital` | `bigint` |  |
| `medical_and_care_establishment_local_authority` | `bigint` |  |
| `med_care_estab_local_authority_children_s_home` | `bigint` |  |
| `med_care_estab_la_care_home_w_nursing` | `bigint` |  |
| `med_care_estab_la_care_home_no_nursing` | `bigint` |  |
| `med_care_estab_local_authority_other_home` | `bigint` |  |
| `med_care_estab_rsl_or_housing_assoc` | `bigint` |  |
| `med_care_estab_rsl_or_ha_home_hostel` | `bigint` |  |
| `medical_and_care_establishment_other` | `bigint` |  |
| `med_care_estab_other_care_home_with_nursing` | `bigint` |  |
| `med_care_estab_other_care_home_without_nursing` | `bigint` |  |
| `med_care_estab_other_children_s_home` | `bigint` |  |
| `med_care_estab_other_mental_health_hospital_or_unit` | `bigint` |  |
| `medical_and_care_establishment_other_hospital` | `bigint` |  |
| `medical_and_care_establishment_other_establishment` | `bigint` |  |
| `other_establishment` | `bigint` |  |
| `other_establishment_defence` | `bigint` |  |
| `other_establishment_prison_service` | `bigint` |  |
| `other_establishment_approved_premises` | `bigint` |  |
| `other_estab_detention_centres_and_other_detention` | `bigint` |  |
| `other_establishment_education` | `bigint` |  |
| `other_estab_hotel_guest_house_b_or_youth_hostel` | `bigint` |  |
| `other_estab_hostel_or_temp_shelter` | `bigint` |  |
| `other_establishment_holiday_accommodation` | `bigint` |  |
| `other_estab_other_travel_or_temporary_accommodation` | `bigint` |  |
| `other_establishment_religious` | `bigint` |  |
| `other_estab_staff_or_worker_accommodation_or_other` | `bigint` |  |
| `establishment_not_stated` | `bigint` |  |
| `num_bedrooms_total` | `bigint` |  |
| `t_1_bedroom` | `bigint` |  |
| `t_2_bedrooms` | `bigint` |  |
| `t_3_bedrooms` | `bigint` |  |
| `t_4_or_more_bedrooms` | `bigint` |  |
| `number_of_rooms_total` | `bigint` |  |
| `t_1_room` | `bigint` |  |
| `t_2_rooms` | `bigint` |  |
| `t_3_rooms` | `bigint` |  |
| `t_4_rooms` | `bigint` |  |
| `t_5_rooms` | `bigint` |  |
| `t_6_rooms` | `bigint` |  |
| `t_7_rooms` | `bigint` |  |
| `t_8_rooms` | `bigint` |  |
| `t_9_or_more_rooms` | `bigint` |  |
| `occupancy_rating_bedrooms_total` | `bigint` |  |
| `occupancy_rating_of_bedrooms_2_or_more` | `bigint` |  |
| `occupancy_rating_of_bedrooms_1` | `bigint` |  |
| `occupancy_rating_of_bedrooms_0` | `bigint` |  |
| `occupancy_rating_of_bedrooms_1_2` | `bigint` |  |
| `occupancy_rating_of_bedrooms_2_or_less` | `bigint` |  |
| `occupancy_rating_rooms_total` | `bigint` |  |
| `occupancy_rating_of_rooms_2_or_more` | `bigint` |  |
| `occupancy_rating_of_rooms_1` | `bigint` |  |
| `occupancy_rating_of_rooms_0` | `bigint` |  |
| `occupancy_rating_of_rooms_1_2` | `bigint` |  |
| `occupancy_rating_of_rooms_2_or_less` | `bigint` |  |
| `tenure_total` | `bigint` |  |
| `owned` | `bigint` |  |
| `owned_owns_outright` | `bigint` |  |
| `owned_owns_with_a_mortgage_or_loan` | `bigint` |  |
| `shared_ownership` | `bigint` |  |
| `shared_ownership_shared_ownership` | `bigint` |  |
| `social_rented` | `bigint` |  |
| `social_rented_council_or_la` | `bigint` |  |
| `social_rented_other_social_rented` | `bigint` |  |
| `private_rented` | `bigint` |  |
| `private_rented_private_landlord_or_letting_agency` | `bigint` |  |
| `private_rented_other_private_rented` | `bigint` |  |
| `lives_rent_free` | `bigint` |  |
| `second_address_type_total` | `bigint` |  |
| `armed_forces_base_address` | `bigint` |  |
| `another_address_when_working_away_from_home` | `bigint` |  |
| `holiday_home` | `bigint` |  |
| `student_s_term_time_address` | `bigint` |  |
| `student_s_home_address` | `bigint` |  |
| `another_parent_or_guardian_s_address` | `bigint` |  |
| `partner_s_address` | `bigint` |  |
| `other` | `bigint` |  |
| `not_specified` | `bigint` |  |
| `second_address_total` | `bigint` |  |
| `no_second_address` | `bigint` |  |
| `is_in_the_uk` | `bigint` |  |
| `is_outside_the_uk` | `bigint` |  |
