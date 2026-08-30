# National Identity Intzone

## Overview

- **Identifier:** `a_nrs_scotland/national_identity_intzone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `national_identity_intzone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

National Identity Intzone is an authoritative dataset published by National Records of Scotland. It contains records relating to national identity intzone.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_people` | `double precision` | Count or numeric value for all people in the represented area. | statistical_value | Yes | No | No |
| `scottish_identity_only` | `double precision` | Count or numeric value for scottish identity only in the represented area. | statistical_value | Yes | No | No |
| `british_identity_only` | `double precision` | Count or numeric value for british identity only in the represented area. | statistical_value | Yes | No | No |
| `scottish_and_british_identities_only` | `double precision` | Count or numeric value for scottish and british identities only in the represented area. | statistical_value | Yes | No | No |
| `scottish_and_any_other_identities` | `double precision` | Count or numeric value for scottish and any other identities in the represented area. | statistical_value | Yes | No | No |
| `english_identity_only` | `double precision` | Count or numeric value for english identity only in the represented area. | statistical_value | Yes | No | No |
| `any_other_combination_of_uk_identities_uk_only` | `double precision` | Count or numeric value for any other combination of uk identities uk only in the represented area. | statistical_value | Yes | No | No |
| `other_identity_only_1` | `double precision` | Count or numeric value for other identity only 1 in the represented area. | statistical_value | Yes | No | No |
| `other_identity_and_at_least_one_uk_identity` | `double precision` | Count or numeric value for other identity and at least one uk identity in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
