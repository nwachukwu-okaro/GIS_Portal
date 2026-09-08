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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
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
| `english` | `text` | Publisher-supplied english for the represented feature or record. |
| `gaeilge` | `text` | Publisher-supplied gaeilge for the represented feature or record. |
| `contae` | `text` | Publisher-supplied contae for the represented feature or record. |
| `county` | `text` | Publisher-supplied county for the represented feature or record. |
| `province` | `text` | Publisher-supplied province for the represented feature or record. |
| `guid` | `text` | Publisher-assigned guid for the record. |
| `centroid_x` | `double precision` | Count or numeric value for centroid x in the represented area. |
| `centroid_y` | `double precision` | Count or numeric value for centroid y in the represented area. |
| `area` | `double precision` | Numeric area value recorded for the feature. |
| `cc_id` | `double precision` | Identifier assigned by the source dataset. |
| `esri_oid` | `bigint` | Count or numeric value for esri oid in the represented area. |
| `shape` | `geometry` | Spatial geometry of the represented feature. |
