# Area Information Data 2021 Sdz

## Overview

- **Identifier:** `a_nisra_nireland/area_information_data_2021_sdz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nisra_nireland`
- **Table:** `area_information_data_2021_sdz`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 850
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Area Information Data 2021 Sdz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to area information data 2021 sdz.

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
| `population` | `text` |  |
| `households` | `text` |  |
| `area_hectares_note_1` | `double precision` |  |
| `population_density_number_of_usual_residents_per_hectare` | `double precision` | Population density expressed as the number of usual residents per hectare. |
| `unnamed_7` | `double precision` |  |
| `unnamed_8` | `double precision` |  |
| `unnamed_9` | `double precision` |  |
| `unnamed_10` | `double precision` |  |
