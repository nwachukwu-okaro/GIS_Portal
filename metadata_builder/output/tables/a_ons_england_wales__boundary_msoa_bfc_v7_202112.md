# Boundary Msoa Bfc V7 202112

## Overview

- **Identifier:** `a_ons_england_wales/boundary_msoa_bfc_v7_202112`
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
- **Table:** `boundary_msoa_bfc_v7_202112`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 7264
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Boundary Msoa Bfc V7 202112 is an authoritative dataset published by Office for National Statistics. It represents boundary msoa bfc v7 202112 features using geometry geometry.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `msoa21cd` | `varchar(9)` |  |
| `msoa21nm` | `varchar(39)` |  |
| `msoa21nmw` | `varchar(29)` |  |
| `bng_e` | `integer` | Count or numeric value for bng e in the represented area. |
| `bng_n` | `integer` | Count or numeric value for bng n in the represented area. |
| `lat` | `double precision` | Numeric lat value recorded for the feature. |
| `long` | `double precision` | Numeric long value recorded for the feature. |
| `globalid` | `varchar(38)` | Publisher-assigned globalid for the record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
