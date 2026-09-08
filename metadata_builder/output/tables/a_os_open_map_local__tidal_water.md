# Tidal Water

## Overview

- **Identifier:** `a_os_open_map_local/tidal_water`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Map Local
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-map-local
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.756498, 49.814737, 1.848147, 60.948016]`
- **Topic category:** imageryBaseMapsEarthCover
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_open_map_local`
- **Table:** `tidal_water`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 3167
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Contains OS data © Crown copyright and database right 2026

## Lineage

Published by Ordnance Survey as part of OS Open Map Local. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. |
| `feature_code` | `integer` | Code assigned by the source dataset. |
| `fid` | `integer` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
