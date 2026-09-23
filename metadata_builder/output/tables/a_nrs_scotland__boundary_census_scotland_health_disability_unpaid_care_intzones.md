# Boundary Census Scotland Health Disability Unpaid Care Intzones

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_health_disability_unpaid_care_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.650007, 54.633238, -0.724609, 60.860766]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_census_scotland_health_disability_unpaid_care_intzones`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1280
- **Columns:** 28
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Health Disability Unpaid Care Intzones is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland health disability unpaid care intzones features using multipolygon geometry.

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
| `geography_name` | `text` | Name associated with the represented feature. |
| `general_health_all_people` | `bigint` |  |
| `very_good` | `bigint` |  |
| `good` | `bigint` |  |
| `fair` | `bigint` |  |
| `bad` | `bigint` |  |
| `very_bad` | `bigint` |  |
| `lt_disability_all_people` | `bigint` |  |
| `daily_activities_limited_a_lot` | `bigint` |  |
| `daily_activities_limited_a_little` | `bigint` |  |
| `daily_activities_not_limited` | `bigint` |  |
| `lt_health_all_people` | `bigint` |  |
| `hearing_impairment` | `bigint` |  |
| `vision_impairment` | `bigint` |  |
| `speech_impairment` | `bigint` |  |
| `learning_disability_or_difficulty` | `bigint` |  |
| `physical_disability` | `bigint` |  |
| `mental_health_condition` | `bigint` |  |
| `long_term_illness` | `bigint` |  |
| `all_people_3plus` | `bigint` | Recorded census measure for the category "all people 3plus" in the represented area. Units and population base require the source table. |
| `no_unpaid_care` | `bigint` |  |
| `all_unpaid_carers` | `bigint` |  |
| `unpaid_care_1_19hrs_pw` | `bigint` |  |
| `unpaid_care_20_34hrs_pw` | `bigint` |  |
| `unpaid_care_35_49hrs_pw` | `bigint` |  |
| `unpaid_care_50plus_hrs_pw` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
