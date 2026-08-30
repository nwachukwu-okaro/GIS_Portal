# Census2021 Ts030 Ltla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts030_ltla`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts030_ltla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 331
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Census2021 Ts030 Ltla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts030 ltla.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents` | `bigint` | Count or numeric value for total all usual residents in the represented area. | statistical_value | Yes | No | No |
| `no_religion` | `bigint` | Count or numeric value for number religion in the represented area. | statistical_value | Yes | No | No |
| `christian` | `bigint` | Count or numeric value for christian in the represented area. | statistical_value | Yes | No | No |
| `buddhist` | `bigint` | Count or numeric value for buddhist in the represented area. | statistical_value | Yes | No | No |
| `hindu` | `bigint` | Count or numeric value for hindu in the represented area. | statistical_value | Yes | No | No |
| `jewish` | `bigint` | Count or numeric value for jewish in the represented area. | statistical_value | Yes | No | No |
| `muslim` | `bigint` | Count or numeric value for muslim in the represented area. | statistical_value | Yes | No | No |
| `sikh` | `bigint` | Count or numeric value for sikh in the represented area. | statistical_value | Yes | No | No |
| `other_religion` | `bigint` | Count or numeric value for other religion in the represented area. | statistical_value | Yes | No | No |
| `not_answered` | `bigint` | Count or numeric value for not answered in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
