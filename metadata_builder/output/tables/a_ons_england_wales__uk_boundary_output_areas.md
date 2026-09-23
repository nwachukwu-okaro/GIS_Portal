# UK Boundary Output Areas

## Overview

- **Identifier:** `a_ons_england_wales/uk_boundary_output_areas`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418601, 49.864674, 1.763680, 55.811091]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ons_england_wales`
- **Table:** `uk_boundary_output_areas`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 188880
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

UK Boundary Output Areas is an authoritative dataset published by Office for National Statistics. It represents uk boundary output areas features using geometry geometry.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `oa21cd` | `text` |  |
| `lsoa21cd` | `text` |  |
| `lsoa21nm` | `text` |  |
| `lsoa21nmw` | `text` |  |
| `bng_e` | `integer` |  |
| `bng_n` | `integer` |  |
| `lat` | `real` |  |
| `long` | `real` |  |
| `globalid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `shape` | `geometry` | Spatial geometry of the represented feature. |
