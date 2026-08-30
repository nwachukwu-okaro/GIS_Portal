# Census2021 Ts050 Oa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts050_oa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts050_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 188880
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Census2021 Ts050 Oa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts050 oa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. | statistical_value | Yes | No | No |
| `col_1_bedroom` | `bigint` | Count or numeric value for col 1 bedroom in the represented area. | statistical_value | Yes | No | No |
| `col_2_bedrooms` | `bigint` | Count or numeric value for col 2 bedrooms in the represented area. | statistical_value | Yes | No | No |
| `col_3_bedrooms` | `bigint` | Count or numeric value for col 3 bedrooms in the represented area. | statistical_value | Yes | No | No |
| `col_4_or_more_bedrooms` | `bigint` | Count or numeric value for col 4 or more bedrooms in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
