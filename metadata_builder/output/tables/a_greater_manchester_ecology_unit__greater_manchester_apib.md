# Greater Manchester Apib

## Overview

- **Identifier:** `a_greater_manchester_ecology_unit/greater_manchester_apib`
- **Source organisation:** Greater Manchester Ecology Unit
- **Source:** https://www.gmenvironment.org.uk/gmeu/
- **Schema:** `a_greater_manchester_ecology_unit`
- **Table:** `greater_manchester_apib`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 2059
- **Metadata status:** source_mapped

## Description

Greater Manchester Apib is an authoritative dataset published by Greater Manchester Ecology Unit. It represents greater manchester apib features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `lnrs_id` | `numeric` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `apib_id` | `numeric` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `apib_type` | `varchar(6)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `apib_name` | `varchar(60)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `apib_site_` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `gmapib_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
