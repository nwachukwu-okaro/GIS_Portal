# Census2021 Ts019 Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts019_lsoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts019_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Census2021 Ts019 Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts019 lsoa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents` | `bigint` | Count or numeric value for total all usual residents in the represented area. | statistical_value | Yes | No | No |
| `address_one_year_ago_is_the_same_as_the_address_of_enumeration` | `bigint` | Count or numeric value for address one year ago is the same as the address of enumeration in the represented area. | statistical_value | Yes | No | No |
| `address_one_year_ago_is_student_term_time_or_boarding_school_ad` | `bigint` | Count or numeric value for address one year ago is student term time or boarding school ad in the represented area. | statistical_value | Yes | No | No |
| `migrant_from_within_the_uk_address_one_year_ago_was_in_the_uk` | `bigint` | Count or numeric value for migrant from within the uk address one year ago was in the uk in the represented area. | statistical_value | Yes | No | No |
| `migrant_from_outside_the_uk_address_one_year_ago_was_outside_th` | `bigint` | Count or numeric value for migrant from outside the uk address one year ago was outside th in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
