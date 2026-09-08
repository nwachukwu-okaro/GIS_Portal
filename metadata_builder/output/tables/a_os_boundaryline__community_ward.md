# Community Ward

## Overview

- **Identifier:** `a_os_boundaryline/community_ward`
- **Source organisation:** Ordnance Survey
- **Product:** Boundary-Line
- **Source:** https://www.ordnancesurvey.co.uk/products/boundary-line
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-5.670302, 51.374542, -2.649864, 53.435798]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_boundaryline`
- **Table:** `community_ward`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1698
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Community Ward is part of Boundary-Line, published by Ordnance Survey. It represents community ward features using multipolygon geometry.

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
| `Area_Description` | `varchar(35)` | Publisher-supplied area description for the represented feature or record. |
| `Community` | `varchar(100)` | Publisher-supplied community for the represented feature or record. |
| `File_Name` | `varchar(100)` | Name associated with the represented feature. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
