# Household Composition Household Intzones

## Overview

- **Identifier:** `a_nrs_scotland/household_composition_household_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `household_composition_household_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 27
- **Metadata status:** source_mapped

## Description

Household Composition Household Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to household composition household intzones.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `all_households` | `double precision` | Recorded census measure for the category "all households" in the represented area. Units and population base require the source table. |
| `one_person_household_total` | `double precision` | Recorded census measure for the category "one person household total" in the represented area. Units and population base require the source table. |
| `one_person_household_aged_66_and_over` | `double precision` | Recorded census measure for the category "one person household aged 66 and over" in the represented area. Units and population base require the source table. |
| `one_person_household_aged_under_66` | `double precision` |  |
| `one_family_household_total` | `double precision` |  |
| `one_family_household_all_aged_66_and_over` | `double precision` |  |
| `one_family_household_married_or_civil_partnership_couple_tot` | `double precision` |  |
| `one_family_household_married_or_civil_partnership_couple_no_` | `double precision` |  |
| `one_family_household_married_or_civil_partnership_couple_one` | `double precision` |  |
| `one_family_household_married_or_civil_partnership_couple_two` | `double precision` |  |
| `one_family_household_married_or_civil_partnership_couple_all` | `double precision` |  |
| `one_family_household_cohabiting_couple_total` | `double precision` |  |
| `one_family_household_cohabiting_couple_no_children` | `double precision` |  |
| `one_family_household_cohabiting_couple_one_dependent_child` | `double precision` |  |
| `one_family_household_cohabiting_couple_two_or_more_dependent` | `double precision` |  |
| `one_family_household_cohabiting_couple_all_children_non_depe` | `double precision` |  |
| `one_family_household_lone_parent_family_total` | `double precision` |  |
| `one_family_household_lone_parent_family_one_dependent_child` | `double precision` |  |
| `one_family_household_lone_parent_family_two_or_more_dependen` | `double precision` |  |
| `one_family_household_lone_parent_family_all_children_non_dep` | `double precision` |  |
| `other_household_types_total` | `double precision` |  |
| `other_household_types_one_dependent_child` | `double precision` |  |
| `other_household_types_two_or_more_dependent_children` | `double precision` |  |
| `other_household_types_all_full_time_students` | `double precision` |  |
| `other_household_types_all_aged_66_and_over` | `double precision` |  |
| `other_household_types_other` | `double precision` |  |
