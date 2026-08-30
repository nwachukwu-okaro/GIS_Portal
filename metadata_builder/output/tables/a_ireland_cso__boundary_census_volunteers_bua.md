# Boundary Census Volunteers Bua

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_volunteers_bua`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.426272, 54.617106, 3.355468, 58.377636]`
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_volunteers_bua`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 867
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Boundary Census Volunteers Bua is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census volunteers bua features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `geogid` | `text` | Publisher-assigned geogid for the record. | source_identifier | Yes | No | No |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `number_of_volunteers` | `bigint` | Count or numeric value for number of volunteers in the represented area. | statistical_value | Yes | No | No |
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
