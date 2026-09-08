# Boundary Census Demography Data 2021 Sdz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_demography_data_2021_sdz`
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
- **Table:** `boundary_census_demography_data_2021_sdz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 850
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Boundary Census Demography Data 2021 Sdz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census demography data 2021 sdz features using multipolygon geometry.

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
| `broad_age_bands_years_0_14_years` | `bigint` | Publisher-supplied broad age bands years 0 14 years for the represented feature or record. |
| `broad_age_bands_years_15_39_years` | `text` | Publisher-supplied broad age bands years 15 39 years for the represented feature or record. |
| `broad_age_bands_years_40_64_years` | `text` | Publisher-supplied broad age bands years 40 64 years for the represented feature or record. |
| `broad_age_bands_years_65_years` | `bigint` | Publisher-supplied broad age bands years 65 years for the represented feature or record. |
| `household_size_five_or_more_people` | `bigint` | Publisher-supplied household size five or more people for the represented feature or record. |
| `household_size_four_people` | `bigint` | Publisher-supplied household size four people for the represented feature or record. |
| `household_size_one_person` | `bigint` | Publisher-supplied household size one person for the represented feature or record. |
| `household_size_three_people` | `bigint` | Publisher-supplied household size three people for the represented feature or record. |
| `household_size_two_people` | `bigint` | Publisher-supplied household size two people for the represented feature or record. |
| `sex_females` | `text` | Publisher-supplied sex females for the represented feature or record. |
| `sex_males` | `text` | Publisher-supplied sex males for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
