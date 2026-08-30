# Blue Green Infra OS Sports Provision Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_OS_Sports_Provision_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_OS_Sports_Provision_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 74573
- **Metadata status:** source_mapped

## Description

Blue Green Infra OS Sports Provision Ogl is an authoritative dataset published by Natural England. It represents blue green infra os sports provision ogl features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system object identifier. | identifier | Yes | No | No |
| `dataset` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `accessible` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `angst` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `naturalness` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `typologytitle` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `license` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `greenspacetopology` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `habitat` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `designation` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `attribute` | `varchar(8000)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `typologycode` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `orig_area` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `perc_manmade` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `vxcount` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
