# Scotland Labour Market Intzones

## Overview

- **Identifier:** `a_nrs_scotland/scotland_labour_market_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `scotland_labour_market_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1279
- **Columns:** 214
- **Metadata status:** source_mapped

## Description

Scotland Labour Market Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to scotland labour market intzones.

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
| `all_people_16plus_econ_activity` | `bigint` | Recorded census measure for the category "all people 16plus econ activity" in the represented area. Units and population base require the source table. |
| `all_econ_active_excl_stu_total` | `bigint` |  |
| `all_econ_active_excl_stu_emp_total` | `bigint` |  |
| `all_econ_active_excl_stu_emp_pt` | `bigint` |  |
| `all_econ_active_excl_stu_emp_ft` | `bigint` |  |
| `all_econ_active_excl_stu_se_w_emp_tot` | `bigint` |  |
| `all_econ_active_excl_stu_se_w_emp_pt` | `bigint` |  |
| `all_econ_active_excl_stu_se_w_emp_ft` | `bigint` |  |
| `all_econ_active_excl_stu_se_no_emp_tot` | `bigint` |  |
| `all_econ_active_excl_stu_se_no_emp_pt` | `bigint` |  |
| `all_econ_active_excl_stu_se_no_emp_ft` | `bigint` |  |
| `all_econ_active_excl_stu_unemployed` | `bigint` |  |
| `all_econ_active_stu_total` | `bigint` |  |
| `all_econ_active_stu_emp_total` | `bigint` |  |
| `all_econ_active_stu_emp_pt` | `bigint` |  |
| `all_econ_active_stu_emp_ft` | `bigint` |  |
| `all_econ_active_stu_se_w_emp_tot` | `bigint` |  |
| `all_econ_active_stu_se_w_emp_pt` | `bigint` |  |
| `all_econ_active_stu_se_w_emp_ft` | `bigint` |  |
| `all_econ_active_stu_se_no_emp_tot` | `bigint` |  |
| `all_econ_active_stu_se_no_emp_pt` | `bigint` |  |
| `all_econ_active_stu_se_no_emp_ft` | `bigint` |  |
| `all_econ_active_stu_unemployed` | `bigint` |  |
| `all_econ_inactive_total` | `bigint` |  |
| `all_econ_inactive_retired` | `bigint` |  |
| `all_econ_inactive_student` | `bigint` |  |
| `all_econ_inactive_home_family` | `bigint` |  |
| `all_econ_inactive_lt_sick` | `bigint` |  |
| `all_econ_inactive_other` | `bigint` |  |
| `all_students_16plus` | `bigint` |  |
| `stu_econ_active_total` | `bigint` |  |
| `stu_econ_active_emp_total` | `bigint` |  |
| `stu_econ_active_emp_pt` | `bigint` |  |
| `stu_econ_active_emp_ft` | `bigint` |  |
| `stu_econ_active_se_w_emp_tot` | `bigint` |  |
| `stu_econ_active_se_w_emp_pt` | `bigint` |  |
| `stu_econ_active_se_w_emp_ft` | `bigint` |  |
| `stu_econ_active_se_no_emp_tot` | `bigint` |  |
| `stu_econ_active_se_no_emp_pt` | `bigint` |  |
| `stu_econ_active_se_no_emp_ft` | `bigint` |  |
| `stu_econ_active_unemployed` | `bigint` |  |
| `econ_inactive` | `bigint` |  |
| `all_hrp_16plus` | `bigint` |  |
| `hrp_econ_active_excl_stu_total` | `bigint` |  |
| `hrp_econ_active_excl_stu_emp_total` | `bigint` |  |
| `hrp_econ_active_excl_stu_emp_pt` | `bigint` |  |
| `hrp_econ_active_excl_stu_emp_ft` | `bigint` |  |
| `hrp_econ_active_excl_stu_se_w_emp_tot` | `bigint` |  |
| `hrp_econ_active_excl_stu_se_w_emp_pt` | `bigint` |  |
| `hrp_econ_active_excl_stu_se_w_emp_ft` | `bigint` |  |
| `hrp_econ_active_excl_stu_se_no_emp_tot` | `bigint` |  |
| `hrp_econ_active_excl_stu_se_no_emp_pt` | `bigint` |  |
| `hrp_econ_active_excl_stu_se_no_emp_ft` | `bigint` |  |
| `hrp_econ_active_excl_stu_unemployed` | `bigint` |  |
| `hrp_econ_active_stu_total` | `bigint` |  |
| `hrp_econ_active_stu_emp_total` | `bigint` |  |
| `hrp_econ_active_stu_emp_pt` | `bigint` |  |
| `hrp_econ_active_stu_emp_ft` | `bigint` |  |
| `hrp_econ_active_stu_se_w_emp_tot` | `bigint` |  |
| `hrp_econ_active_stu_se_w_emp_pt` | `bigint` |  |
| `hrp_econ_active_stu_se_w_emp_ft` | `bigint` |  |
| `hrp_econ_active_stu_se_no_emp_tot` | `bigint` |  |
| `hrp_econ_active_stu_se_no_emp_pt` | `bigint` |  |
| `hrp_econ_active_stu_se_no_emp_ft` | `bigint` |  |
| `hrp_econ_active_stu_unemployed` | `bigint` |  |
| `hrp_econ_inactive_total` | `bigint` |  |
| `hrp_econ_inactive_retired` | `bigint` |  |
| `hrp_econ_inactive_student` | `bigint` |  |
| `hrp_econ_inactive_home_family` | `bigint` |  |
| `hrp_econ_inactive_lt_sick` | `bigint` |  |
| `hrp_econ_inactive_other` | `bigint` |  |
| `all_in_employment_hours` | `bigint` |  |
| `hours_0_15` | `bigint` |  |
| `hours_16_30` | `bigint` |  |
| `hours_31_48` | `bigint` |  |
| `hours_49plus` | `bigint` |  |
| `all_in_employment_industry` | `bigint` |  |
| `ind_agriculture` | `bigint` |  |
| `ind_mining_quarrying` | `bigint` |  |
| `ind_manufacturing` | `bigint` |  |
| `ind_electricity_gas` | `bigint` |  |
| `ind_water_waste` | `bigint` |  |
| `ind_construction` | `bigint` |  |
| `ind_wholesale_retail` | `bigint` |  |
| `ind_transport_storage` | `bigint` |  |
| `ind_accommodation_food` | `bigint` |  |
| `ind_information_comms` | `bigint` |  |
| `ind_financial_insurance` | `bigint` |  |
| `ind_real_estate` | `bigint` |  |
| `ind_professional_scientific` | `bigint` |  |
| `ind_admin_support` | `bigint` |  |
| `ind_public_admin_defence` | `bigint` |  |
| `ind_education` | `bigint` |  |
| `ind_health_social_work` | `bigint` |  |
| `ind_arts_entertainment` | `bigint` |  |
| `ind_other_services` | `bigint` |  |
| `ind_household_employers` | `bigint` |  |
| `ind_extra_territorial` | `bigint` |  |
| `all_in_employment_occupation` | `bigint` |  |
| `occ_managers_total` | `bigint` |  |
| `occ_corporate_managers` | `bigint` |  |
| `occ_other_managers` | `bigint` |  |
| `occ_professional_total` | `bigint` |  |
| `occ_science_eng_tech_prof` | `bigint` |  |
| `occ_health_prof` | `bigint` |  |
| `occ_teaching_prof` | `bigint` |  |
| `occ_business_public_prof` | `bigint` |  |
| `occ_assoc_prof_total` | `bigint` |  |
| `occ_science_eng_tech_assoc` | `bigint` |  |
| `occ_health_social_assoc` | `bigint` |  |
| `occ_protective_services` | `bigint` |  |
| `occ_culture_media_sports` | `bigint` |  |
| `occ_business_public_assoc` | `bigint` |  |
| `occ_admin_secretarial_total` | `bigint` |  |
| `occ_administrative` | `bigint` |  |
| `occ_secretarial` | `bigint` |  |
| `occ_skilled_trades_total` | `bigint` |  |
| `occ_skilled_agriculture` | `bigint` |  |
| `occ_skilled_metal_electrical` | `bigint` |  |
| `occ_skilled_construction` | `bigint` |  |
| `occ_textiles_printing` | `bigint` |  |
| `occ_caring_leisure_total` | `bigint` |  |
| `occ_caring_personal` | `bigint` |  |
| `occ_leisure_travel` | `bigint` |  |
| `occ_community_enforcement` | `bigint` |  |
| `occ_sales_customer_total` | `bigint` |  |
| `occ_sales` | `bigint` |  |
| `occ_customer_service` | `bigint` |  |
| `occ_process_plant_total` | `bigint` |  |
| `occ_process_plant` | `bigint` |  |
| `occ_transport_drivers` | `bigint` |  |
| `occ_elementary_total` | `bigint` |  |
| `occ_elementary_trades` | `bigint` |  |
| `occ_elementary_admin` | `bigint` |  |
| `all_occupied_hhs_ns_sec_hrp` | `bigint` |  |
| `hrp_ns_sec_l1_large_employers` | `bigint` |  |
| `hrp_ns_sec_l2_higher_mgr_admin` | `bigint` |  |
| `hrp_ns_sec_l3_higher_prof` | `bigint` |  |
| `hrp_ns_sec_l4_lower_prof_tech` | `bigint` |  |
| `hrp_ns_sec_l5_lower_mgr_admin` | `bigint` |  |
| `hrp_ns_sec_l6_higher_supervisory` | `bigint` |  |
| `hrp_ns_sec_l7_intermediate` | `bigint` |  |
| `hrp_ns_sec_l8_small_employers` | `bigint` |  |
| `hrp_ns_sec_l9_own_account` | `bigint` |  |
| `hrp_ns_sec_l10_lower_supervisory` | `bigint` |  |
| `hrp_ns_sec_l11_lower_tech` | `bigint` |  |
| `hrp_ns_sec_l12_semi_routine` | `bigint` |  |
| `hrp_ns_sec_l13_routine` | `bigint` |  |
| `hrp_ns_sec_l14_1_never_worked` | `bigint` |  |
| `hrp_ns_sec_l14_2_lt_unemployed` | `bigint` |  |
| `hrp_ns_sec_l15_students` | `bigint` |  |
| `all_people_16plus_ns_sec` | `bigint` | Recorded census measure for the category "all people 16plus ns sec" in the represented area. Units and population base require the source table. |
| `all_ns_sec_l1_large_employers` | `bigint` |  |
| `all_ns_sec_l2_higher_mgr_admin` | `bigint` |  |
| `all_ns_sec_l3_higher_prof` | `bigint` |  |
| `all_ns_sec_l4_lower_prof_tech` | `bigint` |  |
| `all_ns_sec_l5_lower_mgr_admin` | `bigint` |  |
| `all_ns_sec_l6_higher_supervisory` | `bigint` |  |
| `all_ns_sec_l7_intermediate` | `bigint` |  |
| `all_ns_sec_l8_small_employers` | `bigint` |  |
| `all_ns_sec_l9_own_account` | `bigint` |  |
| `all_ns_sec_l10_lower_supervisory` | `bigint` |  |
| `all_ns_sec_l11_lower_tech` | `bigint` |  |
| `all_ns_sec_l12_semi_routine` | `bigint` |  |
| `all_ns_sec_l13_routine` | `bigint` |  |
| `all_ns_sec_l14_1_never_worked` | `bigint` |  |
| `all_ns_sec_l14_2_lt_unemployed` | `bigint` |  |
| `all_ns_sec_l15_students` | `bigint` |  |
| `all_in_employment_distance` | `bigint` |  |
| `work_from_home` | `bigint` |  |
| `dist_less_2km` | `bigint` |  |
| `dist_2_5km` | `bigint` |  |
| `dist_5_10km` | `bigint` |  |
| `dist_10_20km` | `bigint` |  |
| `dist_20_30km` | `bigint` |  |
| `dist_30_40km` | `bigint` |  |
| `dist_40_60km` | `bigint` |  |
| `dist_60km_plus` | `bigint` |  |
| `dist_no_fixed_or_abroad` | `bigint` |  |
| `all_in_employment_travel_method` | `bigint` |  |
| `travel_work_from_home` | `bigint` |  |
| `travel_car_driver` | `bigint` |  |
| `travel_car_passenger` | `bigint` |  |
| `travel_taxi` | `bigint` |  |
| `travel_motorcycle` | `bigint` |  |
| `travel_on_foot` | `bigint` |  |
| `travel_bicycle` | `bigint` |  |
| `travel_bus` | `bigint` |  |
| `travel_train` | `bigint` |  |
| `travel_underground_tram` | `bigint` |  |
| `other` | `bigint` |  |
| `all_occupied_hhs_travel_hh` | `bigint` |  |
| `hh_no_worker` | `bigint` |  |
| `hh_1_worker_total` | `bigint` |  |
| `hh_1_worker_car_driver` | `bigint` |  |
| `hh_1_worker_other_travel` | `bigint` |  |
| `hh_1_worker_at_home` | `bigint` |  |
| `hh_2_workers_total` | `bigint` |  |
| `hh_2_workers_both_car` | `bigint` |  |
| `hh_2_workers_both_other` | `bigint` |  |
| `hh_2_workers_both_home` | `bigint` |  |
| `hh_2_workers_1_car_1_other` | `bigint` |  |
| `hh_2_workers_1_car_1_home` | `bigint` |  |
| `hh_2_1_other_1_home` | `bigint` |  |
| `hh_3plus_workers_total` | `bigint` |  |
| `hh_3plus_workers_all_car` | `bigint` |  |
| `hh_3plus_workers_all_other` | `bigint` |  |
| `hh_3plus_workers_all_home` | `bigint` |  |
| `hh_3plus_mix_car_other` | `bigint` |  |
| `hh_3plus_mix_car_home` | `bigint` |  |
| `hh_3plus_mix_other_home` | `bigint` |  |
| `hh_3plus_mix_all` | `bigint` |  |
