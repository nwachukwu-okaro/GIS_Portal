# Blpu

## Overview

- **Identifier:** `a_os_addressbase_premium/blpu`
- **Source organisation:** Ordnance Survey
- **Product:** AddressBase Premium
- **Source:** https://www.ordnancesurvey.co.uk/products/addressbase-premium
- **Schema:** `a_os_addressbase_premium`
- **Table:** `blpu`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 41546482
- **Metadata status:** source_mapped

## Description

Blpu is part of AddressBase Premium, published by Ordnance Survey. It represents blpu features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `change_type` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `uprn` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `logical_status` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `blpu_state` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `blpu_state_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `parent_uprn` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `x_coordinate` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `y_coordinate` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `latitude` | `double precision` | Latitude coordinate, normally expressed in decimal degrees. | latitude | Yes | No | No |
| `longitude` | `double precision` | Longitude coordinate, normally expressed in decimal degrees. | longitude | Yes | No | No |
| `rpc` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `local_custodian_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `country` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `start_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `end_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `last_update_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `entry_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `addressbase_postal` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `postcode_locator` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `multi_occ_count` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
