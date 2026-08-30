# Administrative Area Boundary

## Overview

- **Identifier:** `a_irl_central_statistics_office/administrative_area_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Schema:** `a_irl_central_statistics_office`
- **Table:** `administrative_area_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 31
- **Metadata status:** source_mapped

## Description

Administrative Area Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents administrative area boundary features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `english` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `gaeilge` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `contae` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `county` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `province` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `guid` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `centroid_x` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `centroid_y` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `area` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `cc_id` | `double precision` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `esri_oid` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
