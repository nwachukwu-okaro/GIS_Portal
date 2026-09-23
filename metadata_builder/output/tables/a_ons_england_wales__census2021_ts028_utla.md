# Census2021 Ts028 Utla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts028_utla`
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
- **Table:** `census2021_ts028_utla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 174
- **Columns:** 94
- **Metadata status:** source_mapped

## Description

Census2021 Ts028 Utla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts028 utla.

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
| `total_all_usual_residents` | `bigint` | Census total for all usual residents in the represented geographical area; measurement unit requires the table documentation. |
| `uk_identity` | `bigint` |  |
| `uk_identity_british_only_identity` | `bigint` |  |
| `uk_identity_english_only_identity` | `bigint` |  |
| `uk_identity_english_and_british_only_identity` | `bigint` |  |
| `uk_identity_welsh_only_identity` | `bigint` |  |
| `uk_identity_welsh_and_british_only_identity` | `bigint` |  |
| `uk_identity_scottish_only_identity` | `bigint` |  |
| `uk_identity_scottish_and_british_only_identity` | `bigint` |  |
| `uk_identity_northern_irish_only_identity` | `bigint` |  |
| `uk_identity_northern_irish_and_british_only_identity` | `bigint` |  |
| `uk_identity_cornish_only_identity` | `bigint` |  |
| `uk_identity_cornish_and_british_only_identity` | `bigint` |  |
| `uk_identity_any_other_combination_of_uk_identities_uk_only` | `bigint` |  |
| `uk_identity_other_identity_and_at_least_one_uk_identity` | `bigint` |  |
| `other_identity_only` | `bigint` |  |
| `other_identity_only_guernsey_islander` | `bigint` |  |
| `other_identity_only_jersey_islander` | `bigint` |  |
| `other_identity_only_isle_of_man_manx` | `bigint` |  |
| `other_identity_only_channel_islander_not_otherwise_specified` | `bigint` |  |
| `other_identity_only_irish_only_identity` | `bigint` |  |
| `other_identity_only_irish_and_at_least_one_uk_identity` | `bigint` |  |
| `other_identity_only_european` | `bigint` |  |
| `other_identity_only_european_eu_countries` | `bigint` |  |
| `other_identity_only_european_eu_countries_french` | `bigint` |  |
| `other_identity_only_european_eu_countries_german` | `bigint` |  |
| `other_identity_only_european_eu_countries_italian` | `bigint` |  |
| `other_identity_only_european_eu_countries_portuguese` | `bigint` |  |
| `other_identity_only_european_eu_countries_spanish_including_can` | `bigint` |  |
| `other_identity_only_european_eu_countries_other_member_countrie` | `bigint` |  |
| `other_identity_only_european_eu_countries_lithuanian` | `bigint` |  |
| `other_identity_only_european_eu_countries_polish` | `bigint` |  |
| `other_identity_only_european_eu_countries_romanian` | `bigint` |  |
| `other_identity_only_european_eu_countries_other_member_countr_1` | `bigint` |  |
| `other_identity_only_european_non_eu_countries` | `bigint` |  |
| `other_identity_only_european_non_eu_countries_turkish` | `bigint` |  |
| `other_identity_only_european_non_eu_countries_other_european` | `bigint` |  |
| `other_identity_only_african` | `bigint` |  |
| `other_identity_only_african_north_african` | `bigint` |  |
| `other_identity_only_african_central_and_western_african` | `bigint` |  |
| `other_identity_only_african_central_and_western_african_ghanaia` | `bigint` |  |
| `other_identity_only_african_central_and_western_african_nigeria` | `bigint` |  |
| `other_identity_only_african_central_and_western_african_other_c` | `bigint` |  |
| `other_identity_only_african_south_and_eastern_african` | `bigint` |  |
| `other_identity_only_african_south_and_eastern_african_kenyan` | `bigint` |  |
| `other_identity_only_african_south_and_eastern_african_somali` | `bigint` |  |
| `other_identity_only_african_south_and_eastern_african_south_afr` | `bigint` |  |
| `other_identity_only_african_south_and_eastern_african_zimbabwea` | `bigint` |  |
| `other_identity_only_african_south_and_eastern_african_other_sou` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_middle_eastern` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_middle_eastern_kur` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_middle_eastern_ira` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_middle_eastern_i_1` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_middle_eastern_oth` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_eastern_asian` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_eastern_asian_chin` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_eastern_asian_hong` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_eastern_asian_japa` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_eastern_asian_othe` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_southern_asian` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_southern_asian_afg` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_southern_asian_ban` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_southern_asian_ind` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_southern_asian_pak` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_southern_asian_sri` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_southern_asian_oth` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_south_east_asian` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_south_east_asian_f` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_south_east_asian_m` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_south_east_asian_s` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_south_east_asian_o` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_central_asian` | `bigint` |  |
| `other_identity_only_middle_eastern_and_asian_asian_not_otherwis` | `bigint` |  |
| `other_identity_only_american_and_caribbean` | `bigint` |  |
| `other_identity_only_american_and_caribbean_north_american` | `bigint` |  |
| `other_identity_only_american_and_caribbean_north_american_canad` | `bigint` |  |
| `other_identity_only_american_and_caribbean_north_american_us_ci` | `bigint` |  |
| `other_identity_only_american_and_caribbean_north_american_other` | `bigint` |  |
| `other_identity_only_american_and_caribbean_central_american` | `bigint` |  |
| `other_identity_only_american_and_caribbean_south_american` | `bigint` |  |
| `other_identity_only_american_and_caribbean_caribbean` | `bigint` |  |
| `other_identity_only_american_and_caribbean_caribbean_jamaican` | `bigint` |  |
| `other_identity_only_american_and_caribbean_caribbean_other_cari` | `bigint` |  |
| `other_identity_only_antarctican_and_oceanian` | `bigint` |  |
| `other_identity_only_antarctican_and_oceanian_australasian` | `bigint` |  |
| `other_identity_only_antarctican_and_oceanian_australasian_austr` | `bigint` |  |
| `other_identity_only_antarctican_and_oceanian_australasian_new_z` | `bigint` |  |
| `other_identity_only_antarctican_and_oceanian_australasian_other` | `bigint` |  |
| `other_identity_only_antarctican_and_oceanian_other_oceanian` | `bigint` |  |
| `other_identity_only_other` | `bigint` |  |
