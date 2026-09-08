# Household Composition Car Van Availability Msoa

## Overview

- **Identifier:** `a_ons_england_wales/household_composition_car_van_availability_msoa`
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
- **Table:** `household_composition_car_van_availability_msoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7230
- **Columns:** 38
- **Metadata status:** source_mapped

## Description

Household Composition Car Van Availability Msoa is an authoritative dataset published by Office for National Statistics. It contains records relating to household composition car van availability msoa.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `msoa_code` | `varchar(9)` | Code assigned by the source dataset. |
| `geography` | `varchar(39)` | Publisher-supplied geography for the represented feature or record. |
| `does_not_apply_0_car_van` | `bigint` |  |
| `does_not_apply_1_car_van` | `bigint` |  |
| `does_not_apply_2_car_van` | `bigint` |  |
| `does_not_apply_3_car_van` | `bigint` |  |
| `does_not_apply_4_more_car_van` | `bigint` |  |
| `does_not_apply_does_not_apply` | `bigint` |  |
| `one_person_hh_0_car_van` | `bigint` |  |
| `one_person_hh_1_car_van` | `bigint` |  |
| `one_person_hh_2_car_van` | `bigint` |  |
| `one_person_hh_3_car_van` | `bigint` |  |
| `one_person_hh_4_more_car_van` | `bigint` |  |
| `one_person_hh_does_not_apply` | `bigint` |  |
| `single_fam_hh_all_66yrs_over_0_car_van` | `bigint` |  |
| `single_fam_hh_all_66yrs_over_1_car_van` | `bigint` |  |
| `single_fam_hh_all_66yrs_over_2_car_van` | `bigint` |  |
| `single_fam_hh_all_66yrs_over_3_car_van` | `bigint` |  |
| `single_fam_hh_all_66yrs_over_4_more_car_van` | `bigint` |  |
| `single_fam_hh_all_66yrs_over_does_not_apply` | `bigint` |  |
| `single_fam_hh_all_couple_family_0_car_van` | `bigint` |  |
| `single_fam_hh_all_couple_family_1_car_van` | `bigint` |  |
| `single_fam_hh_all_couple_family_2_car_van` | `bigint` |  |
| `single_fam_hh_all_couple_family_3_car_van` | `bigint` |  |
| `single_fam_hh_all_couple_family_4_more_car_van` | `bigint` |  |
| `single_fam_hh_all_couple_family_does_not_apply` | `bigint` |  |
| `single_fam_hh_all_lone_parent_0_car_van` | `bigint` |  |
| `single_fam_hh_all_lone_parent_1_car_van` | `bigint` |  |
| `single_fam_hh_all_lone_parent_2_car_van` | `bigint` |  |
| `single_fam_hh_all_lone_parent_3_car_van` | `bigint` |  |
| `single_fam_hh_all_lone_parent_4_more_car_van` | `bigint` |  |
| `single_fam_hh_all_lone_parent_does_not_apply` | `bigint` |  |
| `other_hh_types_0_car_van` | `bigint` |  |
| `other_hh_types_1_car_van` | `bigint` |  |
| `other_hh_types_2_car_van` | `bigint` |  |
| `other_hh_types_3_car_van` | `bigint` |  |
| `other_hh_types_4_more_car_van` | `bigint` |  |
| `other_hh_types_does_not_apply` | `bigint` |  |
