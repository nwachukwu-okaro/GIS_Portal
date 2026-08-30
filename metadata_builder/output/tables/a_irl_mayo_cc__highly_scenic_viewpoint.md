# Highly Scenic Viewpoint

## Overview

- **Identifier:** `a_irl_mayo_cc/highly_scenic_viewpoint`
- **Source organisation:** Mayo County Council
- **Source:** https://data.gov.ie/organization/mayo-county-council
- **Geographic coverage:** County Mayo
- **WGS84 extent:** `[-10.184220, 53.588907, -9.034434, 54.312163]`
- **Schema:** `a_irl_mayo_cc`
- **Table:** `highly_scenic_viewpoint`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:3857
- **Rows:** 79
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Highly Scenic Viewpoint is an authoritative dataset published by Mayo County Council. It represents highly scenic viewpoint features using multipoint geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `fid` | `integer` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
| `highly_scenic_viewpoints` | `varchar` | Publisher-supplied highly scenic viewpoints for the represented feature or record. | source_attribute | Yes | No | No |
| `hsv_pk` | `integer` | Count or numeric value for hsv pk in the represented area. | statistical_value | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

## Supported operations

- filter
- select
- reproject
- validate_geometry
- buffer
- clip
- intersect
- spatial_join
- export

## Operation requirements

- Intersect, clip and spatial-join inputs must use matching coordinate reference systems.
- Buffer operations require a suitable projected coordinate reference system.
- Reprojection is performed on working outputs; source tables remain unchanged.

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
