# Census2021 Ts056 Ctry

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts056_ctry`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts056_ctry`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Census2021 Ts056 Ctry is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts056 ctry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents` | `bigint` | Count or numeric value for total all usual residents in the represented area. | statistical_value | Yes | No | No |
| `no_second_address` | `bigint` | Count or numeric value for number second address in the represented area. | statistical_value | Yes | No | No |
| `second_address_is_in_the_uk` | `bigint` | Count or numeric value for second address is in the uk in the represented area. | statistical_value | Yes | No | No |
| `second_address_is_outside_the_uk` | `bigint` | Count or numeric value for second address is outside the uk in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
