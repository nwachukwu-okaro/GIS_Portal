# Census2021 Ts016 Msoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts016_msoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts016_msoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Census2021 Ts016 Msoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts016 msoa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents` | `bigint` | Count or numeric value for total all usual residents in the represented area. | statistical_value | Yes | No | No |
| `born_in_the_uk` | `bigint` | Count or numeric value for born in the uk in the represented area. | statistical_value | Yes | No | No |
| `col_10_years_or_more` | `bigint` | Count or numeric value for col 10 years or more in the represented area. | statistical_value | Yes | No | No |
| `col_5_years_or_more_but_less_than_10_years` | `bigint` | Count or numeric value for col 5 years or more but less than 10 years in the represented area. | statistical_value | Yes | No | No |
| `col_2_years_or_more_but_less_than_5_years` | `bigint` | Count or numeric value for col 2 years or more but less than 5 years in the represented area. | statistical_value | Yes | No | No |
| `less_than_2_years` | `bigint` | Count or numeric value for less than 2 years in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
