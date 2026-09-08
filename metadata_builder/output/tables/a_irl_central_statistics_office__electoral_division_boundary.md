# Electoral Division Boundary

## Overview

- **Identifier:** `a_irl_central_statistics_office/electoral_division_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.662971, 51.419897, -5.996278, 55.446580]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_central_statistics_office`
- **Table:** `electoral_division_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
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
| `ed_guid` | `text` | Publisher-assigned ed guid for the record. |
| `ed_official` | `text` | Publisher-supplied ed official for the represented feature or record. |
| `ed_english` | `text` | Publisher-supplied ed english for the represented feature or record. |
| `ed_gaeilge` | `text` | Publisher-supplied ed gaeilge for the represented feature or record. |
| `ed_id_str` | `text` | Publisher-supplied ed identifier str for the represented feature or record. |
| `ed_part_count` | `smallint` | Count or numeric value for ed part count in the represented area. |
| `county_code` | `text` | Code assigned by the source dataset. |
| `county_english` | `text` | Publisher-supplied county english for the represented feature or record. |
| `county_gaeilge` | `text` | Publisher-supplied county gaeilge for the represented feature or record. |
| `cso_lea` | `text` | Publisher-supplied cso lea for the represented feature or record. |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `shape` | `geometry` | Spatial geometry of the represented feature. |
