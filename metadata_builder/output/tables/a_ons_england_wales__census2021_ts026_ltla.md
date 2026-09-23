# Census2021 Ts026 Ltla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts026_ltla`
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
- **Table:** `census2021_ts026_ltla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 331
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Census2021 Ts026 Ltla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts026 ltla.

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
| `total_all_households` | `bigint` | Census total for all households in the represented geographical area; measurement unit requires the table documentation. |
| `one_person_household` | `bigint` | Recorded census measure for the category "one person household" in the represented area. Units and population base require the source table. |
| `all_household_members_have_the_same_main_language` | `bigint` |  |
| `main_language_differs_between_generations_but_not_within_partne` | `bigint` |  |
| `main_language_differs_within_partnerships` | `bigint` |  |
| `any_other_combination_of_multiple_main_languages` | `bigint` |  |
