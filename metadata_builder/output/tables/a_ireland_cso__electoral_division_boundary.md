# Electoral Division Boundary

## Overview

- **Identifier:** `a_ireland_cso/electoral_division_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.726726, 54.563349, 3.417194, 58.519873]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `electoral_division_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 3420
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Electoral Division Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents electoral division boundary features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `ed_guid` | `text` |  |
| `ed_official` | `text` |  |
| `ed_english` | `text` |  |
| `ed_gaeilge` | `text` |  |
| `ed_id_str` | `text` |  |
| `ed_part_count` | `smallint` |  |
| `county_code` | `text` | Code assigned by the source dataset. |
| `county_english` | `text` |  |
| `county_gaeilge` | `text` |  |
| `cso_lea` | `text` |  |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `shape` | `geometry` | Spatial geometry of the represented feature. |
