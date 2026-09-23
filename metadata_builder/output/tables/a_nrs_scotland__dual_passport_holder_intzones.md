# Dual Passport Holder Intzones

## Overview

- **Identifier:** `a_nrs_scotland/dual_passport_holder_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `dual_passport_holder_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Dual Passport Holder Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to dual passport holder intzones.

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
| `uk_and_irish_passport` | `double precision` |  |
| `uk_and_other_passport_europe_european_union` | `double precision` |  |
| `uk_and_other_passport_europe_other_europe` | `double precision` |  |
| `uk_and_non_european_passport` | `double precision` |  |
| `irish_and_other_passport_europe_european_union` | `double precision` |  |
| `irish_and_other_passport_europe_other_europe` | `double precision` |  |
| `irish_and_non_european_passport` | `double precision` |  |
| `other_combination_of_passports` | `double precision` |  |
| `does_not_have_dual_passports` | `double precision` |  |
