# Census2021 Ts025 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts025_rgn`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts025_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Census2021 Ts025 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts025 rgn.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. | statistical_value | Yes | No | No |
| `all_adults_in_household_have_english_in_england_or_english_or_w` | `bigint` | Count or numeric value for all adults in household have english in england or english or w in the represented area. | statistical_value | Yes | No | No |
| `at_least_one_but_not_all_adults_in_household_have_english_in_en` | `bigint` | Count or numeric value for at least one but not all adults in household have english in en in the represented area. | statistical_value | Yes | No | No |
| `no_adults_in_household_but_at_least_one_person_aged_3_to_15_yea` | `bigint` | Count or numeric value for number adults in household but at least one person aged 3 to 15 yea in the represented area. | statistical_value | Yes | No | No |
| `no_people_in_household_have_english_in_england_or_english_or_we` | `bigint` | Count or numeric value for number people in household have english in england or english or we in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
