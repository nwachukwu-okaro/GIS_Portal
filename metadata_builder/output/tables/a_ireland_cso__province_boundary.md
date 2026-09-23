# Province Boundary

## Overview

- **Identifier:** `a_ireland_cso/province_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.682125, 51.420091, -5.996278, 55.446936]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `province_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 4
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Province Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents province boundary features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `province` | `text` | Province associated with the represented administrative area. |
| `pv_id` | `integer` | Identifier assigned by the source dataset. |
| `guid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `centroid_x` | `double precision` | X coordinate of the feature centroid; units and reference system are not confirmed for this attribute. |
| `centroid_y` | `double precision` | Y coordinate of the feature centroid; units and reference system are not confirmed for this attribute. |
| `area` | `double precision` |  |
| `esri_oid` | `bigint` | Primary-key identifier for records in province_boundary. |
| `shape` | `geometry` | Spatial geometry of the represented feature. |
