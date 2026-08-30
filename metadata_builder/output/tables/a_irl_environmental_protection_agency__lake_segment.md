# Lake Segment

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/lake_segment`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.425985, 51.453245, -6.049586, 55.353164]`
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `lake_segment`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29903
- **Rows:** 12217
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Lake Segment is an authoritative dataset published by Environmental Protection Agency Ireland. It represents lake segment features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `segment_code` | `varchar(24)` | Code assigned by the source dataset. | code | Yes | No | No |
| `name` | `varchar(100)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `area_in_km_square` | `double precision` | Numeric area in km square value recorded for the feature. | measure | Yes | No | No |
| `area_in_hectares` | `double precision` | Numeric area in hectares value recorded for the feature. | measure | Yes | No | No |
| `perimeter` | `double precision` | Count or numeric value for perimeter in the represented area. | statistical_value | Yes | No | No |
| `hydrometric_area` | `varchar(3)` | Publisher-supplied hydrometric area for the represented feature or record. | source_attribute | Yes | No | No |
| `order` | `double precision` | Count or numeric value for order in the represented area. | statistical_value | Yes | No | No |
| `os__layer` | `varchar(16)` | Publisher-supplied os layer for the represented feature or record. | source_attribute | Yes | No | No |
| `source` | `varchar(40)` | Publisher-supplied source for the represented feature or record. | source_attribute | Yes | No | No |
| `lake_water_body` | `varchar(3)` | Publisher-supplied lake water body for the represented feature or record. | source_attribute | Yes | No | No |
| `eden_lake_code` | `varchar(50)` | Code assigned by the source dataset. | code | Yes | No | No |
| `ls_pk` | `integer` | Count or numeric value for ls pk in the represented area. | statistical_value | Yes | No | No |
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
