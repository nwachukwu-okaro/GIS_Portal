# Polling Districts England

## Overview

- **Identifier:** `a_os_boundaryline/polling_districts_england`
- **Source organisation:** Ordnance Survey
- **Product:** Boundary-Line
- **Source:** https://www.ordnancesurvey.co.uk/products/boundary-line
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-5.747107, 49.956393, 1.768912, 55.811668]`
- **Schema:** `a_os_boundaryline`
- **Table:** `polling_districts_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 31631
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Polling Districts England is part of Boundary-Line, published by Ordnance Survey. It represents polling districts england features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `PD_ID` | `varchar(10)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `County` | `varchar(100)` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
| `Distric_Bo` | `varchar(100)` | Publisher-supplied distric bo for the represented feature or record. | source_attribute | Yes | No | No |
| `Ward` | `varchar(100)` | Publisher-supplied ward for the represented feature or record. | source_attribute | Yes | No | No |
| `Parish` | `varchar(100)` | Publisher-supplied parish for the represented feature or record. | source_attribute | Yes | No | No |
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
