# Tenure People Intzones

## Overview

- **Identifier:** `a_nrs_scotland/tenure_people_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `tenure_people_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Tenure People Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to tenure people intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_occupied_households` | `double precision` | Count or numeric value for all occupied households in the represented area. | statistical_value | Yes | No | No |
| `owned_total` | `double precision` | Count or numeric value for owned total in the represented area. | statistical_value | Yes | No | No |
| `owned_owned_outright` | `double precision` | Count or numeric value for owned owned outright in the represented area. | statistical_value | Yes | No | No |
| `owned_owned_with_a_mortgage_or_loan` | `double precision` | Count or numeric value for owned owned with a mortgage or loan in the represented area. | statistical_value | Yes | No | No |
| `owned_shared_ownership_part_owned_and_part_rented` | `double precision` | Count or numeric value for owned shared ownership part owned and part rented in the represented area. | statistical_value | Yes | No | No |
| `owned_shared_equity_e_g_lift_or_help_to_buy` | `double precision` | Count or numeric value for owned shared equity e g lift or help to buy in the represented area. | statistical_value | Yes | No | No |
| `social_rented_council_la_or_housing_association_registered_s` | `double precision` | Count or numeric value for social rented council la or housing association registered s in the represented area. | statistical_value | Yes | No | No |
| `private_rented_total` | `double precision` | Count or numeric value for private rented total in the represented area. | statistical_value | Yes | No | No |
| `private_rented_private_landlord_or_letting_agency` | `double precision` | Count or numeric value for private rented private landlord or letting agency in the represented area. | statistical_value | Yes | No | No |
| `private_rented_other` | `double precision` | Count or numeric value for private rented other in the represented area. | statistical_value | Yes | No | No |
| `lives_rent_free` | `double precision` | Count or numeric value for lives rent free in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
