# National Cycle Network Public

## Overview

- **Identifier:** `a_sustrans/national_cycle_network_public`
- **Source organisation:** Sustrans
- **Source:** https://data.sustrans.org.uk/
- **Schema:** `a_sustrans`
- **Table:** `national_cycle_network_public`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 37210
- **Metadata status:** source_mapped

## Description

National Cycle Network Public is an authoritative dataset published by Sustrans. It represents national cycle network public features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `desc_` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `greenway` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `routetype` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `routeno` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `linkno` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `routecat` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `openstatus` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `surface` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `quality` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lighting` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `roadclass` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `globalid` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `segmentid` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
