# Provision Of Unpaid Care Intzones

## Overview

- **Identifier:** `a_nrs_scotland/provision_of_unpaid_care_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `provision_of_unpaid_care_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Provision Of Unpaid Care Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to provision of unpaid care intzones.

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
| `no` | `double precision` |  |
| `all_unpaid_carers` | `double precision` |  |
| `yes_1_to_19_hours_a_week` | `double precision` |  |
| `yes_20_to_34_hours_a_week` | `double precision` |  |
| `yes_35_to_49_hours_a_week` | `double precision` |  |
| `yes_50_or_more_hours_a_week` | `double precision` |  |
