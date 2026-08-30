# Boundary Census Data Area Information Dea

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_data_area_information_dea`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177502, 54.022724, -5.432789, 55.312984]`
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_data_area_information_dea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 80
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Boundary Census Data Area Information Dea is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census data area information dea features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `finalr_dea` | `varchar` | Publisher-supplied finalr dea for the represented feature or record. | source_attribute | Yes | No | No |
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `population` | `text` | Publisher-supplied population for the represented feature or record. | source_attribute | Yes | No | No |
| `households` | `text` | Publisher-supplied households for the represented feature or record. | source_attribute | Yes | No | No |
| `area_hectares_note_1` | `double precision` | Numeric area hectares note 1 value recorded for the feature. | measure | Yes | No | No |
| `population_density_number_of_usual_residents_per_hectare` | `double precision` | Numeric population density number of usual residents per hectare value recorded for the feature. | measure | Yes | No | No |

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
