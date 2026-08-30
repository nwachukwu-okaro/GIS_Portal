# Census2021 Ts039asp Utla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts039asp_utla`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts039asp_utla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 174
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Census2021 Ts039asp Utla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts039asp utla.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `provides_no_unpaid_care` | `double precision` | Count or numeric value for provides number unpaid care in the represented area. | statistical_value | Yes | No | No |
| `provides_19_or_less_hours_unpaid_care_a_week` | `double precision` | Count or numeric value for provides 19 or less hours unpaid care a week in the represented area. | statistical_value | Yes | No | No |
| `provides_20_to_49_hours_unpaid_care_a_week` | `double precision` | Count or numeric value for provides 20 to 49 hours unpaid care a week in the represented area. | statistical_value | Yes | No | No |
| `provides_50_or_more_hours_unpaid_carea_week` | `double precision` | Numeric provides 50 or more hours unpaid carea week value recorded for the feature. | measure | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
