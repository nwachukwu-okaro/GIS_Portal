# Highly Scenic Viewpoint

## Overview

- **Identifier:** `a_irl_mayo_cc/highly_scenic_viewpoint`
- **Source organisation:** Mayo County Council
- **Source:** https://data.gov.ie/organization/mayo-county-council
- **Geographic coverage:** County Mayo
- **WGS84 extent:** `[-10.184220, 53.588907, -9.034434, 54.312163]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_irl_mayo_cc`
- **Table:** `highly_scenic_viewpoint`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:3857
- **Rows:** 79
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Highly Scenic Viewpoint is an authoritative dataset published by Mayo County Council. It represents highly scenic viewpoint features using multipoint geometry.

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
| `highly_scenic_viewpoints` | `varchar` | Publisher-supplied highly scenic viewpoints for the represented feature or record. |
| `hsv_pk` | `integer` | Count or numeric value for hsv pk in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
