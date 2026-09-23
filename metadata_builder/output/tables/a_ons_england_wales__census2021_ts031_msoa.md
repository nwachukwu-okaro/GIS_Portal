# Census2021 Ts031 Msoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts031_msoa`
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
- **Table:** `census2021_ts031_msoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Columns:** 63
- **Metadata status:** source_mapped

## Description

Census2021 Ts031 Msoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts031 msoa.

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
| `christian` | `bigint` |  |
| `buddhist` | `bigint` |  |
| `hindu` | `bigint` |  |
| `jewish` | `bigint` |  |
| `muslim` | `bigint` |  |
| `sikh` | `bigint` |  |
| `no_religion` | `bigint` |  |
| `no_religion_agnostic` | `bigint` |  |
| `no_religion_atheist` | `bigint` |  |
| `no_religion_free_thinker` | `bigint` |  |
| `no_religion_humanist` | `bigint` |  |
| `no_religion_no_religion` | `bigint` |  |
| `no_religion_realist` | `bigint` |  |
| `other_religion` | `bigint` |  |
| `other_religion_alevi` | `bigint` |  |
| `other_religion_animism` | `bigint` |  |
| `other_religion_baha_i` | `bigint` |  |
| `other_religion_believe_in_god` | `bigint` |  |
| `other_religion_brahma_kumari` | `bigint` |  |
| `other_religion_chinese_religion` | `bigint` |  |
| `other_religion_church_of_all_religion` | `bigint` |  |
| `other_religion_confucianist` | `bigint` |  |
| `other_religion_deist` | `bigint` |  |
| `other_religion_druid` | `bigint` |  |
| `other_religion_druze` | `bigint` |  |
| `other_religion_eckankar` | `bigint` |  |
| `other_religion_heathen` | `bigint` |  |
| `other_religion_jain` | `bigint` |  |
| `other_religion_mixed_religion` | `bigint` |  |
| `other_religion_mysticism` | `bigint` |  |
| `other_religion_native_american_church` | `bigint` |  |
| `other_religion_new_age` | `bigint` |  |
| `other_religion_occult` | `bigint` |  |
| `other_religion_other_religions` | `bigint` |  |
| `other_religion_own_belief_system` | `bigint` |  |
| `other_religion_pagan` | `bigint` |  |
| `other_religion_pantheism` | `bigint` |  |
| `other_religion_rastafarian` | `bigint` |  |
| `other_religion_ravidassia` | `bigint` |  |
| `other_religion_reconstructionist` | `bigint` |  |
| `other_religion_satanism` | `bigint` |  |
| `other_religion_scientology` | `bigint` |  |
| `other_religion_shamanism` | `bigint` |  |
| `other_religion_shintoism` | `bigint` |  |
| `other_religion_spiritual` | `bigint` |  |
| `other_religion_spiritualist` | `bigint` |  |
| `other_religion_taoist` | `bigint` |  |
| `other_religion_theism` | `bigint` |  |
| `other_religion_thelemite` | `bigint` |  |
| `other_religion_traditional_african_religion` | `bigint` |  |
| `other_religion_unification_church` | `bigint` |  |
| `other_religion_universalist` | `bigint` |  |
| `other_religion_valmiki` | `bigint` |  |
| `other_religion_vodun` | `bigint` |  |
| `other_religion_wicca` | `bigint` |  |
| `other_religion_witchcraft` | `bigint` |  |
| `other_religion_yazidi` | `bigint` |  |
| `other_religion_zoroastrian` | `bigint` |  |
| `religion_not_stated` | `bigint` | Recorded census measure for the category "religion not stated" in the represented area. Units and population base require the source table. |
