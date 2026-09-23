# Boundary Census Language Data 2021 Sdz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_language_data_2021_sdz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177484, 54.022725, -5.432790, 55.312985]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_language_data_2021_sdz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 850
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Boundary Census Language Data 2021 Sdz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census language data 2021 sdz features using multipolygon geometry.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geocode` | `text` | Code identifying the geographical area represented by the row. |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `year` | `bigint` | Reference year recorded for the statistical observation. |
| `population` | `text` |  |
| `knowledge_of_irish_no_ability_in_irish` | `text` |  |
| `knowledge_of_irish_some_ability_in_irish` | `text` |  |
| `knowledge_of_ulster_scots_no_ability_in_ulster_scots` | `text` |  |
| `knowledge_of_ulster_scots_some_ability_in_ulster_scots` | `text` |  |
| `main_language_english` | `text` |  |
| `main_language_other_languages` | `text` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
