# River Net Routes

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/river_net_routes`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `river_net_routes`
- **Geometry:** LINESTRING
- **CRS:** EPSG:29903
- **Rows:** 102108
- **Metadata status:** source_mapped

## Description

River Net Routes is an authoritative dataset published by Environmental Protection Agency Ireland. It represents river net routes features using linestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `segment_code` | `varchar(20)` | Code assigned by the source dataset. | code | Yes | No | No |
| `epa_name` | `varchar(100)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `epa_code` | `varchar(5)` | Code assigned by the source dataset. | code | Yes | No | No |
| `stream_order` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `continua` | `varchar(1)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `river_water_body_code` | `varchar(100)` | Code assigned by the source dataset. | code | Yes | No | No |
| `lake_water_body_code` | `varchar(100)` | Code assigned by the source dataset. | code | Yes | No | No |
| `transitional_water_body_code` | `varchar(100)` | Code assigned by the source dataset. | code | Yes | No | No |
| `segment_length` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `coastal_water_body_code` | `varchar(100)` | Code assigned by the source dataset. | code | Yes | No | No |
| `rnr_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
