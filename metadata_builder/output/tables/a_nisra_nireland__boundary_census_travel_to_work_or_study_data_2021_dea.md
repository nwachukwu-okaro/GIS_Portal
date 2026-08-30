# Boundary Census Travel To Work Or Study Data 2021 Dea

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_travel_to_work_or_study_data_2021_dea`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_travel_to_work_or_study_data_2021_dea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 80
- **Metadata status:** source_mapped

## Description

Boundary Census Travel To Work Or Study Data 2021 Dea is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census travel to work or study data 2021 dea features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geography` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `year` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `distance_travelled_to_study_20km_and_over` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `distance_travelled_to_study_5km_20km` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `distance_travelled_to_study_less_than_5km` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `distance_travelled_to_study_mainly_at_or_from_home` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `distance_travelled_to_study_no_fixed_place` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `distance_travelled_to_study_outside_northern_ireland` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `distance_travelled_to_work_20km_and_over` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `distance_travelled_to_work_5km_20km` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `distance_travelled_to_work_less_than_5km` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `distance_travelled_to_work_mainly_at_or_from_home` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `distance_travelled_to_work_no_fixed_place` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `distance_travelled_to_work_outside_northern_ireland` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `method_of_travel_to_study_bus_or_train` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `method_of_travel_to_study_driving_a_car_or_van` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `method_of_travel_to_study_mainly_at_or_from_home` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `method_of_travel_to_study_other` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `method_of_travel_to_study_passenger_in_a_car_or_van` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `method_of_travel_to_study_walking_or_cycling` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `method_of_travel_to_work_bus_or_train` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `method_of_travel_to_work_driving_a_car_or_van` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `method_of_travel_to_work_mainly_at_or_from_home` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `method_of_travel_to_work_other` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `method_of_travel_to_work_passenger_in_a_car_or_van` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `method_of_travel_to_work_walking_or_cycling` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
