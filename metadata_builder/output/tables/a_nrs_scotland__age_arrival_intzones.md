# Age Arrival Intzones

## Overview

- **Identifier:** `a_nrs_scotland/age_arrival_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `age_arrival_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Age Arrival Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to age arrival intzones.

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
| `col_0_15` | `double precision` |  |
| `col_16_24` | `double precision` |  |
| `col_25_34` | `double precision` |  |
| `col_35_49` | `double precision` |  |
| `col_50_64` | `double precision` |  |
| `col_65_and_over` | `double precision` |  |
