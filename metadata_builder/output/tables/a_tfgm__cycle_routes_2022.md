# Cycle Routes 2022

## Overview

- **Identifier:** `a_tfgm/cycle_routes_2022`
- **Source organisation:** Transport for Greater Manchester
- **Source:** https://developer.tfgm.com/
- **Schema:** `a_tfgm`
- **Table:** `cycle_routes_2022`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 3573
- **Metadata status:** source_mapped

## Description

Cycle Routes 2022 is an authoritative dataset published by Transport for Greater Manchester. It represents cycle routes 2022 features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `cr_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `routetype` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `routestatu` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `routesurfa` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ncnroute` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ncnroutenu` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `notes` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `date_updat` | `date` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `strategic_` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `mand_advis` | `varchar(1)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `recovery_s` | `varchar(4)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `reduce_hgw` | `varchar(1)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `reduce_ftw` | `varchar(1)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `tranche` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
