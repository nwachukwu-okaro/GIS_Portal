# Longterm Disabilities Intzones

## Overview

- **Identifier:** `a_nrs_scotland/longterm_disabilities_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `longterm_disabilities_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Longterm Disabilities Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to longterm disabilities intzones.

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
| `day_to_day_activities_limited_a_lot` | `double precision` |  |
| `day_to_day_activities_limited_a_little` | `double precision` |  |
| `day_to_day_activities_not_limited` | `double precision` |  |
