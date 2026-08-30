# Census2021 Ts037asp Ctry

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts037asp_ctry`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts037asp_ctry`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Census2021 Ts037asp Ctry is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts037asp ctry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `very_good_health` | `double precision` | Count or numeric value for very good health in the represented area. | statistical_value | Yes | No | No |
| `good_health` | `double precision` | Count or numeric value for good health in the represented area. | statistical_value | Yes | No | No |
| `fair_health` | `double precision` | Count or numeric value for fair health in the represented area. | statistical_value | Yes | No | No |
| `bad_health` | `double precision` | Count or numeric value for bad health in the represented area. | statistical_value | Yes | No | No |
| `very_bad_health` | `double precision` | Count or numeric value for very bad health in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
