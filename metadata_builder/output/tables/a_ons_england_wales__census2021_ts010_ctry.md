# Census2021 Ts010 Ctry

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts010_ctry`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts010_ctry`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3
- **Columns:** 18
- **Metadata status:** source_mapped

## Description

Census2021 Ts010 Ctry is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts010 ctry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total` | `bigint` | Count or numeric value for total in the represented area. | statistical_value | Yes | No | No |
| `living_in_a_couple` | `bigint` | Count or numeric value for living in a couple in the represented area. | statistical_value | Yes | No | No |
| `living_in_a_couple_married_or_in_a_civil_partnership` | `bigint` | Count or numeric value for living in a couple married or in a civil partnership in the represented area. | statistical_value | Yes | No | No |
| `living_in_a_couple_married_or_in_a_civil_partnership_opposite_s` | `bigint` | Count or numeric value for living in a couple married or in a civil partnership opposite s in the represented area. | statistical_value | Yes | No | No |
| `living_in_a_couple_married_or_in_a_civil_partnership_same_sex_c` | `bigint` | Count or numeric value for living in a couple married or in a civil partnership same sex c in the represented area. | statistical_value | Yes | No | No |
| `living_in_a_couple_separated_but_still_married_or_in_a_civil_pa` | `bigint` | Count or numeric value for living in a couple separated but still married or in a civil pa in the represented area. | statistical_value | Yes | No | No |
| `living_in_a_couple_cohabiting` | `bigint` | Count or numeric value for living in a couple cohabiting in the represented area. | statistical_value | Yes | No | No |
| `living_in_a_couple_cohabiting_opposite_sex_couple` | `bigint` | Count or numeric value for living in a couple cohabiting opposite sex couple in the represented area. | statistical_value | Yes | No | No |
| `living_in_a_couple_cohabiting_same_sex_couple` | `bigint` | Count or numeric value for living in a couple cohabiting same sex couple in the represented area. | statistical_value | Yes | No | No |
| `not_living_in_a_couple` | `bigint` | Count or numeric value for not living in a couple in the represented area. | statistical_value | Yes | No | No |
| `not_living_in_a_couple_single_never_married_and_never_registere` | `bigint` | Count or numeric value for not living in a couple single never married and never registere in the represented area. | statistical_value | Yes | No | No |
| `not_living_in_a_couple_married_or_in_a_registered_civil_partner` | `bigint` | Count or numeric value for not living in a couple married or in a registered civil partner in the represented area. | statistical_value | Yes | No | No |
| `not_living_in_a_couple_separated_including_those_who_are_marrie` | `bigint` | Count or numeric value for not living in a couple separated including those who are marrie in the represented area. | statistical_value | Yes | No | No |
| `not_living_in_a_couple_divorced_or_formerly_in_a_civil_partners` | `bigint` | Count or numeric value for not living in a couple divorced or formerly in a civil partners in the represented area. | statistical_value | Yes | No | No |
| `not_living_in_a_couple_widowed_or_surviving_partner_from_a_civi` | `bigint` | Count or numeric value for not living in a couple widowed or surviving partner from a civi in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
