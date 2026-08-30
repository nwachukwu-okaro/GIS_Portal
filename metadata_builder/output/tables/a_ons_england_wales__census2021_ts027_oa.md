# Census2021 Ts027 Oa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts027_oa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts027_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 188880
- **Columns:** 23
- **Metadata status:** source_mapped

## Description

Census2021 Ts027 Oa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts027 oa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents` | `bigint` | Count or numeric value for total all usual residents in the represented area. | statistical_value | Yes | No | No |
| `british_only_identity` | `bigint` | Count or numeric value for british only identity in the represented area. | statistical_value | Yes | No | No |
| `english_only_identity` | `bigint` | Count or numeric value for english only identity in the represented area. | statistical_value | Yes | No | No |
| `english_and_british_only_identity` | `bigint` | Count or numeric value for english and british only identity in the represented area. | statistical_value | Yes | No | No |
| `welsh_only_identity` | `bigint` | Count or numeric value for welsh only identity in the represented area. | statistical_value | Yes | No | No |
| `welsh_and_british_only_identity` | `bigint` | Count or numeric value for welsh and british only identity in the represented area. | statistical_value | Yes | No | No |
| `any_other_combination_of_only_uk_identities` | `bigint` | Count or numeric value for any other combination of only uk identities in the represented area. | statistical_value | Yes | No | No |
| `scottish_only_identity` | `bigint` | Count or numeric value for scottish only identity in the represented area. | statistical_value | Yes | No | No |
| `scottish_and_british_only_identity` | `bigint` | Count or numeric value for scottish and british only identity in the represented area. | statistical_value | Yes | No | No |
| `northern_irish_only_identity` | `bigint` | Count or numeric value for northern irish only identity in the represented area. | statistical_value | Yes | No | No |
| `northern_irish_and_british_only_identity` | `bigint` | Count or numeric value for northern irish and british only identity in the represented area. | statistical_value | Yes | No | No |
| `cornish_only_identity` | `bigint` | Count or numeric value for cornish only identity in the represented area. | statistical_value | Yes | No | No |
| `cornish_and_british_only_identity` | `bigint` | Count or numeric value for cornish and british only identity in the represented area. | statistical_value | Yes | No | No |
| `any_other_combination_of_only_uk_identities_1` | `bigint` | Count or numeric value for any other combination of only uk identities 1 in the represented area. | statistical_value | Yes | No | No |
| `irish_only_identity` | `bigint` | Count or numeric value for irish only identity in the represented area. | statistical_value | Yes | No | No |
| `irish_and_at_least_one_uk_identity` | `bigint` | Count or numeric value for irish and at least one uk identity in the represented area. | statistical_value | Yes | No | No |
| `other_identity_only` | `bigint` | Count or numeric value for other identity only in the represented area. | statistical_value | Yes | No | No |
| `other_identity_and_at_least_one_uk_identity` | `bigint` | Count or numeric value for other identity and at least one uk identity in the represented area. | statistical_value | Yes | No | No |
| `non_uk_identity_only` | `bigint` | Count or numeric value for non uk identity only in the represented area. | statistical_value | Yes | No | No |
| `uk_identity_and_non_uk_identity` | `bigint` | Count or numeric value for uk identity and non uk identity in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
