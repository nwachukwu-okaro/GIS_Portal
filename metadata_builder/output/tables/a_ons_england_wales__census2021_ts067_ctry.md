# Census2021 Ts067 Ctry

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts067_ctry`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts067_ctry`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Census2021 Ts067 Ctry is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts067 ctry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents_aged_16_years_and_over` | `bigint` | Count or numeric value for total all usual residents aged 16 years and over in the represented area. | statistical_value | Yes | No | No |
| `no_qualifications` | `bigint` | Count or numeric value for number qualifications in the represented area. | statistical_value | Yes | No | No |
| `level_1_and_entry_level_qualifications` | `bigint` | Count or numeric value for level 1 and entry level qualifications in the represented area. | statistical_value | Yes | No | No |
| `level_2_qualifications` | `bigint` | Count or numeric value for level 2 qualifications in the represented area. | statistical_value | Yes | No | No |
| `apprenticeship` | `bigint` | Count or numeric value for apprenticeship in the represented area. | statistical_value | Yes | No | No |
| `level_3_qualifications` | `bigint` | Count or numeric value for level 3 qualifications in the represented area. | statistical_value | Yes | No | No |
| `level_4_qualifications_and_above` | `bigint` | Count or numeric value for level 4 qualifications and above in the represented area. | statistical_value | Yes | No | No |
| `other_qualifications` | `bigint` | Count or numeric value for other qualifications in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
