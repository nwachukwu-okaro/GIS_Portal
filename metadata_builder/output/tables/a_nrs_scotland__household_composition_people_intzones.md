# Household Composition People Intzones

## Overview

- **Identifier:** `a_nrs_scotland/household_composition_people_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `household_composition_people_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 27
- **Metadata status:** source_mapped

## Description

Household Composition People Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to household composition people intzones.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `all_people_in_households` | `double precision` | Count or numeric value for all people in households in the represented area. |
| `one_person_household_total` | `double precision` | Count or numeric value for one person household total in the represented area. |
| `one_person_household_aged_66_and_over` | `double precision` | Count or numeric value for one person household aged 66 and over in the represented area. |
| `one_person_household_aged_under_66` | `double precision` | Count or numeric value for one person household aged under 66 in the represented area. |
| `one_family_household_total` | `double precision` | Count or numeric value for one family household total in the represented area. |
| `one_family_household_all_aged_66_and_over` | `double precision` | Count or numeric value for one family household all aged 66 and over in the represented area. |
| `one_family_household_married_or_civil_partnership_couple_tot` | `double precision` | Count or numeric value for one family household married or civil partnership couple total in the represented area. |
| `one_family_household_married_or_civil_partnership_couple_no_` | `double precision` | Count or numeric value for one family household married or civil partnership couple number in the represented area. |
| `one_family_household_married_or_civil_partnership_couple_one` | `double precision` | Count or numeric value for one family household married or civil partnership couple one in the represented area. |
| `one_family_household_married_or_civil_partnership_couple_two` | `double precision` | Count or numeric value for one family household married or civil partnership couple two in the represented area. |
| `one_family_household_married_or_civil_partnership_couple_all` | `double precision` | Count or numeric value for one family household married or civil partnership couple all in the represented area. |
| `one_family_household_cohabiting_couple_total` | `double precision` | Count or numeric value for one family household cohabiting couple total in the represented area. |
| `one_family_household_cohabiting_couple_no_children` | `double precision` | Count or numeric value for one family household cohabiting couple number children in the represented area. |
| `one_family_household_cohabiting_couple_one_dependent_child` | `double precision` | Count or numeric value for one family household cohabiting couple one dependent child in the represented area. |
| `one_family_household_cohabiting_couple_two_or_more_dependent` | `double precision` | Count or numeric value for one family household cohabiting couple two or more dependent in the represented area. |
| `one_family_household_cohabiting_couple_all_children_non_depe` | `double precision` | Count or numeric value for one family household cohabiting couple all children non depe in the represented area. |
| `one_family_household_lone_parent_family_total` | `double precision` | Numeric one family household lone parent family total value recorded for the feature. |
| `one_family_household_lone_parent_family_one_dependent_child` | `double precision` | Numeric one family household lone parent family one dependent child value recorded for the feature. |
| `one_family_household_lone_parent_family_two_or_more_dependen` | `double precision` | Numeric one family household lone parent family two or more dependen value recorded for the feature. |
| `one_family_household_lone_parent_family_all_children_non_dep` | `double precision` | Numeric one family household lone parent family all children non dep value recorded for the feature. |
| `other_household_types_total` | `double precision` | Count or numeric value for other household types total in the represented area. |
| `other_household_types_one_dependent_child` | `double precision` | Count or numeric value for other household types one dependent child in the represented area. |
| `other_household_types_two_or_more_dependent_children` | `double precision` | Count or numeric value for other household types two or more dependent children in the represented area. |
| `other_household_types_all_full_time_students` | `double precision` | Count or numeric value for other household types all full time students in the represented area. |
| `other_household_types_all_aged_66_and_over` | `double precision` | Count or numeric value for other household types all aged 66 and over in the represented area. |
| `other_household_types_other` | `double precision` | Count or numeric value for other household types other in the represented area. |
