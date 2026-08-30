# Emergency Areas

## Overview

- **Identifier:** `a_national_highways/emergency_areas`
- **Source organisation:** National Highways
- **Source:** https://developer.data.nationalhighways.co.uk/
- **Geographic coverage:** England
- **WGS84 extent:** `[-2.591876, 50.867387, 0.464372, 53.747101]`
- **Schema:** `a_national_highways`
- **Table:** `emergency_areas`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 438
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

Emergency Areas is an authoritative dataset published by National Highways. It represents emergency areas features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid_1` | `integer` | Count or numeric value for objectid 1 in the represented area. | statistical_value | Yes | No | No |
| `globalid_1` | `varchar` | Publisher-supplied globalid 1 for the represented feature or record. | source_attribute | Yes | No | No |
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
