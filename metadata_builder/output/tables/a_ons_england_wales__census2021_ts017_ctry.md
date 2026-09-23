# Census2021 Ts017 Ctry

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts017_ctry`
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
- **Table:** `census2021_ts017_ctry`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Census2021 Ts017 Ctry is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts017 ctry.

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
| `total_all_household_spaces` | `bigint` | Recorded census measure for the category "total all household spaces" in the represented area. Units and population base require the source table. |
| `col_0_people_in_household` | `bigint` |  |
| `col_1_person_in_household` | `bigint` |  |
| `col_2_people_in_household` | `bigint` |  |
| `col_3_people_in_household` | `bigint` |  |
| `col_4_people_in_household` | `bigint` |  |
| `col_5_people_in_household` | `bigint` |  |
| `col_6_people_in_household` | `bigint` |  |
| `col_7_people_in_household` | `bigint` |  |
| `col_8_or_more_people_in_household` | `bigint` |  |
