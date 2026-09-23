# Boundary Census Labour Market And Qualifications Data 2021 Sdz

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_labour_market_and_qualifications_data_2021_sdz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177484, 54.022725, -5.432790, 55.312985]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_labour_market_and_qualifications_data_2021_sdz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 850
- **Columns:** 35
- **Metadata status:** source_mapped

## Description

Boundary Census Labour Market And Qualifications Data 2021 Sdz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census labour market and qualifications data 2021 sdz features using multipolygon geometry.

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
| `economic_activity_economically_inactive` | `text` |  |
| `economic_activity_in_employment` | `text` |  |
| `economic_activity_unemployed` | `bigint` |  |
| `highest_level_of_qualifications_apprenticeship` | `bigint` |  |
| `highest_level_of_qualifications_level_1` | `bigint` |  |
| `highest_level_of_qualifications_level_2` | `bigint` |  |
| `highest_level_of_qualifications_level_3` | `text` |  |
| `highest_level_of_qualifications_level_4_and_above` | `text` |  |
| `highest_level_of_qualifications_no_qualifications` | `text` |  |
| `highest_level_of_qualifications_other` | `bigint` |  |
| `hours_worked_per_week_15_hours_or_less` | `bigint` |  |
| `hours_worked_per_week_16_30_hours` | `bigint` |  |
| `hours_worked_per_week_31_48_hours` | `text` |  |
| `hours_worked_per_week_49_hours` | `bigint` |  |
| `industry_of_employment_agriculture_energy_and_water` | `bigint` |  |
| `industry_of_employment_construction` | `bigint` |  |
| `industry_of_employment_distribution_hotels_and_restaurants` | `bigint` |  |
| `industry_of_employment_financial_real_estate_professional_and_a` | `bigint` |  |
| `industry_of_employment_manufacturing` | `bigint` |  |
| `industry_of_employment_other` | `bigint` |  |
| `industry_of_employment_public_administration_education_and_heal` | `bigint` |  |
| `industry_of_employment_transport_and_communication` | `bigint` |  |
| `occupation_administrative_and_secretarial_occupations` | `bigint` |  |
| `occupation_associate_professional_and_technical_occupations` | `bigint` |  |
| `occupation_caring_leisure_and_other_service_occupations` | `bigint` |  |
| `occupation_elementary_occupations` | `bigint` |  |
| `occupation_managers_directors_and_senior_officials` | `bigint` |  |
| `occupation_process_plant_and_machine_operatives` | `bigint` |  |
| `occupation_professional_occupations` | `bigint` |  |
| `occupation_sales_and_customer_service_occupations` | `bigint` |  |
| `occupation_skilled_trades_occupations` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
