# Dual Passport Holder Intzones

## Overview

- **Identifier:** `a_nrs_scotland/dual_passport_holder_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `dual_passport_holder_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Dual Passport Holder Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to dual passport holder intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_people` | `double precision` | Count or numeric value for all people in the represented area. | statistical_value | Yes | No | No |
| `uk_and_irish_passport` | `double precision` | Count or numeric value for uk and irish passport in the represented area. | statistical_value | Yes | No | No |
| `uk_and_other_passport_europe_european_union` | `double precision` | Count or numeric value for uk and other passport europe european union in the represented area. | statistical_value | Yes | No | No |
| `uk_and_other_passport_europe_other_europe` | `double precision` | Count or numeric value for uk and other passport europe other europe in the represented area. | statistical_value | Yes | No | No |
| `uk_and_non_european_passport` | `double precision` | Count or numeric value for uk and non european passport in the represented area. | statistical_value | Yes | No | No |
| `irish_and_other_passport_europe_european_union` | `double precision` | Count or numeric value for irish and other passport europe european union in the represented area. | statistical_value | Yes | No | No |
| `irish_and_other_passport_europe_other_europe` | `double precision` | Count or numeric value for irish and other passport europe other europe in the represented area. | statistical_value | Yes | No | No |
| `irish_and_non_european_passport` | `double precision` | Count or numeric value for irish and non european passport in the represented area. | statistical_value | Yes | No | No |
| `other_combination_of_passports` | `double precision` | Count or numeric value for other combination of passports in the represented area. | statistical_value | Yes | No | No |
| `does_not_have_dual_passports` | `double precision` | Count or numeric value for does not have dual passports in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
