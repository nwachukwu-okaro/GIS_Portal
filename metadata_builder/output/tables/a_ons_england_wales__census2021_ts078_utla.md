# Census2021 Ts078 Utla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts078_utla`
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
- **Table:** `census2021_ts078_utla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 174
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Census2021 Ts078 Utla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts078 utla.

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
| `gender_identity_the_same_as_sex_registered_at_birth` | `bigint` |  |
| `gender_identity_different_from_sex_registered_at_birth_but_no_s` | `bigint` |  |
| `trans_woman` | `bigint` |  |
| `trans_man` | `bigint` |  |
| `all_other_gender_identities` | `bigint` |  |
| `not_answered` | `bigint` |  |
