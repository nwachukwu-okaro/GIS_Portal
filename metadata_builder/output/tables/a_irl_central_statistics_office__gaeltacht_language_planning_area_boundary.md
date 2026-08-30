# Gaeltacht Language Planning Area Boundary

## Overview

- **Identifier:** `a_irl_central_statistics_office/gaeltacht_language_planning_area_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Schema:** `a_irl_central_statistics_office`
- **Table:** `gaeltacht_language_planning_area_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 26
- **Metadata status:** source_mapped

## Description

Gaeltacht Language Planning Area Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents gaeltacht language planning area boundary features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `gpa_id` | `text` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `gpa_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `gpa_name_e` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `contae` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `county` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `guid` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
