# Census2021 Ts021 Ltla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts021_ltla`
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
- **Table:** `census2021_ts021_ltla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 331
- **Columns:** 28
- **Metadata status:** source_mapped

## Description

Census2021 Ts021 Ltla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts021 ltla.

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
| `asian_asian_british_or_asian_welsh` | `bigint` |  |
| `asian_asian_british_or_asian_welsh_bangladeshi` | `bigint` |  |
| `asian_asian_british_or_asian_welsh_chinese` | `bigint` |  |
| `asian_asian_british_or_asian_welsh_indian` | `bigint` |  |
| `asian_asian_british_or_asian_welsh_pakistani` | `bigint` |  |
| `asian_asian_british_or_asian_welsh_other_asian` | `bigint` |  |
| `black_black_british_black_welsh_caribbean_or_african` | `bigint` |  |
| `black_black_british_black_welsh_caribbean_or_african_african` | `bigint` |  |
| `black_black_british_black_welsh_caribbean_or_african_caribbean` | `bigint` |  |
| `black_black_british_black_welsh_caribbean_or_african_other_blac` | `bigint` |  |
| `mixed_or_multiple_ethnic_groups` | `bigint` |  |
| `mixed_or_multiple_ethnic_groups_white_and_asian` | `bigint` |  |
| `mixed_or_multiple_ethnic_groups_white_and_black_african` | `bigint` |  |
| `mixed_or_multiple_ethnic_groups_white_and_black_caribbean` | `bigint` |  |
| `mixed_or_multiple_ethnic_groups_other_mixed_or_multiple_ethnic` | `bigint` |  |
| `white` | `bigint` |  |
| `white_english_welsh_scottish_northern_irish_or_british` | `bigint` |  |
| `white_irish` | `bigint` |  |
| `white_gypsy_or_irish_traveller` | `bigint` |  |
| `white_roma` | `bigint` |  |
| `white_other_white` | `bigint` |  |
| `other_ethnic_group` | `bigint` |  |
| `other_ethnic_group_arab` | `bigint` |  |
| `other_ethnic_group_any_other_ethnic_group` | `bigint` |  |
