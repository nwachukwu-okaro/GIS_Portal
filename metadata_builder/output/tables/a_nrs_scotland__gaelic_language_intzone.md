# Gaelic Language Intzone

## Overview

- **Identifier:** `a_nrs_scotland/gaelic_language_intzone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `gaelic_language_intzone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Gaelic Language Intzone is an authoritative dataset published by National Records of Scotland. It contains records relating to gaelic language intzone.

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
| `all_people_aged_3_and_over` | `double precision` | Recorded census measure for the category "all people aged 3 and over" in the represented area. Units and population base require the source table. |
| `understands_but_does_not_speak_read_or_write_gaelic` | `double precision` |  |
| `speaks_reads_and_writes_gaelic` | `double precision` | Recorded census measure for the category "speaks reads and writes gaelic" in the represented area. Units and population base require the source table. |
| `speaks_but_does_not_read_or_write_gaelic` | `double precision` | Recorded census measure for the category "speaks but does not read or write gaelic" in the represented area. Units and population base require the source table. |
| `speaks_and_reads_but_does_not_write_gaelic` | `double precision` | Recorded census measure for the category "speaks and reads but does not write gaelic" in the represented area. Units and population base require the source table. |
| `reads_but_does_not_speak_or_write_gaelic` | `double precision` | Recorded census measure for the category "reads but does not speak or write gaelic" in the represented area. Units and population base require the source table. |
| `other_combination_of_skills_in_gaelic` | `double precision` |  |
| `no_skills_in_gaelic` | `double precision` |  |
