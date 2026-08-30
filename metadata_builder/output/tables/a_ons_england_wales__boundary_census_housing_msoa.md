# Boundary Census Housing Msoa

## Overview

- **Identifier:** `a_ons_england_wales/boundary_census_housing_msoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418601, 49.864798, 1.763680, 55.811120]`
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_census_housing_msoa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 7264
- **Columns:** 141
- **Metadata status:** source_mapped

## Description

Boundary Census Housing Msoa is an authoritative dataset published by Office for National Statistics. It represents boundary census housing msoa features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `accommodation_type_total` | `bigint` | Count or numeric value for accommodation type total in the represented area. | statistical_value | Yes | No | No |
| `detached` | `bigint` | Count or numeric value for detached in the represented area. | statistical_value | Yes | No | No |
| `semi_detached` | `bigint` | Count or numeric value for semi detached in the represented area. | statistical_value | Yes | No | No |
| `terraced` | `bigint` | Count or numeric value for terraced in the represented area. | statistical_value | Yes | No | No |
| `in_a_purpose_built_block_of_flats_or_tenement` | `bigint` | Numeric in a purpose built block of flats or tenement value recorded for the feature. | measure | Yes | No | No |
| `converted_or_shared_house_incl_bedsits` | `bigint` | Count or numeric value for converted or shared house incl bedsits in the represented area. | statistical_value | Yes | No | No |
| `converted_bldg_eg_school_church_warehouse` | `bigint` | Count or numeric value for converted bldg eg school church warehouse in the represented area. | statistical_value | Yes | No | No |
| `commercial_bldg_eg_office_hotel_shop` | `bigint` | Count or numeric value for commercial bldg eg office hotel shop in the represented area. | statistical_value | Yes | No | No |
| `a_caravan_or_other_mobile_or_temporary_structure` | `bigint` | Count or numeric value for a caravan or other mobile or temporary structure in the represented area. | statistical_value | Yes | No | No |
| `num_cars_or_vans_total` | `bigint` | Count or numeric value for num cars or vans total in the represented area. | statistical_value | Yes | No | No |
| `no_cars_or_vans_in_household` | `bigint` | Count or numeric value for number cars or vans in household in the represented area. | statistical_value | Yes | No | No |
| `t_1_car_or_van_in_household` | `bigint` | Count or numeric value for t 1 car or van in household in the represented area. | statistical_value | Yes | No | No |
| `t_2_cars_or_vans_in_household` | `bigint` | Count or numeric value for t 2 cars or vans in household in the represented area. | statistical_value | Yes | No | No |
| `t_3_or_more_cars_or_vans_in_household` | `bigint` | Count or numeric value for t 3 or more cars or vans in household in the represented area. | statistical_value | Yes | No | No |
| `central_heating_total` | `bigint` | Count or numeric value for central heating total in the represented area. | statistical_value | Yes | No | No |
| `no_central_heating` | `bigint` | Count or numeric value for number central heating in the represented area. | statistical_value | Yes | No | No |
| `mains_gas_only` | `bigint` | Count or numeric value for mains gas only in the represented area. | statistical_value | Yes | No | No |
| `tank_or_bottled_gas_only` | `bigint` | Count or numeric value for tank or bottled gas only in the represented area. | statistical_value | Yes | No | No |
| `electric_only` | `bigint` | Count or numeric value for electric only in the represented area. | statistical_value | Yes | No | No |
| `oil_only` | `bigint` | Count or numeric value for oil only in the represented area. | statistical_value | Yes | No | No |
| `wood_only` | `bigint` | Count or numeric value for wood only in the represented area. | statistical_value | Yes | No | No |
| `solid_fuel_only` | `bigint` | Count or numeric value for solid fuel only in the represented area. | statistical_value | Yes | No | No |
| `renewable_energy_only` | `bigint` | Count or numeric value for renewable energy only in the represented area. | statistical_value | Yes | No | No |
| `district_or_communal_heat_networks_only` | `bigint` | Count or numeric value for district or communal heat networks only in the represented area. | statistical_value | Yes | No | No |
| `other_central_heating_only` | `bigint` | Count or numeric value for other central heating only in the represented area. | statistical_value | Yes | No | No |
| `two_or_more_types_of_central_heating` | `bigint` | Count or numeric value for two or more types of central heating in the represented area. | statistical_value | Yes | No | No |
| `two_or_more_types_of_central_heating_2` | `bigint` | Count or numeric value for two or more types of central heating 2 in the represented area. | statistical_value | Yes | No | No |
| `communal_estab_position_total` | `bigint` | Count or numeric value for communal estab position total in the represented area. | statistical_value | Yes | No | No |
| `resident` | `bigint` | Count or numeric value for resident in the represented area. | statistical_value | Yes | No | No |
| `resident_male` | `bigint` | Count or numeric value for resident male in the represented area. | statistical_value | Yes | No | No |
| `resident_male_aged_0_to_15_years` | `bigint` | Count or numeric value for resident male aged 0 to 15 years in the represented area. | statistical_value | Yes | No | No |
| `resident_male_aged_16_to_24_years` | `bigint` | Count or numeric value for resident male aged 16 to 24 years in the represented area. | statistical_value | Yes | No | No |
| `resident_male_aged_25_to_34_years` | `bigint` | Count or numeric value for resident male aged 25 to 34 years in the represented area. | statistical_value | Yes | No | No |
| `resident_male_aged_35_to_49_years` | `bigint` | Count or numeric value for resident male aged 35 to 49 years in the represented area. | statistical_value | Yes | No | No |
| `resident_male_aged_50_to_64_years` | `bigint` | Count or numeric value for resident male aged 50 to 64 years in the represented area. | statistical_value | Yes | No | No |
| `resident_male_aged_65_to_74_years` | `bigint` | Count or numeric value for resident male aged 65 to 74 years in the represented area. | statistical_value | Yes | No | No |
| `resident_male_aged_75_to_84_years` | `bigint` | Count or numeric value for resident male aged 75 to 84 years in the represented area. | statistical_value | Yes | No | No |
| `resident_male_aged_85_years_and_over` | `bigint` | Count or numeric value for resident male aged 85 years and over in the represented area. | statistical_value | Yes | No | No |
| `resident_female` | `bigint` | Count or numeric value for resident female in the represented area. | statistical_value | Yes | No | No |
| `resident_female_aged_0_to_15_years` | `bigint` | Count or numeric value for resident female aged 0 to 15 years in the represented area. | statistical_value | Yes | No | No |
| `resident_female_aged_16_to_24_years` | `bigint` | Count or numeric value for resident female aged 16 to 24 years in the represented area. | statistical_value | Yes | No | No |
| `resident_female_aged_25_to_34_years` | `bigint` | Count or numeric value for resident female aged 25 to 34 years in the represented area. | statistical_value | Yes | No | No |
| `resident_female_aged_35_to_49_years` | `bigint` | Count or numeric value for resident female aged 35 to 49 years in the represented area. | statistical_value | Yes | No | No |
| `resident_female_aged_50_to_64_years` | `bigint` | Count or numeric value for resident female aged 50 to 64 years in the represented area. | statistical_value | Yes | No | No |
| `resident_female_aged_65_to_74_years` | `bigint` | Count or numeric value for resident female aged 65 to 74 years in the represented area. | statistical_value | Yes | No | No |
| `resident_female_aged_75_to_84_years` | `bigint` | Count or numeric value for resident female aged 75 to 84 years in the represented area. | statistical_value | Yes | No | No |
| `resident_female_aged_85_years_and_over` | `bigint` | Count or numeric value for resident female aged 85 years and over in the represented area. | statistical_value | Yes | No | No |
| `staff_or_owner` | `bigint` | Count or numeric value for staff or owner in the represented area. | statistical_value | Yes | No | No |
| `family_member_or_partner_of_staff_or_owner` | `bigint` | Count or numeric value for family member or partner of staff or owner in the represented area. | statistical_value | Yes | No | No |
| `staying_temporarily` | `bigint` | Count or numeric value for staying temporarily in the represented area. | statistical_value | Yes | No | No |
| `communal_estab_mgmt_total` | `bigint` | Count or numeric value for communal estab mgmt total in the represented area. | statistical_value | Yes | No | No |
| `medical_and_care_establishment` | `bigint` | Count or numeric value for medical and care establishment in the represented area. | statistical_value | Yes | No | No |
| `medical_and_care_establishment_nhs` | `bigint` | Count or numeric value for medical and care establishment nhs in the represented area. | statistical_value | Yes | No | No |
| `med_care_estab_nhs_general_hospital` | `bigint` | Count or numeric value for med care estab nhs general hospital in the represented area. | statistical_value | Yes | No | No |
| `med_care_estab_nhs_mental_health_hospital_or_unit` | `bigint` | Count or numeric value for med care estab nhs mental health hospital or unit in the represented area. | statistical_value | Yes | No | No |
| `medical_and_care_establishment_nhs_other_hospital` | `bigint` | Count or numeric value for medical and care establishment nhs other hospital in the represented area. | statistical_value | Yes | No | No |
| `medical_and_care_establishment_local_authority` | `bigint` | Count or numeric value for medical and care establishment local authority in the represented area. | statistical_value | Yes | No | No |
| `med_care_estab_local_authority_children_s_home` | `bigint` | Count or numeric value for med care estab local authority children s home in the represented area. | statistical_value | Yes | No | No |
| `med_care_estab_la_care_home_w_nursing` | `bigint` | Count or numeric value for med care estab la care home w nursing in the represented area. | statistical_value | Yes | No | No |
| `med_care_estab_la_care_home_no_nursing` | `bigint` | Count or numeric value for med care estab la care home number nursing in the represented area. | statistical_value | Yes | No | No |
| `med_care_estab_local_authority_other_home` | `bigint` | Count or numeric value for med care estab local authority other home in the represented area. | statistical_value | Yes | No | No |
| `med_care_estab_rsl_or_housing_assoc` | `bigint` | Count or numeric value for med care estab rsl or housing assoc in the represented area. | statistical_value | Yes | No | No |
| `med_care_estab_rsl_or_ha_home_hostel` | `bigint` | Count or numeric value for med care estab rsl or ha home hostel in the represented area. | statistical_value | Yes | No | No |
| `medical_and_care_establishment_other` | `bigint` | Count or numeric value for medical and care establishment other in the represented area. | statistical_value | Yes | No | No |
| `med_care_estab_other_care_home_with_nursing` | `bigint` | Count or numeric value for med care estab other care home with nursing in the represented area. | statistical_value | Yes | No | No |
| `med_care_estab_other_care_home_without_nursing` | `bigint` | Count or numeric value for med care estab other care home without nursing in the represented area. | statistical_value | Yes | No | No |
| `med_care_estab_other_children_s_home` | `bigint` | Count or numeric value for med care estab other children s home in the represented area. | statistical_value | Yes | No | No |
| `med_care_estab_other_mental_health_hospital_or_unit` | `bigint` | Count or numeric value for med care estab other mental health hospital or unit in the represented area. | statistical_value | Yes | No | No |
| `medical_and_care_establishment_other_hospital` | `bigint` | Count or numeric value for medical and care establishment other hospital in the represented area. | statistical_value | Yes | No | No |
| `medical_and_care_establishment_other_establishment` | `bigint` | Count or numeric value for medical and care establishment other establishment in the represented area. | statistical_value | Yes | No | No |
| `other_establishment` | `bigint` | Count or numeric value for other establishment in the represented area. | statistical_value | Yes | No | No |
| `other_establishment_defence` | `bigint` | Count or numeric value for other establishment defence in the represented area. | statistical_value | Yes | No | No |
| `other_establishment_prison_service` | `bigint` | Count or numeric value for other establishment prison service in the represented area. | statistical_value | Yes | No | No |
| `other_establishment_approved_premises` | `bigint` | Count or numeric value for other establishment approved premises in the represented area. | statistical_value | Yes | No | No |
| `other_estab_detention_centres_and_other_detention` | `bigint` | Count or numeric value for other estab detention centres and other detention in the represented area. | statistical_value | Yes | No | No |
| `other_establishment_education` | `bigint` | Count or numeric value for other establishment education in the represented area. | statistical_value | Yes | No | No |
| `other_estab_hotel_guest_house_b_or_youth_hostel` | `bigint` | Count or numeric value for other estab hotel guest house b or youth hostel in the represented area. | statistical_value | Yes | No | No |
| `other_estab_hostel_or_temp_shelter` | `bigint` | Count or numeric value for other estab hostel or temp shelter in the represented area. | statistical_value | Yes | No | No |
| `other_establishment_holiday_accommodation` | `bigint` | Count or numeric value for other establishment holiday accommodation in the represented area. | statistical_value | Yes | No | No |
| `other_estab_other_travel_or_temporary_accommodation` | `bigint` | Count or numeric value for other estab other travel or temporary accommodation in the represented area. | statistical_value | Yes | No | No |
| `other_establishment_religious` | `bigint` | Count or numeric value for other establishment religious in the represented area. | statistical_value | Yes | No | No |
| `other_estab_staff_or_worker_accommodation_or_other` | `bigint` | Count or numeric value for other estab staff or worker accommodation or other in the represented area. | statistical_value | Yes | No | No |
| `establishment_not_stated` | `bigint` | Count or numeric value for establishment not stated in the represented area. | statistical_value | Yes | No | No |
| `num_bedrooms_total` | `bigint` | Count or numeric value for num bedrooms total in the represented area. | statistical_value | Yes | No | No |
| `t_1_bedroom` | `bigint` | Count or numeric value for t 1 bedroom in the represented area. | statistical_value | Yes | No | No |
| `t_2_bedrooms` | `bigint` | Count or numeric value for t 2 bedrooms in the represented area. | statistical_value | Yes | No | No |
| `t_3_bedrooms` | `bigint` | Count or numeric value for t 3 bedrooms in the represented area. | statistical_value | Yes | No | No |
| `t_4_or_more_bedrooms` | `bigint` | Count or numeric value for t 4 or more bedrooms in the represented area. | statistical_value | Yes | No | No |
| `number_of_rooms_total` | `bigint` | Count or numeric value for number of rooms total in the represented area. | statistical_value | Yes | No | No |
| `t_1_room` | `bigint` | Count or numeric value for t 1 room in the represented area. | statistical_value | Yes | No | No |
| `t_2_rooms` | `bigint` | Count or numeric value for t 2 rooms in the represented area. | statistical_value | Yes | No | No |
| `t_3_rooms` | `bigint` | Count or numeric value for t 3 rooms in the represented area. | statistical_value | Yes | No | No |
| `t_4_rooms` | `bigint` | Count or numeric value for t 4 rooms in the represented area. | statistical_value | Yes | No | No |
| `t_5_rooms` | `bigint` | Count or numeric value for t 5 rooms in the represented area. | statistical_value | Yes | No | No |
| `t_6_rooms` | `bigint` | Count or numeric value for t 6 rooms in the represented area. | statistical_value | Yes | No | No |
| `t_7_rooms` | `bigint` | Count or numeric value for t 7 rooms in the represented area. | statistical_value | Yes | No | No |
| `t_8_rooms` | `bigint` | Count or numeric value for t 8 rooms in the represented area. | statistical_value | Yes | No | No |
| `t_9_or_more_rooms` | `bigint` | Count or numeric value for t 9 or more rooms in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_bedrooms_total` | `bigint` | Count or numeric value for occupancy rating bedrooms total in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_bedrooms_2_or_more` | `bigint` | Count or numeric value for occupancy rating of bedrooms 2 or more in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_bedrooms_1` | `bigint` | Count or numeric value for occupancy rating of bedrooms 1 in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_bedrooms_0` | `bigint` | Count or numeric value for occupancy rating of bedrooms 0 in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_bedrooms_1_2` | `bigint` | Count or numeric value for occupancy rating of bedrooms 1 2 in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_bedrooms_2_or_less` | `bigint` | Count or numeric value for occupancy rating of bedrooms 2 or less in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_rooms_total` | `bigint` | Count or numeric value for occupancy rating rooms total in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_rooms_2_or_more` | `bigint` | Count or numeric value for occupancy rating of rooms 2 or more in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_rooms_1` | `bigint` | Count or numeric value for occupancy rating of rooms 1 in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_rooms_0` | `bigint` | Count or numeric value for occupancy rating of rooms 0 in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_rooms_1_2` | `bigint` | Count or numeric value for occupancy rating of rooms 1 2 in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_rooms_2_or_less` | `bigint` | Count or numeric value for occupancy rating of rooms 2 or less in the represented area. | statistical_value | Yes | No | No |
| `tenure_total` | `bigint` | Count or numeric value for tenure total in the represented area. | statistical_value | Yes | No | No |
| `owned` | `bigint` | Count or numeric value for owned in the represented area. | statistical_value | Yes | No | No |
| `owned_owns_outright` | `bigint` | Count or numeric value for owned owns outright in the represented area. | statistical_value | Yes | No | No |
| `owned_owns_with_a_mortgage_or_loan` | `bigint` | Count or numeric value for owned owns with a mortgage or loan in the represented area. | statistical_value | Yes | No | No |
| `shared_ownership` | `bigint` | Count or numeric value for shared ownership in the represented area. | statistical_value | Yes | No | No |
| `shared_ownership_shared_ownership` | `bigint` | Count or numeric value for shared ownership shared ownership in the represented area. | statistical_value | Yes | No | No |
| `social_rented` | `bigint` | Count or numeric value for social rented in the represented area. | statistical_value | Yes | No | No |
| `social_rented_council_or_la` | `bigint` | Count or numeric value for social rented council or la in the represented area. | statistical_value | Yes | No | No |
| `social_rented_other_social_rented` | `bigint` | Count or numeric value for social rented other social rented in the represented area. | statistical_value | Yes | No | No |
| `private_rented` | `bigint` | Count or numeric value for private rented in the represented area. | statistical_value | Yes | No | No |
| `private_rented_private_landlord_or_letting_agency` | `bigint` | Count or numeric value for private rented private landlord or letting agency in the represented area. | statistical_value | Yes | No | No |
| `private_rented_other_private_rented` | `bigint` | Count or numeric value for private rented other private rented in the represented area. | statistical_value | Yes | No | No |
| `lives_rent_free` | `bigint` | Count or numeric value for lives rent free in the represented area. | statistical_value | Yes | No | No |
| `second_address_type_total` | `bigint` | Count or numeric value for second address type total in the represented area. | statistical_value | Yes | No | No |
| `armed_forces_base_address` | `bigint` | Count or numeric value for armed forces base address in the represented area. | statistical_value | Yes | No | No |
| `another_address_when_working_away_from_home` | `bigint` | Count or numeric value for another address when working away from home in the represented area. | statistical_value | Yes | No | No |
| `holiday_home` | `bigint` | Count or numeric value for holiday home in the represented area. | statistical_value | Yes | No | No |
| `student_s_term_time_address` | `bigint` | Count or numeric value for student s term time address in the represented area. | statistical_value | Yes | No | No |
| `student_s_home_address` | `bigint` | Count or numeric value for student s home address in the represented area. | statistical_value | Yes | No | No |
| `another_parent_or_guardian_s_address` | `bigint` | Count or numeric value for another parent or guardian s address in the represented area. | statistical_value | Yes | No | No |
| `partner_s_address` | `bigint` | Count or numeric value for partner s address in the represented area. | statistical_value | Yes | No | No |
| `other` | `bigint` | Count or numeric value for other in the represented area. | statistical_value | Yes | No | No |
| `not_specified` | `bigint` | Count or numeric value for not specified in the represented area. | statistical_value | Yes | No | No |
| `second_address_total` | `bigint` | Count or numeric value for second address total in the represented area. | statistical_value | Yes | No | No |
| `no_second_address` | `bigint` | Count or numeric value for number second address in the represented area. | statistical_value | Yes | No | No |
| `is_in_the_uk` | `bigint` | Count or numeric value for is in the uk in the represented area. | statistical_value | Yes | No | No |
| `is_outside_the_uk` | `bigint` | Count or numeric value for is outside the uk in the represented area. | statistical_value | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
