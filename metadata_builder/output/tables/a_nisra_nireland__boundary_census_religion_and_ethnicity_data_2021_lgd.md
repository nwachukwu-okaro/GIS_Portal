# Boundary Census Religion And Ethnicity Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_religion_and_ethnicity_data_2021_lgd`
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
- **Table:** `boundary_census_religion_and_ethnicity_data_2021_lgd`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 11
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

Boundary Census Religion And Ethnicity Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census religion and ethnicity data 2021 lgd features using multipolygon geometry.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geocode` | `text` | Code identifying the geographical area represented by the row. |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `year` | `bigint` | Reference year recorded for the statistical observation. |
| `population` | `text` |  |
| `ethnic_group_other_ethnic_group` | `text` | Recorded census measure for the category "ethnic group other ethnic group" in the represented area. Units and population base require the source table. |
| `ethnic_group_white` | `text` | Recorded census measure for the category "ethnic group white" in the represented area. Units and population base require the source table. |
| `religion_or_religion_brought_up_in_catholic` | `text` | Recorded census measure for the category "religion or religion brought up in catholic" in the represented area. Units and population base require the source table. |
| `religion_or_religion_brought_up_in_other_religions` | `text` | Recorded census measure for the category "religion or religion brought up in other religions" in the represented area. Units and population base require the source table. |
| `religion_or_religion_brought_up_in_protestant_and_other_christi` | `text` |  |
| `religion_catholic` | `text` | Recorded census measure for the category "religion catholic" in the represented area. Units and population base require the source table. |
| `religion_church_of_ireland` | `text` | Recorded census measure for the category "religion church of ireland" in the represented area. Units and population base require the source table. |
| `religion_methodist_church_in_ireland` | `text` | Recorded census measure for the category "religion methodist church in ireland" in the represented area. Units and population base require the source table. |
| `religion_no_religion_not_stated` | `text` | Recorded census measure for the category "religion no religion not stated" in the represented area. Units and population base require the source table. |
| `religion_other_christian_including_christian_related` | `text` | Recorded census measure for the category "religion other christian including christian related" in the represented area. Units and population base require the source table. |
| `religion_other_religions` | `text` | Recorded census measure for the category "religion other religions" in the represented area. Units and population base require the source table. |
| `religion_presbyterian_church_in_ireland` | `text` | Recorded census measure for the category "religion presbyterian church in ireland" in the represented area. Units and population base require the source table. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
