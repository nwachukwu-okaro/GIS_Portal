# Boundary Census Sexual Orientation Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_sexual_orientation_data_2021_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177503, 54.022724, -5.432784, 55.312985]`
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_sexual_orientation_data_2021_lgd`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 11
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Boundary Census Sexual Orientation Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census sexual orientation data 2021 lgd features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `population` | `text` | Publisher-supplied population for the represented feature or record. | source_attribute | Yes | No | No |
| `sexual_orientation_gay_lesbian_bisexual_or_other_sexual_orienta` | `text` | Publisher-supplied sexual orientation gay lesbian bisexual or other sexual orienta for the represented feature or record. | source_attribute | Yes | No | No |
| `sexual_orientation_prefer_not_to_say_or_not_stated` | `text` | Publisher-supplied sexual orientation prefer not to say or not stated for the represented feature or record. | source_attribute | Yes | No | No |
| `sexual_orientation_straight_or_heterosexual` | `text` | Publisher-supplied sexual orientation straight or heterosexual for the represented feature or record. | source_attribute | Yes | No | No |
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
