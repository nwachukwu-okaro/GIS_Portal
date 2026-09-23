# Boundary Census Migration Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_migration_data_2021_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177503, 54.022724, -5.432784, 55.312985]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_migration_data_2021_lgd`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 22
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

Boundary Census Migration Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census migration data 2021 lgd features using multipolygon geometry.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `lgdname` | `varchar` |  |
| `area` | `double precision` |  |
| `lgdcode` | `varchar` |  |
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geocode` | `text` | Code identifying the geographical area represented by the row. |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `year` | `bigint` | Reference year recorded for the statistical observation. |
| `population` | `text` |  |
| `address_one_year_ago_different_address_outside_northern_ireland` | `text` |  |
| `address_one_year_ago_different_address_within_northern_ireland` | `text` | Recorded census measure for the category "address one year ago different address within northern ireland" in the represented area. Units and population base require the source table. |
| `address_one_year_ago_lived_at_same_address` | `text` | Recorded census measure for the category "address one year ago lived at same address" in the represented area. Units and population base require the source table. |
| `year_of_arrival_to_live_in_ni_arrived_2001_2010` | `text` |  |
| `year_of_arrival_to_live_in_ni_arrived_2011_2021` | `text` |  |
| `year_of_arrival_to_live_in_ni_arrived_before_2001` | `text` |  |
| `year_of_arrival_to_live_in_ni_born_in_northern_ireland` | `text` |  |
