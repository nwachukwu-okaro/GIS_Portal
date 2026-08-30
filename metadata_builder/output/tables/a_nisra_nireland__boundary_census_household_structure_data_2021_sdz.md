# Boundary Census Household Structure Data 2021 Sdz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_household_structure_data_2021_sdz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177484, 54.022725, -5.432790, 55.312985]`
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_household_structure_data_2021_sdz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 850
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Boundary Census Household Structure Data 2021 Sdz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census household structure data 2021 sdz features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `population` | `text` | Publisher-supplied population for the represented feature or record. | source_attribute | Yes | No | No |
| `household_composition_one_person_household` | `bigint` | Publisher-supplied household composition one person household for the represented feature or record. | source_attribute | Yes | No | No |
| `household_composition_other_household_types_note_3` | `bigint` | Publisher-supplied household composition other household types note 3 for the represented feature or record. | source_attribute | Yes | No | No |
| `household_composition_single_family_all_pension_age_and_over_no` | `bigint` | Publisher-supplied household composition single family all pension age and over number for the represented feature or record. | source_attribute | Yes | No | No |
| `household_composition_single_family_cohabiting_couple_family` | `bigint` | Publisher-supplied household composition single family cohabiting couple family for the represented feature or record. | source_attribute | Yes | No | No |
| `household_composition_single_family_lone_parent_family` | `bigint` | Publisher-supplied household composition single family lone parent family for the represented feature or record. | source_attribute | Yes | No | No |
| `household_composition_single_family_married_or_civil_partnershi` | `bigint` | Publisher-supplied household composition single family married or civil partnershi for the represented feature or record. | source_attribute | Yes | No | No |
| `number_of_dependent_children_no_dependent_children_note_1` | `bigint` | Count or numeric value for number of dependent children number dependent children note 1 in the represented area. | statistical_value | Yes | No | No |
| `number_of_dependent_children_one` | `bigint` | Count or numeric value for number of dependent children one in the represented area. | statistical_value | Yes | No | No |
| `number_of_dependent_children_three_or_more` | `bigint` | Count or numeric value for number of dependent children three or more in the represented area. | statistical_value | Yes | No | No |
| `number_of_dependent_children_two` | `bigint` | Count or numeric value for number of dependent children two in the represented area. | statistical_value | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

## Supported operations

- filter
- select
- reproject
- validate_geometry
- buffer
- clip
- intersect
- spatial_join
- export

## Operation requirements

- Intersect, clip and spatial-join inputs must use matching coordinate reference systems.
- Buffer operations require a suitable projected coordinate reference system.
- Reprojection is performed on working outputs; source tables remain unchanged.

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
