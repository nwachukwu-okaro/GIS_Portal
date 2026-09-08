# Boundary Census Country Of Birth And Nationality Data Dz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_country_of_birth_and_nationality_data_dz`
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
- **Table:** `boundary_census_country_of_birth_and_nationality_data_dz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 3780
- **Columns:** 24
- **Metadata status:** source_mapped

## Description

Boundary Census Country Of Birth And Nationality Data Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census country of birth and nationality data dz features using multipolygon geometry.

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
| `country_of_birth_england` | `bigint` | Count or numeric value for country of birth england in the represented area. |
| `country_of_birth_northern_ireland` | `text` | Publisher-supplied country of birth northern ireland for the represented feature or record. |
| `country_of_birth_other_countries` | `bigint` | Publisher-supplied country of birth other countries for the represented feature or record. |
| `country_of_birth_republic_of_ireland` | `bigint` | Count or numeric value for country of birth republic of ireland in the represented area. |
| `country_of_birth_scotland` | `bigint` | Count or numeric value for country of birth scotland in the represented area. |
| `country_of_birth_wales` | `bigint` | Count or numeric value for country of birth wales in the represented area. |
| `national_identity_person_based_british_irish_only` | `bigint` | Count or numeric value for national identity person based british irish only in the represented area. |
| `national_identity_person_based_british_northern_irish_only` | `bigint` | Count or numeric value for national identity person based british northern irish only in the represented area. |
| `national_identity_person_based_british_only` | `bigint` | Publisher-supplied national identity person based british only for the represented feature or record. |
| `national_identity_person_based_british_irish_northern_irish_onl` | `bigint` | Count or numeric value for national identity person based british irish northern irish onl in the represented area. |
| `national_identity_person_based_irish_northern_irish_only` | `bigint` | Count or numeric value for national identity person based irish northern irish only in the represented area. |
| `national_identity_person_based_irish_only` | `bigint` | Publisher-supplied national identity person based irish only for the represented feature or record. |
| `national_identity_person_based_northern_irish_only` | `bigint` | Count or numeric value for national identity person based northern irish only in the represented area. |
| `national_identity_person_based_other_national_identities` | `bigint` | Publisher-supplied national identity person based other national identities for the represented feature or record. |
| `passport_s_held_ireland_only` | `bigint` | Publisher-supplied passport s held ireland only for the represented feature or record. |
| `passport_s_held_no_passport` | `bigint` | Count or numeric value for passport s held number passport in the represented area. |
| `passport_s_held_other_passport_s` | `bigint` | Publisher-supplied passport s held other passport s for the represented feature or record. |
| `passport_s_held_uk_ireland` | `bigint` | Count or numeric value for passport s held uk ireland in the represented area. |
| `passport_s_held_uk_only` | `bigint` | Publisher-supplied passport s held uk only for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
