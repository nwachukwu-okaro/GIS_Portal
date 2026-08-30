# Gm Sbi Polygon

## Overview

- **Identifier:** `a_greater_manchester_ecology_unit/gm_sbi_polygon`
- **Source organisation:** Greater Manchester Ecology Unit
- **Source:** https://www.gmenvironment.org.uk/gmeu/
- **Schema:** `a_greater_manchester_ecology_unit`
- **Table:** `gm_sbi_polygon`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 539
- **Metadata status:** source_mapped

## Description

Gm Sbi Polygon is an authoritative dataset published by Greater Manchester Ecology Unit. It represents gm sbi polygon features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `site_id` | `text` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `site_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `cent_gr` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `site_gra` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `district` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `features` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `date_est` | `date` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
