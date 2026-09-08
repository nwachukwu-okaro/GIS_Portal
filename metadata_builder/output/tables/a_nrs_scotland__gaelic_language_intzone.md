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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
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
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `all_people_aged_3_and_over` | `double precision` | Count or numeric value for all people aged 3 and over in the represented area. |
| `understands_but_does_not_speak_read_or_write_gaelic` | `double precision` | Count or numeric value for understands but does not speak read or write gaelic in the represented area. |
| `speaks_reads_and_writes_gaelic` | `double precision` | Count or numeric value for speaks reads and writes gaelic in the represented area. |
| `speaks_but_does_not_read_or_write_gaelic` | `double precision` | Count or numeric value for speaks but does not read or write gaelic in the represented area. |
| `speaks_and_reads_but_does_not_write_gaelic` | `double precision` | Count or numeric value for speaks and reads but does not write gaelic in the represented area. |
| `reads_but_does_not_speak_or_write_gaelic` | `double precision` | Count or numeric value for reads but does not speak or write gaelic in the represented area. |
| `other_combination_of_skills_in_gaelic` | `double precision` | Count or numeric value for other combination of skills in gaelic in the represented area. |
| `no_skills_in_gaelic` | `double precision` | Count or numeric value for number skills in gaelic in the represented area. |
