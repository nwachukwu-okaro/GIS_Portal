# Boundary Census Work Travel Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/boundary_census_work_travel_lsoa`
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
- **Table:** `boundary_census_work_travel_lsoa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 35672
- **Columns:** 89
- **Metadata status:** source_mapped

## Description

Boundary Census Work Travel Lsoa is an authoritative dataset published by Office for National Statistics. It represents boundary census work travel lsoa features using geometry geometry.

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
| `occupation_total` | `bigint` |  |
| `t_1_managers_directors_and_senior_officials` | `bigint` |  |
| `t_2_professional_occupations` | `bigint` |  |
| `t_3_associate_professional_and_technical_occupations` | `bigint` |  |
| `t_4_administrative_and_secretarial_occupations` | `bigint` |  |
| `t_5_skilled_trades_occupations` | `bigint` |  |
| `t_6_caring_leisure_and_other_service_occupations` | `bigint` |  |
| `t_7_sales_and_customer_service_occupations` | `bigint` |  |
| `t_8_process_plant_and_machine_operatives` | `bigint` |  |
| `t_9_elementary_occupations` | `bigint` |  |
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
