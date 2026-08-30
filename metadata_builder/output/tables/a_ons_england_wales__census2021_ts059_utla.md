# Census2021 Ts059 Utla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts059_utla`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts059_utla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 174
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Census2021 Ts059 Utla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts059 utla.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents_aged_16_years_and_over_in_employment` | `bigint` | Count or numeric value for total all usual residents aged 16 years and over in employment in the represented area. | statistical_value | Yes | No | No |
| `part_time` | `bigint` | Count or numeric value for part time in the represented area. | statistical_value | Yes | No | No |
| `part_time_15_hours_or_less_worked` | `bigint` | Count or numeric value for part time 15 hours or less worked in the represented area. | statistical_value | Yes | No | No |
| `part_time_16_to_30_hours_worked` | `bigint` | Count or numeric value for part time 16 to 30 hours worked in the represented area. | statistical_value | Yes | No | No |
| `full_time` | `bigint` | Count or numeric value for full time in the represented area. | statistical_value | Yes | No | No |
| `full_time_31_to_48_hours_worked` | `bigint` | Count or numeric value for full time 31 to 48 hours worked in the represented area. | statistical_value | Yes | No | No |
| `full_time_49_or_more_hours_worked` | `bigint` | Count or numeric value for full time 49 or more hours worked in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
