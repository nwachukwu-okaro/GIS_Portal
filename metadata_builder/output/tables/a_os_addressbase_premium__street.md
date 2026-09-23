# Street

## Overview

- **Identifier:** `a_os_addressbase_premium/street`
- **Source organisation:** Ordnance Survey
- **Product:** AddressBase Premium
- **Source:** https://www.ordnancesurvey.co.uk/products/addressbase-premium
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.571197, 49.872875, 1.761354, 60.814182]`
- **Topic category:** location
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_addressbase_premium`
- **Table:** `street`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 1526341
- **Columns:** 24
- **Metadata status:** source_mapped

## Description

Street is part of AddressBase Premium, published by Ordnance Survey. It represents street features using geometry geometry.

## Lineage

Published by Ordnance Survey as part of AddressBase Premium. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `change_type` | `text` |  |
| `usrn` | `bigint` | Unique Street Reference Number identifying the street. |
| `record_type` | `bigint` |  |
| `swa_org_ref_naming` | `bigint` |  |
| `state` | `bigint` |  |
| `state_date` | `text` | Date associated with the represented feature or source record. |
| `street_surface` | `bigint` |  |
| `street_classification` | `bigint` |  |
| `version` | `bigint` |  |
| `street_start_date` | `text` | Date associated with the represented feature or source record. |
| `street_end_date` | `text` | Date associated with the represented feature or source record. |
| `last_update_date` | `text` | Date associated with the represented feature or source record. |
| `record_entry_date` | `text` | Date associated with the represented feature or source record. |
| `street_start_x` | `double precision` |  |
| `street_start_y` | `double precision` |  |
| `street_start_lat` | `double precision` |  |
| `street_start_long` | `double precision` |  |
| `street_end_x` | `double precision` |  |
| `street_end_y` | `double precision` |  |
| `street_end_lat` | `double precision` |  |
| `street_end_long` | `double precision` |  |
| `street_tolerance` | `bigint` |  |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
