# Administrative Counties Boundary

## Overview

- **Identifier:** `a_ireland_cso/administrative_counties_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.746471, 54.563349, 3.417194, 58.520162]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `administrative_counties_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 31
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Administrative Counties Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents administrative counties boundary features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `english` | `text` | English-language name of the administrative area. |
| `gaeilge` | `text` | Irish-language name of the administrative area. |
| `contae` | `text` |  |
| `county` | `text` | County associated with the represented administrative area. |
| `province` | `text` | Province associated with the represented administrative area. |
| `guid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `centroid_x` | `double precision` | X coordinate of the feature centroid; units and reference system are not confirmed for this attribute. |
| `centroid_y` | `double precision` | Y coordinate of the feature centroid; units and reference system are not confirmed for this attribute. |
| `area` | `double precision` |  |
| `cc_id` | `double precision` | Identifier assigned by the source dataset. |
| `esri_oid` | `bigint` | Primary-key identifier for records in administrative_counties_boundary. |
| `shape` | `geometry` | Spatial geometry of the represented feature. |
