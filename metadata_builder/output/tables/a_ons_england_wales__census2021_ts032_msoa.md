# Census2021 Ts032 Msoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts032_msoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts032_msoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 408
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Census2021 Ts032 Msoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts032 msoa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents_aged_3_years_and_over` | `bigint` | Count or numeric value for total all usual residents aged 3 years and over in the represented area. | statistical_value | Yes | No | No |
| `can_understand_spoken_welsh_only` | `bigint` | Count or numeric value for can understand spoken welsh only in the represented area. | statistical_value | Yes | No | No |
| `can_speak_read_and_write_welsh` | `bigint` | Count or numeric value for can speak read and write welsh in the represented area. | statistical_value | Yes | No | No |
| `can_speak_but_cannot_read_or_write_welsh` | `bigint` | Count or numeric value for can speak but cannot read or write welsh in the represented area. | statistical_value | Yes | No | No |
| `can_speak_and_read_but_cannot_write_welsh` | `bigint` | Count or numeric value for can speak and read but cannot write welsh in the represented area. | statistical_value | Yes | No | No |
| `can_read_but_cannot_speak_or_write_welsh` | `bigint` | Count or numeric value for can read but cannot speak or write welsh in the represented area. | statistical_value | Yes | No | No |
| `can_write_but_cannot_speak_or_read_welsh` | `bigint` | Count or numeric value for can write but cannot speak or read welsh in the represented area. | statistical_value | Yes | No | No |
| `can_read_and_write_but_cannot_speak_welsh` | `bigint` | Count or numeric value for can read and write but cannot speak welsh in the represented area. | statistical_value | Yes | No | No |
| `can_speak_and_other_combinations_of_skills_in_welsh` | `bigint` | Count or numeric value for can speak and other combinations of skills in welsh in the represented area. | statistical_value | Yes | No | No |
| `no_skills_in_welsh` | `bigint` | Count or numeric value for number skills in welsh in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
