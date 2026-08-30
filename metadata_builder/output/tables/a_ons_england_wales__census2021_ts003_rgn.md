# Census2021 Ts003 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts003_rgn`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts003_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 25
- **Metadata status:** source_mapped

## Description

Census2021 Ts003 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts003 rgn.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total` | `bigint` | Count or numeric value for total in the represented area. | statistical_value | Yes | No | No |
| `total_one_person_hh` | `bigint` | Count or numeric value for total one person households in the represented area. | statistical_value | Yes | No | No |
| `one_person_hh_66plus` | `bigint` | Count or numeric value for one person households 66plus in the represented area. | statistical_value | Yes | No | No |
| `one_person_hh_other` | `bigint` | Count or numeric value for one person households other in the represented area. | statistical_value | Yes | No | No |
| `total_single_family_hh` | `bigint` | Count or numeric value for total single family households in the represented area. | statistical_value | Yes | No | No |
| `single_family_hh_66plus` | `bigint` | Count or numeric value for single family households 66plus in the represented area. | statistical_value | Yes | No | No |
| `total_single_family_hh_married_civil_partnership_couple` | `bigint` | Count or numeric value for total single family households married civil partnership couple in the represented area. | statistical_value | Yes | No | No |
| `single_family_hh_married_civil_partnership_couple_no_children` | `bigint` | Count or numeric value for single family households married civil partnership couple number children in the represented area. | statistical_value | Yes | No | No |
| `single_family_hh_married_civil_partnership_couple_dependent_chi` | `bigint` | Count or numeric value for single family households married civil partnership couple dependent chi in the represented area. | statistical_value | Yes | No | No |
| `single_family_hh_married_civil_partnership_couple_non_dependent` | `bigint` | Count or numeric value for single family households married civil partnership couple non dependent in the represented area. | statistical_value | Yes | No | No |
| `total_single_family_hh_cohabiting_couple_family` | `bigint` | Count or numeric value for total single family households cohabiting couple family in the represented area. | statistical_value | Yes | No | No |
| `single_family_hh_cohabiting_couple_family_no_children` | `bigint` | Count or numeric value for single family households cohabiting couple family number children in the represented area. | statistical_value | Yes | No | No |
| `single_family_hh_cohabiting_couple_family_dependent_children` | `bigint` | Count or numeric value for single family households cohabiting couple family dependent children in the represented area. | statistical_value | Yes | No | No |
| `single_family_hh_cohabiting_couple_family_non_dependent_childre` | `bigint` | Count or numeric value for single family households cohabiting couple family non dependent childre in the represented area. | statistical_value | Yes | No | No |
| `total_single_family_hh_lone_parent_family` | `bigint` | Numeric total single family households lone parent family value recorded for the feature. | measure | Yes | No | No |
| `single_family_hh_lone_parent_family_dependent_children` | `bigint` | Numeric single family households lone parent family dependent children value recorded for the feature. | measure | Yes | No | No |
| `single_family_hh_lone_parent_family_non_dependent_children` | `bigint` | Numeric single family households lone parent family non dependent children value recorded for the feature. | measure | Yes | No | No |
| `total_other_single_family_hh` | `bigint` | Count or numeric value for total other single family households in the represented area. | statistical_value | Yes | No | No |
| `other_single_family_hh_other_family_composition` | `bigint` | Count or numeric value for other single family households other family composition in the represented area. | statistical_value | Yes | No | No |
| `total_other_hh_types` | `bigint` | Count or numeric value for total other households types in the represented area. | statistical_value | Yes | No | No |
| `other_hh_types_dependent_children` | `bigint` | Count or numeric value for other households types dependent children in the represented area. | statistical_value | Yes | No | No |
| `other_hh_types_full_time_students_66plus` | `bigint` | Count or numeric value for other households types full time students 66plus in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
