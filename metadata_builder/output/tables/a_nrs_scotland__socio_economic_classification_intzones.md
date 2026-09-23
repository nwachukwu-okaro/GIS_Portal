# Socio Economic Classification Intzones

## Overview

- **Identifier:** `a_nrs_scotland/socio_economic_classification_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `socio_economic_classification_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 18
- **Metadata status:** source_mapped

## Description

Socio Economic Classification Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to socio economic classification intzones.

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
| `all_people_aged_16_and_over` | `double precision` | Recorded census measure for the category "all people aged 16 and over" in the represented area. Units and population base require the source table. |
| `l1_employers_in_large_establishments` | `double precision` |  |
| `l2_higher_managerial_and_administrative_occupations` | `double precision` |  |
| `l3_higher_professional_occupations` | `double precision` |  |
| `l4_lower_professional_and_higher_technical_occupations` | `double precision` |  |
| `l5_lower_managerial_and_administrative_occupations` | `double precision` |  |
| `l6_higher_supervisory_occupations` | `double precision` |  |
| `l7_intermediate_occupations` | `double precision` |  |
| `l8_employers_in_small_establishments` | `double precision` |  |
| `l9_own_account_workers` | `double precision` |  |
| `l10_lower_supervisory_occupations` | `double precision` |  |
| `l11_lower_technical_occupations` | `double precision` |  |
| `l12_semi_routine_occupations` | `double precision` |  |
| `l13_routine_occupations` | `double precision` |  |
| `l14_1_never_worked` | `double precision` |  |
| `l14_2_long_term_unemployed` | `double precision` |  |
| `l15_full_time_students` | `double precision` |  |
