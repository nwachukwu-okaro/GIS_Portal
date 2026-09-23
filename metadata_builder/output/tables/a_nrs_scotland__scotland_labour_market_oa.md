# Scotland Labour Market Oa

## Overview

- **Identifier:** `a_nrs_scotland/scotland_labour_market_oa`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `scotland_labour_market_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 46363
- **Columns:** 344
- **Metadata status:** source_mapped

## Description

Scotland Labour Market Oa is an authoritative dataset published by National Records of Scotland. It contains records relating to scotland labour market oa.

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
| `all_people_aged_16_and_over_econ_act` | `bigint` | Recorded census measure for the category "all people aged 16 and over econ act" in the represented area. Units and population base require the source table. |
| `economically_active_excluding_full_time_students_total` | `double precision` |  |
| `econ_active_excl_employee` | `double precision` |  |
| `econ_active_excl_emp_pt` | `double precision` |  |
| `econ_active_excl_emp_ft` | `double precision` |  |
| `econ_active_excl_se_w_emp` | `double precision` |  |
| `econ_active_excl_se_w_emp_pt` | `double precision` |  |
| `econ_active_excl_se_w_emp_ft` | `double precision` |  |
| `econ_active_excl_se_no_emp` | `double precision` |  |
| `econ_active_excl_se_no_emp_pt` | `double precision` |  |
| `econ_active_excl_se_no_emp_ft` | `double precision` |  |
| `econ_active_excl_unemployed` | `double precision` |  |
| `economically_active_full_time_students_total_econ_act` | `double precision` |  |
| `econ_active_stu_employee_econ_act` | `double precision` |  |
| `econ_active_stu_emp_pt` | `double precision` |  |
| `econ_active_stu_emp_ft` | `double precision` |  |
| `econ_active_stu_se_w_emp` | `double precision` |  |
| `econ_active_stu_se_w_emp_pt` | `double precision` |  |
| `econ_active_stu_se_w_emp_ft` | `double precision` |  |
| `econ_active_stu_se_no_emp` | `double precision` |  |
| `econ_active_stu_se_no_emp_pt_total` | `double precision` |  |
| `econ_active_stu_se_no_emp_ft_total` | `double precision` |  |
| `econ_active_stu_unemployed` | `double precision` |  |
| `economically_inactive_total_econ_act` | `double precision` |  |
| `economically_inactive_retired_econ_act` | `double precision` |  |
| `economically_inactive_student_econ_act` | `double precision` |  |
| `econ_inactive_home_family_econ_act` | `double precision` |  |
| `econ_inactive_lt_sick_econ_act` | `double precision` |  |
| `economically_inactive_other_econ_act` | `double precision` |  |
| `all_household_reference_persons_aged_16_and_over` | `bigint` |  |
| `econ_active_stu_total_econ_act_hrp` | `double precision` |  |
| `econ_active_stu_employee_econ_act_hrp` | `double precision` |  |
| `econ_active_excl_stu_emp_pt` | `double precision` |  |
| `econ_active_excl_stu_emp_ft` | `double precision` |  |
| `econ_active_excl_stu_se_w_emp` | `double precision` |  |
| `econ_active_excl_stu_se_w_emp_pt` | `double precision` |  |
| `econ_active_excl_stu_se_w_emp_ft` | `double precision` |  |
| `econ_active_excl_stu_se_no_emp` | `double precision` |  |
| `econ_active_excl_stu_se_no_emp_pt` | `double precision` |  |
| `econ_active_excl_stu_se_no_emp_ft` | `double precision` |  |
| `econ_active_excl_stu_unemployed` | `double precision` |  |
| `economically_active_full_time_student_total` | `double precision` |  |
| `economically_active_full_time_student_employee_total` | `double precision` |  |
| `econ_active_stu_employee_part_time` | `double precision` |  |
| `econ_active_stu_employee_full_time` | `double precision` |  |
| `econ_active_stu_self_employed_with_employees_total` | `double precision` |  |
| `econ_active_stu_self_employed_with_employees_part_time` | `double precision` |  |
| `econ_active_stu_self_employed_with_employees_full_time` | `double precision` |  |
| `econ_active_stu_self_employed_without_employees_total` | `double precision` |  |
| `econ_active_stu_se_no_emp_pt_hrp` | `double precision` |  |
| `econ_active_stu_se_no_emp_ft_hrp` | `double precision` |  |
| `econ_active_stu_unemployed_available_for_work` | `double precision` |  |
| `economically_inactive_total_econ_act_hrp` | `double precision` |  |
| `economically_inactive_retired_econ_act_hrp` | `double precision` |  |
| `economically_inactive_student_econ_act_hrp` | `double precision` |  |
| `econ_inactive_home_family_econ_act_hrp` | `double precision` |  |
| `econ_inactive_lt_sick_econ_act_hrp` | `double precision` |  |
| `economically_inactive_other_econ_act_hrp` | `double precision` |  |
| `all_in_employment_hrs_worked` | `double precision` |  |
| `t_0_to_15_hours_hrs_worked` | `double precision` |  |
| `t_16_to_30_hours_hrs_worked` | `double precision` |  |
| `t_31_to_48_hours_hrs_worked` | `double precision` |  |
| `t_49_or_more_hours_hrs_worked` | `double precision` |  |
| `all_in_employment_hrs_worked_age` | `double precision` |  |
| `all_in_employment_16_24` | `double precision` |  |
| `all_in_employment_25_34` | `double precision` |  |
| `all_in_employment_35_49` | `double precision` |  |
| `all_in_employment_50_64` | `double precision` |  |
| `all_in_employment_65_plus` | `double precision` |  |
| `t_0_to_15_hours_hrs_worked_age` | `double precision` |  |
| `t_0_to_15_hours_16_24` | `double precision` |  |
| `t_0_to_15_hours_25_34` | `double precision` |  |
| `t_0_to_15_hours_35_49` | `double precision` |  |
| `t_0_to_15_hours_50_64` | `double precision` |  |
| `t_0_to_15_hours_65_plus` | `double precision` |  |
| `t_16_to_30_hours_hrs_worked_age` | `double precision` |  |
| `t_16_to_30_hours_16_24` | `double precision` |  |
| `t_16_to_30_hours_25_34` | `double precision` |  |
| `t_16_to_30_hours_35_49` | `double precision` |  |
| `t_16_to_30_hours_50_64` | `double precision` |  |
| `t_16_to_30_hours_65_plus` | `double precision` |  |
| `t_31_to_48_hours_hrs_worked_age` | `double precision` |  |
| `t_31_to_48_hours_16_24` | `double precision` |  |
| `t_31_to_48_hours_25_34` | `double precision` |  |
| `t_31_to_48_hours_35_49` | `double precision` |  |
| `t_31_to_48_hours_50_64` | `double precision` |  |
| `t_31_to_48_hours_65_plus` | `double precision` |  |
| `t_49_or_more_hours_hrs_worked_age` | `double precision` |  |
| `t_49_or_more_hours_16_24` | `double precision` |  |
| `t_49_or_more_hours_25_34` | `double precision` |  |
| `t_49_or_more_hours_35_49` | `double precision` |  |
| `t_49_or_more_hours_50_64` | `double precision` |  |
| `t_49_or_more_hours_65_plus` | `double precision` |  |
| `all_in_employment_industry` | `double precision` |  |
| `agriculture_forestry_fishing` | `double precision` |  |
| `mining_and_quarrying` | `double precision` |  |
| `manufacturing` | `double precision` |  |
| `electricity_gas_steam_and_air_conditioning_supply` | `double precision` |  |
| `water_sewage_waste_mgmt` | `double precision` |  |
| `construction` | `double precision` |  |
| `wholesale_retail_motor` | `double precision` |  |
| `transport_and_storage` | `double precision` |  |
| `accommodation_and_food_service_activities` | `double precision` |  |
| `information_and_communication` | `double precision` |  |
| `financial_and_insurance_activities` | `double precision` |  |
| `real_estate_activities` | `double precision` |  |
| `professional_scientific_and_technical_activities` | `double precision` |  |
| `administrative_and_support_service_activities` | `double precision` |  |
| `public_admin_defence` | `double precision` |  |
| `education` | `double precision` |  |
| `human_health_and_social_work_activities` | `double precision` |  |
| `arts_entertainment_and_recreation` | `double precision` |  |
| `other_service_activities` | `double precision` |  |
| `hh_employer_activities` | `double precision` |  |
| `extra_territorial_orgs` | `double precision` |  |
| `all_in_employment_occupation` | `double precision` |  |
| `managers_directors_and_senior_officials_total` | `double precision` |  |
| `corporate_managers_and_directors` | `double precision` |  |
| `other_managers_and_proprietors` | `double precision` |  |
| `professional_occupations_total` | `double precision` |  |
| `science_tech_professionals` | `double precision` |  |
| `health_professionals` | `double precision` |  |
| `teaching_and_educational_professionals` | `double precision` |  |
| `business_media_and_public_service_professionals` | `double precision` |  |
| `associate_professional_and_technical_occupations_total` | `double precision` |  |
| `science_tech_assoc_prof` | `double precision` |  |
| `health_and_social_care_associate_professionals` | `double precision` |  |
| `protective_service_occupations` | `double precision` |  |
| `culture_media_and_sports_occupations` | `double precision` |  |
| `business_and_public_service_associate_professionals` | `double precision` |  |
| `administrative_and_secretarial_occupations_total` | `double precision` |  |
| `administrative_occupations` | `double precision` |  |
| `secretarial_and_related_occupations` | `double precision` |  |
| `skilled_trade_occupations_total` | `double precision` |  |
| `skilled_agriculture_and_related_trades` | `double precision` |  |
| `skilled_metal_electrical_and_electronic_trades` | `double precision` |  |
| `skilled_construction_and_building_trades` | `double precision` |  |
| `textiles_printing_and_other_skilled_trades` | `double precision` |  |
| `caring_leisure_and_other_service_occupations_total` | `double precision` |  |
| `caring_personal_service_occupations` | `double precision` |  |
| `leisure_travel_and_related_personal_service` | `double precision` |  |
| `community_and_civil_enforcement_occupations` | `double precision` |  |
| `sales_and_customer_service_occupations_total` | `double precision` |  |
| `sales_occupations` | `double precision` |  |
| `customer_service_occupations` | `double precision` |  |
| `process_plant_and_machine_operatives_total` | `double precision` |  |
| `process_plant_and_machine_operatives` | `double precision` |  |
| `transport_and_mobile_machine_drivers_and_operatives` | `double precision` |  |
| `elementary_occupations_total` | `double precision` |  |
| `elementary_trades_and_related_occupations` | `double precision` |  |
| `elementary_administration_and_service_occupations` | `double precision` |  |
| `all_people_aged_16_and_over_ns_sec` | `bigint` | Recorded census measure for the category "all people aged 16 and over ns sec" in the represented area. Units and population base require the source table. |
| `l1_employers_in_large_establishments` | `double precision` |  |
| `l2_higher_managerial_and_administrative_occupations` | `double precision` |  |
| `l3_higher_professional_occupations` | `double precision` |  |
| `l4_lower_professional_and_higher_technical_occupations` | `double precision` |  |
| `l5_lower_managerial_and_administrative_occupations` | `double precision` |  |
| `l6_higher_supervisory_occupations` | `double precision` |  |
| `l7_intermediate_occupations` | `double precision` |  |
| `l8_employers_in_small_establishments` | `double precision` |  |
| `l9_own_account_workers` | `double precision` |  |
| `l10_lower_supervisory_occupations` | `double precision` |  |
| `l11_lower_technical_occupations` | `double precision` |  |
| `l12_semi_routine_occupations` | `double precision` |  |
| `l13_routine_occupations` | `double precision` |  |
| `l14_1_never_worked` | `double precision` |  |
| `l14_2_long_term_unemployed` | `double precision` |  |
| `l15_full_time_students` | `double precision` |  |
| `all_employed_incl_students_travel_work` | `double precision` |  |
| `work_mainly_at_or_from_home_total` | `double precision` |  |
| `driving_a_car_or_van_travel_work` | `double precision` |  |
| `passenger_in_a_car_or_van_travel_work` | `double precision` |  |
| `taxi_or_private_hire` | `double precision` |  |
| `motorcycle_scooter_or_moped` | `double precision` |  |
| `on_foot_travel_work` | `double precision` |  |
| `bicycle_travel_work` | `double precision` |  |
| `bus_minibus_or_coach_travel_work` | `double precision` |  |
| `train` | `double precision` |  |
| `underground_subway_or_tram` | `double precision` |  |
| `other` | `double precision` |  |
| `all_employed_incl_students_travel_work_age` | `double precision` |  |
| `all_employed_incl_students_16_24_travel_work_age` | `double precision` |  |
| `all_employed_incl_students_25_34_travel_work_age` | `double precision` |  |
| `all_employed_incl_students_35_49_travel_work_age` | `double precision` |  |
| `all_employed_incl_students_50_64_travel_work_age` | `double precision` |  |
| `all_employed_incl_students_65_plus_travel_work_age` | `double precision` |  |
| `work_mainly_at_or_from_home_age` | `double precision` |  |
| `work_mainly_at_or_from_home_16_24` | `double precision` |  |
| `work_mainly_at_or_from_home_25_34` | `double precision` |  |
| `work_mainly_at_or_from_home_35_49` | `double precision` |  |
| `work_mainly_at_or_from_home_50_64` | `double precision` |  |
| `work_mainly_at_or_from_home_65_plus` | `double precision` |  |
| `driving_a_car_or_van_travel_work_age` | `double precision` |  |
| `driving_a_car_or_van_16_24` | `double precision` |  |
| `driving_a_car_or_van_25_34` | `double precision` |  |
| `driving_a_car_or_van_35_49` | `double precision` |  |
| `driving_a_car_or_van_50_64` | `double precision` |  |
| `driving_a_car_or_van_65_plus` | `double precision` |  |
| `passenger_in_a_car_or_van_travel_work_age` | `double precision` |  |
| `passenger_in_a_car_or_van_16_24` | `double precision` |  |
| `passenger_in_a_car_or_van_25_34` | `double precision` |  |
| `passenger_in_a_car_or_van_35_49` | `double precision` |  |
| `passenger_in_a_car_or_van_50_64` | `double precision` |  |
| `passenger_in_a_car_or_van_65_plus` | `double precision` |  |
| `on_foot_travel_work_age` | `double precision` |  |
| `on_foot_16_24` | `double precision` |  |
| `on_foot_25_34` | `double precision` |  |
| `on_foot_35_49` | `double precision` |  |
| `on_foot_50_64` | `double precision` |  |
| `on_foot_65_plus` | `double precision` |  |
| `bicycle_travel_work_age` | `double precision` |  |
| `bicycle_16_24` | `double precision` |  |
| `bicycle_25_34` | `double precision` |  |
| `bicycle_35_49` | `double precision` |  |
| `bicycle_50_64` | `double precision` |  |
| `bicycle_65_plus` | `double precision` |  |
| `bus_minibus_or_coach_travel_work_age` | `double precision` |  |
| `bus_minibus_or_coach_16_24` | `double precision` |  |
| `bus_minibus_or_coach_25_34` | `double precision` |  |
| `bus_minibus_or_coach_35_49` | `double precision` |  |
| `bus_minibus_or_coach_50_64` | `double precision` |  |
| `bus_minibus_or_coach_65_plus` | `double precision` |  |
| `train_underground_subway_or_tram` | `double precision` |  |
| `train_underground_subway_or_tram_16_24` | `double precision` |  |
| `train_underground_subway_or_tram_25_34` | `double precision` |  |
| `train_underground_subway_or_tram_35_49` | `double precision` |  |
| `train_underground_subway_or_tram_50_64` | `double precision` |  |
| `train_underground_subway_or_tram_65_plus` | `double precision` |  |
| `taxi_motorcycle_and_all_other_methods_of_travel_to_work` | `double precision` |  |
| `taxi_moped_other_travel_16_24` | `double precision` |  |
| `taxi_moped_other_travel_25_34` | `double precision` |  |
| `taxi_moped_other_travel_35_49` | `double precision` |  |
| `taxi_moped_other_travel_50_64` | `double precision` |  |
| `taxi_moped_other_travel_65_plus` | `double precision` |  |
| `all_occupied_households` | `bigint` | Recorded census measure for the category "all occupied households" in the represented area. Units and population base require the source table. |
| `no_person_working_or_studying_in_the_household` | `double precision` |  |
| `one_person_working_or_studying_in_the_household_total` | `double precision` |  |
| `t_1_working_studying_car_driver` | `double precision` |  |
| `t_1_working_other_travel` | `double precision` |  |
| `t_1_working_at_home` | `double precision` |  |
| `two_people_working_or_studying_in_the_household_total` | `double precision` |  |
| `t_2_working_both_car_drivers` | `double precision` |  |
| `t_2_working_both_other_travel` | `double precision` |  |
| `t_2_working_both_home` | `double precision` |  |
| `t_2_working_studying_one_car_driver_one_other_method` | `double precision` |  |
| `t_2_working_studying_one_car_driver_one_working_at_home` | `double precision` |  |
| `t_2_working_one_other_one_home` | `double precision` |  |
| `t_3plus_working_studying_total` | `double precision` |  |
| `t_3plus_working_all_car_drivers` | `double precision` |  |
| `t_3plus_working_studying_all_other_travel` | `double precision` |  |
| `t_3plus_working_all_home` | `double precision` |  |
| `t_3plus_mix_car_other` | `double precision` |  |
| `t_3plus_mix_car_home` | `double precision` |  |
| `t_3plus_working_mix_other_home` | `double precision` |  |
| `t_3plus_mix_car_other_home` | `double precision` |  |
| `all_employed_incl_students_dist_work` | `double precision` |  |
| `mainly_work_from_home_total` | `double precision` |  |
| `less_than_2km_dist_work` | `double precision` |  |
| `t_2km_to_less_than_5km_dist_work` | `double precision` |  |
| `t_5km_to_less_than_10km_dist_work` | `double precision` |  |
| `t_10km_to_less_than_20km_dist_work` | `double precision` |  |
| `t_20km_to_less_than_30km_dist_work` | `double precision` |  |
| `t_30km_to_less_than_40km_dist_work` | `double precision` |  |
| `t_40km_to_less_than_60km_dist_work` | `double precision` |  |
| `t_60km_and_over_dist_work` | `double precision` |  |
| `other_no_fixed_work_outside_uk_total` | `double precision` |  |
| `all_employed_incl_students_dist_work_age` | `double precision` |  |
| `all_employed_incl_students_16_24_dist_work_age` | `double precision` |  |
| `all_employed_incl_students_25_34_dist_work_age` | `double precision` |  |
| `all_employed_incl_students_35_49_dist_work_age` | `double precision` |  |
| `all_employed_incl_students_50_64_dist_work_age` | `double precision` |  |
| `all_employed_incl_students_65_plus_dist_work_age` | `double precision` |  |
| `mainly_work_from_home_age` | `double precision` |  |
| `mainly_work_from_home_16_24` | `double precision` |  |
| `mainly_work_from_home_25_34` | `double precision` |  |
| `mainly_work_from_home_35_49` | `double precision` |  |
| `mainly_work_from_home_50_64` | `double precision` |  |
| `mainly_work_from_home_65_plus` | `double precision` |  |
| `less_than_2km_dist_work_age` | `double precision` |  |
| `less_than_2km_16_24` | `double precision` |  |
| `less_than_2km_25_34` | `double precision` |  |
| `less_than_2km_35_49` | `double precision` |  |
| `less_than_2km_50_64` | `double precision` |  |
| `less_than_2km_65_plus` | `double precision` |  |
| `t_2km_to_less_than_5km_dist_work_age` | `double precision` |  |
| `t_2km_to_less_than_5km_16_24` | `double precision` |  |
| `t_2km_to_less_than_5km_25_34` | `double precision` |  |
| `t_2km_to_less_than_5km_35_49` | `double precision` |  |
| `t_2km_to_less_than_5km_50_64` | `double precision` |  |
| `t_2km_to_less_than_5km_65_plus` | `double precision` |  |
| `t_5km_to_less_than_10km_dist_work_age` | `double precision` |  |
| `t_5km_to_less_than_10km_16_24` | `double precision` |  |
| `t_5km_to_less_than_10km_25_34` | `double precision` |  |
| `t_5km_to_less_than_10km_35_49` | `double precision` |  |
| `t_5km_to_less_than_10km_50_64` | `double precision` |  |
| `t_5km_to_less_than_10km_65_plus` | `double precision` |  |
| `t_10km_to_less_than_20km_dist_work_age` | `double precision` |  |
| `t_10km_to_less_than_20km_16_24` | `double precision` |  |
| `t_10km_to_less_than_20km_25_34` | `double precision` |  |
| `t_10km_to_less_than_20km_35_49` | `double precision` |  |
| `t_10km_to_less_than_20km_50_64` | `double precision` |  |
| `t_10km_to_less_than_20km_65_plus` | `double precision` |  |
| `t_20km_to_less_than_30km_dist_work_age` | `double precision` |  |
| `t_20km_to_less_than_30km_16_24` | `double precision` |  |
| `t_20km_to_less_than_30km_25_34` | `double precision` |  |
| `t_20km_to_less_than_30km_35_49` | `double precision` |  |
| `t_20km_to_less_than_30km_50_64` | `double precision` |  |
| `t_20km_to_less_than_30km_65_plus` | `double precision` |  |
| `t_30km_to_less_than_40km_dist_work_age` | `double precision` |  |
| `t_30km_to_less_than_40km_16_24` | `double precision` |  |
| `t_30km_to_less_than_40km_25_34` | `double precision` |  |
| `t_30km_to_less_than_40km_35_49` | `double precision` |  |
| `t_30km_to_less_than_40km_50_64` | `double precision` |  |
| `t_30km_to_less_than_40km_65_plus` | `double precision` |  |
| `t_40km_to_less_than_60km_dist_work_age` | `double precision` |  |
| `t_40km_to_less_than_60km_16_24` | `double precision` |  |
| `t_40km_to_less_than_60km_25_34` | `double precision` |  |
| `t_40km_to_less_than_60km_35_49` | `double precision` |  |
| `t_40km_to_less_than_60km_50_64` | `double precision` |  |
| `t_40km_to_less_than_60km_65_plus` | `double precision` |  |
| `t_60km_and_over_dist_work_age` | `double precision` |  |
| `t_60km_and_over_16_24` | `double precision` |  |
| `t_60km_and_over_25_34` | `double precision` |  |
| `t_60km_and_over_35_49` | `double precision` |  |
| `t_60km_and_over_50_64` | `double precision` |  |
| `t_60km_and_over_65_plus` | `double precision` |  |
| `other_no_fixed_work_outside_uk_age` | `double precision` |  |
| `other_no_fixed_work_outside_uk_16_24` | `double precision` |  |
| `other_no_fixed_work_outside_uk_25_34` | `double precision` |  |
| `other_no_fixed_work_outside_uk_35_49` | `double precision` |  |
| `other_no_fixed_work_outside_uk_50_64` | `double precision` |  |
| `other_no_fixed_work_outside_uk_65_plus` | `double precision` |  |
| `all_studying` | `double precision` |  |
| `mainly_study_from_home` | `double precision` |  |
| `less_than_2km_dist_study` | `double precision` |  |
| `t_2km_to_less_than_5km_dist_study` | `double precision` |  |
| `t_5km_to_less_than_10km_dist_study` | `double precision` |  |
| `t_10km_to_less_than_20km_dist_study` | `double precision` |  |
| `t_20km_to_less_than_30km_dist_study` | `double precision` |  |
| `t_30km_to_less_than_40km_dist_study` | `double precision` |  |
| `t_40km_to_less_than_60km_dist_study` | `double precision` |  |
| `t_60km_and_over_dist_study` | `double precision` |  |
| `no_fixed_study_outside_uk` | `double precision` |  |
