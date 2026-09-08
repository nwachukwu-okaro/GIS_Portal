# Boundary Census Data Area Information Dz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_data_area_information_dz`
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
- **Table:** `boundary_census_data_area_information_dz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 3780
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

Boundary Census Data Area Information Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census data area information dz features using multipolygon geometry.

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
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `dz2021_cd` | `varchar(10)` | Publisher-supplied dz2021 cd for the represented feature or record. |
| `dz2021_nm` | `varchar(35)` | Publisher-supplied dz2021 nm for the represented feature or record. |
| `sdz2021_cd` | `varchar(254)` | Publisher-supplied sdz2021 cd for the represented feature or record. |
| `sdz2021_nm` | `varchar(32)` | Publisher-supplied sdz2021 nm for the represented feature or record. |
| `dea2014_cd` | `varchar(254)` | Publisher-supplied dea2014 cd for the represented feature or record. |
| `dea2014_nm` | `varchar(26)` | Publisher-supplied dea2014 nm for the represented feature or record. |
| `lgd2014_cd` | `varchar(9)` | Publisher-supplied lgd2014 cd for the represented feature or record. |
| `lgd2014_nm` | `varchar(36)` | Publisher-supplied lgd2014 nm for the represented feature or record. |
| `shape_length` | `double precision` | Numeric shape length value recorded for the feature. |
| `shape_area` | `double precision` | Numeric shape area value recorded for the feature. |
| `population` | `text` | Publisher-supplied population for the represented feature or record. |
| `households` | `bigint` | Publisher-supplied households for the represented feature or record. |
| `area_hectares_note_1` | `text` | Numeric area hectares note 1 value recorded for the feature. |
| `population_density_number_of_usual_residents_per_hectare` | `double precision` | Numeric population density number of usual residents per hectare value recorded for the feature. |
