# Religion Intzone

## Overview

- **Identifier:** `a_nrs_scotland/religion_intzone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `religion_intzone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Religion Intzone is an authoritative dataset published by National Records of Scotland. It contains records relating to religion intzone.

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
| `church_of_scotland` | `double precision` |  |
| `roman_catholic` | `double precision` |  |
| `other_christian` | `double precision` |  |
| `buddhist` | `double precision` |  |
| `hindu` | `double precision` |  |
| `jewish` | `double precision` |  |
| `muslim` | `double precision` |  |
| `sikh` | `double precision` |  |
| `pagan` | `double precision` |  |
| `other_religion` | `double precision` |  |
| `no_religion` | `double precision` |  |
| `religion_not_stated` | `double precision` | Recorded census measure for the category "religion not stated" in the represented area. Units and population base require the source table. |
