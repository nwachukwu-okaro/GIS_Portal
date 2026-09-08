# Boundary Census Household Structure Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_household_structure_data_2021_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177503, 54.022724, -5.432784, 55.312985]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_household_structure_data_2021_lgd`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 11
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Boundary Census Household Structure Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census household structure data 2021 lgd features using multipolygon geometry.

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
| `household_composition_one_person_household` | `text` | Publisher-supplied household composition one person household for the represented feature or record. |
| `household_composition_other_household_types_note_3` | `text` | Publisher-supplied household composition other household types note 3 for the represented feature or record. |
| `household_composition_single_family_all_pension_age_and_over_no` | `text` | Publisher-supplied household composition single family all pension age and over number for the represented feature or record. |
| `household_composition_single_family_cohabiting_couple_family` | `text` | Publisher-supplied household composition single family cohabiting couple family for the represented feature or record. |
| `household_composition_single_family_lone_parent_family` | `text` | Publisher-supplied household composition single family lone parent family for the represented feature or record. |
| `number_of_dependent_children_no_dependent_children_note_1` | `text` | Count or numeric value for number of dependent children number dependent children note 1 in the represented area. |
| `number_of_dependent_children_one` | `text` | Count or numeric value for number of dependent children one in the represented area. |
| `number_of_dependent_children_three_or_more` | `text` | Count or numeric value for number of dependent children three or more in the represented area. |
| `number_of_dependent_children_two` | `text` | Count or numeric value for number of dependent children two in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
