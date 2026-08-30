# Boundary Census Country Of Birth And Nationality Data Dea

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_country_of_birth_and_nationality_data_dea`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177502, 54.022724, -5.432789, 55.312984]`
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_country_of_birth_and_nationality_data_dea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 80
- **Columns:** 24
- **Metadata status:** source_mapped

## Description

Boundary Census Country Of Birth And Nationality Data Dea is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census country of birth and nationality data dea features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `population` | `text` | Publisher-supplied population for the represented feature or record. | source_attribute | Yes | No | No |
| `country_of_birth_england` | `text` | Count or numeric value for country of birth england in the represented area. | statistical_value | Yes | No | No |
| `country_of_birth_northern_ireland` | `text` | Publisher-supplied country of birth northern ireland for the represented feature or record. | source_attribute | Yes | No | No |
| `country_of_birth_other_countries` | `text` | Publisher-supplied country of birth other countries for the represented feature or record. | source_attribute | Yes | No | No |
| `country_of_birth_republic_of_ireland` | `text` | Count or numeric value for country of birth republic of ireland in the represented area. | statistical_value | Yes | No | No |
| `country_of_birth_scotland` | `bigint` | Count or numeric value for country of birth scotland in the represented area. | statistical_value | Yes | No | No |
| `country_of_birth_wales` | `bigint` | Count or numeric value for country of birth wales in the represented area. | statistical_value | Yes | No | No |
| `national_identity_person_based_british_irish_only` | `bigint` | Count or numeric value for national identity person based british irish only in the represented area. | statistical_value | Yes | No | No |
| `national_identity_person_based_british_northern_irish_only` | `text` | Count or numeric value for national identity person based british northern irish only in the represented area. | statistical_value | Yes | No | No |
| `national_identity_person_based_british_only` | `text` | Publisher-supplied national identity person based british only for the represented feature or record. | source_attribute | Yes | No | No |
| `national_identity_person_based_british_irish_northern_irish_onl` | `text` | Count or numeric value for national identity person based british irish northern irish onl in the represented area. | statistical_value | Yes | No | No |
| `national_identity_person_based_irish_northern_irish_only` | `text` | Count or numeric value for national identity person based irish northern irish only in the represented area. | statistical_value | Yes | No | No |
| `national_identity_person_based_irish_only` | `text` | Publisher-supplied national identity person based irish only for the represented feature or record. | source_attribute | Yes | No | No |
| `national_identity_person_based_northern_irish_only` | `text` | Count or numeric value for national identity person based northern irish only in the represented area. | statistical_value | Yes | No | No |
| `national_identity_person_based_other_national_identities` | `text` | Publisher-supplied national identity person based other national identities for the represented feature or record. | source_attribute | Yes | No | No |
| `passport_s_held_ireland_only` | `text` | Publisher-supplied passport s held ireland only for the represented feature or record. | source_attribute | Yes | No | No |
| `passport_s_held_no_passport` | `text` | Count or numeric value for passport s held number passport in the represented area. | statistical_value | Yes | No | No |
| `passport_s_held_other_passport_s` | `text` | Publisher-supplied passport s held other passport s for the represented feature or record. | source_attribute | Yes | No | No |
| `passport_s_held_uk_ireland` | `text` | Count or numeric value for passport s held uk ireland in the represented area. | statistical_value | Yes | No | No |
| `passport_s_held_uk_only` | `text` | Publisher-supplied passport s held uk only for the represented feature or record. | source_attribute | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

## Supported operations

- filter
- select
- reproject
- validate_geometry
- buffer
- clip
- intersect
- spatial_join
- export

## Operation requirements

- Intersect, clip and spatial-join inputs must use matching coordinate reference systems.
- Buffer operations require a suitable projected coordinate reference system.
- Reprojection is performed on working outputs; source tables remain unchanged.

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
