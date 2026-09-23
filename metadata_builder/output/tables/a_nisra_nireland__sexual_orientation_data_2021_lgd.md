# Sexual Orientation Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/sexual_orientation_data_2021_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nisra_nireland`
- **Table:** `sexual_orientation_data_2021_lgd`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 11
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Sexual Orientation Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to sexual orientation data 2021 lgd.

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
| `sexual_orientation_gay_lesbian_bisexual_or_other_sexual_orienta` | `text` |  |
| `sexual_orientation_prefer_not_to_say_or_not_stated` | `text` |  |
| `sexual_orientation_straight_or_heterosexual` | `text` |  |
