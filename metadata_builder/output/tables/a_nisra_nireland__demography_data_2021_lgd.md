# Demography Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/demography_data_2021_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nisra_nireland`
- **Table:** `demography_data_2021_lgd`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 11
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Demography Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to demography data 2021 lgd.

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
| `broad_age_bands_years_0_14_years` | `text` |  |
| `broad_age_bands_years_15_39_years` | `text` |  |
| `broad_age_bands_years_40_64_years` | `text` |  |
| `broad_age_bands_years_65_years` | `text` |  |
| `household_size_five_or_more_people` | `text` |  |
| `household_size_four_people` | `text` |  |
| `household_size_one_person` | `text` |  |
| `household_size_three_people` | `text` |  |
| `household_size_two_people` | `text` |  |
| `sex_females` | `text` |  |
| `sex_males` | `text` |  |
