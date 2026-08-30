# Gaeltacht Language Planning Area Boundary

## Overview

- **Identifier:** `a_ireland_cso/gaeltacht_language_planning_area_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.726726, 54.563349, 2.676080, 58.377837]`
- **Schema:** `a_ireland_cso`
- **Table:** `gaeltacht_language_planning_area_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 26
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Gaeltacht Language Planning Area Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents gaeltacht language planning area boundary features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `gpa_id` | `text` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `gpa_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `gpa_name_e` | `text` | Publisher-supplied gpa name e for the represented feature or record. | source_attribute | Yes | No | No |
| `contae` | `text` | Publisher-supplied contae for the represented feature or record. | source_attribute | Yes | No | No |
| `county` | `text` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
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
