# Census2021 Ts066 Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts066_lsoa`
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
- **Table:** `census2021_ts066_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 34
- **Metadata status:** source_mapped

## Description

Census2021 Ts066 Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts066 lsoa.

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
| `total_all_usual_residents_aged_16_years_and_over` | `bigint` | Recorded census measure for the category "total all usual residents aged 16 years and over" in the represented area. Units and population base require the source table. |
| `economically_active_excluding_full_time_students` | `bigint` |  |
| `economically_active_excluding_full_time_students_in_employment` | `bigint` |  |
| `economically_active_excluding_full_time_students_in_employmen_1` | `bigint` |  |
| `economically_active_excluding_full_time_students_in_employmen_2` | `bigint` |  |
| `economically_active_excluding_full_time_students_in_employmen_3` | `bigint` |  |
| `economically_active_excluding_full_time_students_in_employmen_4` | `bigint` |  |
| `economically_active_excluding_full_time_students_in_employmen_5` | `bigint` |  |
| `economically_active_excluding_full_time_students_in_employmen_6` | `bigint` |  |
| `economically_active_excluding_full_time_students_in_employmen_7` | `bigint` |  |
| `economically_active_excluding_full_time_students_in_employmen_8` | `bigint` |  |
| `economically_active_excluding_full_time_students_in_employmen_9` | `bigint` |  |
| `economically_active_excluding_full_time_students_unemployed` | `bigint` |  |
| `economically_active_and_a_full_time_student` | `bigint` |  |
| `economically_active_and_a_full_time_student_in_employment` | `bigint` |  |
| `economically_active_and_a_full_time_student_in_employment_emplo` | `bigint` |  |
| `economically_active_and_a_full_time_student_in_employment_emp_1` | `bigint` |  |
| `economically_active_and_a_full_time_student_in_employment_emp_2` | `bigint` |  |
| `economically_active_and_a_full_time_student_in_employment_self` | `bigint` |  |
| `economically_active_and_a_full_time_student_in_employment_sel_1` | `bigint` |  |
| `economically_active_and_a_full_time_student_in_employment_sel_2` | `bigint` |  |
| `economically_active_and_a_full_time_student_in_employment_sel_3` | `bigint` |  |
| `economically_active_and_a_full_time_student_in_employment_sel_4` | `bigint` |  |
| `economically_active_and_a_full_time_student_in_employment_sel_5` | `bigint` |  |
| `economically_active_and_a_full_time_student_unemployed` | `bigint` |  |
| `economically_inactive` | `bigint` |  |
| `economically_inactive_retired` | `bigint` |  |
| `economically_inactive_student` | `bigint` |  |
| `economically_inactive_looking_after_home_or_family` | `bigint` |  |
| `economically_inactive_long_term_sick_or_disabled` | `bigint` |  |
| `economically_inactive_other` | `bigint` |  |
