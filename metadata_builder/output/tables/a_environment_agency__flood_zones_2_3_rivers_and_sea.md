# Flood Zones 2 3 Rivers And Sea

## Overview

- **Identifier:** `a_environment_agency/flood_zones_2_3_rivers_and_sea`
- **Source organisation:** Environment Agency
- **Source:** https://environment.data.gov.uk/
- **Schema:** `a_environment_agency`
- **Table:** `flood_zones_2_3_rivers_and_sea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 12804126
- **Metadata status:** source_mapped

## Description

version: 20251120
Source: https://www.data.gov.uk/dataset/104434b0-5263-4c90-9b1e-e43b1d57c750/flood-map-for-planning-flood-zones1

Attribution: © Environment Agency copyright and/or database right 2025. All rights reserved.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `origin` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `flood_zone` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `flood_source` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `objectid` | `bigint` | Source-system object identifier. | identifier | Yes | No | No |
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

- Schema default only; verify dataset-specific restrictions and third-party rights.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
