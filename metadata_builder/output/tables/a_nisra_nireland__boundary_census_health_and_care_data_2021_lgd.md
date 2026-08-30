# Boundary Census Health And Care Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_health_and_care_data_2021_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_health_and_care_data_2021_lgd`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 11
- **Metadata status:** source_mapped

## Description

Boundary Census Health And Care Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census health and care data 2021 lgd features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geography` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `year` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `general_health_bad` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `general_health_fair` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `general_health_good` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `general_health_very_bad` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `general_health_very_good` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `long_term_health_conditions_1_condition` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `long_term_health_conditions_2_conditions` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `long_term_health_conditions_3_or_more_conditions` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `long_term_health_conditions_no_conditions` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `long_term_health_problem_or_disability_activities_not_limited` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `long_term_health_problem_or_disability_limited_a_little` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `long_term_health_problem_or_disability_limited_a_lot` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `unpaid_care_1_19_hours` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `unpaid_care_20_49_hours` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `unpaid_care_50_hours` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `unpaid_care_provides_no_unpaid_care` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
