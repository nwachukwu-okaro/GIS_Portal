# National Trails England

## Overview

- **Identifier:** `a_natural_england/national_trails_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Schema:** `a_natural_england`
- **Table:** `national_trails_england`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:3857
- **Rows:** 14
- **Metadata status:** source_mapped

## Description

National Trails England is an authoritative dataset published by Natural England. It represents national trails england features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `objectid_1` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `objectid` | `integer` | Source-system object identifier. | identifier | Yes | No | No |
| `name` | `varchar(50)` | Name of the represented feature. | feature_name | Yes | Yes | No |
| `opened` | `timestamp` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `start` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `end_` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `length_km` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `length_mil` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `updated` | `timestamp` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `last_vr` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
