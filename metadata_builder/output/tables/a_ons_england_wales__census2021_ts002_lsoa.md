# Census2021 Ts002 Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts002_lsoa`
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
- **Table:** `census2021_ts002_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 21
- **Metadata status:** source_mapped

## Description

Census2021 Ts002 Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts002 lsoa.

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
| `never_married_and_never_registered_a_civil_partnership` | `bigint` |  |
| `married_or_in_a_registered_civil_partnership` | `bigint` |  |
| `married_or_in_a_registered_civil_partnership_married` | `bigint` |  |
| `married_or_in_a_registered_civil_partnership_married_opposite_s` | `bigint` |  |
| `married_or_in_a_registered_civil_partnership_married_same_sex` | `bigint` |  |
| `married_or_in_a_registered_civil_partnership_in_a_registered_ci` | `bigint` |  |
| `married_or_in_a_registered_civil_partnership_in_a_registered_1` | `bigint` |  |
| `married_or_in_a_registered_civil_partnership_in_a_registered_2` | `bigint` |  |
| `separated_but_still_legally_married_or_still_legally_in_a_civil` | `bigint` |  |
| `separated_but_still_legally_married_or_still_legally_in_a_civ_1` | `bigint` |  |
| `separated_but_still_legally_married_or_still_legally_in_a_civ_2` | `bigint` |  |
| `divorced_or_civil_partnership_dissolved` | `bigint` |  |
| `divorced_or_civil_partnership_dissolved_divorced` | `bigint` |  |
| `divorced_or_civil_partnership_dissolved_formerly_in_a_civil_par` | `bigint` |  |
| `widowed_or_surviving_civil_partnership_partner` | `bigint` |  |
| `widowed_or_surviving_civil_partnership_partner_widowed` | `bigint` |  |
| `widowed_or_surviving_civil_partnership_partner_surviving_partne` | `bigint` |  |
