# Census2021 Ts074 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts074_rgn`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts074_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Census2021 Ts074 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts074 rgn.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. | statistical_value | Yes | No | No |
| `household_reference_person_previously_served_in_regular_uk_arme` | `bigint` | Count or numeric value for household reference person previously served in regular uk arme in the represented area. | statistical_value | Yes | No | No |
| `household_reference_person_previously_served_in_reserve_uk_arme` | `bigint` | Count or numeric value for household reference person previously served in reserve uk arme in the represented area. | statistical_value | Yes | No | No |
| `household_reference_person_previously_served_in_both_regular_an` | `bigint` | Count or numeric value for household reference person previously served in both regular an in the represented area. | statistical_value | Yes | No | No |
| `household_reference_person_has_not_previously_served_in_regular` | `bigint` | Count or numeric value for household reference person has not previously served in regular in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
