# Information Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/information_data_2021_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Schema:** `a_nisra_nireland`
- **Table:** `information_data_2021_lgd`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 11
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Information Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to information data 2021 lgd.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `population` | `text` | Publisher-supplied population for the represented feature or record. | source_attribute | Yes | No | No |
| `households` | `text` | Publisher-supplied households for the represented feature or record. | source_attribute | Yes | No | No |
| `area_hectares_note_1` | `text` | Numeric area hectares note 1 value recorded for the feature. | measure | Yes | No | No |
| `population_density_number_of_usual_residents_per_hectare` | `double precision` | Numeric population density number of usual residents per hectare value recorded for the feature. | measure | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
