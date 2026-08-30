# Census2021 Ts075 Ltla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts075_ltla`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts075_ltla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 331
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Census2021 Ts075 Ltla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts075 ltla.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total` | `bigint` | Count or numeric value for total in the represented area. | statistical_value | Yes | No | No |
| `one_person_household` | `bigint` | Count or numeric value for one person household in the represented area. | statistical_value | Yes | No | No |
| `multi_person_household_no_people_stated_their_religion` | `bigint` | Count or numeric value for multi person household number people stated their religion in the represented area. | statistical_value | Yes | No | No |
| `multi_person_household_same_religion_at_least_one_person_has_st` | `bigint` | Count or numeric value for multi person household same religion at least one person has st in the represented area. | statistical_value | Yes | No | No |
| `multi_person_household_no_religion_household_may_include_people` | `bigint` | Count or numeric value for multi person household number religion household may include people in the represented area. | statistical_value | Yes | No | No |
| `multi_person_household_same_religion_and_no_religion_household` | `bigint` | Count or numeric value for multi person household same religion and number religion household in the represented area. | statistical_value | Yes | No | No |
| `multi_person_household_at_least_two_different_religions_stated` | `bigint` | Count or numeric value for multi person household at least two different religions stated in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
