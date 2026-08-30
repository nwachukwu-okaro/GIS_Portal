# Urban Areas Boundary

## Overview

- **Identifier:** `a_ireland_cso/urban_areas_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.426272, 54.617106, 3.355468, 58.377636]`
- **Schema:** `a_ireland_cso`
- **Table:** `urban_areas_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 867
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Urban Areas Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents urban areas boundary features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `urban_area_guid` | `text` | Publisher-assigned urban area guid for the record. | source_identifier | Yes | No | No |
| `urban_area_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `urban_area_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `county` | `text` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
| `centroid_x` | `double precision` | Count or numeric value for centroid x in the represented area. | statistical_value | Yes | No | No |
| `centroid_y` | `double precision` | Count or numeric value for centroid y in the represented area. | statistical_value | Yes | No | No |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
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
