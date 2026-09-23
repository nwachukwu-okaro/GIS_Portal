# Occupancy Rating Intzones

## Overview

- **Identifier:** `a_nrs_scotland/occupancy_rating_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `occupancy_rating_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Occupancy Rating Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to occupancy rating intzones.

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
| `all_occupied_households` | `double precision` | Recorded census measure for the category "all occupied households" in the represented area. Units and population base require the source table. |
| `one_bedroom` | `double precision` |  |
| `two_bedrooms` | `double precision` |  |
| `three_bedrooms` | `double precision` |  |
| `four_bedrooms` | `double precision` |  |
| `five_or_more_bedrooms` | `double precision` |  |
