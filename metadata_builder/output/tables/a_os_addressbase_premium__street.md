# Street

## Overview

- **Identifier:** `a_os_addressbase_premium/street`
- **Source organisation:** Ordnance Survey
- **Product:** AddressBase Premium
- **Source:** https://www.ordnancesurvey.co.uk/products/addressbase-premium
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.571197, 49.872875, 1.761354, 60.814182]`
- **Schema:** `a_os_addressbase_premium`
- **Table:** `street`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 1526341
- **Columns:** 24
- **Metadata status:** source_mapped

## Description

Street is part of AddressBase Premium, published by Ordnance Survey. It represents street features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `change_type` | `text` | Publisher-supplied change type for the represented feature or record. | source_attribute | Yes | No | No |
| `usrn` | `bigint` | Count or numeric value for usrn in the represented area. | statistical_value | Yes | No | No |
| `record_type` | `bigint` | Count or numeric value for record type in the represented area. | statistical_value | Yes | No | No |
| `swa_org_ref_naming` | `bigint` | Count or numeric value for swa org reference naming in the represented area. | statistical_value | Yes | No | No |
| `state` | `bigint` | Count or numeric value for state in the represented area. | statistical_value | Yes | No | No |
| `state_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `street_surface` | `bigint` | Count or numeric value for street surface in the represented area. | statistical_value | Yes | No | No |
| `street_classification` | `bigint` | Count or numeric value for street classification in the represented area. | statistical_value | Yes | No | No |
| `version` | `bigint` | Count or numeric value for version in the represented area. | statistical_value | Yes | No | No |
| `street_start_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `street_end_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `last_update_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `record_entry_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `street_start_x` | `double precision` | Count or numeric value for street start x in the represented area. | statistical_value | Yes | No | No |
| `street_start_y` | `double precision` | Count or numeric value for street start y in the represented area. | statistical_value | Yes | No | No |
| `street_start_lat` | `double precision` | Numeric street start lat value recorded for the feature. | measure | Yes | No | No |
| `street_start_long` | `double precision` | Numeric street start long value recorded for the feature. | measure | Yes | No | No |
| `street_end_x` | `double precision` | Count or numeric value for street end x in the represented area. | statistical_value | Yes | No | No |
| `street_end_y` | `double precision` | Count or numeric value for street end y in the represented area. | statistical_value | Yes | No | No |
| `street_end_lat` | `double precision` | Numeric street end lat value recorded for the feature. | measure | Yes | No | No |
| `street_end_long` | `double precision` | Numeric street end long value recorded for the feature. | measure | Yes | No | No |
| `street_tolerance` | `bigint` | Count or numeric value for street tolerance in the represented area. | statistical_value | Yes | No | No |
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
