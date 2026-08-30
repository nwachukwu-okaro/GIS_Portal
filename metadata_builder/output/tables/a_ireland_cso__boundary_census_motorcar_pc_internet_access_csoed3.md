# Boundary Census Motorcar Pc Internet Access Csoed3

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_motorcar_pc_internet_access_csoed3`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_motorcar_pc_internet_access_csoed3`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 3420
- **Metadata status:** source_mapped

## Description

Boundary Census Motorcar Pc Internet Access Csoed3 is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census motorcar pc internet access csoed3 features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `ed_english` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `guid` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geogid` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geogdesc` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `no_motor_car` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `t_1_motor_car` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `t_2_motor_cars` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `t_3_motor_cars` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `t_4_or_more_motor_cars` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `not_stated` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `total` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `broadband` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `other_internet_connection` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `no_internet_connection` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `type_of_internet_connection_not_stated` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `all_internet_connections` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
