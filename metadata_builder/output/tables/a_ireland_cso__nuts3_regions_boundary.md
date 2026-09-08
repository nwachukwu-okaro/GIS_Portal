# Nuts3 Regions Boundary

## Overview

- **Identifier:** `a_ireland_cso/nuts3_regions_boundary`
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
- **Table:** `nuts3_regions_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 8
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Nuts3 Regions Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents nuts3 regions boundary features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `nuts1` | `text` |  |
| `nuts1name` | `text` |  |
| `nuts2` | `text` |  |
| `nuts2name` | `text` |  |
| `nuts3` | `text` |  |
| `nuts3name` | `text` |  |
| `guid` | `text` | Publisher-assigned guid for the record. |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `shape` | `geometry` | Spatial geometry of the represented feature. |
