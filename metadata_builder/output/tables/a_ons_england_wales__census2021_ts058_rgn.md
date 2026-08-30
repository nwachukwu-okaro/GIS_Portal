# Census2021 Ts058 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts058_rgn`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts058_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Census2021 Ts058 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts058 rgn.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents_aged_16_years_and_over_in_employment` | `bigint` | Count or numeric value for total all usual residents aged 16 years and over in employment in the represented area. | statistical_value | Yes | No | No |
| `less_than_2km` | `bigint` | Count or numeric value for less than 2km in the represented area. | statistical_value | Yes | No | No |
| `col_2km_to_less_than_5km` | `bigint` | Count or numeric value for col 2km to less than 5km in the represented area. | statistical_value | Yes | No | No |
| `col_5km_to_less_than_10km` | `bigint` | Count or numeric value for col 5km to less than 10km in the represented area. | statistical_value | Yes | No | No |
| `col_10km_to_less_than_20km` | `bigint` | Count or numeric value for col 10km to less than 20km in the represented area. | statistical_value | Yes | No | No |
| `col_20km_to_less_than_30km` | `bigint` | Count or numeric value for col 20km to less than 30km in the represented area. | statistical_value | Yes | No | No |
| `col_30km_to_less_than_40km` | `bigint` | Count or numeric value for col 30km to less than 40km in the represented area. | statistical_value | Yes | No | No |
| `col_40km_to_less_than_60km` | `bigint` | Count or numeric value for col 40km to less than 60km in the represented area. | statistical_value | Yes | No | No |
| `col_60km_and_over` | `bigint` | Count or numeric value for col 60km and over in the represented area. | statistical_value | Yes | No | No |
| `works_mainly_from_home` | `bigint` | Count or numeric value for works mainly from home in the represented area. | statistical_value | Yes | No | No |
| `works_mainly_at_an_offshore_installation_in_no_fixed_place_or_o` | `bigint` | Numeric works mainly at an offshore installation in number fixed place or o value recorded for the feature. | measure | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
