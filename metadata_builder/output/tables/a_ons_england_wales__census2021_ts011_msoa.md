# Census2021 Ts011 Msoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts011_msoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts011_msoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Census2021 Ts011 Msoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts011 msoa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. | statistical_value | Yes | No | No |
| `household_is_not_deprived_in_any_dimension` | `bigint` | Count or numeric value for household is not deprived in any dimension in the represented area. | statistical_value | Yes | No | No |
| `household_is_deprived_in_one_dimension` | `bigint` | Count or numeric value for household is deprived in one dimension in the represented area. | statistical_value | Yes | No | No |
| `household_is_deprived_in_two_dimensions` | `bigint` | Count or numeric value for household is deprived in two dimensions in the represented area. | statistical_value | Yes | No | No |
| `household_is_deprived_in_three_dimensions` | `bigint` | Count or numeric value for household is deprived in three dimensions in the represented area. | statistical_value | Yes | No | No |
| `household_is_deprived_in_four_dimensions` | `bigint` | Count or numeric value for household is deprived in four dimensions in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
