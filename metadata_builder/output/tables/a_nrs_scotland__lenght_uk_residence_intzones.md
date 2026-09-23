# Lenght UK Residence Intzones

## Overview

- **Identifier:** `a_nrs_scotland/lenght_uk_residence_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `lenght_uk_residence_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Lenght UK Residence Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to lenght uk residence intzones.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `all_people` | `double precision` | Recorded census measure for the category "all people" in the represented area. Units and population base require the source table. |
| `born_in_the_uk` | `double precision` | Recorded census measure for the category "born in the UK" in the represented area. Units and population base require the source table. |
| `less_than_2_years` | `double precision` |  |
| `col_2_years_or_more_and_less_than_5_years` | `double precision` |  |
| `col_5_years_or_more_and_less_than_10_years` | `double precision` |  |
| `col_10_years_or_more` | `double precision` |  |
