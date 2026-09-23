# Small Areas Boundary

## Overview

- **Identifier:** `a_ireland_cso/small_areas_boundary`
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
- **Table:** `small_areas_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 18919
- **Columns:** 27
- **Metadata status:** source_mapped

## Description

Small Areas Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents small areas boundary features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `sa_guid_2016` | `text` |  |
| `sa_guid_2022` | `text` |  |
| `sa_pub2011` | `text` |  |
| `sa_pub2016` | `text` |  |
| `sa_pub2022` | `text` |  |
| `sa_geogid_2022` | `text` |  |
| `sa_change_code` | `smallint` | Code assigned by the source dataset. |
| `sa_urban_area_flag` | `smallint` |  |
| `sa_urban_area_name` | `text` | Name associated with the represented feature. |
| `sa_nuts1` | `text` |  |
| `sa_nuts1_name` | `text` | Name associated with the represented feature. |
| `sa_nuts2` | `text` |  |
| `sa_nuts2_name` | `text` | Name associated with the represented feature. |
| `sa_nuts3` | `text` |  |
| `sa_nuts3_name` | `text` | Name associated with the represented feature. |
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
