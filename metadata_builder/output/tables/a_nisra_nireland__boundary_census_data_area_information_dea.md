# Boundary Census Data Area Information Dea

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_data_area_information_dea`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177502, 54.022724, -5.432789, 55.312984]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_data_area_information_dea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 80
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Boundary Census Data Area Information Dea is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census data area information dea features using multipolygon geometry.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `finalr_dea` | `varchar` | Publisher-supplied finalr dea for the represented feature or record. |
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `population` | `text` | Publisher-supplied population for the represented feature or record. |
| `households` | `text` | Publisher-supplied households for the represented feature or record. |
| `area_hectares_note_1` | `double precision` | Numeric area hectares note 1 value recorded for the feature. |
| `population_density_number_of_usual_residents_per_hectare` | `double precision` | Numeric population density number of usual residents per hectare value recorded for the feature. |
