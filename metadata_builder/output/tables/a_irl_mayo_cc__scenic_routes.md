# Scenic Routes

## Overview

- **Identifier:** `a_irl_mayo_cc/scenic_routes`
- **Source organisation:** Mayo County Council
- **Source:** https://data.gov.ie/organization/mayo-county-council
- **Geographic coverage:** County Mayo
- **WGS84 extent:** `[-10.192775, 53.543198, -8.870419, 54.310350]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_mayo_cc`
- **Table:** `scenic_routes`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:3857
- **Rows:** 54
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Scenic Routes is an authoritative dataset published by Mayo County Council. It represents scenic routes features using multilinestring geometry.

## Lineage

Published by Mayo County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `fid` | `integer` | Feature identifier assigned by the source or import process. |
| `id` | `double precision` | Count or numeric value for identifier in the represented area. |
| `sr_pk` | `integer` | Count or numeric value for sr pk in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
