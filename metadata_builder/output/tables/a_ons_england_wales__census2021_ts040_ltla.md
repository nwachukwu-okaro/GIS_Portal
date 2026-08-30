# Census2021 Ts040 Ltla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts040_ltla`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts040_ltla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 331
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Census2021 Ts040 Ltla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts040 ltla.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. | statistical_value | Yes | No | No |
| `no_people_disabled_under_the_equality_act_in_household` | `bigint` | Count or numeric value for number people disabled under the equality act in household in the represented area. | statistical_value | Yes | No | No |
| `col_1_person_disabled_under_the_equality_act_in_household` | `bigint` | Count or numeric value for col 1 person disabled under the equality act in household in the represented area. | statistical_value | Yes | No | No |
| `col_2_or_more_people_disabled_under_the_equality_act_in_househo` | `bigint` | Count or numeric value for col 2 or more people disabled under the equality act in househo in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
