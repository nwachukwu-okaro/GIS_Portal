# Nwr Gtcl Newlinks 20251215

## Overview

- **Identifier:** `a_network_rail/nwr_gtcl_newlinks_20251215`
- **Source organisation:** Network Rail
- **Source:** https://www.networkrail.co.uk/who-we-are/transparency-and-ethics/transparency/open-data-feeds/
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-4.606090, 51.322594, 1.716912, 55.155648]`
- **Schema:** `a_network_rail`
- **Table:** `nwr_gtcl_newlinks_20251215`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 3316
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Nwr Gtcl Newlinks 20251215 is an authoritative dataset published by Network Rail. It represents nwr gtcl newlinks 20251215 features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `source` | `text` | Publisher-supplied source for the represented feature or record. | source_attribute | Yes | No | No |
| `closest_elr` | `text` | Publisher-supplied closest elr for the represented feature or record. | source_attribute | Yes | No | No |
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
