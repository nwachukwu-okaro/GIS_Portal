# Urban Area Boundary

## Overview

- **Identifier:** `a_irl_central_statistics_office/urban_area_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.371391, 51.477104, -6.012232, 55.303636]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_central_statistics_office`
- **Table:** `urban_area_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 867
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Urban Area Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents urban area boundary features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `urban_area_guid` | `text` | Publisher-assigned urban area guid for the record. |
| `urban_area_code` | `text` | Code assigned by the source dataset. |
| `urban_area_name` | `text` | Name associated with the represented feature. |
| `county` | `text` | Publisher-supplied county for the represented feature or record. |
| `centroid_x` | `double precision` | Count or numeric value for centroid x in the represented area. |
| `centroid_y` | `double precision` | Count or numeric value for centroid y in the represented area. |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `shape` | `geometry` | Spatial geometry of the represented feature. |
