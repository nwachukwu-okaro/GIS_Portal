# Boundary Census Labour Market And Qualifications Data 2021 Dea

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_labour_market_and_qualifications_data_2021_dea`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177502, 54.022724, -5.432789, 55.312984]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_labour_market_and_qualifications_data_2021_dea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 80
- **Columns:** 35
- **Metadata status:** source_mapped

## Description

Boundary Census Labour Market And Qualifications Data 2021 Dea is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census labour market and qualifications data 2021 dea features using multipolygon geometry.

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
| `economic_activity_unemployed` | `text` |  |
| `highest_level_of_qualifications_apprenticeship` | `text` |  |
| `highest_level_of_qualifications_level_1` | `text` |  |
| `highest_level_of_qualifications_level_2` | `text` |  |
| `highest_level_of_qualifications_level_3` | `text` |  |
| `highest_level_of_qualifications_level_4_and_above` | `text` |  |
| `highest_level_of_qualifications_no_qualifications` | `text` |  |
| `highest_level_of_qualifications_other` | `bigint` |  |
| `hours_worked_per_week_15_hours_or_less` | `text` |  |
| `hours_worked_per_week_16_30_hours` | `text` |  |
| `hours_worked_per_week_31_48_hours` | `text` |  |
| `hours_worked_per_week_49_hours` | `text` |  |
| `industry_of_employment_agriculture_energy_and_water` | `text` |  |
| `industry_of_employment_construction` | `text` |  |
| `industry_of_employment_distribution_hotels_and_restaurants` | `text` |  |
| `industry_of_employment_financial_real_estate_professional_and_a` | `text` |  |
| `industry_of_employment_manufacturing` | `text` |  |
| `industry_of_employment_other` | `bigint` |  |
| `industry_of_employment_public_administration_education_and_heal` | `text` |  |
| `industry_of_employment_transport_and_communication` | `text` |  |
| `occupation_administrative_and_secretarial_occupations` | `text` |  |
| `occupation_associate_professional_and_technical_occupations` | `text` |  |
| `occupation_caring_leisure_and_other_service_occupations` | `text` |  |
| `occupation_elementary_occupations` | `text` |  |
| `occupation_managers_directors_and_senior_officials` | `text` |  |
| `occupation_process_plant_and_machine_operatives` | `text` |  |
| `occupation_professional_occupations` | `text` |  |
| `occupation_sales_and_customer_service_occupations` | `text` |  |
| `occupation_skilled_trades_occupations` | `text` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
