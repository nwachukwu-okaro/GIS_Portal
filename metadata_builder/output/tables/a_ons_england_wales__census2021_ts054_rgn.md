# Census2021 Ts054 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts054_rgn`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts054_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Census2021 Ts054 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts054 rgn.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. | statistical_value | Yes | No | No |
| `owned` | `bigint` | Count or numeric value for owned in the represented area. | statistical_value | Yes | No | No |
| `owned_owns_outright` | `bigint` | Count or numeric value for owned owns outright in the represented area. | statistical_value | Yes | No | No |
| `owned_owns_with_a_mortgage_or_loan` | `bigint` | Count or numeric value for owned owns with a mortgage or loan in the represented area. | statistical_value | Yes | No | No |
| `shared_ownership` | `bigint` | Count or numeric value for shared ownership in the represented area. | statistical_value | Yes | No | No |
| `shared_ownership_shared_ownership` | `bigint` | Count or numeric value for shared ownership shared ownership in the represented area. | statistical_value | Yes | No | No |
| `social_rented` | `bigint` | Count or numeric value for social rented in the represented area. | statistical_value | Yes | No | No |
| `social_rented_rents_from_council_or_local_authority` | `bigint` | Count or numeric value for social rented rents from council or local authority in the represented area. | statistical_value | Yes | No | No |
| `social_rented_other_social_rented` | `bigint` | Count or numeric value for social rented other social rented in the represented area. | statistical_value | Yes | No | No |
| `private_rented` | `bigint` | Count or numeric value for private rented in the represented area. | statistical_value | Yes | No | No |
| `private_rented_private_landlord_or_letting_agency` | `bigint` | Count or numeric value for private rented private landlord or letting agency in the represented area. | statistical_value | Yes | No | No |
| `private_rented_other_private_rented` | `bigint` | Count or numeric value for private rented other private rented in the represented area. | statistical_value | Yes | No | No |
| `lives_rent_free` | `bigint` | Count or numeric value for lives rent free in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
