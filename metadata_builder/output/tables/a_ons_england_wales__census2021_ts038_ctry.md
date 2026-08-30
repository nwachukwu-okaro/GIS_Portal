# Census2021 Ts038 Ctry

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts038_ctry`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts038_ctry`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Census2021 Ts038 Ctry is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts038 ctry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents` | `bigint` | Count or numeric value for total all usual residents in the represented area. | statistical_value | Yes | No | No |
| `disabled_under_the_equality_act` | `bigint` | Count or numeric value for disabled under the equality act in the represented area. | statistical_value | Yes | No | No |
| `disabled_under_the_equality_act_day_to_day_activities_limited_a` | `bigint` | Count or numeric value for disabled under the equality act day to day activities limited a in the represented area. | statistical_value | Yes | No | No |
| `disabled_under_the_equality_act_day_to_day_activities_limited_1` | `bigint` | Count or numeric value for disabled under the equality act day to day activities limited 1 in the represented area. | statistical_value | Yes | No | No |
| `not_disabled_under_the_equality_act` | `bigint` | Count or numeric value for not disabled under the equality act in the represented area. | statistical_value | Yes | No | No |
| `not_disabled_under_the_equality_act_has_long_term_physical_or_m` | `bigint` | Numeric not disabled under the equality act has long term physical or male value recorded for the feature. | measure | Yes | No | No |
| `not_disabled_under_the_equality_act_no_long_term_physical_or_me` | `bigint` | Numeric not disabled under the equality act number long term physical or me value recorded for the feature. | measure | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
