# Boundary Census Marital Civil Partnership Status Data 2021 Dz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_marital_civil_partnership_status_data_2021_dz`
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
- **Table:** `boundary_census_marital_civil_partnership_status_data_2021_dz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 3780
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Boundary Census Marital Civil Partnership Status Data 2021 Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census marital civil partnership status data 2021 dz features using multipolygon geometry.

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
| `marital_and_civil_partnership_status_divorced_or_formerly_in_a_` | `bigint` |  |
| `marital_and_civil_partnership_status_married_or_in_a_civil_part` | `bigint` |  |
| `marital_and_civil_partnership_status_separated` | `bigint` |  |
| `marital_and_civil_partnership_status_single` | `text` |  |
| `marital_and_civil_partnership_status_widowed_or_surviving_partn` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
