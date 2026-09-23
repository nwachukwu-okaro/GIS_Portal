# National Identity Intzone

## Overview

- **Identifier:** `a_nrs_scotland/national_identity_intzone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `national_identity_intzone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

National Identity Intzone is an authoritative dataset published by National Records of Scotland. It contains records relating to national identity intzone.

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
| `scottish_identity_only` | `double precision` |  |
| `british_identity_only` | `double precision` |  |
| `scottish_and_british_identities_only` | `double precision` |  |
| `scottish_and_any_other_identities` | `double precision` |  |
| `english_identity_only` | `double precision` |  |
| `any_other_combination_of_uk_identities_uk_only` | `double precision` |  |
| `other_identity_only_1` | `double precision` |  |
| `other_identity_and_at_least_one_uk_identity` | `double precision` |  |
