# Work Travel Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/work_travel_lsoa`
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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_ons_england_wales`
- **Table:** `work_travel_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 88
- **Metadata status:** source_mapped

## Description

Work Travel Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to work travel lsoa.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `dist_to_work_total` | `bigint` | Count or numeric value for dist to work total in the represented area. |
| `less_than_2km` | `bigint` | Count or numeric value for less than 2km in the represented area. |
| `t_2km_to_less_than_5km` | `bigint` | Count or numeric value for t 2km to less than 5km in the represented area. |
| `t_5km_to_less_than_10km` | `bigint` | Count or numeric value for t 5km to less than 10km in the represented area. |
| `t_10km_to_less_than_20km` | `bigint` | Count or numeric value for t 10km to less than 20km in the represented area. |
| `t_20km_to_less_than_30km` | `bigint` | Count or numeric value for t 20km to less than 30km in the represented area. |
| `t_30km_to_less_than_40km` | `bigint` | Count or numeric value for t 30km to less than 40km in the represented area. |
| `t_40km_to_less_than_60km` | `bigint` | Count or numeric value for t 40km to less than 60km in the represented area. |
| `t_60km_and_over` | `bigint` | Count or numeric value for t 60km and over in the represented area. |
| `works_mainly_from_home` | `bigint` | Count or numeric value for works mainly from home in the represented area. |
| `works_offshore_no_fixed_place_or_overseas` | `bigint` | Count or numeric value for works offshore number fixed place or overseas in the represented area. |
| `hours_worked_total` | `bigint` | Count or numeric value for hours worked total in the represented area. |
| `part_time` | `bigint` | Count or numeric value for part time in the represented area. |
| `part_time_15_hours_or_less_worked` | `bigint` | Count or numeric value for part time 15 hours or less worked in the represented area. |
| `part_time_16_to_30_hours_worked` | `bigint` | Count or numeric value for part time 16 to 30 hours worked in the represented area. |
| `full_time` | `bigint` | Count or numeric value for full time in the represented area. |
| `full_time_31_to_48_hours_worked` | `bigint` | Count or numeric value for full time 31 to 48 hours worked in the represented area. |
| `full_time_49_or_more_hours_worked` | `bigint` | Count or numeric value for full time 49 or more hours worked in the represented area. |
| `travel_to_work_total` | `bigint` | Count or numeric value for travel to work total in the represented area. |
| `work_mainly_at_or_from_home` | `bigint` | Count or numeric value for work mainly at or from home in the represented area. |
| `underground_metro_light_rail_tram` | `bigint` | Count or numeric value for underground metro light rail tram in the represented area. |
| `train` | `bigint` | Count or numeric value for train in the represented area. |
| `bus_minibus_or_coach` | `bigint` | Count or numeric value for bus minibus or coach in the represented area. |
| `taxi` | `bigint` | Count or numeric value for taxi in the represented area. |
| `motorcycle_scooter_or_moped` | `bigint` | Count or numeric value for motorcycle scooter or moped in the represented area. |
| `driving_a_car_or_van` | `bigint` | Count or numeric value for driving a car or van in the represented area. |
| `passenger_in_a_car_or_van` | `bigint` | Count or numeric value for passenger in a car or van in the represented area. |
| `bicycle` | `bigint` | Count or numeric value for bicycle in the represented area. |
| `on_foot` | `bigint` | Count or numeric value for on foot in the represented area. |
| `other_method_of_travel_to_work` | `bigint` | Count or numeric value for other method of travel to work in the represented area. |
| `ns_sec_total` | `bigint` | Count or numeric value for ns sec total in the represented area. |
| `higher_managerial_admin_and_prof` | `bigint` | Count or numeric value for higher managerial admin and prof in the represented area. |
| `lower_managerial_admin_and_prof` | `bigint` | Count or numeric value for lower managerial admin and prof in the represented area. |
| `l7_intermediate_occupations` | `bigint` | Count or numeric value for l7 intermediate occupations in the represented area. |
| `l8_and_l9_small_employers_and_own_account_workers` | `bigint` | Count or numeric value for l8 and l9 small employers and own account workers in the represented area. |
| `l10_and_l11_lower_supervisory_and_technical_occupations` | `bigint` | Count or numeric value for l10 and l11 lower supervisory and technical occupations in the represented area. |
| `l12_semi_routine_occupations` | `bigint` | Count or numeric value for l12 semi routine occupations in the represented area. |
| `l13_routine_occupations` | `bigint` | Count or numeric value for l13 routine occupations in the represented area. |
| `l14_1_and_l14_2_never_worked_and_long_term_unemployed` | `bigint` | Numeric l14 1 and l14 2 never worked and long term unemployed value recorded for the feature. |
| `l15_full_time_students` | `bigint` | Count or numeric value for l15 full time students in the represented area. |
| `occupation_total` | `bigint` | Count or numeric value for occupation total in the represented area. |
| `t_1_managers_directors_and_senior_officials` | `bigint` | Count or numeric value for t 1 managers directors and senior officials in the represented area. |
| `t_2_professional_occupations` | `bigint` | Count or numeric value for t 2 professional occupations in the represented area. |
| `t_3_associate_professional_and_technical_occupations` | `bigint` | Count or numeric value for t 3 associate professional and technical occupations in the represented area. |
| `t_4_administrative_and_secretarial_occupations` | `bigint` | Count or numeric value for t 4 administrative and secretarial occupations in the represented area. |
| `t_5_skilled_trades_occupations` | `bigint` | Count or numeric value for t 5 skilled trades occupations in the represented area. |
| `t_6_caring_leisure_and_other_service_occupations` | `bigint` | Count or numeric value for t 6 caring leisure and other service occupations in the represented area. |
| `t_7_sales_and_customer_service_occupations` | `bigint` | Count or numeric value for t 7 sales and customer service occupations in the represented area. |
| `t_8_process_plant_and_machine_operatives` | `bigint` | Count or numeric value for t 8 process plant and machine operatives in the represented area. |
| `t_9_elementary_occupations` | `bigint` | Count or numeric value for t 9 elementary occupations in the represented area. |
| `unemployment_history_total` | `bigint` | Count or numeric value for unemployment history total in the represented area. |
| `not_in_employment_worked_in_the_last_12_months` | `bigint` | Count or numeric value for not in employment worked in the last 12 months in the represented area. |
| `not_in_employment_not_worked_in_the_last_12_months` | `bigint` | Count or numeric value for not in employment not worked in the last 12 months in the represented area. |
| `not_in_employment_never_worked` | `bigint` | Count or numeric value for not in employment never worked in the represented area. |
| `econ_activity_total` | `bigint` | Count or numeric value for econ activity total in the represented area. |
| `economically_active` | `bigint` | Count or numeric value for economically active in the represented area. |
| `economically_active_in_employment` | `bigint` | Count or numeric value for economically active in employment in the represented area. |
| `economically_active_in_employment_employee` | `bigint` | Count or numeric value for economically active in employment employee in the represented area. |
| `econ_active_in_employment_employee_part_time` | `bigint` | Count or numeric value for econ active in employment employee part time in the represented area. |
| `econ_active_in_employment_employee_full_time` | `bigint` | Count or numeric value for econ active in employment employee full time in the represented area. |
| `econ_active_in_employment_self_emp_w_emp` | `bigint` | Count or numeric value for econ active in employment self emp w emp in the represented area. |
| `econ_active_in_employment_self_emp_w_emp_part_time` | `bigint` | Count or numeric value for econ active in employment self emp w emp part time in the represented area. |
| `econ_active_in_employment_self_emp_w_emp_full_time` | `bigint` | Count or numeric value for econ active in employment self emp w emp full time in the represented area. |
| `econ_active_in_employment_self_emp_no_emp` | `bigint` | Count or numeric value for econ active in employment self emp number emp in the represented area. |
| `econ_active_in_employment_self_emp_no_emp_part_time` | `bigint` | Count or numeric value for econ active in employment self emp number emp part time in the represented area. |
| `econ_active_in_employment_self_emp_no_emp_full_time` | `bigint` | Count or numeric value for econ active in employment self emp number emp full time in the represented area. |
| `economically_active_unemployed` | `bigint` | Count or numeric value for economically active unemployed in the represented area. |
| `economically_active_and_a_full_time_student` | `bigint` | Count or numeric value for economically active and a full time student in the represented area. |
| `econ_active_student_in_employment` | `bigint` | Count or numeric value for econ active student in employment in the represented area. |
| `econ_active_student_in_employment_employee` | `bigint` | Count or numeric value for econ active student in employment employee in the represented area. |
| `econ_active_student_in_employment_employee_part_time` | `bigint` | Count or numeric value for econ active student in employment employee part time in the represented area. |
| `econ_active_student_in_employment_employee_full_time` | `bigint` | Count or numeric value for econ active student in employment employee full time in the represented area. |
| `econ_active_student_self_emp_w_emp` | `bigint` | Count or numeric value for econ active student self emp w emp in the represented area. |
| `econ_active_student_self_emp_w_emp_pt` | `bigint` | Count or numeric value for econ active student self emp w emp pt in the represented area. |
| `econ_active_student_self_emp_w_emp_ft` | `bigint` | Count or numeric value for econ active student self emp w emp ft in the represented area. |
| `econ_active_student_self_emp_no_emp` | `bigint` | Count or numeric value for econ active student self emp number emp in the represented area. |
| `econ_active_student_self_emp_no_emp_pt` | `bigint` | Count or numeric value for econ active student self emp number emp pt in the represented area. |
| `econ_active_student_self_emp_no_emp_ft` | `bigint` | Count or numeric value for econ active student self emp number emp ft in the represented area. |
| `econ_active_student_unemployed` | `bigint` | Count or numeric value for econ active student unemployed in the represented area. |
| `economically_inactive` | `bigint` | Count or numeric value for economically inactive in the represented area. |
| `economically_inactive_retired` | `bigint` | Count or numeric value for economically inactive retired in the represented area. |
| `economically_inactive_student` | `bigint` | Count or numeric value for economically inactive student in the represented area. |
| `economically_inactive_looking_after_home_or_family` | `bigint` | Count or numeric value for economically inactive looking after home or family in the represented area. |
| `economically_inactive_long_term_sick_or_disabled` | `bigint` | Numeric economically inactive long term sick or disabled value recorded for the feature. |
| `economically_inactive_other` | `bigint` | Count or numeric value for economically inactive other in the represented area. |
