# Uv303 Disability Oa

## Overview

- **Identifier:** `a_nrs_scotland/uv303_disability_oa`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `uv303_disability_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 46368
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Uv303 Disability Oa is an authoritative dataset published by National Records of Scotland. It contains records relating to uv303 disability oa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `all_people` | `double precision` | Count or numeric value for all people in the represented area. | statistical_value | Yes | No | No |
| `day_to_day_activities_limited_a_lot` | `double precision` | Count or numeric value for day to day activities limited a lot in the represented area. | statistical_value | Yes | No | No |
| `day_to_day_activities_limited_a_little` | `double precision` | Count or numeric value for day to day activities limited a little in the represented area. | statistical_value | Yes | No | No |
| `day_to_day_activities_not_limited` | `double precision` | Count or numeric value for day to day activities not limited in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
