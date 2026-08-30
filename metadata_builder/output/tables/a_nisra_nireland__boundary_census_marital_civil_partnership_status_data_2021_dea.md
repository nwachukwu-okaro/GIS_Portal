# Boundary Census Marital Civil Partnership Status Data 2021 Dea

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_marital_civil_partnership_status_data_2021_dea`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_marital_civil_partnership_status_data_2021_dea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 80
- **Metadata status:** source_mapped

## Description

Boundary Census Marital Civil Partnership Status Data 2021 Dea is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census marital civil partnership status data 2021 dea features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geography` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `year` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `population` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `marital_and_civil_partnership_status_divorced_or_formerly_in_a_` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `marital_and_civil_partnership_status_married_or_in_a_civil_part` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `marital_and_civil_partnership_status_separated` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `marital_and_civil_partnership_status_single` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `marital_and_civil_partnership_status_widowed_or_surviving_partn` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
