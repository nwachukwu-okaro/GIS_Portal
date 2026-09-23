# Boundary Census Household Structure Data 2021 Dea

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_household_structure_data_2021_dea`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177502, 54.022724, -5.432789, 55.312984]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_household_structure_data_2021_dea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 80
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Boundary Census Household Structure Data 2021 Dea is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census household structure data 2021 dea features using multipolygon geometry.

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
| `household_composition_one_person_household` | `text` |  |
| `household_composition_other_household_types_note_3` | `text` |  |
| `household_composition_single_family_all_pension_age_and_over_no` | `text` |  |
| `household_composition_single_family_cohabiting_couple_family` | `text` |  |
| `household_composition_single_family_lone_parent_family` | `text` |  |
| `household_composition_single_family_married_or_civil_partnershi` | `text` |  |
| `number_of_dependent_children_no_dependent_children_note_1` | `bigint` |  |
| `number_of_dependent_children_one` | `bigint` |  |
| `number_of_dependent_children_three_or_more` | `bigint` |  |
| `number_of_dependent_children_two` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
