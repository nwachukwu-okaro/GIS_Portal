# Census2021 Ts038asp Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts038asp_rgn`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts038asp_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Census2021 Ts038asp Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts038asp rgn.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `disabled_under_the_equality_act_day_to_day_activities_limited_a` | `double precision` | Count or numeric value for disabled under the equality act day to day activities limited a in the represented area. | statistical_value | Yes | No | No |
| `disabled_under_the_equality_act_day_to_day_activities_limited_1` | `double precision` | Count or numeric value for disabled under the equality act day to day activities limited 1 in the represented area. | statistical_value | Yes | No | No |
| `not_disabled_under_the_equality_act` | `double precision` | Count or numeric value for not disabled under the equality act in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
