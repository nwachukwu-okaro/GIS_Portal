# Historic European Region

## Overview

- **Identifier:** `a_os_boundaryline/historic_european_region`
- **Source organisation:** Ordnance Survey
- **Product:** Boundary-Line
- **Source:** https://www.ordnancesurvey.co.uk/products/boundary-line
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.650007, 49.864637, 1.768912, 60.860846]`
- **Schema:** `a_os_boundaryline`
- **Table:** `historic_european_region`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 2742
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Historic European Region is part of Boundary-Line, published by Ordnance Survey. It represents historic european region features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `Name` | `varchar(100)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `Area_Description` | `varchar(50)` | Publisher-supplied area description for the represented feature or record. | source_attribute | Yes | No | No |
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
