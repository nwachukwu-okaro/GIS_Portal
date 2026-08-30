# Metrolink Park And Ride

## Overview

- **Identifier:** `a_tfgm/metrolink_park_and_ride`
- **Source organisation:** Transport for Greater Manchester
- **Source:** https://developer.tfgm.com/
- **Geographic coverage:** Greater Manchester
- **WGS84 extent:** `[-2.719122, 53.358241, -1.948611, 53.643312]`
- **Schema:** `a_tfgm`
- **Table:** `metrolink_park_and_ride`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 80
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Metrolink Park And Ride is an authoritative dataset published by Transport for Greater Manchester. It represents metrolink park and ride features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `park_and_ride_pk` | `integer` | Count or numeric value for park and ride pk in the represented area. | statistical_value | Yes | No | No |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `stationcod` | `varchar` | Publisher-supplied stationcod for the represented feature or record. | source_attribute | Yes | No | No |
| `mode` | `varchar` | Publisher-supplied mode for the represented feature or record. | source_attribute | Yes | No | No |
| `spaces` | `integer` | Count or numeric value for spaces in the represented area. | statistical_value | Yes | No | No |
| `url` | `varchar` | Publisher-supplied url for the represented feature or record. | source_attribute | Yes | No | No |
| `uprn` | `bigint` | Count or numeric value for uprn in the represented area. | statistical_value | Yes | No | No |
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
