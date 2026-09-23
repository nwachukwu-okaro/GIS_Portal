# Boundary Census Work Travel Msoa

## Overview

- **Identifier:** `a_ons_england_wales/boundary_census_work_travel_msoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418601, 49.864798, 1.763680, 55.811120]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_census_work_travel_msoa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 7264
- **Columns:** 300
- **Metadata status:** source_mapped

## Description

Boundary Census Work Travel Msoa is an authoritative dataset published by Office for National Statistics. It represents boundary census work travel msoa features using geometry geometry.

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
| `dist_to_work_total` | `bigint` |  |
| `less_than_2km` | `bigint` |  |
| `t_2km_to_less_than_5km` | `bigint` |  |
| `t_5km_to_less_than_10km` | `bigint` |  |
| `t_10km_to_less_than_20km` | `bigint` |  |
| `t_20km_to_less_than_30km` | `bigint` |  |
| `t_30km_to_less_than_40km` | `bigint` |  |
| `t_40km_to_less_than_60km` | `bigint` |  |
| `t_60km_and_over` | `bigint` |  |
| `works_mainly_from_home` | `bigint` |  |
| `works_offshore_no_fixed_place_or_overseas` | `bigint` |  |
| `hours_worked_total` | `bigint` |  |
| `part_time` | `bigint` |  |
| `part_time_15_hours_or_less_worked` | `bigint` |  |
| `part_time_16_to_30_hours_worked` | `bigint` |  |
| `full_time` | `bigint` |  |
| `full_time_31_to_48_hours_worked` | `bigint` |  |
| `full_time_49_or_more_hours_worked` | `bigint` |  |
| `industry_total` | `bigint` |  |
| `a_agriculture_forestry_and_fishing` | `bigint` |  |
| `crop_animal_production_hunting` | `bigint` |  |
| `t_02_forestry_and_logging` | `bigint` |  |
| `t_03_fishing_and_aquaculture` | `bigint` |  |
| `b_mining_and_quarrying` | `bigint` |  |
| `t_05_mining_of_coal_and_lignite` | `bigint` |  |
| `t_06_extraction_of_crude_petroleum_and_natural_gas` | `bigint` |  |
| `t_07_mining_of_metal_ores` | `bigint` |  |
| `t_08_other_mining_and_quarrying` | `bigint` |  |
| `t_09_mining_support_service_activities` | `bigint` |  |
| `c_manufacturing` | `bigint` |  |
| `t_10_manufacture_of_food_products` | `bigint` |  |
| `t_11_manufacture_of_beverages` | `bigint` |  |
| `t_12_manufacture_of_tobacco_products` | `bigint` |  |
| `t_13_manufacture_of_textiles` | `bigint` |  |
| `t_14_manufacture_of_wearing_apparel` | `bigint` |  |
| `t_15_manufacture_of_leather_and_related_products` | `bigint` |  |
| `manuf_wood_cork_excl_furniture_straw` | `bigint` |  |
| `t_17_manufacture_of_paper_and_paper_products` | `bigint` |  |
| `t_18_printing_and_reproduction_of_recorded_media` | `bigint` |  |
| `manuf_of_coke_and_refined_petroleum_products` | `bigint` |  |
| `t_20_manufacture_of_chemicals_and_chemical_products` | `bigint` |  |
| `manuf_basic_pharma_products` | `bigint` |  |
| `t_22_manufacture_of_rubber_and_plastic_products` | `bigint` |  |
| `manuf_of_other_non_metallic_mineral_products` | `bigint` |  |
| `t_24_manufacture_of_basic_metals` | `bigint` |  |
| `manuf_fabricated_metal_excl_machinery` | `bigint` |  |
| `manuf_of_computer_electrical_and_optical_products` | `bigint` |  |
| `t_27_manufacture_of_electrical_equipment` | `bigint` |  |
| `manuf_machinery_and_equipment_nos` | `bigint` |  |
| `manuf_of_motor_vehicles_trailers_and_semi_trailers` | `bigint` |  |
| `t_30_manufacture_of_other_transport_equipment` | `bigint` |  |
| `t_31_manufacture_of_furniture` | `bigint` |  |
| `t_32_other_manufacturing` | `bigint` |  |
| `repair_and_installation_of_machinery_and_equipment` | `bigint` |  |
| `d_electricity_gas_steam_and_air_conditioning_supply` | `bigint` |  |
| `electricity_gas_steam_and_air_conditioning_supply` | `bigint` |  |
| `sewerage_waste_mgmt_and_remediation` | `bigint` |  |
| `t_36_water_collection_treatment_and_supply` | `bigint` |  |
| `t_37_sewerage` | `bigint` |  |
| `waste_collection_disposal_materials_recovery` | `bigint` |  |
| `remediation_and_waste_mgmt` | `bigint` |  |
| `f_construction` | `bigint` |  |
| `constr_buildings_civil_eng_specialised` | `bigint` |  |
| `wholesale_retail_trade_motor_vehicles` | `bigint` |  |
| `wholesale_retail_motor_vehicles` | `bigint` |  |
| `wholesale_trade_excl_motor_vehicles` | `bigint` |  |
| `retail_trade_except_of_motor_vehicles_and_motorcycles` | `bigint` |  |
| `t_48_wholesale_and_retail_not_otherwise_specified` | `bigint` |  |
| `h_transport_and_storage` | `bigint` |  |
| `t_49_land_transport_and_transport_via_pipelines` | `bigint` |  |
| `t_50_water_transport` | `bigint` |  |
| `t_51_air_transport` | `bigint` |  |
| `warehousing_and_transport_support` | `bigint` |  |
| `t_53_postal_and_courier_activities` | `bigint` |  |
| `i_accommodation_and_food_service_activities` | `bigint` |  |
| `t_55_accommodation` | `bigint` |  |
| `t_56_food_and_beverage_service_activities` | `bigint` |  |
| `j_information_and_communication` | `bigint` |  |
| `t_58_publishing_activities` | `bigint` |  |
| `film_tv_sound_recording_music_pub` | `bigint` |  |
| `t_60_programming_and_broadcasting_activities` | `bigint` |  |
| `t_61_telecommunications` | `bigint` |  |
| `it_programming_consultancy` | `bigint` |  |
| `t_63_information_service_activities` | `bigint` |  |
| `k_financial_and_insurance_activities` | `bigint` |  |
| `financial_svcs_excl_insurance_pension` | `bigint` |  |
| `insurance_reinsurance_pension_excl_compulsory` | `bigint` |  |
| `auxiliary_financial_and_insurance_svcs` | `bigint` |  |
| `l_real_estate_activities` | `bigint` |  |
| `t_68_real_estate_activities` | `bigint` |  |
| `m_professional_scientific_and_technical_activities` | `bigint` |  |
| `t_69_legal_and_accounting_activities` | `bigint` |  |
| `head_offices_management_consultancy` | `bigint` |  |
| `architecture_engineering_technical_testing` | `bigint` |  |
| `t_72_scientific_research_and_development` | `bigint` |  |
| `t_73_advertising_and_market_research` | `bigint` |  |
| `other_professional_scientific_technical` | `bigint` |  |
| `t_75_veterinary_activities` | `bigint` |  |
| `n_administrative_and_support_service_activities` | `bigint` |  |
| `t_77_rental_and_leasing_activities` | `bigint` |  |
| `t_78_employment_activities` | `bigint` |  |
| `travel_agency_tour_operator_reservation_svcs` | `bigint` |  |
| `t_80_security_and_investigation_activities` | `bigint` |  |
| `t_81_services_to_buildings_and_landscape_activities` | `bigint` |  |
| `office_admin_and_business_support` | `bigint` |  |
| `o_public_admin_and_defence_compulsory_social_security` | `bigint` |  |
| `public_admin_and_defence_compulsory_social_security` | `bigint` |  |
| `p_education` | `bigint` |  |
| `t_85_education` | `bigint` |  |
| `q_human_health_and_social_work_activities` | `bigint` |  |
| `t_86_human_health_activities` | `bigint` |  |
| `t_87_residential_care_activities` | `bigint` |  |
| `t_88_social_work_activities_without_accommodation` | `bigint` |  |
| `r_s_t_u_other` | `bigint` |  |
| `t_90_creative_arts_and_entertainment_activities` | `bigint` |  |
| `libraries_archives_museums_cultural` | `bigint` |  |
| `t_92_gambling_and_betting_activities` | `bigint` |  |
| `sports_amusement_and_recreation` | `bigint` |  |
| `t_94_activities_of_membership_organisations` | `bigint` |  |
| `repair_of_computers_and_personal_and_hh_goods` | `bigint` |  |
| `t_96_other_personal_service_activities` | `bigint` |  |
| `activities_of_hhs_as_employers_of_domestic_personnel` | `bigint` |  |
| `private_hh_goods_svcs_own_use` | `bigint` |  |
| `activities_of_extraterritorial_organisations_and_bodies` | `bigint` |  |
| `travel_to_work_total` | `bigint` |  |
| `work_mainly_at_or_from_home` | `bigint` |  |
| `underground_metro_light_rail_tram` | `bigint` |  |
| `train` | `bigint` |  |
| `bus_minibus_or_coach` | `bigint` |  |
| `taxi` | `bigint` |  |
| `motorcycle_scooter_or_moped` | `bigint` |  |
| `driving_a_car_or_van` | `bigint` |  |
| `passenger_in_a_car_or_van` | `bigint` |  |
| `bicycle` | `bigint` |  |
| `on_foot` | `bigint` |  |
| `other_method_of_travel_to_work` | `bigint` |  |
| `ns_sec_total` | `bigint` |  |
| `higher_managerial_admin_and_prof` | `bigint` |  |
| `lower_managerial_admin_and_prof` | `bigint` |  |
| `l7_intermediate_occupations` | `bigint` |  |
| `l8_and_l9_small_employers_and_own_account_workers` | `bigint` |  |
| `l10_and_l11_lower_supervisory_and_technical_occupations` | `bigint` |  |
| `l12_semi_routine_occupations` | `bigint` |  |
| `l13_routine_occupations` | `bigint` |  |
| `l14_1_and_l14_2_never_worked_and_long_term_unemployed` | `bigint` |  |
| `l15_full_time_students` | `bigint` |  |
| `occupation_total_t1` | `bigint` |  |
| `t_1_managers_directors_and_senior_officials` | `bigint` |  |
| `t_2_professional_occupations` | `bigint` |  |
| `t_3_associate_professional_and_technical_occupations` | `bigint` |  |
| `t_4_administrative_and_secretarial_occupations` | `bigint` |  |
| `t_5_skilled_trades_occupations` | `bigint` |  |
| `t_6_caring_leisure_and_other_service_occupations` | `bigint` |  |
| `t_7_sales_and_customer_service_occupations` | `bigint` |  |
| `t_8_process_plant_and_machine_operatives` | `bigint` |  |
| `t_9_elementary_occupations` | `bigint` |  |
| `occupation_total_t2` | `bigint` |  |
| `t_111_chief_executives_and_senior_officials` | `bigint` |  |
| `t_112_production_managers_and_directors` | `bigint` |  |
| `t_113_functional_managers_and_directors` | `bigint` |  |
| `directors_in_logistics_warehousing_and_transport` | `bigint` |  |
| `t_115_managers_and_directors_in_retail_and_wholesale` | `bigint` |  |
| `t_116_senior_officers_in_protective_services` | `bigint` |  |
| `health_and_social_services_managers_and_directors` | `bigint` |  |
| `managers_proprietors_agriculture_svcs` | `bigint` |  |
| `managers_proprietors_hospitality_leisure` | `bigint` |  |
| `managers_and_proprietors_in_health_and_care_services` | `bigint` |  |
| `managers_in_logistics_warehousing_and_transport` | `bigint` |  |
| `t_125_managers_and_proprietors_in_other_services` | `bigint` |  |
| `t_211_natural_and_social_science_professionals` | `bigint` |  |
| `t_212_engineering_professionals` | `bigint` |  |
| `t_213_information_technology_professionals` | `bigint` |  |
| `t_214_web_and_multimedia_design_professionals` | `bigint` |  |
| `t_215_conservation_and_environment_professionals` | `bigint` |  |
| `research_and_development_and_other_research_profs` | `bigint` |  |
| `t_221_medical_practitioners` | `bigint` |  |
| `t_222_therapy_professionals` | `bigint` |  |
| `t_223_nursing_and_midwifery_professionals` | `bigint` |  |
| `t_224_veterinarians` | `bigint` |  |
| `t_225_other_health_professionals` | `bigint` |  |
| `t_231_teaching_and_other_educational_professionals` | `bigint` |  |
| `t_232_other_educational_professionals` | `bigint` |  |
| `t_241_legal_professionals` | `bigint` |  |
| `t_242_finance_professionals` | `bigint` |  |
| `business_research_and_administrative_profs` | `bigint` |  |
| `business_and_financial_project_management_profs` | `bigint` |  |
| `architects_planners_surveyors_constr_profs` | `bigint` |  |
| `t_246_welfare_professionals` | `bigint` |  |
| `t_247_librarians_and_related_professionals` | `bigint` |  |
| `t_248_quality_and_regulatory_professionals` | `bigint` |  |
| `t_249_media_professionals` | `bigint` |  |
| `t_311_science_engineering_and_production_technicians` | `bigint` |  |
| `t_312_cad_drawing_and_architectural_technicians` | `bigint` |  |
| `t_313_information_technology_technicians` | `bigint` |  |
| `t_321_health_associate_professionals` | `bigint` |  |
| `t_322_welfare_and_housing_associate_professionals` | `bigint` |  |
| `t_323_teaching_and_childcare_associate_professionals` | `bigint` |  |
| `t_324_veterinary_nurses` | `bigint` |  |
| `t_331_protective_service_occupations` | `bigint` |  |
| `t_341_artistic_literary_and_media_occupations` | `bigint` |  |
| `t_342_design_occupations` | `bigint` |  |
| `t_343_sports_and_fitness_occupations` | `bigint` |  |
| `t_351_transport_associate_professionals` | `bigint` |  |
| `t_352_legal_associate_professionals` | `bigint` |  |
| `t_353_finance_associate_professionals` | `bigint` |  |
| `t_354_business_associate_professionals` | `bigint` |  |
| `sales_marketing_and_related_associate_profs` | `bigint` |  |
| `t_356_public_services_associate_professionals` | `bigint` |  |
| `hr_training_and_vocational_guidance_profs` | `bigint` |  |
| `t_358_regulatory_associate_professionals` | `bigint` |  |
| `admin_occupations_govt_and_related` | `bigint` |  |
| `t_412_administrative_occupations_finance` | `bigint` |  |
| `t_413_administrative_occupations_records` | `bigint` |  |
| `admin_occupations_office_mgrs_supervisors` | `bigint` |  |
| `t_415_other_administrative_occupations` | `bigint` |  |
| `t_421_secretarial_and_related_occupations` | `bigint` |  |
| `t_511_agricultural_and_related_trades` | `bigint` |  |
| `t_521_metal_forming_welding_and_related_trades` | `bigint` |  |
| `metal_machining_fitting_and_instrument_making_trades` | `bigint` |  |
| `t_523_vehicle_trades` | `bigint` |  |
| `t_524_electrical_and_electronic_trades` | `bigint` |  |
| `skilled_metal_electrical_trades_supervisors` | `bigint` |  |
| `t_531_construction_and_building_trades` | `bigint` |  |
| `t_532_building_finishing_trades` | `bigint` |  |
| `t_533_construction_and_building_trades_supervisors` | `bigint` |  |
| `t_541_textiles_and_garments_trades` | `bigint` |  |
| `t_542_printing_trades` | `bigint` |  |
| `t_543_food_preparation_and_hospitality_trades` | `bigint` |  |
| `t_544_other_skilled_trades` | `bigint` |  |
| `t_611_teaching_and_childcare_support_occupations` | `bigint` |  |
| `t_612_animal_care_and_control_services` | `bigint` |  |
| `t_613_caring_personal_services` | `bigint` |  |
| `t_621_leisure_and_travel_services` | `bigint` |  |
| `t_622_hairdressers_and_related_services` | `bigint` |  |
| `t_623_housekeeping_and_related_services` | `bigint` |  |
| `cleaning_and_housekeeping_managers_and_supervisors` | `bigint` |  |
| `bed_breakfast_and_guest_house_owners` | `bigint` |  |
| `t_631_community_and_civil_enforcement_occupations` | `bigint` |  |
| `t_711_sales_assistants_and_retail_cashiers` | `bigint` |  |
| `t_712_sales_related_occupations` | `bigint` |  |
| `t_713_shopkeepers_and_sales_supervisors` | `bigint` |  |
| `t_721_customer_service_occupations` | `bigint` |  |
| `t_722_customer_service_supervisors` | `bigint` |  |
| `t_811_process_operatives` | `bigint` |  |
| `t_812_metal_working_machine_operatives` | `bigint` |  |
| `t_813_plant_and_machine_operatives` | `bigint` |  |
| `t_814_assemblers_and_routine_operatives` | `bigint` |  |
| `t_815_construction_operatives` | `bigint` |  |
| `t_816_production_factory_and_assembly_supervisors` | `bigint` |  |
| `t_821_road_transport_drivers` | `bigint` |  |
| `t_822_mobile_machine_drivers_and_operatives` | `bigint` |  |
| `t_823_other_drivers_and_transport_operatives` | `bigint` |  |
| `t_911_elementary_agricultural_occupations` | `bigint` |  |
| `t_912_elementary_construction_occupations` | `bigint` |  |
| `t_913_elementary_process_plant_occupations` | `bigint` |  |
| `t_921_elementary_administration_occupations` | `bigint` |  |
| `t_922_elementary_cleaning_occupations` | `bigint` |  |
| `t_923_elementary_security_occupations` | `bigint` |  |
| `t_924_elementary_sales_occupations` | `bigint` |  |
| `t_925_elementary_storage_occupations` | `bigint` |  |
| `t_926_other_elementary_services_occupations` | `bigint` |  |
| `unemployment_history_total` | `bigint` |  |
| `not_in_employment_worked_in_the_last_12_months` | `bigint` |  |
| `not_in_employment_not_worked_in_the_last_12_months` | `bigint` |  |
| `not_in_employment_never_worked` | `bigint` |  |
| `econ_activity_total` | `bigint` |  |
| `economically_active` | `bigint` |  |
| `economically_active_in_employment` | `bigint` |  |
| `economically_active_in_employment_employee` | `bigint` |  |
| `econ_active_in_employment_employee_part_time` | `bigint` |  |
| `econ_active_in_employment_employee_full_time` | `bigint` |  |
| `econ_active_in_employment_self_emp_w_emp` | `bigint` |  |
| `econ_active_in_employment_self_emp_w_emp_part_time` | `bigint` |  |
| `econ_active_in_employment_self_emp_w_emp_full_time` | `bigint` |  |
| `econ_active_in_employment_self_emp_no_emp` | `bigint` |  |
| `econ_active_in_employment_self_emp_no_emp_part_time` | `bigint` |  |
| `econ_active_in_employment_self_emp_no_emp_full_time` | `bigint` |  |
| `economically_active_unemployed` | `bigint` |  |
| `economically_active_and_a_full_time_student` | `bigint` |  |
| `econ_active_student_in_employment` | `bigint` |  |
| `econ_active_student_in_employment_employee` | `bigint` |  |
| `econ_active_student_in_employment_employee_part_time` | `bigint` |  |
| `econ_active_student_in_employment_employee_full_time` | `bigint` |  |
| `econ_active_student_self_emp_w_emp` | `bigint` |  |
| `econ_active_student_self_emp_w_emp_pt` | `bigint` |  |
| `econ_active_student_self_emp_w_emp_ft` | `bigint` |  |
| `econ_active_student_self_emp_no_emp` | `bigint` |  |
| `econ_active_student_self_emp_no_emp_pt` | `bigint` |  |
| `econ_active_student_self_emp_no_emp_ft` | `bigint` |  |
| `econ_active_student_unemployed` | `bigint` |  |
| `economically_inactive` | `bigint` |  |
| `economically_inactive_retired` | `bigint` |  |
| `economically_inactive_student` | `bigint` |  |
| `economically_inactive_looking_after_home_or_family` | `bigint` |  |
| `economically_inactive_long_term_sick_or_disabled` | `bigint` |  |
| `economically_inactive_other` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
