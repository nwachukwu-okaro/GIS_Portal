# Ramsar Sites Listed And Proposed

## Overview

- **Identifier:** `a_natural_england/ramsar_sites_listed_and_proposed`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Schema:** `a_natural_england`
- **Table:** `ramsar_sites_listed_and_proposed`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1495
- **Metadata status:** source_mapped

## Description

Ramsar Sites Listed And Proposed is an authoritative dataset published by Natural England. It represents ramsar sites listed and proposed features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `name` | `text` | Name of the represented feature. | feature_name | Yes | Yes | No |
| `code` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `status` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `file` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `gis_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `version` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `rse_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
