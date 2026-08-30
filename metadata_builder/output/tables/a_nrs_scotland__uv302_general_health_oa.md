# Uv302 General Health Oa

## Overview

- **Identifier:** `a_nrs_scotland/uv302_general_health_oa`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `uv302_general_health_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 46368
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Uv302 General Health Oa is an authoritative dataset published by National Records of Scotland. It contains records relating to uv302 general health oa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `all_people` | `double precision` | Count or numeric value for all people in the represented area. | statistical_value | Yes | No | No |
| `very_good` | `double precision` | Count or numeric value for very good in the represented area. | statistical_value | Yes | No | No |
| `good` | `double precision` | Count or numeric value for good in the represented area. | statistical_value | Yes | No | No |
| `fair` | `double precision` | Count or numeric value for fair in the represented area. | statistical_value | Yes | No | No |
| `bad` | `double precision` | Count or numeric value for bad in the represented area. | statistical_value | Yes | No | No |
| `very_bad` | `double precision` | Count or numeric value for very bad in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
