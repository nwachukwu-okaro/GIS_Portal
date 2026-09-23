# Ethnicity Identity Language Religion Oa

## Overview

- **Identifier:** `a_ons_england_wales/ethnicity_identity_language_religion_oa`
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
- **Table:** `ethnicity_identity_language_religion_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 188880
- **Columns:** 82
- **Metadata status:** source_mapped

## Description

Ethnicity Identity Language Religion Oa is an authoritative dataset published by Office for National Statistics. It contains records relating to ethnicity identity language religion oa.

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
| `ethnic_group_total` | `bigint` | Recorded census measure for the category "ethnic group total" in the represented area. Units and population base require the source table. |
| `asian_british_or_asian_welsh` | `bigint` |  |
| `asian_british_or_asian_welsh_bangladeshi` | `bigint` |  |
| `asian_british_or_asian_welsh_chinese` | `bigint` |  |
| `asian_british_or_asian_welsh_indian` | `bigint` |  |
| `asian_british_or_asian_welsh_pakistani` | `bigint` |  |
| `asian_british_or_asian_welsh_other_asian` | `bigint` |  |
| `black_british_black_welsh_caribbean_or_african` | `bigint` |  |
| `black_british_black_welsh_caribbean_or_african_2` | `bigint` |  |
| `black_british_welsh_caribbean` | `bigint` |  |
| `black_british_welsh_caribbean_or_african_other` | `bigint` |  |
| `mixed_or_multiple_ethnic_groups` | `bigint` |  |
| `mixed_or_multiple_ethnic_groups_white_and_asian` | `bigint` |  |
| `mixed_ethnic_white_and_black_african` | `bigint` |  |
| `mixed_ethnic_white_and_black_caribbean` | `bigint` |  |
| `mixed_ethnic_other_mixed_ethnic` | `bigint` |  |
| `white` | `bigint` |  |
| `white_english_welsh_scottish_northern_irish_or_british` | `bigint` |  |
| `white_irish` | `bigint` |  |
| `white_gypsy_or_irish_traveller` | `bigint` |  |
| `white_roma` | `bigint` |  |
| `white_other_white` | `bigint` |  |
| `other_ethnic_group` | `bigint` |  |
| `other_ethnic_group_arab` | `bigint` |  |
| `other_ethnic_group_any_other_ethnic_group` | `bigint` |  |
| `multi_ethnic_hh_total` | `bigint` |  |
| `one_person_household` | `bigint` | Recorded census measure for the category "one person household" in the represented area. Units and population base require the source table. |
| `all_household_members_have_the_same_ethnic_group` | `bigint` |  |
| `ethnic_grp_differs_between_generations` | `bigint` |  |
| `ethnic_groups_differ_within_partnerships` | `bigint` |  |
| `any_other_combination_of_multiple_ethnic_identities` | `bigint` |  |
| `household_language_total` | `bigint` |  |
| `all_adults_hh_eng_or_welsh_main_lang` | `bigint` |  |
| `some_adults_hh_eng_or_welsh_main_lang` | `bigint` |  |
| `no_adults_hh_child_3_15_eng_or_welsh_lang` | `bigint` |  |
| `no_people_hh_eng_or_welsh_main_lang` | `bigint` |  |
| `multi_lang_hh_total` | `bigint` |  |
| `one_person_household_2` | `bigint` |  |
| `all_household_members_have_the_same_main_language` | `bigint` |  |
| `main_lang_differs_between_generations` | `bigint` |  |
| `main_language_differs_within_partnerships` | `bigint` |  |
| `any_other_combination_of_multiple_main_languages` | `bigint` |  |
| `national_identity_total` | `bigint` |  |
| `british_only_identity` | `bigint` |  |
| `english_only_identity` | `bigint` |  |
| `english_and_british_only_identity` | `bigint` |  |
| `welsh_only_identity` | `bigint` |  |
| `welsh_and_british_only_identity` | `bigint` |  |
| `any_other_combination_of_only_uk_identities` | `bigint` |  |
| `scottish_only_identity` | `bigint` |  |
| `scottish_and_british_only_identity` | `bigint` |  |
| `northern_irish_only_identity` | `bigint` |  |
| `northern_irish_and_british_only_identity` | `bigint` |  |
| `cornish_only_identity` | `bigint` |  |
| `cornish_and_british_only_identity` | `bigint` |  |
| `any_other_combination_of_only_uk_identities_2` | `bigint` |  |
| `irish_only_identity` | `bigint` |  |
| `irish_and_at_least_one_uk_identity` | `bigint` |  |
| `other_identity_only` | `bigint` |  |
| `other_identity_and_at_least_one_uk_identity` | `bigint` |  |
| `non_uk_identity_only` | `bigint` |  |
| `uk_identity_and_non_uk_identity` | `bigint` |  |
| `proficiency_in_english_language_total` | `bigint` |  |
| `main_language_is_english` | `bigint` |  |
| `main_language_is_not_english` | `bigint` |  |
| `non_english_main_lang_speaks_eng_very_well` | `bigint` |  |
| `main_language_is_not_english_can_speak_english_well` | `bigint` |  |
| `main_language_is_not_english_cannot_speak_english_well` | `bigint` |  |
| `main_language_is_not_english_cannot_speak_english` | `bigint` |  |
| `religion_total` | `bigint` | Recorded census measure for the category "religion total" in the represented area. Units and population base require the source table. |
| `no_religion` | `bigint` |  |
| `christian` | `bigint` |  |
| `buddhist` | `bigint` |  |
| `hindu` | `bigint` |  |
| `jewish` | `bigint` |  |
| `muslim` | `bigint` |  |
| `sikh` | `bigint` |  |
| `other_religion` | `bigint` |  |
| `not_answered` | `bigint` |  |
