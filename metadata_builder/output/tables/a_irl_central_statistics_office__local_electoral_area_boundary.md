# Local Electoral Area Boundary

## Overview

- **Identifier:** `a_irl_central_statistics_office/local_electoral_area_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.662971, 51.419897, -5.996278, 55.446580]`
- **Schema:** `a_irl_central_statistics_office`
- **Table:** `local_electoral_area_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 166
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Local Electoral Area Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents local electoral area boundary features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `lea_guid` | `text` | Publisher-assigned lea guid for the record. | source_identifier | Yes | No | No |
| `lea_official` | `text` | Publisher-supplied lea official for the represented feature or record. | source_attribute | Yes | No | No |
| `cso_lea` | `text` | Publisher-supplied cso lea for the represented feature or record. | source_attribute | Yes | No | No |
| `lea_id` | `text` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `county` | `text` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
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
