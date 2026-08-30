# Boundary Census Marital Civil Partnership Status Data 2021 Sdz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_marital_civil_partnership_status_data_2021_sdz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177484, 54.022725, -5.432790, 55.312985]`
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_marital_civil_partnership_status_data_2021_sdz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 850
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Boundary Census Marital Civil Partnership Status Data 2021 Sdz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census marital civil partnership status data 2021 sdz features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `population` | `text` | Publisher-supplied population for the represented feature or record. | source_attribute | Yes | No | No |
| `marital_and_civil_partnership_status_divorced_or_formerly_in_a_` | `bigint` | Publisher-supplied marital and civil partnership status divorced or formerly in a for the represented feature or record. | source_attribute | Yes | No | No |
| `marital_and_civil_partnership_status_married_or_in_a_civil_part` | `text` | Publisher-supplied marital and civil partnership status married or in a civil part for the represented feature or record. | source_attribute | Yes | No | No |
| `marital_and_civil_partnership_status_separated` | `bigint` | Publisher-supplied marital and civil partnership status separated for the represented feature or record. | source_attribute | Yes | No | No |
| `marital_and_civil_partnership_status_single` | `text` | Publisher-supplied marital and civil partnership status single for the represented feature or record. | source_attribute | Yes | No | No |
| `marital_and_civil_partnership_status_widowed_or_surviving_partn` | `bigint` | Publisher-supplied marital and civil partnership status widowed or surviving partn for the represented feature or record. | source_attribute | Yes | No | No |
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
