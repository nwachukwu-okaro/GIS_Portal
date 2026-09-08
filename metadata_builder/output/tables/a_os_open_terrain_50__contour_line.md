# Contour Line

## Overview

- **Identifier:** `a_os_open_terrain_50/contour_line`
- **Source organisation:** Ordnance Survey
- **Product:** OS Terrain 50
- **Source:** https://www.ordnancesurvey.co.uk/products/os-terrain-50
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.649890, 49.865154, 1.760211, 60.860674]`
- **Topic category:** elevation
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Spatial resolution:** 50 metres (OS Terrain 50 grid post spacing)
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_os_open_terrain_50`
- **Table:** `contour_line`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 1006737
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Contains OS data © Crown copyright and database right 2026

## Lineage

Published by Ordnance Survey as part of OS Terrain 50. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. |
| `property_value` | `double precision` | Count or numeric value for property value in the represented area. |
| `contour_line_type` | `varchar` | Publisher-supplied contour line type for the represented feature or record. |
| `fid` | `integer` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
