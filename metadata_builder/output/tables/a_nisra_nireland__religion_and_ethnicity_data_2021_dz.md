# Religion And Ethnicity Data 2021 Dz

## Overview

- **Identifier:** `a_nisra_nireland/religion_and_ethnicity_data_2021_dz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nisra_nireland`
- **Table:** `religion_and_ethnicity_data_2021_dz`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3780
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Religion And Ethnicity Data 2021 Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to religion and ethnicity data 2021 dz.

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
| `ethnic_group_other_ethnic_groups` | `bigint` | Recorded census measure for the category "ethnic group other ethnic groups" in the represented area. Units and population base require the source table. |
| `ethnic_group_white` | `text` | Recorded census measure for the category "ethnic group white" in the represented area. Units and population base require the source table. |
| `religion_or_religion_brought_up_in_catholic` | `text` | Recorded census measure for the category "religion or religion brought up in catholic" in the represented area. Units and population base require the source table. |
| `religion_or_religion_brought_up_in_other_religions` | `bigint` | Recorded census measure for the category "religion or religion brought up in other religions" in the represented area. Units and population base require the source table. |
| `religion_or_religion_brought_up_in_protestant_other_christian_i` | `bigint` |  |
| `religion_catholic` | `text` | Recorded census measure for the category "religion catholic" in the represented area. Units and population base require the source table. |
| `religion_church_of_ireland` | `bigint` | Recorded census measure for the category "religion church of ireland" in the represented area. Units and population base require the source table. |
| `religion_methodist` | `bigint` | Recorded census measure for the category "religion methodist" in the represented area. Units and population base require the source table. |
| `religion_no_religion_not_stated` | `bigint` | Recorded census measure for the category "religion no religion not stated" in the represented area. Units and population base require the source table. |
| `religion_other_christian_religions` | `bigint` | Recorded census measure for the category "religion other christian religions" in the represented area. Units and population base require the source table. |
| `religion_other_religions` | `bigint` | Recorded census measure for the category "religion other religions" in the represented area. Units and population base require the source table. |
| `religion_presbyterian` | `bigint` | Recorded census measure for the category "religion presbyterian" in the represented area. Units and population base require the source table. |
