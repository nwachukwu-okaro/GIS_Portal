# Surface Water Small Watercourses

## Overview

- **Identifier:** `a_natural_resources_wales/surface_water_small_watercourses`
- **Source organisation:** Natural Resources Wales
- **WGS84 extent:** `[-5.350525, 51.381359, -2.651628, 53.427691]`
- **Temporal extent:** 2022-11-28T00:00:00 to 2022-11-28T00:00:00
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, source_url, topic_category, dataset_reference_date, lineage, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_resources_wales`
- **Table:** `surface_water_small_watercourses`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 2659117
- **Columns:** 9
- **Metadata status:** technical

## Description

Surface Water Small Watercourses is an authoritative dataset published by Natural Resources Wales. It represents surface water small watercourses features using multipolygon geometry.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `mm_id` | `text` | Identifier assigned by the source dataset. |
| `pub_date` | `timestamp` | Date associated with the represented feature or source record. |
| `risk` | `text` |  |
| `risk_cy` | `text` |  |
| `shape_stlength__` | `double precision` |  |
| `shape_starea__` | `double precision` |  |
| `id` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
