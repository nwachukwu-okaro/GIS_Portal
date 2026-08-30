# Census2021 Ts020 Ltla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts020_ltla`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts020_ltla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 331
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Census2021 Ts020 Ltla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts020 ltla.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `all_persons` | `bigint` | Count or numeric value for all persons in the represented area. | statistical_value | Yes | No | No |
| `female` | `bigint` | Count or numeric value for female in the represented area. | statistical_value | Yes | No | No |
| `male` | `bigint` | Count or numeric value for male in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
