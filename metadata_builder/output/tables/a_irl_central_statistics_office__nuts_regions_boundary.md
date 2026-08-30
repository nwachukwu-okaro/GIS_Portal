# Nuts Regions Boundary

## Overview

- **Identifier:** `a_irl_central_statistics_office/nuts_regions_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Schema:** `a_irl_central_statistics_office`
- **Table:** `nuts_regions_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 8
- **Metadata status:** source_mapped

## Description

Nuts Regions Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents nuts regions boundary features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `nuts1` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `nuts1name` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `nuts2` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `nuts2name` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `nuts3` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `nuts3name` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
