# Boundary Msoa Bfe V7 202112

## Overview

- **Identifier:** `a_ons_england_wales/boundary_msoa_bfe_v7_202112`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418945, 49.864637, 1.768912, 55.811668]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_msoa_bfe_v7_202112`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 7264
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Boundary Msoa Bfe V7 202112 is an authoritative dataset published by Office for National Statistics. It represents boundary msoa bfe v7 202112 features using geometry geometry.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `msoa21cd` | `varchar` |  |
| `msoa21nm` | `varchar` |  |
| `globalid` | `varchar` | Publisher-assigned globalid for the record. |
| `id` | `integer` | Count or numeric value for identifier in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
