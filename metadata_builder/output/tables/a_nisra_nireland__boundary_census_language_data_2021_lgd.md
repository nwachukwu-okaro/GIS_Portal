# Boundary Census Language Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_language_data_2021_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177503, 54.022724, -5.432784, 55.312985]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_language_data_2021_lgd`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 11
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Boundary Census Language Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census language data 2021 lgd features using multipolygon geometry.

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
| `knowledge_of_irish_no_ability_in_irish` | `text` | Count or numeric value for knowledge of irish number ability in irish in the represented area. |
| `knowledge_of_irish_some_ability_in_irish` | `text` | Count or numeric value for knowledge of irish some ability in irish in the represented area. |
| `knowledge_of_ulster_scots_no_ability_in_ulster_scots` | `text` | Count or numeric value for knowledge of ulster scots number ability in ulster scots in the represented area. |
| `knowledge_of_ulster_scots_some_ability_in_ulster_scots` | `text` | Count or numeric value for knowledge of ulster scots some ability in ulster scots in the represented area. |
| `main_language_english` | `text` | Count or numeric value for main language english in the represented area. |
| `main_language_other_languages` | `text` | Count or numeric value for main language other languages in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
