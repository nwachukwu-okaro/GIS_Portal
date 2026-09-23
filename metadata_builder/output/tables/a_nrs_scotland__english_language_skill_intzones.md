# English Language Skill Intzones

## Overview

- **Identifier:** `a_nrs_scotland/english_language_skill_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `english_language_skill_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

English Language Skill Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to english language skill intzones.

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
| `understands_spoken_english_only` | `double precision` |  |
| `speaks_reads_and_writes_english` | `double precision` | Recorded census measure for the category "speaks reads and writes english" in the represented area. Units and population base require the source table. |
| `speaks_but_does_not_read_or_write_english` | `double precision` | Recorded census measure for the category "speaks but does not read or write english" in the represented area. Units and population base require the source table. |
| `speaks_and_reads_but_does_not_write_english` | `double precision` | Recorded census measure for the category "speaks and reads but does not write english" in the represented area. Units and population base require the source table. |
| `reads_but_does_not_speak_or_write_english` | `double precision` | Recorded census measure for the category "reads but does not speak or write english" in the represented area. Units and population base require the source table. |
| `writes_but_does_not_speak_or_read_english` | `double precision` | Recorded census measure for the category "writes but does not speak or read english" in the represented area. Units and population base require the source table. |
| `reads_and_writes_but_does_not_speak_english` | `double precision` | Recorded census measure for the category "reads and writes but does not speak english" in the represented area. Units and population base require the source table. |
| `other_combinations_of_skills_in_english` | `double precision` |  |
| `limited_english_skills` | `double precision` |  |
| `no_skills_in_english` | `double precision` |  |
