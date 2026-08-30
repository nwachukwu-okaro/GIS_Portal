# Boundary Datazone2022

## Overview

- **Identifier:** `a_nrs_scotland/boundary_datazone2022`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.650007, 54.633240, -0.724609, 60.860766]`
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_datazone2022`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 7392
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Boundary Datazone2022 is an authoritative dataset published by National Records of Scotland. It represents boundary datazone2022 features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `dzcode` | `varchar(254)` | Publisher-assigned dzcode for the record. | source_identifier | Yes | No | No |
| `dzname` | `varchar(254)` | Publisher-supplied dzname for the represented feature or record. | source_attribute | Yes | No | No |
| `totpop2022` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `hhres2022` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `hhcnt2022` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `stdareaha` | `double precision` | Numeric stdareaha value recorded for the feature. | measure | Yes | No | No |
| `stdareakm2` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `st_area_sh` | `double precision` | Numeric st area sh value recorded for the feature. | measure | Yes | No | No |
| `st_length_` | `double precision` | Numeric st length value recorded for the feature. | measure | Yes | No | No |

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
