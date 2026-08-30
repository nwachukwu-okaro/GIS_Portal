# National Nature Reserves

## Overview

- **Identifier:** `a_natural_england/national_nature_reserves`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Schema:** `a_natural_england`
- **Table:** `national_nature_reserves`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 224
- **Metadata status:** source_mapped

## Description

National Nature Reserves is an authoritative dataset published by Natural England. It represents national nature reserves features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `OBJECTID` | `bigint` | Source-system object identifier. | identifier | Yes | No | No |
| `HYPERLINK` | `varchar(16)` | Link supplied by the publisher for the corresponding source record. | source_record_url | Yes | No | No |
| `REF_CODE` | `varchar(10)` | Code assigned by the source dataset. | code | Yes | No | No |
| `NAME` | `varchar(120)` | Name of the represented feature. | feature_name | Yes | Yes | No |
| `MEASURE` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `LABEL` | `varchar(140)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `GlobalID` | `varchar(38)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |

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
