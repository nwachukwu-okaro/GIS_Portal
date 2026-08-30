# Armed Forces Veterans Intzones

## Overview

- **Identifier:** `a_nrs_scotland/armed_forces_veterans_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `armed_forces_veterans_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Armed Forces Veterans Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to armed forces veterans intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `total` | `double precision` | Count or numeric value for total in the represented area. | statistical_value | Yes | No | No |
| `household_contains_at_least_one_uk_armed_forces_veteran` | `double precision` | Count or numeric value for household contains at least one uk armed forces veteran in the represented area. | statistical_value | Yes | No | No |
| `household_contains_no_uk_armed_forces_veterans` | `double precision` | Count or numeric value for household contains number uk armed forces veterans in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
