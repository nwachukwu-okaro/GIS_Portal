# Blue Green Infra Access Points Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Access_Points_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Access_Points_OGL`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 333676
- **Metadata status:** source_mapped

## Description

Blue Green Infra Access Points Ogl is an authoritative dataset published by Natural England. It represents blue green infra access points ogl features using multipoint geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system object identifier. | identifier | Yes | No | No |
| `accesstype` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `accessible_for` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
