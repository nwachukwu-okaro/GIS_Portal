# Census2021 Ts072 Utla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts072_utla`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts072_utla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 174
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Census2021 Ts072 Utla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts072 utla.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. | statistical_value | Yes | No | No |
| `no_people_in_the_household_previously_served_in_uk_armed_forces` | `bigint` | Count or numeric value for number people in the household previously served in uk armed forces in the represented area. | statistical_value | Yes | No | No |
| `col_1_person_in_the_household_previously_served_in_uk_armed_for` | `bigint` | Count or numeric value for col 1 person in the household previously served in uk armed for in the represented area. | statistical_value | Yes | No | No |
| `col_2_people_in_the_household_previously_served_in_uk_armed_for` | `bigint` | Count or numeric value for col 2 people in the household previously served in uk armed for in the represented area. | statistical_value | Yes | No | No |
| `col_3_or_more_people_in_the_household_previously_served_in_uk_a` | `bigint` | Count or numeric value for col 3 or more people in the household previously served in uk a in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
