# Ethnic Group Intzones

## Overview

- **Identifier:** `a_nrs_scotland/ethnic_group_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `ethnic_group_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 26
- **Metadata status:** source_mapped

## Description

Ethnic Group Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to ethnic group intzones.

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
| `white_total` | `double precision` |  |
| `white_white_scottish` | `double precision` |  |
| `white_other_white_british` | `double precision` |  |
| `white_white_irish` | `double precision` |  |
| `white_gypsy_traveller` | `double precision` |  |
| `white_white_polish` | `double precision` |  |
| `other_white` | `double precision` |  |
| `mixed_or_multiple_ethnic_group` | `double precision` |  |
| `asian_asian_scottish_or_asian_british_total` | `double precision` |  |
| `asian_asian_scottish_or_asian_british_pakistani_pakistani_sc` | `double precision` |  |
| `asian_asian_scottish_or_asian_british_indian_indian_scottish` | `double precision` |  |
| `asian_asian_scottish_or_asian_british_bangladeshi_bangladesh` | `double precision` |  |
| `asian_asian_scottish_or_asian_british_chinese_chinese_scotti` | `double precision` |  |
| `asian_asian_scottish_or_asian_british_other_asian` | `double precision` |  |
| `african_total` | `double precision` |  |
| `african_african_african_scottish_or_african_british` | `double precision` |  |
| `african_other_african` | `double precision` |  |
| `caribbean_or_black_total` | `double precision` |  |
| `caribbean_or_black_caribbean_caribbean_scottish_or_caribbean` | `double precision` |  |
| `caribbean_or_black_black_black_scottish_or_black_british` | `double precision` |  |
| `caribbean_or_black_other_caribbean_or_black` | `double precision` |  |
| `other_ethnic_groups_total` | `double precision` |  |
| `other_ethnic_groups_arab_arab_scottish_or_arab_british` | `double precision` |  |
| `other_ethnic_groups_other_ethnic_group` | `double precision` |  |
