# Census2021 Ts003 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts003_rgn`
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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts003_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 25
- **Metadata status:** source_mapped

## Description

Census2021 Ts003 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts003 rgn.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` |  |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `total` | `bigint` |  |
| `total_one_person_hh` | `bigint` |  |
| `one_person_hh_66plus` | `bigint` |  |
| `one_person_hh_other` | `bigint` |  |
| `total_single_family_hh` | `bigint` |  |
| `single_family_hh_66plus` | `bigint` |  |
| `total_single_family_hh_married_civil_partnership_couple` | `bigint` |  |
| `single_family_hh_married_civil_partnership_couple_no_children` | `bigint` |  |
| `single_family_hh_married_civil_partnership_couple_dependent_chi` | `bigint` |  |
| `single_family_hh_married_civil_partnership_couple_non_dependent` | `bigint` |  |
| `total_single_family_hh_cohabiting_couple_family` | `bigint` |  |
| `single_family_hh_cohabiting_couple_family_no_children` | `bigint` |  |
| `single_family_hh_cohabiting_couple_family_dependent_children` | `bigint` |  |
| `single_family_hh_cohabiting_couple_family_non_dependent_childre` | `bigint` |  |
| `total_single_family_hh_lone_parent_family` | `bigint` |  |
| `single_family_hh_lone_parent_family_dependent_children` | `bigint` |  |
| `single_family_hh_lone_parent_family_non_dependent_children` | `bigint` |  |
| `total_other_single_family_hh` | `bigint` |  |
| `other_single_family_hh_other_family_composition` | `bigint` |  |
| `total_other_hh_types` | `bigint` |  |
| `other_hh_types_dependent_children` | `bigint` |  |
| `other_hh_types_full_time_students_66plus` | `bigint` |  |
