# Language Data 2021 Sdz

## Overview

- **Identifier:** `a_nisra_nireland/language_data_2021_sdz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nisra_nireland`
- **Table:** `language_data_2021_sdz`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 850
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Language Data 2021 Sdz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to language data 2021 sdz.

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
| `knowledge_of_irish_no_ability_in_irish` | `text` | Count or numeric value for knowledge of irish number ability in irish in the represented area. |
| `knowledge_of_irish_some_ability_in_irish` | `text` | Count or numeric value for knowledge of irish some ability in irish in the represented area. |
| `knowledge_of_ulster_scots_no_ability_in_ulster_scots` | `text` | Count or numeric value for knowledge of ulster scots number ability in ulster scots in the represented area. |
| `knowledge_of_ulster_scots_some_ability_in_ulster_scots` | `text` | Count or numeric value for knowledge of ulster scots some ability in ulster scots in the represented area. |
| `main_language_english` | `text` | Count or numeric value for main language english in the represented area. |
| `main_language_other_languages` | `text` | Count or numeric value for main language other languages in the represented area. |
