# Boundary Censustravel To Work Or Study Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/boundary_censustravel_to_work_or_study_data_2021_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177503, 54.022724, -5.432784, 55.312985]`
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_censustravel_to_work_or_study_data_2021_lgd`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 11
- **Columns:** 28
- **Metadata status:** source_mapped

## Description

Boundary Censustravel To Work Or Study Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary censustravel to work or study data 2021 lgd features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `distance_travelled_to_study_20km_and_over` | `text` | Publisher-supplied distance travelled to study 20km and over for the represented feature or record. | source_attribute | Yes | No | No |
| `distance_travelled_to_study_5km_20km` | `text` | Publisher-supplied distance travelled to study 5km 20km for the represented feature or record. | source_attribute | Yes | No | No |
| `distance_travelled_to_study_less_than_5km` | `text` | Publisher-supplied distance travelled to study less than 5km for the represented feature or record. | source_attribute | Yes | No | No |
| `distance_travelled_to_study_mainly_at_or_from_home` | `text` | Publisher-supplied distance travelled to study mainly at or from home for the represented feature or record. | source_attribute | Yes | No | No |
| `distance_travelled_to_study_no_fixed_place` | `text` | Count or numeric value for distance travelled to study number fixed place in the represented area. | statistical_value | Yes | No | No |
| `distance_travelled_to_study_outside_northern_ireland` | `bigint` | Count or numeric value for distance travelled to study outside northern ireland in the represented area. | statistical_value | Yes | No | No |
| `distance_travelled_to_work_20km_and_over` | `text` | Publisher-supplied distance travelled to work 20km and over for the represented feature or record. | source_attribute | Yes | No | No |
| `distance_travelled_to_work_5km_20km` | `text` | Publisher-supplied distance travelled to work 5km 20km for the represented feature or record. | source_attribute | Yes | No | No |
| `distance_travelled_to_work_less_than_5km` | `text` | Publisher-supplied distance travelled to work less than 5km for the represented feature or record. | source_attribute | Yes | No | No |
| `distance_travelled_to_work_mainly_at_or_from_home` | `text` | Publisher-supplied distance travelled to work mainly at or from home for the represented feature or record. | source_attribute | Yes | No | No |
| `distance_travelled_to_work_no_fixed_place` | `text` | Publisher-supplied distance travelled to work number fixed place for the represented feature or record. | source_attribute | Yes | No | No |
| `distance_travelled_to_work_outside_northern_ireland` | `text` | Publisher-supplied distance travelled to work outside northern ireland for the represented feature or record. | source_attribute | Yes | No | No |
| `method_of_travel_to_study_bus_or_train` | `text` | Publisher-supplied method of travel to study bus or train for the represented feature or record. | source_attribute | Yes | No | No |
| `method_of_travel_to_study_driving_a_car_or_van` | `text` | Publisher-supplied method of travel to study driving a car or van for the represented feature or record. | source_attribute | Yes | No | No |
| `method_of_travel_to_study_mainly_at_or_from_home` | `text` | Publisher-supplied method of travel to study mainly at or from home for the represented feature or record. | source_attribute | Yes | No | No |
| `method_of_travel_to_study_other` | `text` | Count or numeric value for method of travel to study other in the represented area. | statistical_value | Yes | No | No |
| `method_of_travel_to_study_passenger_in_a_car_or_van` | `text` | Publisher-supplied method of travel to study passenger in a car or van for the represented feature or record. | source_attribute | Yes | No | No |
| `method_of_travel_to_study_walking_or_cycling` | `text` | Publisher-supplied method of travel to study walking or cycling for the represented feature or record. | source_attribute | Yes | No | No |
| `method_of_travel_to_work_bus_or_train` | `text` | Publisher-supplied method of travel to work bus or train for the represented feature or record. | source_attribute | Yes | No | No |
| `method_of_travel_to_work_driving_a_car_or_van` | `text` | Publisher-supplied method of travel to work driving a car or van for the represented feature or record. | source_attribute | Yes | No | No |
| `method_of_travel_to_work_mainly_at_or_from_home` | `text` | Publisher-supplied method of travel to work mainly at or from home for the represented feature or record. | source_attribute | Yes | No | No |
| `method_of_travel_to_work_other` | `text` | Count or numeric value for method of travel to work other in the represented area. | statistical_value | Yes | No | No |
| `method_of_travel_to_work_passenger_in_a_car_or_van` | `text` | Publisher-supplied method of travel to work passenger in a car or van for the represented feature or record. | source_attribute | Yes | No | No |
| `method_of_travel_to_work_walking_or_cycling` | `text` | Publisher-supplied method of travel to work walking or cycling for the represented feature or record. | source_attribute | Yes | No | No |
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
