# Nuts Regions Boundary

## Overview

- **Identifier:** `a_irl_central_statistics_office/nuts_regions_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.662971, 51.419897, -5.996278, 55.446580]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_central_statistics_office`
- **Table:** `nuts_regions_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 8
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Nuts Regions Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents nuts regions boundary features using geometry geometry.

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
