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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
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
| `date` | `bigint` | Count or numeric value for date in the represented area. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `uk_vet_total` | `bigint` | Count or numeric value for uk vet total in the represented area. |
| `previously_served_in_uk_armed_forces` | `bigint` | Count or numeric value for previously served in uk armed forces in the represented area. |
| `previously_served_in_uk_reserve_armed_forces` | `bigint` | Count or numeric value for previously served in uk reserve armed forces in the represented area. |
| `prev_served_regular_and_reserve` | `bigint` | Count or numeric value for prev served regular and reserve in the represented area. |
| `has_not_previously_served_in_any_uk_armed_forces` | `bigint` | Count or numeric value for has not previously served in any uk armed forces in the represented area. |
| `num_in_hh_prev_served_total` | `bigint` | Count or numeric value for num in households prev served total in the represented area. |
| `no_people_in_the_hh_prev_served_uk_armed_forces` | `bigint` | Count or numeric value for number people in the households prev served uk armed forces in the represented area. |
| `person_in_the_hh_prev_served_uk_armed_forces` | `bigint` | Count or numeric value for person in the households prev served uk armed forces in the represented area. |
| `people_in_the_hh_prev_served_uk_armed_forces` | `bigint` | Count or numeric value for people in the households prev served uk armed forces in the represented area. |
| `plus_people_in_the_hh_prev_served_uk_armed_forces` | `bigint` | Count or numeric value for plus people in the households prev served uk armed forces in the represented area. |
| `residence_type_total` | `bigint` | Count or numeric value for residence type total in the represented area. |
| `lives_in_a_household` | `bigint` | Count or numeric value for lives in a household in the represented area. |
| `lives_in_a_communal_establishment` | `bigint` | Count or numeric value for lives in a communal establishment in the represented area. |
| `hrp_prev_served_total` | `bigint` | Count or numeric value for hrp prev served total in the represented area. |
| `hrp_prev_served_uk_regular` | `bigint` | Count or numeric value for hrp prev served uk regular in the represented area. |
| `hrp_prev_served_uk_reserve` | `bigint` | Count or numeric value for hrp prev served uk reserve in the represented area. |
| `hrp_prev_served_regular_and_reserve` | `bigint` | Count or numeric value for hrp prev served regular and reserve in the represented area. |
| `hrp_not_prev_served_uk_armed_forces` | `bigint` | Count or numeric value for hrp not prev served uk armed forces in the represented area. |
