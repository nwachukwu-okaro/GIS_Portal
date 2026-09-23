# Census2021 Ts010 Ltla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts010_ltla`
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
- **Table:** `census2021_ts010_ltla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 331
- **Columns:** 18
- **Metadata status:** source_mapped

## Description

Census2021 Ts010 Ltla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts010 ltla.

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
| `living_in_a_couple` | `bigint` |  |
| `living_in_a_couple_married_or_in_a_civil_partnership` | `bigint` |  |
| `living_in_a_couple_married_or_in_a_civil_partnership_opposite_s` | `bigint` |  |
| `living_in_a_couple_married_or_in_a_civil_partnership_same_sex_c` | `bigint` |  |
| `living_in_a_couple_separated_but_still_married_or_in_a_civil_pa` | `bigint` |  |
| `living_in_a_couple_cohabiting` | `bigint` |  |
| `living_in_a_couple_cohabiting_opposite_sex_couple` | `bigint` |  |
| `living_in_a_couple_cohabiting_same_sex_couple` | `bigint` |  |
| `not_living_in_a_couple` | `bigint` |  |
| `not_living_in_a_couple_single_never_married_and_never_registere` | `bigint` |  |
| `not_living_in_a_couple_married_or_in_a_registered_civil_partner` | `bigint` |  |
| `not_living_in_a_couple_separated_including_those_who_are_marrie` | `bigint` |  |
| `not_living_in_a_couple_divorced_or_formerly_in_a_civil_partners` | `bigint` |  |
| `not_living_in_a_couple_widowed_or_surviving_partner_from_a_civi` | `bigint` |  |
