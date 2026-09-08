# Boundary Lad Dec 2024 UK Bsc

## Overview

- **Identifier:** `a_ons_england_wales/boundary_lad_dec_2024_uk_bsc`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_lad_dec_2024_uk_bsc`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 0
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Boundary Lad Dec 2024 UK Bsc is an authoritative dataset published by Office for National Statistics. It represents boundary lad dec 2024 uk bsc features using multipolygon geometry.

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
| `bng_e` | `integer` | Count or numeric value for bng e in the represented area. |
| `bng_n` | `integer` | Count or numeric value for bng n in the represented area. |
| `long` | `real` | Numeric long value recorded for the feature. |
| `lat` | `real` | Numeric lat value recorded for the feature. |
| `globalid` | `varchar(38)` | Publisher-assigned globalid for the record. |
| `shape` | `geometry` | Spatial geometry of the represented feature. |
