# Boundary Census Scotland Demography Migration Oa

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_demography_migration_oa`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.649996, 54.633220, -0.724450, 60.860787]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_census_scotland_demography_migration_oa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 46363
- **Columns:** 30
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Demography Migration Oa is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland demography migration oa features using geometry geometry.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. |
| `all_people_arrival_yr` | `bigint` | Recorded census measure for the category "all people arrival yr" in the represented area. Units and population base require the source table. |
| `born_in_the_uk_arrival_yr` | `bigint` | Recorded census measure for the category "born in the UK arrival yr" in the represented area. Units and population base require the source table. |
| `arrived_before_1941` | `double precision` |  |
| `arrived_1941_1950` | `double precision` |  |
| `arrived_1951_1960` | `double precision` |  |
| `arrived_1961_1970` | `double precision` |  |
| `arrived_1971_1980` | `double precision` |  |
| `arrived_1981_1990` | `double precision` |  |
| `arrived_1991_2000` | `double precision` |  |
| `arrived_2001_2010` | `double precision` |  |
| `arrived_2011_2013` | `double precision` |  |
| `arrived_2014_2016` | `double precision` |  |
| `arrived_2017_2019` | `double precision` |  |
| `arrived_2020_2022` | `double precision` |  |
| `all_people_arrival_age` | `bigint` | Recorded census measure for the category "all people arrival age" in the represented area. Units and population base require the source table. |
| `born_in_the_uk_arrival_age` | `bigint` | Recorded census measure for the category "born in the UK arrival age" in the represented area. Units and population base require the source table. |
| `arrived_aged_0_15` | `double precision` |  |
| `arrived_aged_16_24` | `double precision` |  |
| `arrived_aged_25_34` | `double precision` |  |
| `arrived_aged_35_49` | `double precision` |  |
| `arrived_aged_50_64` | `double precision` |  |
| `arrived_aged_65_and_over` | `double precision` |  |
| `all_people_residence_len` | `bigint` | Recorded census measure for the category "all people residence len" in the represented area. Units and population base require the source table. |
| `born_in_the_uk_residence_len` | `bigint` | Recorded census measure for the category "born in the UK residence len" in the represented area. Units and population base require the source table. |
| `less_than_2_years` | `double precision` |  |
| `t_2_years_or_more_and_less_than_5_years` | `double precision` |  |
| `t_5_years_or_more_and_less_than_10_years` | `double precision` |  |
| `t_10_years_or_more` | `double precision` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
