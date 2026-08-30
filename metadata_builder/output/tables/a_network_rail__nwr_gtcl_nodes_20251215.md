# Nwr Gtcl Nodes 20251215

## Overview

- **Identifier:** `a_network_rail/nwr_gtcl_nodes_20251215`
- **Source organisation:** Network Rail
- **Source:** https://www.networkrail.co.uk/who-we-are/transparency-and-ethics/transparency/open-data-feeds/
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-5.841335, 50.121776, 1.834690, 58.589994]`
- **Schema:** `a_network_rail`
- **Table:** `nwr_gtcl_nodes_20251215`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 37489
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Nwr Gtcl Nodes 20251215 is an authoritative dataset published by Network Rail. It represents nwr gtcl nodes 20251215 features using multipoint geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `assetid` | `text` | Publisher-assigned assetid for the record. | source_identifier | Yes | No | No |
| `valancy` | `integer` | Count or numeric value for valancy in the represented area. | statistical_value | Yes | No | No |
| `source` | `text` | Publisher-supplied source for the represented feature or record. | source_attribute | Yes | No | No |
| `superceded` | `text` | Publisher-supplied superceded for the represented feature or record. | source_attribute | Yes | No | No |
| `geometry_updated` | `text` | Publisher-supplied geometry updated for the represented feature or record. | source_attribute | Yes | No | No |
| `id` | `bigint` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
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
