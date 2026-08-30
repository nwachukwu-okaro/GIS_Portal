# Boundary Census Migration Data 2021 Dz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_migration_data_2021_dz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_migration_data_2021_dz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 3780
- **Metadata status:** source_mapped

## Description

Boundary Census Migration Data 2021 Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census migration data 2021 dz features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geography` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `year` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `address_one_year_ago_different_address_outside_northern_ireland` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `address_one_year_ago_different_address_within_northern_ireland` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `address_one_year_ago_lived_at_same_address` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `year_of_arrival_to_live_in_ni_arrived_2001_2010` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `year_of_arrival_to_live_in_ni_arrived_2011_2021` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `year_of_arrival_to_live_in_ni_arrived_before_2001` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `year_of_arrival_to_live_in_ni_born_in_northern_ireland` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
