# Uv116 Household Type Oa

## Overview

- **Identifier:** `a_nrs_scotland/uv116_household_type_oa`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `uv116_household_type_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 46368
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Uv116 Household Type Oa is an authoritative dataset published by National Records of Scotland. It contains records relating to uv116 household type oa.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. |
| `all_households` | `double precision` | Recorded census measure for the category "all households" in the represented area. Units and population base require the source table. |
| `one_person_household` | `double precision` | Recorded census measure for the category "one person household" in the represented area. Units and population base require the source table. |
| `married_or_civil_partnership_couple_household_no_dependent_chil` | `double precision` |  |
| `married_or_civil_partnership_couple_household_with_dependent_ch` | `double precision` |  |
| `cohabiting_couple_household_no_dependent_children` | `double precision` |  |
| `cohabiting_couple_household_with_dependent_children` | `double precision` |  |
| `lone_parent_household_no_dependent_children` | `double precision` |  |
| `lone_parent_household_with_dependent_children` | `double precision` |  |
| `multi_person_household_all_full_time_students` | `double precision` |  |
| `multi_person_household_other` | `double precision` |  |
