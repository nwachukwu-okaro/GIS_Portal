# UK Armed Forces Veteran Ltla

## Overview

- **Identifier:** `a_ons_england_wales/uk_armed_forces_veteran_ltla`
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
- **Table:** `uk_armed_forces_veteran_ltla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 331
- **Columns:** 21
- **Metadata status:** source_mapped

## Description

UK Armed Forces Veteran Ltla is an authoritative dataset published by Office for National Statistics. It contains records relating to uk armed forces veteran ltla.

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
| `uk_vet_total` | `bigint` |  |
| `previously_served_in_uk_armed_forces` | `bigint` |  |
| `previously_served_in_uk_reserve_armed_forces` | `bigint` |  |
| `prev_served_regular_and_reserve` | `bigint` |  |
| `has_not_previously_served_in_any_uk_armed_forces` | `bigint` |  |
| `num_in_hh_prev_served_total` | `bigint` |  |
| `no_people_in_the_hh_prev_served_uk_armed_forces` | `bigint` |  |
| `person_in_the_hh_prev_served_uk_armed_forces` | `bigint` |  |
| `people_in_the_hh_prev_served_uk_armed_forces` | `bigint` |  |
| `plus_people_in_the_hh_prev_served_uk_armed_forces` | `bigint` |  |
| `residence_type_total` | `bigint` |  |
| `lives_in_a_household` | `bigint` | Recorded census measure for the category "lives in a household" in the represented area. Units and population base require the source table. |
| `lives_in_a_communal_establishment` | `bigint` | Recorded census measure for the category "lives in a communal establishment" in the represented area. Units and population base require the source table. |
| `hrp_prev_served_total` | `bigint` |  |
| `hrp_prev_served_uk_regular` | `bigint` |  |
| `hrp_prev_served_uk_reserve` | `bigint` |  |
| `hrp_prev_served_regular_and_reserve` | `bigint` |  |
| `hrp_not_prev_served_uk_armed_forces` | `bigint` |  |
