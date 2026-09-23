# Scotland Health Disability Datazone

## Overview

- **Identifier:** `a_nrs_scotland/scotland_health_disability_datazone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `scotland_health_disability_datazone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7392
- **Columns:** 145
- **Metadata status:** source_mapped

## Description

Scotland Health Disability Datazone is an authoritative dataset published by National Records of Scotland. It contains records relating to scotland health disability datazone.

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
| `all_people_aged_3_and_over` | `bigint` | Recorded census measure for the category "all people aged 3 and over" in the represented area. Units and population base require the source table. |
| `no_unpaid_carers` | `bigint` |  |
| `all_unpaid_carers` | `bigint` |  |
| `yes_1_to_19_hours_a_week` | `bigint` |  |
| `yes_20_to_34_hours_a_week` | `double precision` |  |
| `yes_35_to_49_hours_a_week` | `double precision` |  |
| `yes_50_or_more_hours_a_week` | `double precision` |  |
| `all_people_3plus_total` | `bigint` | Recorded census measure for the category "all people 3plus total" in the represented area. Units and population base require the source table. |
| `all_people_aged_3_and_over_provides_no_unpaid_care` | `bigint` | Recorded census measure for the category "all people aged 3 and over provides no unpaid care" in the represented area. Units and population base require the source table. |
| `all_people_3plus_provides_unpaid_care_total` | `bigint` | Recorded census measure for the category "all people 3plus provides unpaid care total" in the represented area. Units and population base require the source table. |
| `all_people_3plus_provides_unpaid_care_1_19_hrs_pw` | `bigint` | Recorded census measure for the category "all people 3plus provides unpaid care 1 19 hrs pw" in the represented area. Units and population base require the source table. |
| `all_people_3plus_provides_unpaid_care_20_34_hrs_pw` | `double precision` | Recorded census measure for the category "all people 3plus provides unpaid care 20 34 hrs pw" in the represented area. Units and population base require the source table. |
| `all_people_3plus_provides_unpaid_care_35_49_hrs_pw` | `double precision` | Recorded census measure for the category "all people 3plus provides unpaid care 35 49 hrs pw" in the represented area. Units and population base require the source table. |
| `all_people_3plus_provides_unpaid_care_50_plus_hours_a_week` | `double precision` | Recorded census measure for the category "all people 3plus provides unpaid care 50 plus hours a week" in the represented area. Units and population base require the source table. |
| `t_3_to_15_all_people_aged_3_and_over` | `bigint` |  |
| `t_3_to_15_provides_no_unpaid_care` | `bigint` |  |
| `t_3_to_15_provides_unpaid_care_total` | `double precision` |  |
| `t_3_to_15_provides_unpaid_care_1_to_19_hours_a_week` | `double precision` |  |
| `t_3_to_15_provides_unpaid_care_20_to_34_hours_a_week` | `double precision` |  |
| `t_3_to_15_provides_unpaid_care_35_to_49_hours_a_week` | `double precision` |  |
| `t_3_to_15_provides_unpaid_care_50_plus_hours_a_week` | `double precision` |  |
| `t_16_to_24_all_people_aged_3_and_over` | `bigint` |  |
| `t_16_to_24_provides_no_unpaid_care` | `bigint` |  |
| `t_16_to_24_provides_unpaid_care_total` | `double precision` |  |
| `t_16_to_24_provides_unpaid_care_1_to_19_hours_a_week` | `double precision` |  |
| `t_16_to_24_provides_unpaid_care_20_34_hrs_pw` | `double precision` |  |
| `t_16_to_24_provides_unpaid_care_35_49_hrs_pw` | `double precision` |  |
| `t_16_to_24_provides_unpaid_care_50_plus_hours_a_week` | `double precision` |  |
| `t_25_to_34_all_people_aged_3_and_over` | `bigint` |  |
| `t_25_to_34_provides_no_unpaid_care` | `bigint` |  |
| `t_25_to_34_provides_unpaid_care_total` | `double precision` |  |
| `t_25_to_34_provides_unpaid_care_1_to_19_hours_a_week` | `double precision` |  |
| `t_25_to_34_provides_unpaid_care_20_34_hrs_pw` | `double precision` |  |
| `t_25_to_34_provides_unpaid_care_35_49_hrs_pw` | `double precision` |  |
| `t_25_to_34_provides_unpaid_care_50_plus_hours_a_week` | `double precision` |  |
| `t_35_to_49_all_people_aged_3_and_over` | `bigint` |  |
| `t_35_to_49_provides_no_unpaid_care` | `bigint` |  |
| `t_35_to_49_provides_unpaid_care_total` | `bigint` |  |
| `t_35_to_49_provides_unpaid_care_1_to_19_hours_a_week` | `double precision` |  |
| `t_35_to_49_provides_unpaid_care_20_34_hrs_pw` | `double precision` |  |
| `t_35_to_49_provides_unpaid_care_35_49_hrs_pw` | `double precision` |  |
| `t_35_to_49_provides_unpaid_care_50_plus_hours_a_week` | `double precision` |  |
| `t_50_to_64_all_people_aged_3_and_over` | `bigint` |  |
| `t_50_to_64_provides_no_unpaid_care` | `bigint` |  |
| `t_50_to_64_provides_unpaid_care_total` | `double precision` |  |
| `t_50_to_64_provides_unpaid_care_1_to_19_hours_a_week` | `double precision` |  |
| `t_50_to_64_provides_unpaid_care_20_34_hrs_pw` | `double precision` |  |
| `t_50_to_64_provides_unpaid_care_35_49_hrs_pw` | `double precision` |  |
| `t_50_to_64_provides_unpaid_care_50_plus_hours_a_week` | `double precision` |  |
| `t_65_and_over_all_people_aged_3_and_over` | `bigint` |  |
| `t_65_and_over_provides_no_unpaid_care` | `bigint` |  |
| `t_65_and_over_provides_unpaid_care_total` | `double precision` |  |
| `t_65_and_over_provides_unpaid_care_1_19_hrs_pw` | `double precision` |  |
| `t_65_and_over_provides_unpaid_care_20_34_hrs_pw` | `double precision` |  |
| `t_65_and_over_provides_unpaid_care_35_49_hrs_pw` | `double precision` |  |
| `t_65_plus_provides_unpaid_care_50_plus_hours_a_week` | `double precision` |  |
| `uv302_all_people` | `bigint` |  |
| `very_good` | `bigint` |  |
| `good` | `bigint` |  |
| `fair` | `bigint` |  |
| `bad` | `double precision` |  |
| `very_bad` | `double precision` |  |
| `uv302b_total_all_people` | `bigint` |  |
| `total_very_good` | `bigint` |  |
| `total_good` | `bigint` |  |
| `total_fair` | `bigint` |  |
| `total_bad` | `double precision` |  |
| `total_very_bad` | `double precision` |  |
| `uv302b_0_to_15_all_people` | `bigint` |  |
| `t_0_to_15_very_good` | `bigint` |  |
| `t_0_to_15_good` | `double precision` |  |
| `t_0_to_15_fair` | `double precision` |  |
| `t_0_to_15_bad` | `double precision` |  |
| `t_0_to_15_very_bad` | `double precision` |  |
| `uv302b_16_to_24_all_people` | `bigint` |  |
| `t_16_to_24_very_good` | `bigint` |  |
| `t_16_to_24_good` | `double precision` |  |
| `t_16_to_24_fair` | `double precision` |  |
| `t_16_to_24_bad` | `double precision` |  |
| `t_16_to_24_very_bad` | `double precision` |  |
| `uv302b_25_to_34_all_people` | `bigint` |  |
| `t_25_to_34_very_good` | `bigint` |  |
| `t_25_to_34_good` | `double precision` |  |
| `t_25_to_34_fair` | `double precision` |  |
| `t_25_to_34_bad` | `double precision` |  |
| `t_25_to_34_very_bad` | `double precision` |  |
| `uv302b_35_to_49_all_people` | `bigint` |  |
| `t_35_to_49_very_good` | `bigint` |  |
| `t_35_to_49_good` | `bigint` |  |
| `t_35_to_49_fair` | `double precision` |  |
| `t_35_to_49_bad` | `double precision` |  |
| `t_35_to_49_very_bad` | `double precision` |  |
| `uv302b_50_to_64_all_people` | `bigint` |  |
| `t_50_to_64_very_good` | `double precision` |  |
| `t_50_to_64_good` | `bigint` |  |
| `t_50_to_64_fair` | `double precision` |  |
| `t_50_to_64_bad` | `double precision` |  |
| `t_50_to_64_very_bad` | `double precision` |  |
| `uv302b_65_and_over_all_people` | `bigint` |  |
| `t_65_and_over_very_good` | `double precision` |  |
| `t_65_and_over_good` | `double precision` |  |
| `t_65_and_over_fair` | `double precision` |  |
| `t_65_and_over_bad` | `double precision` |  |
| `t_65_and_over_very_bad` | `double precision` |  |
| `uv303_all_people` | `bigint` |  |
| `day_to_day_activities_limited_a_lot` | `bigint` |  |
| `day_to_day_activities_limited_a_little` | `bigint` |  |
| `day_to_day_activities_not_limited` | `bigint` |  |
| `uv303b_total_all_people` | `bigint` |  |
| `total_day_to_day_activities_limited_a_lot` | `bigint` |  |
| `total_day_to_day_activities_limited_a_little` | `bigint` |  |
| `total_day_to_day_activities_not_limited` | `bigint` |  |
| `uv303b_0_to_15_all_people` | `bigint` |  |
| `t_0_to_15_day_to_day_activities_limited_a_lot` | `double precision` |  |
| `t_0_to_15_day_to_day_activities_limited_a_little` | `double precision` |  |
| `t_0_to_15_day_to_day_activities_not_limited` | `bigint` |  |
| `uv303b_16_to_24_all_people` | `bigint` |  |
| `t_16_to_24_day_to_day_activities_limited_a_lot` | `double precision` |  |
| `t_16_to_24_day_to_day_activities_limited_a_little` | `double precision` |  |
| `t_16_to_24_day_to_day_activities_not_limited` | `bigint` |  |
| `uv303b_25_to_34_all_people` | `bigint` |  |
| `t_25_to_34_day_to_day_activities_limited_a_lot` | `double precision` |  |
| `t_25_to_34_day_to_day_activities_limited_a_little` | `double precision` |  |
| `t_25_to_34_day_to_day_activities_not_limited` | `bigint` |  |
| `uv303b_35_to_49_all_people` | `bigint` |  |
| `t_35_to_49_day_to_day_activities_limited_a_lot` | `double precision` |  |
| `t_35_to_49_day_to_day_activities_limited_a_little` | `double precision` |  |
| `t_35_to_49_day_to_day_activities_not_limited` | `bigint` |  |
| `uv303b_50_to_64_all_people` | `bigint` |  |
| `t_50_to_64_day_to_day_activities_limited_a_lot` | `double precision` |  |
| `t_50_to_64_day_to_day_activities_limited_a_little` | `double precision` |  |
| `t_50_to_64_day_to_day_activities_not_limited` | `bigint` |  |
| `uv303b_65_and_over_all_people` | `bigint` |  |
| `t_65_and_over_day_to_day_activities_limited_a_lot` | `double precision` |  |
| `t_65_and_over_day_to_day_activities_limited_a_little` | `double precision` |  |
| `t_65_and_over_day_to_day_activities_not_limited` | `double precision` |  |
| `uv304_all_people` | `bigint` |  |
| `deaf_or_partially_hearing_impaired` | `bigint` |  |
| `blind_or_partially_vision_impaired` | `double precision` |  |
| `full_partial_loss_of_voice_or_difficulty_speaking` | `double precision` |  |
| `has_one_plus_of_learning_disability_learning_difficulty_or_deve` | `bigint` |  |
| `physical_disability` | `bigint` |  |
| `mental_health_condition` | `bigint` |  |
| `long_term_illness_disease_or_condition` | `bigint` |  |
