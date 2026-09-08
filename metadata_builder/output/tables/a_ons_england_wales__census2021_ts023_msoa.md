# Census2021 Ts023 Msoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts023_msoa`
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
- **Table:** `census2021_ts023_msoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Census2021 Ts023 Msoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts023 msoa.

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
| `one_person_household` | `bigint` | Count or numeric value for one person household in the represented area. |
| `all_household_members_have_the_same_ethnic_group` | `bigint` | Count or numeric value for all household members have the same ethnic group in the represented area. |
| `ethnic_groups_differ_between_generations_but_not_within_partner` | `bigint` | Count or numeric value for ethnic groups differ between generations but not within partner in the represented area. |
| `ethnic_groups_differ_within_partnerships` | `bigint` | Count or numeric value for ethnic groups differ within partnerships in the represented area. |
| `any_other_combination_of_multiple_ethnic_identities` | `bigint` | Count or numeric value for any other combination of multiple ethnic identities in the represented area. |
