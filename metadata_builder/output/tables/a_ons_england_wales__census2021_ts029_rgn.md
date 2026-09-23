# Census2021 Ts029 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts029_rgn`
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
- **Table:** `census2021_ts029_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Census2021 Ts029 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts029 rgn.

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
| `total_all_usual_residents_aged_3_years_and_over` | `bigint` | Recorded census measure for the category "total all usual residents aged 3 years and over" in the represented area. Units and population base require the source table. |
| `main_language_is_english_english_or_welsh_in_wales` | `bigint` |  |
| `main_language_is_not_english_english_or_welsh_in_wales` | `bigint` |  |
| `main_language_is_not_english_english_or_welsh_in_wales_can_spea` | `bigint` |  |
| `main_language_is_not_english_english_or_welsh_in_wales_can_sp_1` | `bigint` |  |
| `main_language_is_not_english_english_or_welsh_in_wales_cannot_s` | `bigint` |  |
| `main_language_is_not_english_english_or_welsh_in_wales_cannot_1` | `bigint` |  |
