# Boundary Census UK Armed Forces Veteran Utla

## Overview

- **Identifier:** `a_ons_england_wales/boundary_census_uk_armed_forces_veteran_utla`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_census_uk_armed_forces_veteran_utla`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 174
- **Metadata status:** source_mapped

## Description

Boundary Census UK Armed Forces Veteran Utla is an authoritative dataset published by Office for National Statistics. It represents boundary census uk armed forces veteran utla features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geography` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `uk_vet_total` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `previously_served_in_uk_armed_forces` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `previously_served_in_uk_reserve_armed_forces` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `prev_served_regular_and_reserve` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `has_not_previously_served_in_any_uk_armed_forces` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `num_in_hh_prev_served_total` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `no_people_in_the_hh_prev_served_uk_armed_forces` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `person_in_the_hh_prev_served_uk_armed_forces` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `people_in_the_hh_prev_served_uk_armed_forces` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `plus_people_in_the_hh_prev_served_uk_armed_forces` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `residence_type_total` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lives_in_a_household` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lives_in_a_communal_establishment` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `hrp_prev_served_total` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `hrp_prev_served_uk_regular` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `hrp_prev_served_uk_reserve` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `hrp_prev_served_regular_and_reserve` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `hrp_not_prev_served_uk_armed_forces` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
