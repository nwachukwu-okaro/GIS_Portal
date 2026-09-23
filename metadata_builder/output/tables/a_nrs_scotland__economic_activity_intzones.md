# Economic Activity Intzones

## Overview

- **Identifier:** `a_nrs_scotland/economic_activity_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `economic_activity_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 30
- **Metadata status:** source_mapped

## Description

Economic Activity Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to economic activity intzones.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `all_people_aged_16_and_over` | `double precision` | Recorded census measure for the category "all people aged 16 and over" in the represented area. Units and population base require the source table. |
| `economically_active_excluding_full_time_students_total` | `double precision` |  |
| `economically_active_excluding_full_time_students_employee_to` | `double precision` |  |
| `economically_active_excluding_full_time_students_employee_pa` | `double precision` |  |
| `economically_active_excluding_full_time_students_employee_fu` | `double precision` |  |
| `economically_active_excluding_full_time_students_self_employ` | `double precision` |  |
| `economically_active_excluding_full_time_students_self_employ_1` | `double precision` |  |
| `economically_active_excluding_full_time_students_self_employ_2` | `double precision` |  |
| `economically_active_excluding_full_time_students_self_employ_3` | `double precision` |  |
| `economically_active_excluding_full_time_students_self_employ_4` | `double precision` |  |
| `economically_active_excluding_full_time_students_self_employ_5` | `double precision` |  |
| `economically_active_excluding_full_time_students_unemployed_` | `double precision` |  |
| `economically_active_full_time_students_total` | `double precision` |  |
| `economically_active_full_time_students_employee_total` | `double precision` |  |
| `economically_active_full_time_students_employee_part_time` | `double precision` |  |
| `economically_active_full_time_students_employee_full_time` | `double precision` |  |
| `economically_active_full_time_students_self_employed_with_em` | `double precision` |  |
| `economically_active_full_time_students_self_employed_with_em_1` | `double precision` |  |
| `economically_active_full_time_students_self_employed_with_em_2` | `double precision` |  |
| `economically_active_full_time_students_self_employed_without` | `double precision` |  |
| `economically_active_full_time_students_self_employed_without_1` | `double precision` |  |
| `economically_active_full_time_students_self_employed_without_2` | `double precision` |  |
| `economically_active_full_time_students_unemployed_available_` | `double precision` |  |
| `economically_inactive_total` | `double precision` |  |
| `economically_inactive_retired` | `double precision` |  |
| `economically_inactive_student` | `double precision` |  |
| `economically_inactive_looking_after_home_family` | `double precision` |  |
| `economically_inactive_long_term_sick_or_disabled` | `double precision` |  |
| `economically_inactive_other` | `double precision` |  |
