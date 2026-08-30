# England Coast Path

## Overview

- **Identifier:** `a_natural_england/england_coast_path`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Schema:** `a_natural_england`
- **Table:** `england_coast_path`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 16667
- **Metadata status:** source_mapped

## Description

England Coast Path is an authoritative dataset published by Natural England. It represents england coast path features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `objectid` | `bigint` | Source-system object identifier. | identifier | Yes | No | No |
| `stretch` | `varchar(75)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `section_id` | `varchar(15)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `chapter` | `varchar(16)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `status` | `varchar(65)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `alt_route` | `varchar(3)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `rollback_` | `varchar(40)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `pub_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `shape_leng` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `globalid` | `varchar(38)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |

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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
