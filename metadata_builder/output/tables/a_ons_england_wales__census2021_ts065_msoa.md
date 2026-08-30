# Census2021 Ts065 Msoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts065_msoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts065_msoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Census2021 Ts065 Msoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts065 msoa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents_aged_16_years_and_over_not_in_employm` | `bigint` | Count or numeric value for total all usual residents aged 16 years and over not in employm in the represented area. | statistical_value | Yes | No | No |
| `not_in_employment_worked_in_the_last_12_months` | `bigint` | Count or numeric value for not in employment worked in the last 12 months in the represented area. | statistical_value | Yes | No | No |
| `not_in_employment_not_worked_in_the_last_12_months` | `bigint` | Count or numeric value for not in employment not worked in the last 12 months in the represented area. | statistical_value | Yes | No | No |
| `not_in_employment_never_worked` | `bigint` | Count or numeric value for not in employment never worked in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
