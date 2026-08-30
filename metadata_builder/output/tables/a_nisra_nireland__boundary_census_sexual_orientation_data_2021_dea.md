# Boundary Census Sexual Orientation Data 2021 Dea

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_sexual_orientation_data_2021_dea`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_sexual_orientation_data_2021_dea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 80
- **Metadata status:** source_mapped

## Description

Boundary Census Sexual Orientation Data 2021 Dea is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census sexual orientation data 2021 dea features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geography` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `year` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `population` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sexual_orientation_gay_lesbian_bisexual_or_other_sexual_orienta` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sexual_orientation_prefer_not_to_say_or_not_stated` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sexual_orientation_straight_or_heterosexual` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
