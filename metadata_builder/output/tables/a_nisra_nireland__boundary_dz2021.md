# Boundary Dz2021

## Overview

- **Identifier:** `a_nisra_nireland/boundary_dz2021`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177484, 54.022725, -5.432790, 55.312985]`
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_dz2021`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 3780
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Boundary Dz2021 is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary dz2021 features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `dz2021_cd` | `varchar(10)` | Publisher-supplied dz2021 cd for the represented feature or record. | source_attribute | Yes | No | No |
| `dz2021_nm` | `varchar(35)` | Publisher-supplied dz2021 nm for the represented feature or record. | source_attribute | Yes | No | No |
| `sdz2021_cd` | `varchar(254)` | Publisher-supplied sdz2021 cd for the represented feature or record. | source_attribute | Yes | No | No |
| `sdz2021_nm` | `varchar(32)` | Publisher-supplied sdz2021 nm for the represented feature or record. | source_attribute | Yes | No | No |
| `dea2014_cd` | `varchar(254)` | Publisher-supplied dea2014 cd for the represented feature or record. | source_attribute | Yes | No | No |
| `dea2014_nm` | `varchar(26)` | Publisher-supplied dea2014 nm for the represented feature or record. | source_attribute | Yes | No | No |
| `lgd2014_cd` | `varchar(9)` | Publisher-supplied lgd2014 cd for the represented feature or record. | source_attribute | Yes | No | No |
| `lgd2014_nm` | `varchar(36)` | Publisher-supplied lgd2014 nm for the represented feature or record. | source_attribute | Yes | No | No |
| `shape_length` | `double precision` | Numeric shape length value recorded for the feature. | measure | Yes | No | No |
| `shape_area` | `double precision` | Numeric shape area value recorded for the feature. | measure | Yes | No | No |

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
