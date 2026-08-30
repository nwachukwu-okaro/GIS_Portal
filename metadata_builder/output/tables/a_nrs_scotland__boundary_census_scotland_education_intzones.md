# Boundary Census Scotland Education Intzones

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_education_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.650007, 54.633238, -0.724609, 60.860766]`
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_census_scotland_education_intzones`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1280
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Education Intzones is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland education intzones features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `geography_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `all_people_16plus` | `bigint` | Count or numeric value for all people 16plus in the represented area. | statistical_value | Yes | No | No |
| `no_quals` | `bigint` | Count or numeric value for number quals in the represented area. | statistical_value | Yes | No | No |
| `lower_school_quals` | `bigint` | Count or numeric value for lower school quals in the represented area. | statistical_value | Yes | No | No |
| `upper_school_quals` | `bigint` | Count or numeric value for upper school quals in the represented area. | statistical_value | Yes | No | No |
| `apprenticeship` | `bigint` | Count or numeric value for apprenticeship in the represented area. | statistical_value | Yes | No | No |
| `fe_and_sub_degree_he_incl_hnc_hnd` | `bigint` | Count or numeric value for fe and sub degree he incl hnc hnd in the represented area. | statistical_value | Yes | No | No |
| `degree_level_or_above` | `bigint` | Count or numeric value for degree level or above in the represented area. | statistical_value | Yes | No | No |
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
