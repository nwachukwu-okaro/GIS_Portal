# Boundary Census Scotland Education Intzones

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_education_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_census_scotland_education_intzones`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1280
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Education Intzones is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland education intzones features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `geography_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `all_people_16plus` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `no_quals` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lower_school_quals` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `upper_school_quals` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `apprenticeship` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `fe_and_sub_degree_he_incl_hnc_hnd` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `degree_level_or_above` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
