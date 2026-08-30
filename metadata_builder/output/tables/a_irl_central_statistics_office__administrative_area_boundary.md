# Administrative Area Boundary

## Overview

- **Identifier:** `a_irl_central_statistics_office/administrative_area_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.681235, 51.419897, -5.996278, 55.446932]`
- **Schema:** `a_irl_central_statistics_office`
- **Table:** `administrative_area_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 31
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Administrative Area Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents administrative area boundary features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `english` | `text` | Publisher-supplied english for the represented feature or record. | source_attribute | Yes | No | No |
| `gaeilge` | `text` | Publisher-supplied gaeilge for the represented feature or record. | source_attribute | Yes | No | No |
| `contae` | `text` | Publisher-supplied contae for the represented feature or record. | source_attribute | Yes | No | No |
| `county` | `text` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
| `province` | `text` | Publisher-supplied province for the represented feature or record. | source_attribute | Yes | No | No |
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `centroid_x` | `double precision` | Count or numeric value for centroid x in the represented area. | statistical_value | Yes | No | No |
| `centroid_y` | `double precision` | Count or numeric value for centroid y in the represented area. | statistical_value | Yes | No | No |
| `area` | `double precision` | Numeric area value recorded for the feature. | measure | Yes | No | No |
| `cc_id` | `double precision` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `esri_oid` | `bigint` | Count or numeric value for esri oid in the represented area. | statistical_value | Yes | No | No |
| `shape` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

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
