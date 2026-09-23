# Boundary Census Commuting Working From Home And Childcare Csoed

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_commuting_working_from_home_and_childcare_csoed`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.726726, 54.563349, 3.417194, 58.519873]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_commuting_working_from_home_and_childcare_csoed`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 3420
- **Columns:** 66
- **Metadata status:** source_mapped

## Description

Boundary Census Commuting Working From Home And Childcare Csoed is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census commuting working from home and childcare csoed features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `ed_english` | `text` |  |
| `guid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `geogid` | `text` | Code identifying the geographical area represented by the row. |
| `geogdesc` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `on_foot_work` | `bigint` |  |
| `bicycle_work` | `bigint` |  |
| `bus_minibus_or_coach_work` | `bigint` |  |
| `train_dart_or_luas_work` | `bigint` |  |
| `motorcycle_or_scooter_work` | `bigint` |  |
| `car_driver_work` | `bigint` |  |
| `car_passenger_work` | `bigint` |  |
| `van_work` | `bigint` |  |
| `other_incl_lorry_work` | `bigint` |  |
| `work_mainly_at_or_from_home_work` | `bigint` |  |
| `not_stated_work` | `bigint` |  |
| `total_work` | `bigint` |  |
| `on_foot_school_college_or_childcare` | `bigint` |  |
| `bicycle_school_college_or_childcare` | `bigint` |  |
| `bus_minibus_or_coach_school_college_or_childcare` | `bigint` |  |
| `train_dart_or_luas_school_college_or_childcare` | `bigint` |  |
| `motorcycle_or_scooter_school_college_or_childcare` | `bigint` |  |
| `car_driver_school_college_or_childcare` | `bigint` |  |
| `car_passenger_school_college_or_childcare` | `bigint` |  |
| `van_school_college_or_childcare` | `bigint` |  |
| `other_incl_lorry_school_college_or_childcare` | `bigint` |  |
| `work_mainly_at_or_from_home_school_college_or_childcare` | `bigint` |  |
| `not_stated_school_college_or_childcare` | `bigint` |  |
| `total_school_college_or_childcare` | `bigint` |  |
| `on_foot_total` | `bigint` |  |
| `bicycle_total` | `bigint` |  |
| `bus_minibus_or_coach_total` | `bigint` |  |
| `train_dart_or_luas_total` | `bigint` |  |
| `motorcycle_or_scooter_total` | `bigint` |  |
| `car_driver_total` | `bigint` |  |
| `car_passenger_total` | `bigint` |  |
| `van_total` | `bigint` |  |
| `other_incl_lorry_total` | `bigint` |  |
| `work_mainly_at_or_from_home_total` | `bigint` |  |
| `not_stated_total` | `bigint` |  |
| `total` | `bigint` |  |
| `before_0630` | `bigint` |  |
| `t_0630_0700` | `bigint` |  |
| `t_0701_0730` | `bigint` |  |
| `t_0731_0800` | `bigint` |  |
| `t_0801_0830` | `bigint` |  |
| `t_0831_0900` | `bigint` |  |
| `t_0901_0930` | `bigint` |  |
| `after_0930` | `bigint` |  |
| `not_stated` | `bigint` |  |
| `total_1` | `bigint` |  |
| `under_15_mins` | `bigint` |  |
| `t_14_hour_under_12_hour` | `bigint` |  |
| `t_12_hour_under_34_hour` | `bigint` |  |
| `t_34_hour_under_1_hour` | `bigint` |  |
| `t_1_hour_under_1_12_hours` | `bigint` |  |
| `t_1_12_hours_and_over` | `bigint` |  |
| `not_stated_1` | `bigint` |  |
| `total_2` | `bigint` |  |
| `persons_who_work_from_home` | `bigint` |  |
| `persons_who_never_work_from_home` | `bigint` |  |
| `not_stated_2` | `bigint` |  |
| `total_3` | `bigint` |  |
| `children_ages_04_in_childcare` | `bigint` |  |
| `children_ages_514_in_childcare` | `bigint` |  |
| `total_children_under_15_in_childcare` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
