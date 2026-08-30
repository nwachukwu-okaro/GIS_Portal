# Scotland Armed Forces Oa

## Overview

- **Identifier:** `a_nrs_scotland/scotland_armed_forces_oa`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `scotland_armed_forces_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 46363
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Scotland Armed Forces Oa is an authoritative dataset published by National Records of Scotland. It contains records relating to scotland armed forces oa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `all_people_aged_16_and_over` | `bigint` | Count or numeric value for all people aged 16 and over in the represented area. | statistical_value | Yes | No | No |
| `uk_armed_forces_veteran` | `double precision` | Count or numeric value for uk armed forces veteran in the represented area. | statistical_value | Yes | No | No |
| `not_a_uk_armed_forces_veteran` | `bigint` | Count or numeric value for not a uk armed forces veteran in the represented area. | statistical_value | Yes | No | No |
| `all_households` | `bigint` | Count or numeric value for all households in the represented area. | statistical_value | Yes | No | No |
| `household_contains_no_uk_armed_forces_veterans` | `bigint` | Count or numeric value for household contains number uk armed forces veterans in the represented area. | statistical_value | Yes | No | No |
| `household_contains_at_least_one_uk_armed_forces_veteran` | `double precision` | Count or numeric value for household contains at least one uk armed forces veteran in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
