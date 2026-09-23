# Boundary Census Scotland Ethnicity Identity Language Religion I

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_ethnicity_identity_language_religion_i`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.650007, 54.633238, -0.724609, 60.860766]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_census_scotland_ethnicity_identity_language_religion_i`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1280
- **Columns:** 92
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Ethnicity Identity Language Religion I is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland ethnicity identity language religion i features using multipolygon geometry.

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
| `ethnic_group_all_people` | `bigint` | Recorded census measure for the category "ethnic group all people" in the represented area. Units and population base require the source table. |
| `white_total` | `bigint` |  |
| `white_white_scottish` | `bigint` |  |
| `white_other_white_british` | `bigint` |  |
| `white_white_irish` | `bigint` |  |
| `white_gypsy_traveller` | `bigint` |  |
| `white_white_polish` | `bigint` |  |
| `other_white` | `bigint` |  |
| `mixed_or_multiple_ethnic_group` | `bigint` |  |
| `asian_asian_scottish_or_asian_british_total` | `bigint` |  |
| `asian_pakistani` | `bigint` |  |
| `asian_indian` | `bigint` |  |
| `asian_bangladeshi` | `bigint` |  |
| `asian_chinese` | `bigint` |  |
| `asian_asian_scottish_or_asian_british_other_asian` | `bigint` |  |
| `african_total` | `bigint` |  |
| `african_african_scottish_or_british` | `bigint` |  |
| `african_other_african` | `bigint` |  |
| `caribbean_or_black_total` | `bigint` |  |
| `black_caribbean` | `bigint` |  |
| `black_black` | `bigint` |  |
| `caribbean_or_black_other_caribbean_or_black` | `bigint` |  |
| `other_ethnic_groups_total` | `bigint` |  |
| `other_ethnic_arab` | `bigint` |  |
| `other_ethnic_groups_other_ethnic_group` | `bigint` |  |
| `all_occupied_households` | `bigint` | Recorded census measure for the category "all occupied households" in the represented area. Units and population base require the source table. |
| `one_person_household` | `bigint` | Recorded census measure for the category "one person household" in the represented area. Units and population base require the source table. |
| `all_household_members_have_the_same_ethnic_group` | `bigint` |  |
| `different_identities_between_the_generations_only` | `bigint` |  |
| `diff_identities_within_partnerships` | `bigint` |  |
| `other_multiple_ethnic_combo` | `bigint` |  |
| `national_identity_all_people` | `bigint` |  |
| `scottish_identity_only` | `bigint` |  |
| `british_identity_only` | `bigint` |  |
| `scottish_and_british_identities_only` | `bigint` |  |
| `scottish_and_any_other_identities` | `bigint` |  |
| `english_identity_only` | `bigint` |  |
| `any_other_combination_of_uk_identities_uk_only` | `bigint` |  |
| `other_identity_only_1` | `bigint` |  |
| `other_identity_and_at_least_one_uk_identity` | `bigint` |  |
| `bsl_all_people_aged_3_and_over` | `bigint` |  |
| `bsl_user` | `bigint` |  |
| `not_a_bsl_user` | `bigint` |  |
| `gaelic_all_people_aged_3_and_over` | `bigint` |  |
| `understands_only_gaelic` | `bigint` |  |
| `speaks_reads_and_writes_gaelic` | `bigint` | Recorded census measure for the category "speaks reads and writes gaelic" in the represented area. Units and population base require the source table. |
| `speaks_but_does_not_read_or_write_gaelic` | `bigint` | Recorded census measure for the category "speaks but does not read or write gaelic" in the represented area. Units and population base require the source table. |
| `speaks_and_reads_but_does_not_write_gaelic` | `bigint` | Recorded census measure for the category "speaks and reads but does not write gaelic" in the represented area. Units and population base require the source table. |
| `reads_but_does_not_speak_or_write_gaelic` | `bigint` | Recorded census measure for the category "reads but does not speak or write gaelic" in the represented area. Units and population base require the source table. |
| `other_combination_of_skills_in_gaelic` | `bigint` |  |
| `no_skills_in_gaelic` | `bigint` |  |
| `english_lang_all_people_aged_3_and_over` | `bigint` |  |
| `understands_spoken_english_only` | `bigint` |  |
| `speaks_reads_and_writes_english` | `bigint` | Recorded census measure for the category "speaks reads and writes english" in the represented area. Units and population base require the source table. |
| `speaks_but_does_not_read_or_write_english` | `bigint` | Recorded census measure for the category "speaks but does not read or write english" in the represented area. Units and population base require the source table. |
| `speaks_and_reads_but_does_not_write_english` | `bigint` | Recorded census measure for the category "speaks and reads but does not write english" in the represented area. Units and population base require the source table. |
| `reads_but_does_not_speak_or_write_english` | `bigint` | Recorded census measure for the category "reads but does not speak or write english" in the represented area. Units and population base require the source table. |
| `writes_but_does_not_speak_or_read_english` | `bigint` | Recorded census measure for the category "writes but does not speak or read english" in the represented area. Units and population base require the source table. |
| `reads_and_writes_but_does_not_speak_english` | `bigint` | Recorded census measure for the category "reads and writes but does not speak english" in the represented area. Units and population base require the source table. |
| `other_combinations_of_skills_in_english` | `bigint` |  |
| `limited_english_skills` | `bigint` |  |
| `no_skills_in_english` | `bigint` |  |
| `main_language_all_people_aged_3_and_over` | `bigint` |  |
| `english` | `bigint` |  |
| `scots` | `bigint` |  |
| `gaelic` | `bigint` |  |
| `sign_language` | `bigint` |  |
| `other_language` | `bigint` |  |
| `scots_lang_all_people_aged_3_and_over` | `bigint` |  |
| `understands_but_does_not_speak_read_or_write_scots` | `bigint` |  |
| `speaks_reads_and_writes_scots` | `bigint` | Recorded census measure for the category "speaks reads and writes scots" in the represented area. Units and population base require the source table. |
| `speaks_but_does_not_read_or_write_scots` | `bigint` | Recorded census measure for the category "speaks but does not read or write scots" in the represented area. Units and population base require the source table. |
| `speaks_and_reads_but_does_not_write_scots` | `bigint` | Recorded census measure for the category "speaks and reads but does not write scots" in the represented area. Units and population base require the source table. |
| `reads_but_does_not_speak_or_write_scots` | `bigint` | Recorded census measure for the category "reads but does not speak or write scots" in the represented area. Units and population base require the source table. |
| `other_combination_of_skills_in_scots` | `bigint` |  |
| `no_skills_in_scots` | `bigint` |  |
| `religion_all_people` | `bigint` | Recorded census measure for the category "religion all people" in the represented area. Units and population base require the source table. |
| `church_of_scotland` | `bigint` |  |
| `roman_catholic` | `bigint` |  |
| `other_christian` | `bigint` |  |
| `buddhist` | `bigint` |  |
| `hindu` | `bigint` |  |
| `jewish` | `bigint` |  |
| `muslim` | `bigint` |  |
| `sikh` | `bigint` |  |
| `pagan` | `bigint` |  |
| `other_religion` | `bigint` |  |
| `no_religion` | `bigint` |  |
| `religion_not_stated` | `bigint` | Recorded census measure for the category "religion not stated" in the represented area. Units and population base require the source table. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
