# Census2021 Ts027 Oa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts027_oa`
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
- **Table:** `census2021_ts027_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 188880
- **Columns:** 23
- **Metadata status:** source_mapped

## Description

Census2021 Ts027 Oa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts027 oa.

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
| `british_only_identity` | `bigint` |  |
| `english_only_identity` | `bigint` |  |
| `english_and_british_only_identity` | `bigint` |  |
| `welsh_only_identity` | `bigint` |  |
| `welsh_and_british_only_identity` | `bigint` |  |
| `any_other_combination_of_only_uk_identities` | `bigint` |  |
| `scottish_only_identity` | `bigint` |  |
| `scottish_and_british_only_identity` | `bigint` |  |
| `northern_irish_only_identity` | `bigint` |  |
| `northern_irish_and_british_only_identity` | `bigint` |  |
| `cornish_only_identity` | `bigint` |  |
| `cornish_and_british_only_identity` | `bigint` |  |
| `any_other_combination_of_only_uk_identities_1` | `bigint` |  |
| `irish_only_identity` | `bigint` |  |
| `irish_and_at_least_one_uk_identity` | `bigint` |  |
| `other_identity_only` | `bigint` |  |
| `other_identity_and_at_least_one_uk_identity` | `bigint` |  |
| `non_uk_identity_only` | `bigint` |  |
| `uk_identity_and_non_uk_identity` | `bigint` |  |
