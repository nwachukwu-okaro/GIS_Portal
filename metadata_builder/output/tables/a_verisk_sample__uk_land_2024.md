# UK Land 2024

## Overview

- **Identifier:** `a_verisk_sample/uk_land_2024`
- **Source organisation:** Verisk
- **Source:** https://www.verisk.com/en-gb/
- **Schema:** `a_verisk_sample`
- **Table:** `uk_land_2024`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 31863
- **Metadata status:** source_mapped

## Description

UK Land 2024 is an authoritative dataset published by Verisk. It represents uk land 2024 features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `landuse_code` | `double precision` | Code assigned by the source dataset. | code | Yes | No | No |
| `landuse_text` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `high_level_landuse` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `luid` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `date_created` | `date` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
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
