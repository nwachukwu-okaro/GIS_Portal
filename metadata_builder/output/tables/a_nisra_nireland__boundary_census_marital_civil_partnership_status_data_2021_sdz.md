# Boundary Census Marital Civil Partnership Status Data 2021 Sdz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_marital_civil_partnership_status_data_2021_sdz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177484, 54.022725, -5.432790, 55.312985]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_marital_civil_partnership_status_data_2021_sdz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 850
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Boundary Census Marital Civil Partnership Status Data 2021 Sdz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census marital civil partnership status data 2021 sdz features using multipolygon geometry.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `year` | `bigint` | Count or numeric value for year in the represented area. |
| `population` | `text` | Publisher-supplied population for the represented feature or record. |
| `marital_and_civil_partnership_status_divorced_or_formerly_in_a_` | `bigint` | Publisher-supplied marital and civil partnership status divorced or formerly in a for the represented feature or record. |
| `marital_and_civil_partnership_status_married_or_in_a_civil_part` | `text` | Publisher-supplied marital and civil partnership status married or in a civil part for the represented feature or record. |
| `marital_and_civil_partnership_status_separated` | `bigint` | Publisher-supplied marital and civil partnership status separated for the represented feature or record. |
| `marital_and_civil_partnership_status_single` | `text` | Publisher-supplied marital and civil partnership status single for the represented feature or record. |
| `marital_and_civil_partnership_status_widowed_or_surviving_partn` | `bigint` | Publisher-supplied marital and civil partnership status widowed or surviving partn for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
