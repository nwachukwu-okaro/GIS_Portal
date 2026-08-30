# Lake Segment

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/lake_segment`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `lake_segment`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29903
- **Rows:** 12217
- **Metadata status:** source_mapped

## Description

Lake Segment is an authoritative dataset published by Environmental Protection Agency Ireland. It represents lake segment features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `segment_code` | `varchar(24)` | Code assigned by the source dataset. | code | Yes | No | No |
| `name` | `varchar(100)` | Name of the represented feature. | feature_name | Yes | Yes | No |
| `area_in_km_square` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `area_in_hectares` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `perimeter` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `hydrometric_area` | `varchar(3)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `order` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `os__layer` | `varchar(16)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `source` | `varchar(40)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lake_water_body` | `varchar(3)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `eden_lake_code` | `varchar(50)` | Code assigned by the source dataset. | code | Yes | No | No |
| `ls_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
