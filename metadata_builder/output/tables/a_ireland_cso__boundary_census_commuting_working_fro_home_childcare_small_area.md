# Boundary Census Commuting Working Fro Home Childcare Small Area

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_commuting_working_fro_home_childcare_small_area`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_commuting_working_fro_home_childcare_small_area`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 0
- **Metadata status:** source_mapped

## Description

Boundary Census Commuting Working Fro Home Childcare Small Area is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census commuting working fro home childcare small area features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `bigint` | Source-system object identifier. | identifier | Yes | No | No |
| `shape` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

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
