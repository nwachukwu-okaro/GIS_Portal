# Counties And Unitary Authorities December 2024 Boundaries

## Overview

- **Identifier:** `a_ons_england_wales/Counties_and_Unitary_Authorities_December_2024_Boundaries`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Schema:** `a_ons_england_wales`
- **Table:** `Counties_and_Unitary_Authorities_December_2024_Boundaries`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 218
- **Metadata status:** source_mapped

## Description

Counties And Unitary Authorities December 2024 Boundaries is an authoritative dataset published by Office for National Statistics. It represents counties and unitary authorities december 2024 boundaries features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
| `ctyua24cd` | `varchar(9)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ctyua24nm` | `varchar(36)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ctyua24nmw` | `varchar(24)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `bng_e` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `bng_n` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `long` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lat` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
