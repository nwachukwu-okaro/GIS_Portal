# Area Information Data 2021 Ni

## Overview

- **Identifier:** `a_nisra_nireland/area_information_data_2021_ni`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nisra_nireland`
- **Table:** `area_information_data_2021_ni`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Area Information Data 2021 Ni is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to area information data 2021 ni.

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
| `households` | `text` | Publisher-supplied households for the represented feature or record. |
| `area_hectares_note_1` | `text` | Numeric area hectares note 1 value recorded for the feature. |
| `population_density_number_of_usual_residents_per_hectare` | `double precision` | Numeric population density number of usual residents per hectare value recorded for the feature. |
