# Boundary Lad Dec 2024 UK Bfe

## Overview

- **Identifier:** `a_ons_england_wales/boundary_lad_dec_2024_uk_bfe`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-8.650007, 49.864637, 1.768950, 60.860846]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_lad_dec_2024_uk_bfe`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 361
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Boundary Lad Dec 2024 UK Bfe is an authoritative dataset published by Office for National Statistics. It represents boundary lad dec 2024 uk bfe features using multipolygon geometry.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `fid` | `integer` | Feature identifier assigned by the source or import process. |
| `lad24cd` | `varchar(9)` |  |
| `lad24nm` | `varchar(36)` |  |
| `lad24nmw` | `varchar(24)` |  |
| `bng_e` | `integer` |  |
| `bng_n` | `integer` |  |
| `long` | `real` |  |
| `lat` | `real` |  |
| `globalid` | `varchar(38)` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `shape` | `geometry` | Spatial geometry of the represented feature. |
