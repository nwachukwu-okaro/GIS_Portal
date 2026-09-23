# Household Composition Datazone

## Overview

- **Identifier:** `a_nrs_scotland/household_composition_datazone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `household_composition_datazone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7392
- **Columns:** 28
- **Metadata status:** source_mapped

## Description

Household Composition Datazone is an authoritative dataset published by National Records of Scotland. It contains records relating to household composition datazone.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Primary-key identifier for records in household_composition_datazone. |
| `geography_code` | `varchar` | Code assigned by the source dataset. |
| `all_people_in_households` | `integer` | Recorded census measure for the category "all people in households" in the represented area. Units and population base require the source table. |
| `one_family_household__all_aged_66_and_over` | `varchar` |  |
| `one_family_household__cohabiting_couple__all_children_non-depen` | `varchar` |  |
| `one_family_household__cohabiting_couple__no_children` | `varchar` |  |
| `one_family_household__cohabiting_couple__one_dependent_child` | `varchar` |  |
| `one_family_household__cohabiting_couple__total` | `integer` |  |
| `one_family_household__cohabiting_couple__two_or_more_dependent_` | `varchar` |  |
| `one_family_household__lone_parent_family__all_children_non-depe` | `varchar` |  |
| `one_family_household__lone_parent_family__one_dependent_child` | `varchar` |  |
| `one_family_household__lone_parent_family__total` | `integer` |  |
| `one_family_household__lone_parent_family__two_or_more_dependent` | `varchar` |  |
| `one_family_household__married_or_civil_partnership_couple__all_` | `varchar` |  |
| `one_family_household__married_or_civil_partnership_couple__no_c` | `varchar` |  |
| `one_family_household__married_or_civil_partnership_couple__one_` | `varchar` |  |
| `one_family_household__married_or_civil_partnership_couple__tota` | `integer` |  |
| `one_family_household__married_or_civil_partnership_couple__two_` | `varchar` |  |
| `one_family_household__total` | `integer` |  |
| `one_person_household__aged_66_and_over` | `varchar` |  |
| `one_person_household__aged_under_66` | `integer` |  |
| `one_person_household__total` | `integer` | Recorded census measure for the category "one person household  total" in the represented area. Units and population base require the source table. |
| `other_household_types__all_aged_66_and_over` | `varchar` |  |
| `other_household_types__all_full-time_students` | `varchar` |  |
| `other_household_types__one_dependent_child` | `varchar` |  |
| `other_household_types__other` | `varchar` |  |
| `other_household_types__total` | `varchar` |  |
| `other_household_types__two_or_more_dependent_children` | `varchar` |  |
