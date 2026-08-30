# Census2021 Ts070 Ltla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts070_ltla`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts070_ltla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 331
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Census2021 Ts070 Ltla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts070 ltla.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents_aged_16_years_and_over` | `bigint` | Count or numeric value for total all usual residents aged 16 years and over in the represented area. | statistical_value | Yes | No | No |
| `gender_identity_the_same_as_sex_registered_at_birth` | `bigint` | Count or numeric value for gender identity the same as sex registered at birth in the represented area. | statistical_value | Yes | No | No |
| `gender_identity_different_from_sex_registered_at_birth_but_no_s` | `bigint` | Count or numeric value for gender identity different from sex registered at birth but number s in the represented area. | statistical_value | Yes | No | No |
| `trans_woman` | `bigint` | Count or numeric value for trans woman in the represented area. | statistical_value | Yes | No | No |
| `trans_man` | `bigint` | Count or numeric value for trans man in the represented area. | statistical_value | Yes | No | No |
| `non_binary` | `bigint` | Count or numeric value for non binary in the represented area. | statistical_value | Yes | No | No |
| `all_other_gender_identities` | `bigint` | Count or numeric value for all other gender identities in the represented area. | statistical_value | Yes | No | No |
| `not_answered` | `bigint` | Count or numeric value for not answered in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
