# Census2021 Ts025 Ctry

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts025_ctry`
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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts025_ctry`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Census2021 Ts025 Ctry is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts025 ctry.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. |
| `all_adults_in_household_have_english_in_england_or_english_or_w` | `bigint` | Count or numeric value for all adults in household have english in england or english or w in the represented area. |
| `at_least_one_but_not_all_adults_in_household_have_english_in_en` | `bigint` | Count or numeric value for at least one but not all adults in household have english in en in the represented area. |
| `no_adults_in_household_but_at_least_one_person_aged_3_to_15_yea` | `bigint` | Count or numeric value for number adults in household but at least one person aged 3 to 15 yea in the represented area. |
| `no_people_in_household_have_english_in_england_or_english_or_we` | `bigint` | Count or numeric value for number people in household have english in england or english or we in the represented area. |
