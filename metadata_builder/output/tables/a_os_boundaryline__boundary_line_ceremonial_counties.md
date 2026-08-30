# Boundary Line Ceremonial Counties

## Overview

- **Identifier:** `a_os_boundaryline/boundary_line_ceremonial_counties`
- **Source organisation:** Ordnance Survey
- **Product:** Boundary-Line
- **Source:** https://www.ordnancesurvey.co.uk/products/boundary-line
- **Schema:** `a_os_boundaryline`
- **Table:** `boundary_line_ceremonial_counties`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 91
- **Metadata status:** source_mapped

## Description

Boundary Line Ceremonial Counties is part of Boundary-Line, published by Ordnance Survey. It represents boundary line ceremonial counties features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `Name` | `varchar(100)` | Name of the represented feature. | feature_name | Yes | Yes | No |
| `Area_Description` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
