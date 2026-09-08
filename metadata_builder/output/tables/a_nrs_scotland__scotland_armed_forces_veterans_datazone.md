# Scotland Armed Forces Veterans Datazone

## Overview

- **Identifier:** `a_nrs_scotland/scotland_armed_forces_veterans_datazone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `scotland_armed_forces_veterans_datazone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7392
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Scotland Armed Forces Veterans Datazone is an authoritative dataset published by National Records of Scotland. It contains records relating to scotland armed forces veterans datazone.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. |
| `all_people_aged_16_and_over` | `bigint` | Count or numeric value for all people aged 16 and over in the represented area. |
| `uk_armed_forces_veteran` | `double precision` | Count or numeric value for uk armed forces veteran in the represented area. |
| `not_a_uk_armed_forces_veteran` | `bigint` | Count or numeric value for not a uk armed forces veteran in the represented area. |
| `total` | `bigint` | Count or numeric value for total in the represented area. |
| `hh_contains_at_least_one_uk_armed_forces_veteran` | `double precision` | Count or numeric value for households contains at least one uk armed forces veteran in the represented area. |
| `household_contains_no_uk_armed_forces_veterans` | `bigint` | Count or numeric value for household contains number uk armed forces veterans in the represented area. |
