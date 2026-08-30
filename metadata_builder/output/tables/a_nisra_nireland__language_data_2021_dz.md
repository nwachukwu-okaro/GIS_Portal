# Language Data 2021 Dz

## Overview

- **Identifier:** `a_nisra_nireland/language_data_2021_dz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Schema:** `a_nisra_nireland`
- **Table:** `language_data_2021_dz`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3780
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Language Data 2021 Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to language data 2021 dz.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `population` | `text` | Publisher-supplied population for the represented feature or record. | source_attribute | Yes | No | No |
| `knowledge_of_irish_no_ability_in_irish` | `text` | Count or numeric value for knowledge of irish number ability in irish in the represented area. | statistical_value | Yes | No | No |
| `knowledge_of_irish_some_ability_in_irish` | `bigint` | Count or numeric value for knowledge of irish some ability in irish in the represented area. | statistical_value | Yes | No | No |
| `knowledge_of_ulster_scots_no_ability_in_ulster_scots` | `text` | Count or numeric value for knowledge of ulster scots number ability in ulster scots in the represented area. | statistical_value | Yes | No | No |
| `knowledge_of_ulster_scots_some_ability_in_ulster_scots` | `bigint` | Count or numeric value for knowledge of ulster scots some ability in ulster scots in the represented area. | statistical_value | Yes | No | No |
| `main_language_english` | `text` | Count or numeric value for main language english in the represented area. | statistical_value | Yes | No | No |
| `main_language_other_languages` | `bigint` | Count or numeric value for main language other languages in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
