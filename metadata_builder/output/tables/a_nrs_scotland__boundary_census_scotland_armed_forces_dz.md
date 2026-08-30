# Boundary Census Scotland Armed Forces Dz

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_armed_forces_dz`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.650007, 54.633240, -0.724609, 60.860766]`
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_census_scotland_armed_forces_dz`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 7392
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Armed Forces Dz is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland armed forces dz features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `all_people_aged_16_and_over` | `bigint` | Count or numeric value for all people aged 16 and over in the represented area. | statistical_value | Yes | No | No |
| `uk_armed_forces_veteran` | `double precision` | Count or numeric value for uk armed forces veteran in the represented area. | statistical_value | Yes | No | No |
| `not_a_uk_armed_forces_veteran` | `bigint` | Count or numeric value for not a uk armed forces veteran in the represented area. | statistical_value | Yes | No | No |
| `total` | `bigint` | Count or numeric value for total in the represented area. | statistical_value | Yes | No | No |
| `hh_contains_at_least_one_uk_armed_forces_veteran` | `double precision` | Count or numeric value for households contains at least one uk armed forces veteran in the represented area. | statistical_value | Yes | No | No |
| `household_contains_no_uk_armed_forces_veterans` | `bigint` | Count or numeric value for household contains number uk armed forces veterans in the represented area. | statistical_value | Yes | No | No |
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
