# Boundary Census Social Class And Socioeconomic Group Small Area

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_social_class_and_socioeconomic_group_small_area`
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
- **Table:** `boundary_census_social_class_and_socioeconomic_group_small_area`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 18919
- **Columns:** 54
- **Metadata status:** source_mapped

## Description

Boundary Census Social Class And Socioeconomic Group Small Area is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census social class and socioeconomic group small area features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `guid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `geogid` | `text` | Code identifying the geographical area represented by the row. |
| `geogdesc` | `text` |  |
| `ur_category` | `double precision` |  |
| `ur_category_desc` | `text` |  |
| `professional_workers_males` | `bigint` |  |
| `managerial_and_technical_males` | `bigint` |  |
| `nonmanual_males` | `bigint` |  |
| `skilled_manual_males` | `bigint` |  |
| `semiskilled_males` | `bigint` |  |
| `unskilled_males` | `bigint` |  |
| `all_others_gainfully_occupied_and_unknown_males` | `bigint` |  |
| `total_males` | `bigint` | Census total for males in the represented geographical area; measurement unit requires the table documentation. |
| `professional_workers_females` | `bigint` |  |
| `managerial_and_technical_females` | `bigint` |  |
| `nonmanual_females` | `bigint` |  |
| `skilled_manual_females` | `bigint` |  |
| `semiskilled_females` | `bigint` |  |
| `unskilled_females` | `bigint` |  |
| `all_others_gainfully_occupied_and_unknown_females` | `bigint` |  |
| `total_females` | `bigint` | Census total for females in the represented geographical area; measurement unit requires the table documentation. |
| `professional_workers_total` | `bigint` |  |
| `managerial_and_technical_total` | `bigint` |  |
| `nonmanual_total` | `bigint` |  |
| `skilled_manual_total` | `bigint` |  |
| `semiskilled_total` | `bigint` |  |
| `unskilled_total` | `bigint` |  |
| `all_others_gainfully_occupied_and_unknown_total` | `bigint` |  |
| `total` | `bigint` |  |
| `a_employers_and_managers_no_of_households` | `bigint` |  |
| `b_higher_professional_no_of_households` | `bigint` |  |
| `c_lower_professional_no_of_households` | `bigint` |  |
| `d_nonmanual_no_of_households` | `bigint` |  |
| `e_manual_skilled_no_of_households` | `bigint` |  |
| `f_semiskilled_no_of_households` | `bigint` |  |
| `g_unskilled_no_of_households` | `bigint` |  |
| `h_own_account_workers_no_of_households` | `bigint` |  |
| `i_farmers_no_of_households` | `bigint` |  |
| `j_agricultural_workers_no_of_households` | `bigint` |  |
| `z_all_others_gainfully_occupied_and_unknown_no_of_households` | `bigint` |  |
| `total_no_of_households` | `bigint` | Recorded census measure for the category "total number of households" in the represented area. Units and population base require the source table. |
| `a_employers_and_managers_no_of_persons` | `bigint` |  |
| `b_higher_professional_no_of_persons` | `bigint` |  |
| `c_lower_professional_no_of_persons` | `bigint` |  |
| `d_nonmanual_no_of_persons` | `bigint` |  |
| `e_manual_skilled_no_of_persons` | `bigint` |  |
| `f_semiskilled_no_of_persons` | `bigint` |  |
| `g_unskilled_no_of_persons` | `bigint` |  |
| `h_own_account_workers_no_of_persons` | `bigint` |  |
| `i_farmers_no_of_persons` | `bigint` |  |
| `j_agricultural_workers_no_of_persons` | `bigint` |  |
| `z_all_others_gainfully_occupied_and_unknown_no_of_persons` | `bigint` |  |
| `total_no_of_persons` | `bigint` | Recorded census measure for the category "total number of persons" in the represented area. Units and population base require the source table. |
