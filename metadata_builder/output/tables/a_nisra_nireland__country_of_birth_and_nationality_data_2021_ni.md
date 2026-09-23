# Country Of Birth And Nationality Data 2021 Ni

## Overview

- **Identifier:** `a_nisra_nireland/country_of_birth_and_nationality_data_2021_ni`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nisra_nireland`
- **Table:** `country_of_birth_and_nationality_data_2021_ni`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1
- **Columns:** 23
- **Metadata status:** source_mapped

## Description

Country Of Birth And Nationality Data 2021 Ni is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to country of birth and nationality data 2021 ni.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geocode` | `text` | Code identifying the geographical area represented by the row. |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `year` | `bigint` | Reference year recorded for the statistical observation. |
| `population` | `text` |  |
| `country_of_birth_england` | `text` | Recorded census measure for the category "country of birth england" in the represented area. Units and population base require the source table. |
| `country_of_birth_northern_ireland` | `text` | Recorded census measure for the category "country of birth northern ireland" in the represented area. Units and population base require the source table. |
| `country_of_birth_other_countries` | `text` | Recorded census measure for the category "country of birth other countries" in the represented area. Units and population base require the source table. |
| `country_of_birth_republic_of_ireland` | `text` | Recorded census measure for the category "country of birth republic of ireland" in the represented area. Units and population base require the source table. |
| `country_of_birth_scotland` | `text` | Recorded census measure for the category "country of birth scotland" in the represented area. Units and population base require the source table. |
| `country_of_birth_wales` | `text` | Recorded census measure for the category "country of birth wales" in the represented area. Units and population base require the source table. |
| `national_identity_british_and_irish_only` | `text` |  |
| `national_identity_british_and_northern_irish_only` | `text` |  |
| `national_identity_british_only` | `text` |  |
| `national_identity_british_irish_and_northern_irish_only` | `text` |  |
| `national_identity_irish_and_northern_irish_only` | `text` |  |
| `national_identity_irish_only` | `text` |  |
| `national_identity_northern_irish_only` | `text` |  |
| `national_identity_other_national_identities` | `text` |  |
| `passports_held_ireland_only` | `text` |  |
| `passports_held_no_passport` | `text` |  |
| `passports_held_other_passports` | `text` |  |
| `passports_held_united_kingdom_and_ireland_only` | `text` |  |
| `passports_held_united_kingdom_only` | `text` |  |
