# Small Areas Boundary

## Overview

- **Identifier:** `a_ireland_cso/small_areas_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Schema:** `a_ireland_cso`
- **Table:** `small_areas_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 18919
- **Metadata status:** source_mapped

## Description

Small Areas Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents small areas boundary features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `sa_guid_2016` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sa_guid_2022` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sa_pub2011` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sa_pub2016` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sa_pub2022` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sa_geogid_2022` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sa_change_code` | `smallint` | Code assigned by the source dataset. | code | Yes | No | No |
| `sa_urban_area_flag` | `smallint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sa_urban_area_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sa_nuts1` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sa_nuts1_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sa_nuts2` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sa_nuts2_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sa_nuts3` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sa_nuts3_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `ed_guid` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ed_official` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ed_english` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ed_gaeilge` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ed_id_str` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ed_part_count` | `smallint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `county_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `county_english` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `county_gaeilge` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `cso_lea` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `objectid` | `bigint` | Source-system object identifier. | identifier | Yes | No | No |
| `shape` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

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
