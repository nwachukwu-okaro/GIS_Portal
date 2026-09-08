# Railway Station

## Overview

- **Identifier:** `a_os_open_map_local/railway_station`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Map Local
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-map-local
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-5.839545, 50.120998, 1.749599, 58.589996]`
- **Topic category:** imageryBaseMapsEarthCover
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_os_open_map_local`
- **Table:** `railway_station`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 3558
- **Columns:** 6
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
| `classification` | `varchar` | Publisher-supplied classification for the represented feature or record. |
| `distinctive_name` | `varchar` | Name associated with the represented feature. |
| `feature_code` | `integer` | Code assigned by the source dataset. |
| `fid` | `integer` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
