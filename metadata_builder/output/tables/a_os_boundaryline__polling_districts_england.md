# Polling Districts England

## Overview

- **Identifier:** `a_os_boundaryline/polling_districts_england`
- **Source organisation:** Ordnance Survey
- **Product:** Boundary-Line
- **Source:** https://www.ordnancesurvey.co.uk/products/boundary-line
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-5.747107, 49.956393, 1.768912, 55.811668]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_boundaryline`
- **Table:** `polling_districts_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 31631
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Polling Districts England is part of Boundary-Line, published by Ordnance Survey. It represents polling districts england features using multipolygon geometry.

## Lineage

Published by Ordnance Survey as part of Boundary-Line. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `PD_ID` | `varchar(10)` | Identifier assigned by the source dataset. |
| `County` | `varchar(100)` | Publisher-supplied county for the represented feature or record. |
| `Distric_Bo` | `varchar(100)` | Publisher-supplied distric bo for the represented feature or record. |
| `Ward` | `varchar(100)` | Publisher-supplied ward for the represented feature or record. |
| `Parish` | `varchar(100)` | Publisher-supplied parish for the represented feature or record. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
