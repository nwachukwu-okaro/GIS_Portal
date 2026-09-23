# Demography Data 2021 Sdz

## Overview

- **Identifier:** `a_nisra_nireland/demography_data_2021_sdz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nisra_nireland`
- **Table:** `demography_data_2021_sdz`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 850
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Demography Data 2021 Sdz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to demography data 2021 sdz.

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
| `broad_age_bands_years_0_14_years` | `bigint` |  |
| `broad_age_bands_years_15_39_years` | `text` |  |
| `broad_age_bands_years_40_64_years` | `text` |  |
| `broad_age_bands_years_65_years` | `bigint` |  |
| `household_size_five_or_more_people` | `bigint` |  |
| `household_size_four_people` | `bigint` |  |
| `household_size_one_person` | `bigint` |  |
| `household_size_three_people` | `bigint` |  |
| `household_size_two_people` | `bigint` |  |
| `sex_females` | `text` |  |
| `sex_males` | `text` |  |
