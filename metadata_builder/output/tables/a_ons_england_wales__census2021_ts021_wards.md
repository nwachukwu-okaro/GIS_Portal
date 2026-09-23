# Census2021 Ts021 Wards

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts021_wards`
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
- **Table:** `census2021_ts021_wards`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 50
- **Columns:** 27
- **Metadata status:** source_mapped

## Description

Census2021 Ts021 Wards is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts021 wards.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Primary-key identifier for records in census2021_ts021_wards. |
| `ethnic group` | `varchar` |  |
| `total_all_usual_residents` | `integer` | Census total for all usual residents in the represented geographical area; measurement unit requires the table documentation. |
| `asian_asian_british_or_asian_welsh` | `integer` |  |
| `asian_asian_british_or_asian_welsh_bangladeshi` | `integer` |  |
| `asian_asian_british_or_asian_welsh_chinese` | `integer` |  |
| `asian_asian_british_or_asian_welsh_indian` | `integer` |  |
| `asian_asian_british_or_asian_welsh_pakistani` | `integer` |  |
| `asian_asian_british_or_asian_welsh_other_asian` | `integer` |  |
| `black_black_british_black_welsh_caribbean_or_african` | `integer` |  |
| `black_black_british_black_welsh_caribbean_or_african_african` | `integer` |  |
| `black_black_british_black_welsh_caribbean_or_african_caribbean` | `integer` |  |
| `black_black_british_black_welsh_caribbean_or_african_other_blac` | `integer` |  |
| `mixed_or_multiple_ethnic_groups` | `integer` |  |
| `mixed_or_multiple_ethnic_groups_white_and_asian` | `integer` |  |
| `mixed_or_multiple_ethnic_groups_white_and_black_african` | `integer` |  |
| `mixed_or_multiple_ethnic_groups_white_and_black_caribbean` | `integer` |  |
| `mixed_or_multiple_ethnic_groups_other_mixed_or_multiple_ethnic` | `integer` |  |
| `white` | `integer` |  |
| `white_english_welsh_scottish_northern_irish_or_british` | `integer` |  |
| `white_irish` | `integer` |  |
| `white_gypsy_or_irish_traveller` | `integer` |  |
| `white_roma` | `integer` |  |
| `white_other_white` | `integer` |  |
| `other_ethnic_group` | `integer` |  |
| `other_ethnic_group_arab` | `integer` |  |
| `other_ethnic_group_any_other_ethnic_group` | `integer` |  |
