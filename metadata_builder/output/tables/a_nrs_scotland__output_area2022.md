# Output Area2022

## Overview

- **Identifier:** `a_nrs_scotland/output_area2022`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-7.114367, 54.633220, -1.764393, 57.701742]`
- **Schema:** `a_nrs_scotland`
- **Table:** `output_area2022`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 24000
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Output Area2022 is an authoritative dataset published by National Records of Scotland. It represents output area2022 features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `code` | `varchar(9)` | Publisher-assigned code for the record. | source_identifier | Yes | No | No |
| `hhcount` | `integer` | Count or numeric value for hhcount in the represented area. | statistical_value | Yes | No | No |
| `popcount` | `integer` | Count or numeric value for popcount in the represented area. | statistical_value | Yes | No | No |
| `council` | `varchar(9)` | Publisher-supplied council for the represented feature or record. | source_attribute | Yes | No | No |
| `sqkm` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `hect` | `double precision` | Count or numeric value for hect in the represented area. | statistical_value | Yes | No | No |
| `masterpc` | `varchar(9)` | Publisher-supplied masterpc for the represented feature or record. | source_attribute | Yes | No | No |
| `easting` | `varchar(6)` | Easting coordinate in metres in the dataset's projected coordinate reference system. | x_coordinate | Yes | No | No |
| `northing` | `varchar(7)` | Northing coordinate in metres in the dataset's projected coordinate reference system. | y_coordinate | Yes | No | No |
| `shape_leng` | `double precision` | Count or numeric value for shape leng in the represented area. | statistical_value | Yes | No | No |
| `shape_area` | `double precision` | Numeric shape area value recorded for the feature. | measure | Yes | No | No |
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
