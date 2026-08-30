# Uv116 Household Type Oa

## Overview

- **Identifier:** `a_nrs_scotland/uv116_household_type_oa`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `uv116_household_type_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 46368
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Uv116 Household Type Oa is an authoritative dataset published by National Records of Scotland. It contains records relating to uv116 household type oa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `all_households` | `double precision` | Count or numeric value for all households in the represented area. | statistical_value | Yes | No | No |
| `one_person_household` | `double precision` | Count or numeric value for one person household in the represented area. | statistical_value | Yes | No | No |
| `married_or_civil_partnership_couple_household_no_dependent_chil` | `double precision` | Count or numeric value for married or civil partnership couple household number dependent chil in the represented area. | statistical_value | Yes | No | No |
| `married_or_civil_partnership_couple_household_with_dependent_ch` | `double precision` | Count or numeric value for married or civil partnership couple household with dependent ch in the represented area. | statistical_value | Yes | No | No |
| `cohabiting_couple_household_no_dependent_children` | `double precision` | Count or numeric value for cohabiting couple household number dependent children in the represented area. | statistical_value | Yes | No | No |
| `cohabiting_couple_household_with_dependent_children` | `double precision` | Count or numeric value for cohabiting couple household with dependent children in the represented area. | statistical_value | Yes | No | No |
| `lone_parent_household_no_dependent_children` | `double precision` | Numeric lone parent household number dependent children value recorded for the feature. | measure | Yes | No | No |
| `lone_parent_household_with_dependent_children` | `double precision` | Numeric lone parent household with dependent children value recorded for the feature. | measure | Yes | No | No |
| `multi_person_household_all_full_time_students` | `double precision` | Count or numeric value for multi person household all full time students in the represented area. | statistical_value | Yes | No | No |
| `multi_person_household_other` | `double precision` | Count or numeric value for multi person household other in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
