# Boundary Census Country Of Birth And Nationality Data Dea

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_country_of_birth_and_nationality_data_dea`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_country_of_birth_and_nationality_data_dea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 80
- **Metadata status:** source_mapped

## Description

Boundary Census Country Of Birth And Nationality Data Dea is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census country of birth and nationality data dea features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geography` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `year` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `population` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `country_of_birth_england` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `country_of_birth_northern_ireland` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `country_of_birth_other_countries` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `country_of_birth_republic_of_ireland` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `country_of_birth_scotland` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `country_of_birth_wales` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `national_identity_person_based_british_irish_only` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `national_identity_person_based_british_northern_irish_only` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `national_identity_person_based_british_only` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `national_identity_person_based_british_irish_northern_irish_onl` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `national_identity_person_based_irish_northern_irish_only` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `national_identity_person_based_irish_only` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `national_identity_person_based_northern_irish_only` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `national_identity_person_based_other_national_identities` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `passport_s_held_ireland_only` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `passport_s_held_no_passport` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `passport_s_held_other_passport_s` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `passport_s_held_uk_ireland` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `passport_s_held_uk_only` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
