# Armed Forces Veterans Intzones

## Overview

- **Identifier:** `a_nrs_scotland/armed_forces_veterans_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `armed_forces_veterans_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Armed Forces Veterans Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to armed forces veterans intzones.

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
| `total` | `double precision` |  |
| `household_contains_at_least_one_uk_armed_forces_veteran` | `double precision` | Recorded census measure for the category "household contains at least one UK armed forces veteran" in the represented area. Units and population base require the source table. |
| `household_contains_no_uk_armed_forces_veterans` | `double precision` | Recorded census measure for the category "household contains no UK armed forces veterans" in the represented area. Units and population base require the source table. |
