# Census2021 Ts018 Msoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts018_msoa`
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
- **Table:** `census2021_ts018_msoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Columns:** 22
- **Metadata status:** source_mapped

## Description

Census2021 Ts018 Msoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts018 msoa.

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
| `born_in_the_uk` | `bigint` | Recorded census measure for the category "born in the UK" in the represented area. Units and population base require the source table. |
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
