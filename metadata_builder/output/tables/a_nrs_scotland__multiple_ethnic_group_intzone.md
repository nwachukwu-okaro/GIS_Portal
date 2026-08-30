# Multiple Ethnic Group Intzone

## Overview

- **Identifier:** `a_nrs_scotland/multiple_ethnic_group_intzone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `multiple_ethnic_group_intzone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Multiple Ethnic Group Intzone is an authoritative dataset published by National Records of Scotland. It contains records relating to multiple ethnic group intzone.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_occupied_households` | `double precision` | Count or numeric value for all occupied households in the represented area. | statistical_value | Yes | No | No |
| `one_person_household` | `double precision` | Count or numeric value for one person household in the represented area. | statistical_value | Yes | No | No |
| `all_household_members_have_the_same_ethnic_group` | `double precision` | Count or numeric value for all household members have the same ethnic group in the represented area. | statistical_value | Yes | No | No |
| `different_identities_between_the_generations_only` | `double precision` | Count or numeric value for different identities between the generations only in the represented area. | statistical_value | Yes | No | No |
| `different_identities_within_partnerships_whether_or_not_also` | `double precision` | Count or numeric value for different identities within partnerships whether or not also in the represented area. | statistical_value | Yes | No | No |
| `any_other_combination_of_multiple_ethnic_identities` | `double precision` | Count or numeric value for any other combination of multiple ethnic identities in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
