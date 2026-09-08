# Province Boundary

## Overview

- **Identifier:** `a_irl_central_statistics_office/province_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.681232, 51.419905, -5.996278, 55.446932]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_central_statistics_office`
- **Table:** `province_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
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
| `province` | `text` | Publisher-supplied province for the represented feature or record. |
| `pv_id` | `integer` | Identifier assigned by the source dataset. |
| `guid` | `text` | Publisher-assigned guid for the record. |
| `centroid_x` | `double precision` | Count or numeric value for centroid x in the represented area. |
| `centroid_y` | `double precision` | Count or numeric value for centroid y in the represented area. |
| `area` | `double precision` | Numeric area value recorded for the feature. |
| `esri_oid` | `bigint` | Count or numeric value for esri oid in the represented area. |
| `shape` | `geometry` | Spatial geometry of the represented feature. |
