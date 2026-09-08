# Local Electoral Area Boundary

## Overview

- **Identifier:** `a_ireland_cso/local_electoral_area_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.726726, 54.563349, 3.417194, 58.519873]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `local_electoral_area_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 166
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Local Electoral Area Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents local electoral area boundary features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `lea_guid` | `text` | Publisher-assigned lea guid for the record. |
| `lea_official` | `text` | Publisher-supplied lea official for the represented feature or record. |
| `cso_lea` | `text` | Publisher-supplied cso lea for the represented feature or record. |
| `lea_id` | `text` | Identifier assigned by the source dataset. |
| `county` | `text` | Publisher-supplied county for the represented feature or record. |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `shape` | `geometry` | Spatial geometry of the represented feature. |
