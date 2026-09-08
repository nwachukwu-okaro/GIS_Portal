# High Water

## Overview

- **Identifier:** `a_os_boundaryline/high_water`
- **Source organisation:** Ordnance Survey
- **Product:** Boundary-Line
- **Source:** https://www.ordnancesurvey.co.uk/products/boundary-line
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.650007, 49.864674, 1.763680, 60.860766]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_boundaryline`
- **Table:** `high_water`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 32850
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

High Water is part of Boundary-Line, published by Ordnance Survey. It represents high water features using multilinestring geometry.

## Lineage

Published by Ordnance Survey as part of Boundary-Line. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `Feature_Code` | `varchar(4)` | Code assigned by the source dataset. |
| `Feature_Description` | `varchar(21)` | Publisher-supplied feature description for the represented feature or record. |
| `File_Name` | `varchar(100)` | Name associated with the represented feature. |
| `Feature_Serial_Number` | `integer` | Count or numeric value for feature serial number in the represented area. |
| `Global_Link_ID` | `integer` | Identifier assigned by the source dataset. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
