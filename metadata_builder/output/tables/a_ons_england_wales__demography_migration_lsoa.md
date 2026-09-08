# Demography Migration Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/demography_migration_lsoa`
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
- **Table:** `demography_migration_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 162
- **Metadata status:** source_mapped

## Description

Demography Migration Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to demography migration lsoa.

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
| `residence_type_total` | `bigint` | Count or numeric value for residence type total in the represented area. |
| `lives_in_a_household` | `bigint` | Count or numeric value for lives in a household in the represented area. |
| `lives_in_a_communal_establishment` | `bigint` | Count or numeric value for lives in a communal establishment in the represented area. |
| `marital_status_total` | `bigint` | Count or numeric value for marital status total in the represented area. |
| `never_married_or_cp` | `bigint` | Count or numeric value for never married or cp in the represented area. |
| `married_or_in_a_registered_civil_partnership` | `bigint` | Count or numeric value for married or in a registered civil partnership in the represented area. |
| `married_or_reg_cp_married` | `bigint` | Count or numeric value for married or reg cp married in the represented area. |
| `married_or_cp_married_opp_sex` | `bigint` | Count or numeric value for married or cp married opp sex in the represented area. |
| `married_or_cp_married_same_sex` | `bigint` | Count or numeric value for married or cp married same sex in the represented area. |
| `married_or_reg_cp_in_reg_cp` | `bigint` | Count or numeric value for married or reg cp in reg cp in the represented area. |
| `married_or_cp_reg_opp_sex` | `bigint` | Count or numeric value for married or cp reg opp sex in the represented area. |
| `married_or_cp_reg_same_sex` | `bigint` | Count or numeric value for married or cp reg same sex in the represented area. |
| `sep_still_legally_married_or_in_cp` | `bigint` | Count or numeric value for sep still legally married or in cp in the represented area. |
| `sep_still_legally_married` | `bigint` | Count or numeric value for sep still legally married in the represented area. |
| `sep_still_in_reg_cp` | `bigint` | Count or numeric value for sep still in reg cp in the represented area. |
| `divorced_or_civil_partnership_dissolved` | `bigint` | Count or numeric value for divorced or civil partnership dissolved in the represented area. |
| `divorced_or_civil_partnership_dissolved_divorced` | `bigint` | Count or numeric value for divorced or civil partnership dissolved divorced in the represented area. |
| `divorced_or_cp_dissolved` | `bigint` | Count or numeric value for divorced or cp dissolved in the represented area. |
| `widowed_or_surviving_civil_partnership_partner` | `bigint` | Count or numeric value for widowed or surviving civil partnership partner in the represented area. |
| `widowed_or_surviving_cp_partner_widowed` | `bigint` | Count or numeric value for widowed or surviving cp partner widowed in the represented area. |
| `widowed_or_surviving_cp_partner` | `bigint` | Count or numeric value for widowed or surviving cp partner in the represented area. |
| `hh_composition_total` | `bigint` | Count or numeric value for households composition total in the represented area. |
| `one_person_household` | `bigint` | Count or numeric value for one person household in the represented area. |
| `one_person_household_aged_66_years_and_over` | `bigint` | Count or numeric value for one person household aged 66 years and over in the represented area. |
| `one_person_household_other` | `bigint` | Count or numeric value for one person household other in the represented area. |
| `single_family_household` | `bigint` | Count or numeric value for single family household in the represented area. |
| `single_family_household_all_aged_66_years_and_over` | `bigint` | Count or numeric value for single family household all aged 66 years and over in the represented area. |
| `single_family_household_married_or_cp_couple` | `bigint` | Count or numeric value for single family household married or cp couple in the represented area. |
| `single_fam_hh_married_or_cp_couple_no_children` | `bigint` | Count or numeric value for single fam households married or cp couple number children in the represented area. |
| `single_fam_hh_married_or_cp_couple_dependent_children` | `bigint` | Count or numeric value for single fam households married or cp couple dependent children in the represented area. |
| `single_fam_hh_married_or_cp_non_dep_children` | `bigint` | Count or numeric value for single fam households married or cp non dep children in the represented area. |
| `single_family_household_cohabiting_couple_family` | `bigint` | Count or numeric value for single family household cohabiting couple family in the represented area. |
| `single_fam_hh_cohabiting_couple_family_no_children` | `bigint` | Count or numeric value for single fam households cohabiting couple family number children in the represented area. |
| `single_fam_hh_cohabiting_dep_children` | `bigint` | Count or numeric value for single fam households cohabiting dep children in the represented area. |
| `single_fam_hh_cohabiting_non_dep_children` | `bigint` | Count or numeric value for single fam households cohabiting non dep children in the represented area. |
| `single_family_household_lone_parent_family` | `bigint` | Numeric single family household lone parent family value recorded for the feature. |
| `single_fam_hh_lone_parent_dep_children` | `bigint` | Numeric single fam households lone parent dep children value recorded for the feature. |
| `single_fam_hh_lone_parent_non_dep_children` | `bigint` | Numeric single fam households lone parent non dep children value recorded for the feature. |
| `single_fam_hh_other_single_fam_hh` | `bigint` | Count or numeric value for single fam households other single fam households in the represented area. |
| `single_fam_hh_other_family_composition` | `bigint` | Count or numeric value for single fam households other family composition in the represented area. |
| `other_household_types` | `bigint` | Count or numeric value for other household types in the represented area. |
| `other_household_types_with_dependent_children` | `bigint` | Count or numeric value for other household types with dependent children in the represented area. |
| `other_hh_type_incl_students_aged_66_plus` | `bigint` | Count or numeric value for other households type incl students aged 66 plus in the represented area. |
| `country_of_birth_total` | `bigint` | Count or numeric value for country of birth total in the represented area. |
| `europe` | `bigint` | Count or numeric value for europe in the represented area. |
| `europe_united_kingdom` | `bigint` | Count or numeric value for europe united kingdom in the represented area. |
| `europe_eu_countries` | `bigint` | Count or numeric value for europe eu countries in the represented area. |
| `europe_eu_countries_european_union_eu14` | `bigint` | Count or numeric value for europe eu countries european union eu14 in the represented area. |
| `europe_eu_countries_european_union_eu8` | `bigint` | Count or numeric value for europe eu countries european union eu8 in the represented area. |
| `europe_eu_countries_european_union_eu2` | `bigint` | Count or numeric value for europe eu countries european union eu2 in the represented area. |
| `europe_eu_countries_all_other_eu_countries` | `bigint` | Count or numeric value for europe eu countries all other eu countries in the represented area. |
| `europe_non_eu_countries` | `bigint` | Count or numeric value for europe non eu countries in the represented area. |
| `europe_non_eu_countries_all_other_non_eu_countries` | `bigint` | Count or numeric value for europe non eu countries all other non eu countries in the represented area. |
| `africa` | `bigint` | Count or numeric value for africa in the represented area. |
| `middle_east_and_asia` | `bigint` | Count or numeric value for middle east and asia in the represented area. |
| `the_americas_and_the_caribbean` | `bigint` | Count or numeric value for the americas and the caribbean in the represented area. |
| `antarctica_and_oceania_and_other` | `bigint` | Count or numeric value for antarctica and oceania and other in the represented area. |
| `british_overseas` | `bigint` | Count or numeric value for british overseas in the represented area. |
| `passports_held_total` | `bigint` | Count or numeric value for passports held total in the represented area. |
| `europe_2` | `bigint` | Count or numeric value for europe 2 in the represented area. |
| `europe_united_kingdom_2` | `bigint` | Count or numeric value for europe united kingdom 2 in the represented area. |
| `europe_ireland` | `bigint` | Count or numeric value for europe ireland in the represented area. |
| `europe_other_europe` | `bigint` | Count or numeric value for europe other europe in the represented area. |
| `europe_other_europe_eu_member_countries` | `bigint` | Count or numeric value for europe other europe eu member countries in the represented area. |
| `europe_other_europe_eu_member_countries_france` | `bigint` | Count or numeric value for europe other europe eu member countries france in the represented area. |
| `europe_other_europe_eu_member_countries_germany` | `bigint` | Count or numeric value for europe other europe eu member countries germany in the represented area. |
| `europe_other_europe_eu_member_countries_italy` | `bigint` | Count or numeric value for europe other europe eu member countries italy in the represented area. |
| `europe_other_europe_eu_member_countries_portugal` | `bigint` | Count or numeric value for europe other europe eu member countries portugal in the represented area. |
| `europe_other_europe_eu_member_countries_spain` | `bigint` | Count or numeric value for europe other europe eu member countries spain in the represented area. |
| `europe_other_europe_eu_member_countries_lithuania` | `bigint` | Count or numeric value for europe other europe eu member countries lithuania in the represented area. |
| `europe_other_europe_eu_member_countries_poland` | `bigint` | Count or numeric value for europe other europe eu member countries poland in the represented area. |
| `europe_other_europe_eu_member_countries_romania` | `bigint` | Count or numeric value for europe other europe eu member countries romania in the represented area. |
| `other_europe_eu_other_countries` | `bigint` | Count or numeric value for other europe eu other countries in the represented area. |
| `europe_other_europe_rest_of_europe` | `bigint` | Count or numeric value for europe other europe rest of europe in the represented area. |
| `europe_other_europe_rest_of_europe_turkey` | `bigint` | Count or numeric value for europe other europe rest of europe turkey in the represented area. |
| `europe_other_europe_rest_of_europe_other_europe` | `bigint` | Count or numeric value for europe other europe rest of europe other europe in the represented area. |
| `africa_2` | `bigint` | Count or numeric value for africa 2 in the represented area. |
| `africa_north_africa` | `bigint` | Count or numeric value for africa north africa in the represented area. |
| `africa_central_and_western_africa` | `bigint` | Count or numeric value for africa central and western africa in the represented area. |
| `africa_south_and_eastern_africa` | `bigint` | Count or numeric value for africa south and eastern africa in the represented area. |
| `middle_east_and_asia_2` | `bigint` | Count or numeric value for middle east and asia 2 in the represented area. |
| `middle_east_and_asia_middle_east` | `bigint` | Count or numeric value for middle east and asia middle east in the represented area. |
| `middle_east_and_asia_eastern_asia` | `bigint` | Count or numeric value for middle east and asia eastern asia in the represented area. |
| `middle_east_and_asia_southern_asia` | `bigint` | Count or numeric value for middle east and asia southern asia in the represented area. |
| `middle_east_and_asia_south_east_asia` | `bigint` | Count or numeric value for middle east and asia south east asia in the represented area. |
| `middle_east_and_asia_central_asia` | `bigint` | Count or numeric value for middle east and asia central asia in the represented area. |
| `the_americas_and_the_caribbean_2` | `bigint` | Count or numeric value for the americas and the caribbean 2 in the represented area. |
| `americas_north_america_and_caribbean` | `bigint` | Count or numeric value for americas north america and caribbean in the represented area. |
| `americas_central_and_south_america` | `bigint` | Count or numeric value for americas central and south america in the represented area. |
| `antarctica_and_oceania_including_australasia` | `bigint` | Count or numeric value for antarctica and oceania including australasia in the represented area. |
| `british_overseas_territories` | `bigint` | Count or numeric value for british overseas territories in the represented area. |
| `no_passport_held` | `bigint` | Count or numeric value for number passport held in the represented area. |
| `persons_per_square_kilometre` | `double precision` | Count or numeric value for persons per square kilometre in the represented area. |
| `sex_total_t1` | `bigint` | Count or numeric value for sex total t1 in the represented area. |
| `female_t1` | `bigint` | Count or numeric value for female t1 in the represented area. |
| `male_t1` | `bigint` | Count or numeric value for male t1 in the represented area. |
| `hh_deprivation_total` | `bigint` | Count or numeric value for households deprivation total in the represented area. |
| `household_is_not_deprived_in_any_dimension` | `bigint` | Count or numeric value for household is not deprived in any dimension in the represented area. |
| `household_is_deprived_in_one_dimension` | `bigint` | Count or numeric value for household is deprived in one dimension in the represented area. |
| `household_is_deprived_in_two_dimensions` | `bigint` | Count or numeric value for household is deprived in two dimensions in the represented area. |
| `household_is_deprived_in_three_dimensions` | `bigint` | Count or numeric value for household is deprived in three dimensions in the represented area. |
| `household_is_deprived_in_four_dimensions` | `bigint` | Count or numeric value for household is deprived in four dimensions in the represented area. |
| `year_of_arrival_in_the_uk_total` | `bigint` | Count or numeric value for year of arrival in the uk total in the represented area. |
| `born_in_the_uk` | `bigint` | Count or numeric value for born in the uk in the represented area. |
| `arrived_before_1951` | `bigint` | Count or numeric value for arrived before 1951 in the represented area. |
| `arrived_1951_to_1960` | `bigint` | Count or numeric value for arrived 1951 to 1960 in the represented area. |
| `arrived_1961_to_1970` | `bigint` | Count or numeric value for arrived 1961 to 1970 in the represented area. |
| `arrived_1971_to_1980` | `bigint` | Count or numeric value for arrived 1971 to 1980 in the represented area. |
| `arrived_1981_to_1990` | `bigint` | Count or numeric value for arrived 1981 to 1990 in the represented area. |
| `arrived_1991_to_2000` | `bigint` | Count or numeric value for arrived 1991 to 2000 in the represented area. |
| `arrived_2001_to_2010` | `bigint` | Count or numeric value for arrived 2001 to 2010 in the represented area. |
| `arrived_2011_to_2013` | `bigint` | Count or numeric value for arrived 2011 to 2013 in the represented area. |
| `arrived_2014_to_2016` | `bigint` | Count or numeric value for arrived 2014 to 2016 in the represented area. |
| `arrived_2017_to_2019` | `bigint` | Count or numeric value for arrived 2017 to 2019 in the represented area. |
| `arrived_2020_to_2021` | `bigint` | Count or numeric value for arrived 2020 to 2021 in the represented area. |
| `length_of_residence_in_the_uk_total` | `bigint` | Numeric length of residence in the uk total value recorded for the feature. |
| `born_in_the_uk_2` | `bigint` | Count or numeric value for born in the uk 2 in the represented area. |
| `t_10_years_or_more` | `bigint` | Count or numeric value for t 10 years or more in the represented area. |
| `t_5_years_or_more_but_less_than_10_years` | `bigint` | Count or numeric value for t 5 years or more but less than 10 years in the represented area. |
| `t_2_years_or_more_but_less_than_5_years` | `bigint` | Count or numeric value for t 2 years or more but less than 5 years in the represented area. |
| `less_than_2_years` | `bigint` | Count or numeric value for less than 2 years in the represented area. |
| `hh_size_total` | `bigint` | Count or numeric value for households size total in the represented area. |
| `t_0_people_in_household` | `bigint` | Count or numeric value for t 0 people in household in the represented area. |
| `t_1_person_in_household` | `bigint` | Count or numeric value for t 1 person in household in the represented area. |
| `t_2_people_in_household` | `bigint` | Count or numeric value for t 2 people in household in the represented area. |
| `t_3_people_in_household` | `bigint` | Count or numeric value for t 3 people in household in the represented area. |
| `t_4_people_in_household` | `bigint` | Count or numeric value for t 4 people in household in the represented area. |
| `t_5_people_in_household` | `bigint` | Count or numeric value for t 5 people in household in the represented area. |
| `t_6_people_in_household` | `bigint` | Count or numeric value for t 6 people in household in the represented area. |
| `t_7_people_in_household` | `bigint` | Count or numeric value for t 7 people in household in the represented area. |
| `t_8_or_more_people_in_household` | `bigint` | Count or numeric value for t 8 or more people in household in the represented area. |
| `age_total` | `bigint` | Count or numeric value for age total in the represented area. |
| `born_in_the_uk_3` | `bigint` | Count or numeric value for born in the uk 3 in the represented area. |
| `arrived_in_the_uk` | `bigint` | Count or numeric value for arrived in the uk in the represented area. |
| `arrived_in_the_uk_aged_0_to_4_years` | `bigint` | Count or numeric value for arrived in the uk aged 0 to 4 years in the represented area. |
| `arrived_in_the_uk_aged_5_to_7_years` | `bigint` | Count or numeric value for arrived in the uk aged 5 to 7 years in the represented area. |
| `arrived_in_the_uk_aged_8_to_9_years` | `bigint` | Count or numeric value for arrived in the uk aged 8 to 9 years in the represented area. |
| `arrived_in_the_uk_aged_10_to_14_years` | `bigint` | Count or numeric value for arrived in the uk aged 10 to 14 years in the represented area. |
| `arrived_in_the_uk_aged_15_years` | `bigint` | Count or numeric value for arrived in the uk aged 15 years in the represented area. |
| `arrived_in_the_uk_aged_16_to_17_years` | `bigint` | Count or numeric value for arrived in the uk aged 16 to 17 years in the represented area. |
| `arrived_in_the_uk_aged_18_to_19_years` | `bigint` | Count or numeric value for arrived in the uk aged 18 to 19 years in the represented area. |
| `arrived_in_the_uk_aged_20_to_24_years` | `bigint` | Count or numeric value for arrived in the uk aged 20 to 24 years in the represented area. |
| `arrived_in_the_uk_aged_25_to_29_years` | `bigint` | Count or numeric value for arrived in the uk aged 25 to 29 years in the represented area. |
| `arrived_in_the_uk_aged_30_to_44_years` | `bigint` | Count or numeric value for arrived in the uk aged 30 to 44 years in the represented area. |
| `arrived_in_the_uk_aged_45_to_59_years` | `bigint` | Count or numeric value for arrived in the uk aged 45 to 59 years in the represented area. |
| `arrived_in_the_uk_aged_60_to_64_years` | `bigint` | Count or numeric value for arrived in the uk aged 60 to 64 years in the represented area. |
| `arrived_in_the_uk_aged_65_to_74_years` | `bigint` | Count or numeric value for arrived in the uk aged 65 to 74 years in the represented area. |
| `arrived_in_the_uk_aged_75_to_84_years` | `bigint` | Count or numeric value for arrived in the uk aged 75 to 84 years in the represented area. |
| `arrived_in_the_uk_aged_85_to_89_years` | `bigint` | Count or numeric value for arrived in the uk aged 85 to 89 years in the represented area. |
| `arrived_in_the_uk_aged_90_years_and_over` | `bigint` | Count or numeric value for arrived in the uk aged 90 years and over in the represented area. |
| `migrant_indicator_total` | `bigint` | Count or numeric value for migrant indicator total in the represented area. |
| `addr_one_yr_ago_is_the_same_as_the_addr_of_enumeration` | `bigint` | Count or numeric value for addr one year ago is the same as the addr of enumeration in the represented area. |
| `addr_1yr_ago_student_term_time_uk` | `bigint` | Count or numeric value for addr 1yr ago student term time uk in the represented area. |
| `migrant_within_uk_addr_1yr_ago_in_uk` | `bigint` | Count or numeric value for migrant within uk addr 1yr ago in uk in the represented area. |
| `migrant_outside_uk_addr_1yr_ago_outside_uk` | `bigint` | Count or numeric value for migrant outside uk addr 1yr ago outside uk in the represented area. |
| `sex_total_t2` | `bigint` | Count or numeric value for sex total t2 in the represented area. |
| `female_t2` | `bigint` | Count or numeric value for female t2 in the represented area. |
| `male_t2` | `bigint` | Count or numeric value for male t2 in the represented area. |
| `number_of_households` | `bigint` | Count or numeric value for number of households in the represented area. |
