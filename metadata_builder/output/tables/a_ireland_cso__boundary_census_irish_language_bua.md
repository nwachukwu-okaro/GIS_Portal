# Boundary Census Irish Language Bua

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_irish_language_bua`
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
- **Table:** `boundary_census_irish_language_bua`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 867
- **Columns:** 41
- **Metadata status:** source_mapped

## Description

Boundary Census Irish Language Bua is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census irish language bua features using geometry geometry.

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
| `yes` | `bigint` |  |
| `no` | `bigint` |  |
| `not_stated` | `bigint` |  |
| `total` | `bigint` |  |
| `daily_only_within_the_education_system_males` | `bigint` |  |
| `daily_within_and_daily_outside_the_education_system_males` | `bigint` |  |
| `daily_within_and_weekly_outside_the_education_system_males` | `bigint` |  |
| `daily_within_and_less_often_outside_the_education_system_males` | `bigint` |  |
| `daily_within_and_never_outside_the_education_system_males` | `bigint` |  |
| `daily_only_outside_the_education_system_males` | `bigint` |  |
| `weekly_only_outside_the_education_system_males` | `bigint` |  |
| `less_often_only_outside_the_education_system_males` | `bigint` |  |
| `never_speaks_irish_males` | `bigint` |  |
| `not_stated_males` | `bigint` |  |
| `all_irish_speakers_males` | `bigint` |  |
| `daily_only_within_the_education_system_females` | `bigint` |  |
| `daily_within_and_daily_outside_the_education_system_females` | `bigint` |  |
| `daily_within_and_weekly_outside_the_education_system_females` | `bigint` |  |
| `daily_within_and_less_often_outside_the_education_system_female` | `bigint` |  |
| `daily_within_and_never_outside_the_education_system_females` | `bigint` |  |
| `daily_only_outside_the_education_system_females` | `bigint` |  |
| `weekly_only_outside_the_education_system_females` | `bigint` |  |
| `less_often_only_outside_the_education_system_females` | `bigint` |  |
| `never_speaks_irish_females` | `bigint` |  |
| `not_stated_females` | `bigint` |  |
| `all_irish_speakers_females` | `bigint` |  |
| `daily_only_within_the_education_system_total` | `bigint` |  |
| `daily_within_and_daily_outside_the_education_system_total` | `bigint` |  |
| `daily_within_and_weekly_outside_the_education_system_total` | `bigint` |  |
| `daily_within_and_less_often_outside_the_education_system_total` | `bigint` |  |
| `daily_within_and_never_outside_the_education_system_total` | `bigint` |  |
| `daily_only_outside_the_education_system_total` | `bigint` |  |
| `weekly_only_outside_the_education_system_total` | `bigint` |  |
| `less_often_only_outside_the_education_system_total` | `bigint` |  |
| `never_speaks_irish_total` | `bigint` |  |
| `not_stated_total` | `bigint` |  |
| `all_irish_speakers_total` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
