# Codepoint

## Overview

- **Identifier:** `a_os_codepoint/codepoint`
- **Source organisation:** Ordnance Survey
- **Product:** Code-Point Open
- **Source:** https://www.ordnancesurvey.co.uk/products/code-point-open
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.557160, 49.766807, 1.762748, 60.800694]`
- **Schema:** `a_os_codepoint`
- **Table:** `codepoint`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 1749109
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Codepoint is part of Code-Point Open, published by Ordnance Survey. It represents codepoint features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `postcode` | `text` | Publisher-assigned postcode for the record. | source_identifier | Yes | No | No |
| `positional_quality_indicator` | `integer` | Count or numeric value for positional quality indicator in the represented area. | statistical_value | Yes | No | No |
| `country_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `nhs_regional_ha_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `nhs_ha_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `admin_county_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `admin_district_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `admin_ward_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
