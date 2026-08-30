# Nwr Gtcl 20251215

## Overview

- **Identifier:** `a_network_rail/nwr_gtcl_20251215`
- **Source organisation:** Network Rail
- **Source:** https://www.networkrail.co.uk/who-we-are/transparency-and-ethics/transparency/open-data-feeds/
- **Schema:** `a_network_rail`
- **Table:** `nwr_gtcl_20251215`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 48103
- **Metadata status:** source_mapped

## Description

Nwr Gtcl 20251215 is an authoritative dataset published by Network Rail. It represents nwr gtcl 20251215 features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `assetid` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `elr` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `trid` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `source` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `superceded` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geometry_updated` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `id` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
