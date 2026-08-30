# Electoral Division Boundary

## Overview

- **Identifier:** `a_ireland_cso/electoral_division_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Schema:** `a_ireland_cso`
- **Table:** `electoral_division_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 3420
- **Metadata status:** source_mapped

## Description

Electoral Division Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents electoral division boundary features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `ed_guid` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ed_official` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ed_english` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ed_gaeilge` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ed_id_str` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ed_part_count` | `smallint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `county_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `county_english` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `county_gaeilge` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `cso_lea` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
