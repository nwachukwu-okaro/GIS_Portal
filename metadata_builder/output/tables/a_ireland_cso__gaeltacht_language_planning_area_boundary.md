# Gaeltacht Language Planning Area Boundary

## Overview

- **Identifier:** `a_ireland_cso/gaeltacht_language_planning_area_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.726726, 54.563349, 2.676080, 58.377837]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `gaeltacht_language_planning_area_boundary`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 26
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Gaeltacht Language Planning Area Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents gaeltacht language planning area boundary features using multipolygon geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `gpa_id` | `text` | Identifier assigned by the source dataset. |
| `gpa_name` | `text` | Name associated with the represented feature. |
| `gpa_name_e` | `text` | Publisher-supplied gpa name e for the represented feature or record. |
| `contae` | `text` | Publisher-supplied contae for the represented feature or record. |
| `county` | `text` | Publisher-supplied county for the represented feature or record. |
| `guid` | `text` | Publisher-assigned guid for the record. |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `shape` | `geometry` | Spatial geometry of the represented feature. |
