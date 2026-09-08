# Special Areas Of Conservation England

## Overview

- **Identifier:** `a_natural_england/special_areas_of_conservation_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.472186, 49.849107, 1.731077, 55.955753]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `special_areas_of_conservation_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1879
- **Columns:** 18
- **Metadata status:** source_mapped

## Description

Version: 20251009
Source: https://www.data.gov.uk/dataset/a85e64d9-d0f1-4500-9080-b0e29b81fbc8/special-areas-of-conservation-england2

Attribution: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year]. 

## Lineage

Published by Natural England as open environmental and conservation data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `sac_name` | `varchar(120)` | Name associated with the represented feature. |
| `sac_code` | `varchar(12)` | Code assigned by the source dataset. |
| `sac_area` | `double precision` | Numeric sac area value recorded for the feature. |
| `grid_ref` | `varchar(8)` | Publisher-assigned grid reference for the record. |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `latitude` | `varchar(12)` | Latitude coordinate, normally expressed in decimal degrees. |
| `longitude` | `varchar(12)` | Longitude coordinate, normally expressed in decimal degrees. |
| `name` | `varchar(80)` | Official or publisher-assigned name of the represented feature. |
| `status` | `varchar(32)` | Publisher-supplied status for the represented feature or record. |
| `file` | `varchar(20)` | Publisher-supplied file for the represented feature or record. |
| `area` | `double precision` | Numeric area value recorded for the feature. |
| `easting0` | `double precision` |  |
| `northing0` | `double precision` |  |
| `gis_date` | `varchar(20)` | Date associated with the represented feature or source record. |
| `version` | `integer` | Publisher-supplied version for the represented feature or record. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
