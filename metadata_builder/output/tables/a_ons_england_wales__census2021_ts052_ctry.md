# Census2021 Ts052 Ctry

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts052_ctry`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts052_ctry`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Census2021 Ts052 Ctry is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts052 ctry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_bedrooms_2_or_more` | `bigint` | Count or numeric value for occupancy rating of bedrooms 2 or more in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_bedrooms_1` | `bigint` | Count or numeric value for occupancy rating of bedrooms 1 in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_bedrooms_0` | `bigint` | Count or numeric value for occupancy rating of bedrooms 0 in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_bedrooms_1_1` | `bigint` | Count or numeric value for occupancy rating of bedrooms 1 1 in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_bedrooms_2_or_less` | `bigint` | Count or numeric value for occupancy rating of bedrooms 2 or less in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
