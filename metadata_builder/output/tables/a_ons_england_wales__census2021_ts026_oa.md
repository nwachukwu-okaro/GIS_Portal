# Census2021 Ts026 Oa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts026_oa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts026_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 188880
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Census2021 Ts026 Oa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts026 oa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. | statistical_value | Yes | No | No |
| `one_person_household` | `bigint` | Count or numeric value for one person household in the represented area. | statistical_value | Yes | No | No |
| `all_household_members_have_the_same_main_language` | `bigint` | Count or numeric value for all household members have the same main language in the represented area. | statistical_value | Yes | No | No |
| `main_language_differs_between_generations_but_not_within_partne` | `bigint` | Count or numeric value for main language differs between generations but not within partne in the represented area. | statistical_value | Yes | No | No |
| `main_language_differs_within_partnerships` | `bigint` | Count or numeric value for main language differs within partnerships in the represented area. | statistical_value | Yes | No | No |
| `any_other_combination_of_multiple_main_languages` | `bigint` | Count or numeric value for any other combination of multiple main languages in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
