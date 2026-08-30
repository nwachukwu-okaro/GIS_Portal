# Boundary Census Religion And Ethnicity Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_religion_and_ethnicity_data_2021_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_religion_and_ethnicity_data_2021_lgd`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 11
- **Metadata status:** source_mapped

## Description

Boundary Census Religion And Ethnicity Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census religion and ethnicity data 2021 lgd features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geography` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `year` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `population` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ethnic_group_other_ethnic_group` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ethnic_group_white` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `religion_or_religion_brought_up_in_catholic` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `religion_or_religion_brought_up_in_other_religions` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `religion_or_religion_brought_up_in_protestant_and_other_christi` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `religion_catholic` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `religion_church_of_ireland` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `religion_methodist_church_in_ireland` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `religion_no_religion_not_stated` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `religion_other_christian_including_christian_related` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `religion_other_religions` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `religion_presbyterian_church_in_ireland` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
