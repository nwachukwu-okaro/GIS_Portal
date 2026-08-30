# Area Information Data 2021 Sdz

## Overview

- **Identifier:** `a_nisra_nireland/area_information_data_2021_sdz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Schema:** `a_nisra_nireland`
- **Table:** `area_information_data_2021_sdz`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 850
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Area Information Data 2021 Sdz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to area information data 2021 sdz.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `population` | `text` | Publisher-supplied population for the represented feature or record. | source_attribute | Yes | No | No |
| `households` | `text` | Publisher-supplied households for the represented feature or record. | source_attribute | Yes | No | No |
| `area_hectares_note_1` | `double precision` | Numeric area hectares note 1 value recorded for the feature. | measure | Yes | No | No |
| `population_density_number_of_usual_residents_per_hectare` | `double precision` | Numeric population density number of usual residents per hectare value recorded for the feature. | measure | Yes | No | No |
| `unnamed_7` | `double precision` | Count or numeric value for unnamed 7 in the represented area. | statistical_value | Yes | No | No |
| `unnamed_8` | `double precision` | Count or numeric value for unnamed 8 in the represented area. | statistical_value | Yes | No | No |
| `unnamed_9` | `double precision` | Count or numeric value for unnamed 9 in the represented area. | statistical_value | Yes | No | No |
| `unnamed_10` | `double precision` | Count or numeric value for unnamed 10 in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
