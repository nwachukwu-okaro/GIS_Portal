# Boundary Census Religion And Ethnicity Data 2021 Dz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_religion_and_ethnicity_data_2021_dz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177484, 54.022725, -5.432790, 55.312985]`
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_religion_and_ethnicity_data_2021_dz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 3780
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

Boundary Census Religion And Ethnicity Data 2021 Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census religion and ethnicity data 2021 dz features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `population` | `text` | Publisher-supplied population for the represented feature or record. | source_attribute | Yes | No | No |
| `ethnic_group_other_ethnic_groups` | `bigint` | Publisher-supplied ethnic group other ethnic groups for the represented feature or record. | source_attribute | Yes | No | No |
| `ethnic_group_white` | `text` | Publisher-supplied ethnic group white for the represented feature or record. | source_attribute | Yes | No | No |
| `religion_or_religion_brought_up_in_catholic` | `text` | Publisher-supplied religion or religion brought up in catholic for the represented feature or record. | source_attribute | Yes | No | No |
| `religion_or_religion_brought_up_in_other_religions` | `bigint` | Publisher-supplied religion or religion brought up in other religions for the represented feature or record. | source_attribute | Yes | No | No |
| `religion_or_religion_brought_up_in_protestant_other_christian_i` | `bigint` | Publisher-supplied religion or religion brought up in protestant other christian i for the represented feature or record. | source_attribute | Yes | No | No |
| `religion_catholic` | `text` | Publisher-supplied religion catholic for the represented feature or record. | source_attribute | Yes | No | No |
| `religion_church_of_ireland` | `bigint` | Publisher-supplied religion church of ireland for the represented feature or record. | source_attribute | Yes | No | No |
| `religion_methodist` | `bigint` | Publisher-supplied religion methodist for the represented feature or record. | source_attribute | Yes | No | No |
| `religion_no_religion_not_stated` | `bigint` | Publisher-supplied religion number religion not stated for the represented feature or record. | source_attribute | Yes | No | No |
| `religion_other_christian_religions` | `bigint` | Publisher-supplied religion other christian religions for the represented feature or record. | source_attribute | Yes | No | No |
| `religion_other_religions` | `bigint` | Publisher-supplied religion other religions for the represented feature or record. | source_attribute | Yes | No | No |
| `religion_presbyterian` | `bigint` | Publisher-supplied religion presbyterian for the represented feature or record. | source_attribute | Yes | No | No |
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
