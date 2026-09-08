# Sea Flood Zones

## Overview

- **Identifier:** `a_natural_resources_wales/sea_flood_zones`
- **Source organisation:** Natural Resources Wales
- **WGS84 extent:** `[-5.353493, 51.377862, -2.656512, 53.430997]`
- **Temporal extent:** 2026-05-21 to 2026-05-21
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, source_url, topic_category, dataset_reference_date, lineage, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_resources_wales`
- **Table:** `sea_flood_zones`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 30743
- **Columns:** 6
- **Metadata status:** technical

## Description

Sea Flood Zones is an authoritative dataset published by Natural Resources Wales. It represents sea flood zones features using multipolygon geometry.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `mm_id` | `text` | Identifier assigned by the source dataset. |
| `pub_date` | `date` | Date associated with the represented feature or source record. |
| `risk` | `text` |  |
| `risk_cy` | `text` |  |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
