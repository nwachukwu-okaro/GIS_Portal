# Boundary Census Volunteers Small Area

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_volunteers_small_area`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.726726, 54.563349, 3.417194, 58.519873]`
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_volunteers_small_area`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 18919
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Boundary Census Volunteers Small Area is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census volunteers small area features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `geogid` | `text` | Publisher-assigned geogid for the record. | source_identifier | Yes | No | No |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `ur_category` | `double precision` | Count or numeric value for ur category in the represented area. | statistical_value | Yes | No | No |
| `ur_category_desc` | `text` | Publisher-supplied ur category description for the represented feature or record. | source_attribute | Yes | No | No |
| `number_of_volunteers` | `bigint` | Count or numeric value for number of volunteers in the represented area. | statistical_value | Yes | No | No |

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
