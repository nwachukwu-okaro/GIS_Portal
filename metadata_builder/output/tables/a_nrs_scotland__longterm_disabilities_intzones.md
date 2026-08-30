# Longterm Disabilities Intzones

## Overview

- **Identifier:** `a_nrs_scotland/longterm_disabilities_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `longterm_disabilities_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Longterm Disabilities Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to longterm disabilities intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
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
