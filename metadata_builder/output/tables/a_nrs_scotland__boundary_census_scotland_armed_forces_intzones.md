# Boundary Census Scotland Armed Forces Intzones

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_armed_forces_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.650007, 54.633203, -0.724444, 60.860766]`
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_census_scotland_armed_forces_intzones`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1334
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Armed Forces Intzones is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland armed forces intzones features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `all_households` | `double precision` | Count or numeric value for all households in the represented area. | statistical_value | Yes | No | No |
| `hh_has_af_veteran` | `double precision` | Count or numeric value for households has af veteran in the represented area. | statistical_value | Yes | No | No |
| `hh_no_af_veteran` | `double precision` | Count or numeric value for households number af veteran in the represented area. | statistical_value | Yes | No | No |
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
