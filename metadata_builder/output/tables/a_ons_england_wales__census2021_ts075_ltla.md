# Census2021 Ts075 Ltla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts075_ltla`
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
- **Table:** `census2021_ts075_ltla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 331
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Census2021 Ts075 Ltla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts075 ltla.

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
| `total` | `bigint` |  |
| `one_person_household` | `bigint` | Recorded census measure for the category "one person household" in the represented area. Units and population base require the source table. |
| `multi_person_household_no_people_stated_their_religion` | `bigint` |  |
| `multi_person_household_same_religion_at_least_one_person_has_st` | `bigint` |  |
| `multi_person_household_no_religion_household_may_include_people` | `bigint` |  |
| `multi_person_household_same_religion_and_no_religion_household` | `bigint` |  |
| `multi_person_household_at_least_two_different_religions_stated` | `bigint` |  |
