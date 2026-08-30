# Boundary Intermediatezone 2011

## Overview

- **Identifier:** `a_nrs_scotland/boundary_intermediatezone_2011`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.650007, 54.633238, -0.724609, 60.860766]`
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_intermediatezone_2011`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1279
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Boundary Intermediatezone 2011 is an authoritative dataset published by National Records of Scotland. It represents boundary intermediatezone 2011 features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `interzone` | `varchar(10)` | Publisher-supplied interzone for the represented feature or record. | source_attribute | Yes | No | No |
| `name` | `varchar(254)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `totpop2011` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `respop2011` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `hhcnt2011` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `stdareakm2` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `stdareaha` | `double precision` | Numeric stdareaha value recorded for the feature. | measure | Yes | No | No |

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
