# County Electoral Division

## Overview

- **Identifier:** `a_os_boundaryline/county_electoral_division`
- **Source organisation:** Ordnance Survey
- **Product:** Boundary-Line
- **Source:** https://www.ordnancesurvey.co.uk/products/boundary-line
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-4.680963, 50.201824, 1.768950, 54.239557]`
- **Schema:** `a_os_boundaryline`
- **Table:** `county_electoral_division`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1398
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

County Electoral Division is part of Boundary-Line, published by Ordnance Survey. It represents county electoral division features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `Name` | `varchar(100)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `Area_Code` | `varchar(3)` | Code assigned by the source dataset. | code | Yes | No | No |
| `Area_Description` | `varchar(50)` | Publisher-supplied area description for the represented feature or record. | source_attribute | Yes | No | No |
| `File_Name` | `varchar(100)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `Feature_Serial_Number` | `integer` | Count or numeric value for feature serial number in the represented area. | statistical_value | Yes | No | No |
| `Collection_Serial_Number` | `integer` | Count or numeric value for collection serial number in the represented area. | statistical_value | Yes | No | No |
| `Global_Polygon_ID` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `Admin_Unit_ID` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `Census_Code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `Hectares` | `double precision` | Count or numeric value for hectares in the represented area. | statistical_value | Yes | No | No |
| `Non_Inland_Area` | `double precision` | Numeric non inland area value recorded for the feature. | measure | Yes | No | No |
| `Area_Type_Code` | `varchar(2)` | Code assigned by the source dataset. | code | Yes | No | No |
| `Area_Type_Description` | `varchar(25)` | Publisher-supplied area type description for the represented feature or record. | source_attribute | Yes | No | No |
| `Non_Area_Type_Code` | `varchar(3)` | Code assigned by the source dataset. | code | Yes | No | No |
| `Non_Area_Type_Description` | `varchar(36)` | Publisher-supplied non area type description for the represented feature or record. | source_attribute | Yes | No | No |
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
