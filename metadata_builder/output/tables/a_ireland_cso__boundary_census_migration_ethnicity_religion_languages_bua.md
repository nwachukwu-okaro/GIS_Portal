# Boundary Census Migration Ethnicity Religion Languages Bua

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_migration_ethnicity_religion_languages_bua`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.426272, 54.617106, 3.355468, 58.377636]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_migration_ethnicity_religion_languages_bua`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 867
- **Columns:** 48
- **Metadata status:** source_mapped

## Description

Boundary Census Migration Ethnicity Religion Languages Bua is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census migration ethnicity religion languages bua features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `guid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `geogid` | `text` | Code identifying the geographical area represented by the row. |
| `geogdesc` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `ireland_birthplace` | `bigint` |  |
| `uk_birthplace` | `bigint` |  |
| `poland_birthplace` | `bigint` |  |
| `india_birthplace` | `bigint` |  |
| `other_eu27_2020_birthplace` | `bigint` |  |
| `rest_of_world_birthplace` | `bigint` |  |
| `total_birthplace` | `bigint` |  |
| `ireland_citizenship` | `bigint` |  |
| `uk_citizenship` | `bigint` |  |
| `poland_citizenship` | `bigint` |  |
| `india_citizenship` | `bigint` |  |
| `other_eu27_2020_citizenship` | `bigint` |  |
| `rest_of_world_citizenship` | `bigint` |  |
| `not_stated_citizenship` | `bigint` |  |
| `total_citizenship` | `bigint` |  |
| `white_irish` | `bigint` |  |
| `white_irish_traveller` | `bigint` |  |
| `other_white` | `bigint` |  |
| `black_or_black_irish` | `bigint` |  |
| `asian_or_asian_irish` | `bigint` |  |
| `other` | `bigint` |  |
| `not_stated` | `bigint` |  |
| `total` | `bigint` |  |
| `same_address` | `bigint` |  |
| `elsewhere_in_county` | `bigint` |  |
| `elsewhere_in_ireland` | `bigint` |  |
| `outside_ireland` | `bigint` |  |
| `total_1` | `bigint` |  |
| `catholic` | `bigint` |  |
| `other_religion` | `bigint` |  |
| `no_religion` | `bigint` |  |
| `not_stated_1` | `bigint` |  |
| `total_2` | `bigint` |  |
| `polish` | `bigint` |  |
| `french` | `bigint` |  |
| `spanish` | `bigint` |  |
| `other_incl_not_stated` | `bigint` |  |
| `total_3` | `bigint` |  |
| `very_well` | `bigint` |  |
| `well` | `bigint` |  |
| `not_well` | `bigint` |  |
| `not_at_all` | `bigint` |  |
| `not_stated_2` | `bigint` |  |
| `total_4` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
