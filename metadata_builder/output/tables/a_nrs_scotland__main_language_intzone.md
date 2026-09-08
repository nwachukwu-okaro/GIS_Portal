# Main Language Intzone

## Overview

- **Identifier:** `a_nrs_scotland/main_language_intzone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `main_language_intzone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Main Language Intzone is an authoritative dataset published by National Records of Scotland. It contains records relating to main language intzone.

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
| `english` | `double precision` | Count or numeric value for english in the represented area. |
| `scots` | `double precision` | Count or numeric value for scots in the represented area. |
| `gaelic` | `double precision` | Count or numeric value for gaelic in the represented area. |
| `sign_language` | `double precision` | Count or numeric value for sign language in the represented area. |
| `other_language` | `double precision` | Count or numeric value for other language in the represented area. |
