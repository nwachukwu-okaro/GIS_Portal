# Household Structure Data 2021 Dz

## Overview

- **Identifier:** `a_nisra_nireland/household_structure_data_2021_dz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nisra_nireland`
- **Table:** `household_structure_data_2021_dz`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3780
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Household Structure Data 2021 Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to household structure data 2021 dz.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geocode` | `text` | Code identifying the geographical area represented by the row. |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `year` | `bigint` | Reference year recorded for the statistical observation. |
| `population` | `text` |  |
| `household_composition_one_person_household` | `bigint` |  |
| `household_composition_other_household_types` | `bigint` |  |
| `household_composition_single_family_all_pension_age_and_over` | `bigint` |  |
| `household_composition_single_family_cohabiting_couple_family` | `bigint` |  |
| `household_composition_single_family_lone_parent_family` | `bigint` |  |
| `household_composition_single_family_married_or_civil_partnershi` | `bigint` |  |
| `number_of_dependent_children_no_dependent_children` | `bigint` |  |
| `number_of_dependent_children_one` | `bigint` |  |
| `number_of_dependent_children_three_or_more` | `bigint` |  |
| `number_of_dependent_children_two` | `bigint` |  |
