# Language Data 2021 Ni

## Overview

- **Identifier:** `a_nisra_nireland/language_data_2021_ni`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nisra_nireland`
- **Table:** `language_data_2021_ni`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Language Data 2021 Ni is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to language data 2021 ni.

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
| `knowledge_of_irish_no_ability_in_irish` | `text` |  |
| `knowledge_of_irish_some_ability_in_irish` | `text` |  |
| `knowledge_of_ulster_scots_no_ability_in_ulster_scots` | `text` |  |
| `knowledge_of_ulster_scots_some_ability_in_ulster_scots` | `text` |  |
| `main_language_english` | `text` |  |
| `main_language_other_languages` | `text` |  |
