# Metrolink Lines

## Overview

- **Identifier:** `a_tfgm/metrolink_lines`
- **Source organisation:** Transport for Greater Manchester
- **Source:** https://developer.tfgm.com/
- **Schema:** `a_tfgm`
- **Table:** `metrolink_lines`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 20
- **Metadata status:** source_mapped

## Description

Metrolink Lines is an authoritative dataset published by Transport for Greater Manchester. It represents metrolink lines features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `tramline_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `description` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `type` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `name` | `varchar` | Name of the represented feature. | feature_name | Yes | Yes | No |
| `validfrom` | `timestamp` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `validto` | `timestamp` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `currentstatus` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `comments` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
