# Greater London Const

## Overview

- **Identifier:** `a_os_boundaryline/greater_london_const`
- **Source organisation:** Ordnance Survey
- **Product:** Boundary-Line
- **Source:** https://www.ordnancesurvey.co.uk/products/boundary-line
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-0.510326, 51.286792, 0.334016, 51.691873]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_boundaryline`
- **Table:** `greater_london_const`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 14
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

Greater London Const is part of Boundary-Line, published by Ordnance Survey. It represents greater london const features using multipolygon geometry.

## Lineage

Published by Ordnance Survey as part of Boundary-Line. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `Name` | `varchar(100)` | Official or publisher-assigned name of the represented feature. |
| `Area_Code` | `varchar(3)` | Code assigned by the source dataset. |
| `Area_Description` | `varchar(50)` | Publisher-supplied area description for the represented feature or record. |
| `File_Name` | `varchar(100)` | Name associated with the represented feature. |
| `Feature_Serial_Number` | `integer` | Count or numeric value for feature serial number in the represented area. |
| `Collection_Serial_Number` | `integer` | Count or numeric value for collection serial number in the represented area. |
| `Global_Polygon_ID` | `integer` | Identifier assigned by the source dataset. |
| `Admin_Unit_ID` | `integer` | Identifier assigned by the source dataset. |
| `Census_Code` | `varchar(9)` | Code assigned by the source dataset. |
| `Hectares` | `double precision` | Count or numeric value for hectares in the represented area. |
| `Non_Inland_Area` | `double precision` | Numeric non inland area value recorded for the feature. |
| `Area_Type_Code` | `varchar(2)` | Code assigned by the source dataset. |
| `Area_Type_Description` | `varchar(25)` | Publisher-supplied area type description for the represented feature or record. |
| `Non_Area_Type_Code` | `varchar(3)` | Code assigned by the source dataset. |
| `Non_Area_Type_Description` | `varchar(36)` | Publisher-supplied non area type description for the represented feature or record. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
