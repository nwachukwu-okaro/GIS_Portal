# UK Armed Forces Veteran Ltla

## Overview

- **Identifier:** `a_ons_england_wales/uk_armed_forces_veteran_ltla`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `uk_armed_forces_veteran_ltla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 331
- **Columns:** 21
- **Metadata status:** source_mapped

## Description

UK Armed Forces Veteran Ltla is an authoritative dataset published by Office for National Statistics. It contains records relating to uk armed forces veteran ltla.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `uk_vet_total` | `bigint` | Count or numeric value for uk vet total in the represented area. | statistical_value | Yes | No | No |
| `previously_served_in_uk_armed_forces` | `bigint` | Count or numeric value for previously served in uk armed forces in the represented area. | statistical_value | Yes | No | No |
| `previously_served_in_uk_reserve_armed_forces` | `bigint` | Count or numeric value for previously served in uk reserve armed forces in the represented area. | statistical_value | Yes | No | No |
| `prev_served_regular_and_reserve` | `bigint` | Count or numeric value for prev served regular and reserve in the represented area. | statistical_value | Yes | No | No |
| `has_not_previously_served_in_any_uk_armed_forces` | `bigint` | Count or numeric value for has not previously served in any uk armed forces in the represented area. | statistical_value | Yes | No | No |
| `num_in_hh_prev_served_total` | `bigint` | Count or numeric value for num in households prev served total in the represented area. | statistical_value | Yes | No | No |
| `no_people_in_the_hh_prev_served_uk_armed_forces` | `bigint` | Count or numeric value for number people in the households prev served uk armed forces in the represented area. | statistical_value | Yes | No | No |
| `person_in_the_hh_prev_served_uk_armed_forces` | `bigint` | Count or numeric value for person in the households prev served uk armed forces in the represented area. | statistical_value | Yes | No | No |
| `people_in_the_hh_prev_served_uk_armed_forces` | `bigint` | Count or numeric value for people in the households prev served uk armed forces in the represented area. | statistical_value | Yes | No | No |
| `plus_people_in_the_hh_prev_served_uk_armed_forces` | `bigint` | Count or numeric value for plus people in the households prev served uk armed forces in the represented area. | statistical_value | Yes | No | No |
| `residence_type_total` | `bigint` | Count or numeric value for residence type total in the represented area. | statistical_value | Yes | No | No |
| `lives_in_a_household` | `bigint` | Count or numeric value for lives in a household in the represented area. | statistical_value | Yes | No | No |
| `lives_in_a_communal_establishment` | `bigint` | Count or numeric value for lives in a communal establishment in the represented area. | statistical_value | Yes | No | No |
| `hrp_prev_served_total` | `bigint` | Count or numeric value for hrp prev served total in the represented area. | statistical_value | Yes | No | No |
| `hrp_prev_served_uk_regular` | `bigint` | Count or numeric value for hrp prev served uk regular in the represented area. | statistical_value | Yes | No | No |
| `hrp_prev_served_uk_reserve` | `bigint` | Count or numeric value for hrp prev served uk reserve in the represented area. | statistical_value | Yes | No | No |
| `hrp_prev_served_regular_and_reserve` | `bigint` | Count or numeric value for hrp prev served regular and reserve in the represented area. | statistical_value | Yes | No | No |
| `hrp_not_prev_served_uk_armed_forces` | `bigint` | Count or numeric value for hrp not prev served uk armed forces in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
