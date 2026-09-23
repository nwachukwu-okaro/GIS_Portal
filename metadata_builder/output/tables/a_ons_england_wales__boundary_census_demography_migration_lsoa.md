# Boundary Census Demography Migration Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/boundary_census_demography_migration_lsoa`
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
- **Table:** `boundary_census_demography_migration_lsoa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 35672
- **Columns:** 182
- **Metadata status:** source_mapped

## Description

Boundary Census Demography Migration Lsoa is an authoritative dataset published by Office for National Statistics. It represents boundary census demography migration lsoa features using geometry geometry.

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
| `residence_type_total` | `bigint` |  |
| `lives_in_a_household` | `bigint` | Recorded census measure for the category "lives in a household" in the represented area. Units and population base require the source table. |
| `lives_in_a_communal_establishment` | `bigint` | Recorded census measure for the category "lives in a communal establishment" in the represented area. Units and population base require the source table. |
| `marital_status_total` | `bigint` |  |
| `never_married_or_cp` | `bigint` |  |
| `married_or_in_a_registered_civil_partnership` | `bigint` |  |
| `married_or_reg_cp_married` | `bigint` |  |
| `married_or_cp_married_opp_sex` | `bigint` |  |
| `married_or_cp_married_same_sex` | `bigint` |  |
| `married_or_reg_cp_in_reg_cp` | `bigint` |  |
| `married_or_cp_reg_opp_sex` | `bigint` |  |
| `married_or_cp_reg_same_sex` | `bigint` |  |
| `sep_still_legally_married_or_in_cp` | `bigint` |  |
| `sep_still_legally_married` | `bigint` |  |
| `sep_still_in_reg_cp` | `bigint` |  |
| `divorced_or_civil_partnership_dissolved` | `bigint` |  |
| `divorced_or_civil_partnership_dissolved_divorced` | `bigint` |  |
| `divorced_or_cp_dissolved` | `bigint` |  |
| `widowed_or_surviving_civil_partnership_partner` | `bigint` |  |
| `widowed_or_surviving_cp_partner_widowed` | `bigint` |  |
| `widowed_or_surviving_cp_partner` | `bigint` |  |
| `hh_composition_total` | `bigint` |  |
| `one_person_household` | `bigint` | Recorded census measure for the category "one person household" in the represented area. Units and population base require the source table. |
| `one_person_household_aged_66_years_and_over` | `bigint` | Recorded census measure for the category "one person household aged 66 years and over" in the represented area. Units and population base require the source table. |
| `one_person_household_other` | `bigint` | Recorded census measure for the category "one person household other" in the represented area. Units and population base require the source table. |
| `single_family_household` | `bigint` |  |
| `single_family_household_all_aged_66_years_and_over` | `bigint` |  |
| `single_family_household_married_or_cp_couple` | `bigint` |  |
| `single_fam_hh_married_or_cp_couple_no_children` | `bigint` |  |
| `single_fam_hh_married_or_cp_couple_dependent_children` | `bigint` |  |
| `single_fam_hh_married_or_cp_non_dep_children` | `bigint` |  |
| `single_family_household_cohabiting_couple_family` | `bigint` |  |
| `single_fam_hh_cohabiting_couple_family_no_children` | `bigint` |  |
| `single_fam_hh_cohabiting_dep_children` | `bigint` |  |
| `single_fam_hh_cohabiting_non_dep_children` | `bigint` |  |
| `single_family_household_lone_parent_family` | `bigint` |  |
| `single_fam_hh_lone_parent_dep_children` | `bigint` |  |
| `single_fam_hh_lone_parent_non_dep_children` | `bigint` |  |
| `single_fam_hh_other_single_fam_hh` | `bigint` |  |
| `single_fam_hh_other_family_composition` | `bigint` |  |
| `other_household_types` | `bigint` |  |
| `other_household_types_with_dependent_children` | `bigint` |  |
| `other_hh_type_incl_students_aged_66_plus` | `bigint` |  |
| `country_of_birth_total` | `bigint` | Recorded census measure for the category "country of birth total" in the represented area. Units and population base require the source table. |
| `europe` | `bigint` |  |
| `europe_united_kingdom` | `bigint` |  |
| `europe_eu_countries` | `bigint` |  |
| `europe_eu_countries_european_union_eu14` | `bigint` |  |
| `europe_eu_countries_european_union_eu8` | `bigint` |  |
| `europe_eu_countries_european_union_eu2` | `bigint` |  |
| `europe_eu_countries_all_other_eu_countries` | `bigint` |  |
| `europe_non_eu_countries` | `bigint` |  |
| `europe_non_eu_countries_all_other_non_eu_countries` | `bigint` |  |
| `africa` | `bigint` |  |
| `middle_east_and_asia` | `bigint` |  |
| `the_americas_and_the_caribbean` | `bigint` |  |
| `antarctica_and_oceania_and_other` | `bigint` |  |
| `british_overseas` | `bigint` |  |
| `passports_held_total` | `bigint` |  |
| `europe_2` | `bigint` |  |
| `europe_united_kingdom_2` | `bigint` |  |
| `europe_ireland` | `bigint` |  |
| `europe_other_europe` | `bigint` |  |
| `europe_other_europe_eu_member_countries` | `bigint` |  |
| `europe_other_europe_eu_member_countries_france` | `bigint` |  |
| `europe_other_europe_eu_member_countries_germany` | `bigint` |  |
| `europe_other_europe_eu_member_countries_italy` | `bigint` |  |
| `europe_other_europe_eu_member_countries_portugal` | `bigint` |  |
| `europe_other_europe_eu_member_countries_spain` | `bigint` |  |
| `europe_other_europe_eu_member_countries_lithuania` | `bigint` |  |
| `europe_other_europe_eu_member_countries_poland` | `bigint` |  |
| `europe_other_europe_eu_member_countries_romania` | `bigint` |  |
| `other_europe_eu_other_countries` | `bigint` |  |
| `europe_other_europe_rest_of_europe` | `bigint` |  |
| `europe_other_europe_rest_of_europe_turkey` | `bigint` |  |
| `europe_other_europe_rest_of_europe_other_europe` | `bigint` |  |
| `africa_2` | `bigint` |  |
| `africa_north_africa` | `bigint` |  |
| `africa_central_and_western_africa` | `bigint` |  |
| `africa_south_and_eastern_africa` | `bigint` |  |
| `middle_east_and_asia_2` | `bigint` |  |
| `middle_east_and_asia_middle_east` | `bigint` |  |
| `middle_east_and_asia_eastern_asia` | `bigint` |  |
| `middle_east_and_asia_southern_asia` | `bigint` |  |
| `middle_east_and_asia_south_east_asia` | `bigint` |  |
| `middle_east_and_asia_central_asia` | `bigint` |  |
| `the_americas_and_the_caribbean_2` | `bigint` |  |
| `americas_north_america_and_caribbean` | `bigint` |  |
| `americas_central_and_south_america` | `bigint` |  |
| `antarctica_and_oceania_including_australasia` | `bigint` |  |
| `british_overseas_territories` | `bigint` |  |
| `no_passport_held` | `bigint` |  |
| `persons_per_square_kilometre` | `double precision` |  |
| `sex_total_t1` | `bigint` |  |
| `female_t1` | `bigint` |  |
| `male_t1` | `bigint` |  |
| `hh_deprivation_total` | `bigint` |  |
| `household_is_not_deprived_in_any_dimension` | `bigint` |  |
| `household_is_deprived_in_one_dimension` | `bigint` |  |
| `household_is_deprived_in_two_dimensions` | `bigint` |  |
| `household_is_deprived_in_three_dimensions` | `bigint` |  |
| `household_is_deprived_in_four_dimensions` | `bigint` |  |
| `year_of_arrival_in_the_uk_total` | `bigint` |  |
| `born_in_the_uk` | `bigint` | Recorded census measure for the category "born in the UK" in the represented area. Units and population base require the source table. |
| `arrived_before_1951` | `bigint` |  |
| `arrived_1951_to_1960` | `bigint` |  |
| `arrived_1961_to_1970` | `bigint` |  |
| `arrived_1971_to_1980` | `bigint` |  |
| `arrived_1981_to_1990` | `bigint` |  |
| `arrived_1991_to_2000` | `bigint` |  |
| `arrived_2001_to_2010` | `bigint` |  |
| `arrived_2011_to_2013` | `bigint` |  |
| `arrived_2014_to_2016` | `bigint` |  |
| `arrived_2017_to_2019` | `bigint` |  |
| `arrived_2020_to_2021` | `bigint` |  |
| `length_of_residence_in_the_uk_total` | `bigint` |  |
| `born_in_the_uk_2` | `bigint` |  |
| `t_10_years_or_more` | `bigint` |  |
| `t_5_years_or_more_but_less_than_10_years` | `bigint` |  |
| `t_2_years_or_more_but_less_than_5_years` | `bigint` |  |
| `less_than_2_years` | `bigint` |  |
| `hh_size_total` | `bigint` |  |
| `t_0_people_in_household` | `bigint` |  |
| `t_1_person_in_household` | `bigint` |  |
| `t_2_people_in_household` | `bigint` |  |
| `t_3_people_in_household` | `bigint` |  |
| `t_4_people_in_household` | `bigint` |  |
| `t_5_people_in_household` | `bigint` |  |
| `t_6_people_in_household` | `bigint` |  |
| `t_7_people_in_household` | `bigint` |  |
| `t_8_or_more_people_in_household` | `bigint` |  |
| `age_total` | `bigint` |  |
| `born_in_the_uk_3` | `bigint` |  |
| `arrived_in_the_uk` | `bigint` |  |
| `arrived_in_the_uk_aged_0_to_4_years` | `bigint` |  |
| `arrived_in_the_uk_aged_5_to_7_years` | `bigint` |  |
| `arrived_in_the_uk_aged_8_to_9_years` | `bigint` |  |
| `arrived_in_the_uk_aged_10_to_14_years` | `bigint` |  |
| `arrived_in_the_uk_aged_15_years` | `bigint` |  |
| `arrived_in_the_uk_aged_16_to_17_years` | `bigint` |  |
| `arrived_in_the_uk_aged_18_to_19_years` | `bigint` |  |
| `arrived_in_the_uk_aged_20_to_24_years` | `bigint` |  |
| `arrived_in_the_uk_aged_25_to_29_years` | `bigint` |  |
| `arrived_in_the_uk_aged_30_to_44_years` | `bigint` |  |
| `arrived_in_the_uk_aged_45_to_59_years` | `bigint` |  |
| `arrived_in_the_uk_aged_60_to_64_years` | `bigint` |  |
| `arrived_in_the_uk_aged_65_to_74_years` | `bigint` |  |
| `arrived_in_the_uk_aged_75_to_84_years` | `bigint` |  |
| `arrived_in_the_uk_aged_85_to_89_years` | `bigint` |  |
| `arrived_in_the_uk_aged_90_years_and_over` | `bigint` |  |
| `migrant_indicator_total` | `bigint` |  |
| `addr_one_yr_ago_is_the_same_as_the_addr_of_enumeration` | `bigint` |  |
| `addr_1yr_ago_student_term_time_uk` | `bigint` |  |
| `migrant_within_uk_addr_1yr_ago_in_uk` | `bigint` |  |
| `migrant_outside_uk_addr_1yr_ago_outside_uk` | `bigint` |  |
| `sex_total_t2` | `bigint` |  |
| `female_t2` | `bigint` |  |
| `male_t2` | `bigint` |  |
| `number_of_households` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `total` | `integer` |  |
| `aged_4_years_and_under` | `integer` |  |
| `aged_5_to_9_years` | `integer` |  |
| `aged_10_to_14_years` | `integer` |  |
| `aged_15_to_19_years` | `integer` |  |
| `aged_20_to_24_years` | `integer` |  |
| `aged_25_to_29_years` | `integer` |  |
| `aged_30_to_34_years` | `integer` |  |
| `aged_35_to_39_years` | `integer` |  |
| `aged_40_to_44_years` | `integer` |  |
| `aged_45_to_49_years` | `integer` |  |
| `aged_50_to_54_years` | `integer` |  |
| `aged_55_to_59_years` | `integer` |  |
| `aged_60_to_64_years` | `integer` |  |
| `aged_65_to_69_years` | `integer` |  |
| `aged_70_to_74_years` | `integer` |  |
| `aged_75_to_79_years` | `integer` |  |
| `aged_80_to_84_years` | `integer` |  |
| `aged_85_years_and_over` | `integer` |  |
