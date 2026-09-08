# Census2021 Ts003 Oa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts003_oa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts003_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 188880
- **Columns:** 25
- **Metadata status:** source_mapped

## Description

Census2021 Ts003 Oa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts003 oa.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `total` | `bigint` | Count or numeric value for total in the represented area. |
| `total_one_person_hh` | `bigint` | Count or numeric value for total one person households in the represented area. |
| `one_person_hh_66plus` | `bigint` | Count or numeric value for one person households 66plus in the represented area. |
| `one_person_hh_other` | `bigint` | Count or numeric value for one person households other in the represented area. |
| `total_single_family_hh` | `bigint` | Count or numeric value for total single family households in the represented area. |
| `single_family_hh_66plus` | `bigint` | Count or numeric value for single family households 66plus in the represented area. |
| `total_single_family_hh_married_civil_partnership_couple` | `bigint` | Count or numeric value for total single family households married civil partnership couple in the represented area. |
| `single_family_hh_married_civil_partnership_couple_no_children` | `bigint` | Count or numeric value for single family households married civil partnership couple number children in the represented area. |
| `single_family_hh_married_civil_partnership_couple_dependent_chi` | `bigint` | Count or numeric value for single family households married civil partnership couple dependent chi in the represented area. |
| `single_family_hh_married_civil_partnership_couple_non_dependent` | `bigint` | Count or numeric value for single family households married civil partnership couple non dependent in the represented area. |
| `total_single_family_hh_cohabiting_couple_family` | `bigint` | Count or numeric value for total single family households cohabiting couple family in the represented area. |
| `single_family_hh_cohabiting_couple_family_no_children` | `bigint` | Count or numeric value for single family households cohabiting couple family number children in the represented area. |
| `single_family_hh_cohabiting_couple_family_dependent_children` | `bigint` | Count or numeric value for single family households cohabiting couple family dependent children in the represented area. |
| `single_family_hh_cohabiting_couple_family_non_dependent_childre` | `bigint` | Count or numeric value for single family households cohabiting couple family non dependent childre in the represented area. |
| `total_single_family_hh_lone_parent_family` | `bigint` | Numeric total single family households lone parent family value recorded for the feature. |
| `single_family_hh_lone_parent_family_dependent_children` | `bigint` | Numeric single family households lone parent family dependent children value recorded for the feature. |
| `single_family_hh_lone_parent_family_non_dependent_children` | `bigint` | Numeric single family households lone parent family non dependent children value recorded for the feature. |
| `total_other_single_family_hh` | `bigint` | Count or numeric value for total other single family households in the represented area. |
| `other_single_family_hh_other_family_composition` | `bigint` | Count or numeric value for other single family households other family composition in the represented area. |
| `total_other_hh_types` | `bigint` | Count or numeric value for total other households types in the represented area. |
| `other_hh_types_dependent_children` | `bigint` | Count or numeric value for other households types dependent children in the represented area. |
| `other_hh_types_full_time_students_66plus` | `bigint` | Count or numeric value for other households types full time students 66plus in the represented area. |
