# Boundary Census Household Structure Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_household_structure_data_2021_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_household_structure_data_2021_lgd`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 11
- **Metadata status:** source_mapped

## Description

Boundary Census Household Structure Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census household structure data 2021 lgd features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geography` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `year` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `population` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `household_composition_one_person_household` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `household_composition_other_household_types_note_3` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `household_composition_single_family_all_pension_age_and_over_no` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `household_composition_single_family_cohabiting_couple_family` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `household_composition_single_family_lone_parent_family` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `number_of_dependent_children_no_dependent_children_note_1` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `number_of_dependent_children_one` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `number_of_dependent_children_three_or_more` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `number_of_dependent_children_two` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
