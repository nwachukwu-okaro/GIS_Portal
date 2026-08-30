# Statutory Main River

## Overview

- **Identifier:** `a_environment_agency/statutory_main_river`
- **Source organisation:** Environment Agency
- **Source:** https://environment.data.gov.uk/
- **Schema:** `a_environment_agency`
- **Table:** `statutory_main_river`
- **Geometry:** MULTICURVE
- **CRS:** EPSG:27700
- **Rows:** 183911
- **Metadata status:** source_mapped

## Description

Statutory Main River is an authoritative dataset published by Environment Agency. It represents statutory main river features using multicurve geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `fid` | `bigint` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `status` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `length_km` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `shape_length` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |

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

- Schema default only; verify dataset-specific restrictions and third-party rights.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
