# Census2021 Ts062 Utla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts062_utla`
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
- **Table:** `census2021_ts062_utla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 174
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Census2021 Ts062 Utla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts062 utla.

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
| `total_all_usual_residents_aged_16_years_and_over` | `bigint` | Recorded census measure for the category "total all usual residents aged 16 years and over" in the represented area. Units and population base require the source table. |
| `l1_l2_and_l3_higher_managerial_administrative_and_professional` | `bigint` |  |
| `l4_l5_and_l6_lower_managerial_administrative_and_professional_o` | `bigint` |  |
| `l7_intermediate_occupations` | `bigint` |  |
| `l8_and_l9_small_employers_and_own_account_workers` | `bigint` |  |
| `l10_and_l11_lower_supervisory_and_technical_occupations` | `bigint` |  |
| `l12_semi_routine_occupations` | `bigint` |  |
| `l13_routine_occupations` | `bigint` |  |
| `l14_1_and_l14_2_never_worked_and_long_term_unemployed` | `bigint` |  |
| `l15_full_time_students` | `bigint` |  |
