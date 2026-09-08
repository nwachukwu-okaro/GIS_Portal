# Boundary Census Religion And Ethnicity Data 2021 Sdz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_religion_and_ethnicity_data_2021_sdz`
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
- **Table:** `boundary_census_religion_and_ethnicity_data_2021_sdz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 850
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

Boundary Census Religion And Ethnicity Data 2021 Sdz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census religion and ethnicity data 2021 sdz features using multipolygon geometry.

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
| `ethnic_group_other_ethnic_groups` | `text` | Publisher-supplied ethnic group other ethnic groups for the represented feature or record. |
| `ethnic_group_white` | `text` | Publisher-supplied ethnic group white for the represented feature or record. |
| `religion_or_religion_brought_up_in_catholic` | `text` | Publisher-supplied religion or religion brought up in catholic for the represented feature or record. |
| `religion_or_religion_brought_up_in_other_religions` | `bigint` | Publisher-supplied religion or religion brought up in other religions for the represented feature or record. |
| `religion_or_religion_brought_up_in_protestant_other_christian_i` | `text` | Publisher-supplied religion or religion brought up in protestant other christian i for the represented feature or record. |
| `religion_catholic` | `text` | Publisher-supplied religion catholic for the represented feature or record. |
| `religion_church_of_ireland` | `text` | Publisher-supplied religion church of ireland for the represented feature or record. |
| `religion_methodist` | `bigint` | Publisher-supplied religion methodist for the represented feature or record. |
| `religion_no_religion_not_stated` | `text` | Publisher-supplied religion number religion not stated for the represented feature or record. |
| `religion_other_christian_religions` | `bigint` | Publisher-supplied religion other christian religions for the represented feature or record. |
| `religion_other_religions` | `bigint` | Publisher-supplied religion other religions for the represented feature or record. |
| `religion_presbyterian` | `text` | Publisher-supplied religion presbyterian for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
