# Boundary Census Demography Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_demography_data_2021_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177503, 54.022724, -5.432784, 55.312985]`
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_demography_data_2021_lgd`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 11
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Boundary Census Demography Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census demography data 2021 lgd features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `broad_age_bands_years_0_14_years` | `text` | Publisher-supplied broad age bands years 0 14 years for the represented feature or record. | source_attribute | Yes | No | No |
| `broad_age_bands_years_15_39_years` | `text` | Publisher-supplied broad age bands years 15 39 years for the represented feature or record. | source_attribute | Yes | No | No |
| `broad_age_bands_years_40_64_years` | `text` | Publisher-supplied broad age bands years 40 64 years for the represented feature or record. | source_attribute | Yes | No | No |
| `broad_age_bands_years_65_years` | `text` | Publisher-supplied broad age bands years 65 years for the represented feature or record. | source_attribute | Yes | No | No |
| `household_size_five_or_more_people` | `text` | Publisher-supplied household size five or more people for the represented feature or record. | source_attribute | Yes | No | No |
| `household_size_four_people` | `text` | Publisher-supplied household size four people for the represented feature or record. | source_attribute | Yes | No | No |
| `household_size_one_person` | `text` | Publisher-supplied household size one person for the represented feature or record. | source_attribute | Yes | No | No |
| `household_size_three_people` | `text` | Publisher-supplied household size three people for the represented feature or record. | source_attribute | Yes | No | No |
| `household_size_two_people` | `text` | Publisher-supplied household size two people for the represented feature or record. | source_attribute | Yes | No | No |
| `sex_females` | `text` | Publisher-supplied sex females for the represented feature or record. | source_attribute | Yes | No | No |
| `sex_males` | `text` | Publisher-supplied sex males for the represented feature or record. | source_attribute | Yes | No | No |
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
