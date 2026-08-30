# Household Structure Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/household_structure_data_2021_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Schema:** `a_nisra_nireland`
- **Table:** `household_structure_data_2021_lgd`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 11
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Household Structure Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to household structure data 2021 lgd.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `population` | `text` | Publisher-supplied population for the represented feature or record. | source_attribute | Yes | No | No |
| `household_composition_one_person_household` | `text` | Publisher-supplied household composition one person household for the represented feature or record. | source_attribute | Yes | No | No |
| `household_composition_other_household_types_note_3` | `text` | Publisher-supplied household composition other household types note 3 for the represented feature or record. | source_attribute | Yes | No | No |
| `household_composition_single_family_all_pension_age_and_over_no` | `text` | Publisher-supplied household composition single family all pension age and over number for the represented feature or record. | source_attribute | Yes | No | No |
| `household_composition_single_family_cohabiting_couple_family` | `text` | Publisher-supplied household composition single family cohabiting couple family for the represented feature or record. | source_attribute | Yes | No | No |
| `household_composition_single_family_lone_parent_family` | `text` | Publisher-supplied household composition single family lone parent family for the represented feature or record. | source_attribute | Yes | No | No |
| `number_of_dependent_children_no_dependent_children_note_1` | `text` | Count or numeric value for number of dependent children number dependent children note 1 in the represented area. | statistical_value | Yes | No | No |
| `number_of_dependent_children_one` | `text` | Count or numeric value for number of dependent children one in the represented area. | statistical_value | Yes | No | No |
| `number_of_dependent_children_three_or_more` | `text` | Count or numeric value for number of dependent children three or more in the represented area. | statistical_value | Yes | No | No |
| `number_of_dependent_children_two` | `text` | Count or numeric value for number of dependent children two in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
