# Census2021 Ts033 Oa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts033_oa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts033_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10275
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Census2021 Ts033 Oa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts033 oa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents_aged_3_years_and_over` | `bigint` | Count or numeric value for total all usual residents aged 3 years and over in the represented area. | statistical_value | Yes | No | No |
| `cannot_speak_welsh` | `bigint` | Count or numeric value for cannot speak welsh in the represented area. | statistical_value | Yes | No | No |
| `can_speak_welsh` | `bigint` | Count or numeric value for can speak welsh in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
