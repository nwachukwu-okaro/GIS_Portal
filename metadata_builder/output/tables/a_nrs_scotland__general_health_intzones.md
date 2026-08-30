# General Health Intzones

## Overview

- **Identifier:** `a_nrs_scotland/general_health_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `general_health_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

General Health Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to general health intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
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
