# Utla Boundary Bgc

## Overview

- **Identifier:** `a_ons_england_wales/utla_boundary_bgc`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418601, 49.864798, 1.763680, 55.811118]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ons_england_wales`
- **Table:** `utla_boundary_bgc`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 174
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Utla Boundary Bgc is an authoritative dataset published by Office for National Statistics. It represents utla boundary bgc features using multipolygon geometry.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Primary-key identifier for records in utla_boundary_bgc. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `ctyua22cd` | `varchar(9)` |  |
| `ctyua22nm` | `varchar(36)` |  |
| `ctyua22nmw` | `varchar(24)` |  |
| `bng_e` | `integer` |  |
| `bng_n` | `integer` |  |
| `long` | `double precision` |  |
| `lat` | `double precision` |  |
| `globalid` | `varchar(38)` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
