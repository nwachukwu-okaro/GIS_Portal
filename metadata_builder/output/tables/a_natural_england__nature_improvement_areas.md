# Nature Improvement Areas

## Overview

- **Identifier:** `a_natural_england/nature_improvement_areas`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Schema:** `a_natural_england`
- **Table:** `nature_improvement_areas`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 12
- **Metadata status:** source_mapped

## Description

version: 20170425
Source: https://environment.data.gov.uk/dataset/899230b5-0247-4af8-9265-ff65009287eb

Attribution: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year].

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system object identifier. | identifier | Yes | No | No |
| `nia_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `hectares` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `gdb_geomattr_data` | `bytea` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
