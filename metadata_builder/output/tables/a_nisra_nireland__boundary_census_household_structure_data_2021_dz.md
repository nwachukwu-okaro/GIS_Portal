# Boundary Census Household Structure Data 2021 Dz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_household_structure_data_2021_dz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177484, 54.022725, -5.432790, 55.312985]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_household_structure_data_2021_dz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 3780
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Boundary Census Household Structure Data 2021 Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census household structure data 2021 dz features using multipolygon geometry.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `year` | `bigint` | Count or numeric value for year in the represented area. |
| `population` | `text` | Publisher-supplied population for the represented feature or record. |
| `household_composition_one_person_household` | `bigint` | Publisher-supplied household composition one person household for the represented feature or record. |
| `household_composition_other_household_types` | `bigint` | Count or numeric value for household composition other household types in the represented area. |
| `household_composition_single_family_all_pension_age_and_over` | `bigint` | Count or numeric value for household composition single family all pension age and over in the represented area. |
| `household_composition_single_family_cohabiting_couple_family` | `bigint` | Publisher-supplied household composition single family cohabiting couple family for the represented feature or record. |
| `household_composition_single_family_lone_parent_family` | `bigint` | Publisher-supplied household composition single family lone parent family for the represented feature or record. |
| `household_composition_single_family_married_or_civil_partnershi` | `bigint` | Publisher-supplied household composition single family married or civil partnershi for the represented feature or record. |
| `number_of_dependent_children_no_dependent_children` | `bigint` | Count or numeric value for number of dependent children number dependent children in the represented area. |
| `number_of_dependent_children_one` | `bigint` | Count or numeric value for number of dependent children one in the represented area. |
| `number_of_dependent_children_three_or_more` | `bigint` | Count or numeric value for number of dependent children three or more in the represented area. |
| `number_of_dependent_children_two` | `bigint` | Count or numeric value for number of dependent children two in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
