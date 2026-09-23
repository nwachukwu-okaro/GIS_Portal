# Boundary Census Scotland Armed Forces Oa

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_armed_forces_oa`
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
- **Table:** `boundary_census_scotland_armed_forces_oa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 46363
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Armed Forces Oa is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland armed forces oa features using geometry geometry.

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
| `all_people_aged_16_and_over` | `bigint` | Recorded census measure for the category "all people aged 16 and over" in the represented area. Units and population base require the source table. |
| `uk_armed_forces_veteran` | `double precision` |  |
| `not_a_uk_armed_forces_veteran` | `bigint` |  |
| `all_households` | `bigint` | Recorded census measure for the category "all households" in the represented area. Units and population base require the source table. |
| `household_contains_no_uk_armed_forces_veterans` | `bigint` | Recorded census measure for the category "household contains no UK armed forces veterans" in the represented area. Units and population base require the source table. |
| `household_contains_at_least_one_uk_armed_forces_veteran` | `double precision` | Recorded census measure for the category "household contains at least one UK armed forces veteran" in the represented area. Units and population base require the source table. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
