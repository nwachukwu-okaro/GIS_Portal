# High Water

## Overview

- **Identifier:** `a_os_boundaryline/high_water`
- **Source organisation:** Ordnance Survey
- **Product:** Boundary-Line
- **Source:** https://www.ordnancesurvey.co.uk/products/boundary-line
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.650007, 49.864674, 1.763680, 60.860766]`
- **Schema:** `a_os_boundaryline`
- **Table:** `high_water`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 32850
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

High Water is part of Boundary-Line, published by Ordnance Survey. It represents high water features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `Feature_Code` | `varchar(4)` | Code assigned by the source dataset. | code | Yes | No | No |
| `Feature_Description` | `varchar(21)` | Publisher-supplied feature description for the represented feature or record. | source_attribute | Yes | No | No |
| `File_Name` | `varchar(100)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `Feature_Serial_Number` | `integer` | Count or numeric value for feature serial number in the represented area. | statistical_value | Yes | No | No |
| `Global_Link_ID` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
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
