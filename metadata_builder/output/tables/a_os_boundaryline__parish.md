# Parish

## Overview

- **Identifier:** `a_os_boundaryline/parish`
- **Source organisation:** Ordnance Survey
- **Product:** Boundary-Line
- **Source:** https://www.ordnancesurvey.co.uk/products/boundary-line
- **Schema:** `a_os_boundaryline`
- **Table:** `parish`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 14258
- **Metadata status:** source_mapped

## Description

Parish is part of Boundary-Line, published by Ordnance Survey. It represents parish features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `Name` | `varchar(100)` | Name of the represented feature. | feature_name | Yes | Yes | No |
| `Area_Code` | `varchar(3)` | Code assigned by the source dataset. | code | Yes | No | No |
| `Area_Description` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `File_Name` | `varchar(100)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `Feature_Serial_Number` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `Collection_Serial_Number` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `Global_Polygon_ID` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `Admin_Unit_ID` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `Census_Code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `Hectares` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `Non_Inland_Area` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `Area_Type_Code` | `varchar(2)` | Code assigned by the source dataset. | code | Yes | No | No |
| `Area_Type_Description` | `varchar(25)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `Non_Area_Type_Code` | `varchar(3)` | Code assigned by the source dataset. | code | Yes | No | No |
| `Non_Area_Type_Description` | `varchar(36)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
