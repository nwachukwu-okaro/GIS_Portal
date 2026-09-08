# Boundary Census Country Of Birth And Nationality Data Lgd

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_country_of_birth_and_nationality_data_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177503, 54.022724, -5.432784, 55.312985]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_country_of_birth_and_nationality_data_lgd`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 11
- **Columns:** 24
- **Metadata status:** source_mapped

## Description

Boundary Census Country Of Birth And Nationality Data Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census country of birth and nationality data lgd features using multipolygon geometry.

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
| `country_of_birth_england` | `text` | Count or numeric value for country of birth england in the represented area. |
| `country_of_birth_northern_ireland` | `text` | Publisher-supplied country of birth northern ireland for the represented feature or record. |
| `country_of_birth_other_countries` | `text` | Publisher-supplied country of birth other countries for the represented feature or record. |
| `country_of_birth_republic_of_ireland` | `text` | Count or numeric value for country of birth republic of ireland in the represented area. |
| `country_of_birth_scotland` | `text` | Count or numeric value for country of birth scotland in the represented area. |
| `country_of_birth_wales` | `bigint` | Count or numeric value for country of birth wales in the represented area. |
| `national_identity_british_and_irish_only` | `text` | Publisher-supplied national identity british and irish only for the represented feature or record. |
| `national_identity_british_and_northern_irish_only` | `text` | Publisher-supplied national identity british and northern irish only for the represented feature or record. |
| `national_identity_british_only` | `text` | Publisher-supplied national identity british only for the represented feature or record. |
| `national_identity_british_irish_and_northern_irish_only` | `text` | Publisher-supplied national identity british irish and northern irish only for the represented feature or record. |
| `national_identity_irish_and_northern_irish_only` | `text` | Publisher-supplied national identity irish and northern irish only for the represented feature or record. |
| `national_identity_irish_only` | `text` | Publisher-supplied national identity irish only for the represented feature or record. |
| `national_identity_northern_irish_only` | `text` | Publisher-supplied national identity northern irish only for the represented feature or record. |
| `national_identity_other_national_identities` | `text` | Publisher-supplied national identity other national identities for the represented feature or record. |
| `passports_held_ireland_only` | `text` | Publisher-supplied passports held ireland only for the represented feature or record. |
| `passports_held_no_passport` | `text` | Publisher-supplied passports held number passport for the represented feature or record. |
| `passports_held_other_passports` | `text` | Publisher-supplied passports held other passports for the represented feature or record. |
| `passports_held_united_kingdom_and_ireland_only` | `text` | Publisher-supplied passports held united kingdom and ireland only for the represented feature or record. |
| `passports_held_united_kingdom_only` | `text` | Publisher-supplied passports held united kingdom only for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
