# Special Areas Of Conservation England

## Overview

- **Identifier:** `a_natural_england/special_areas_of_conservation_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Local dataset version:** 20251009 (9 October 2025)
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.472186, 49.849107, 1.731077, 55.955753]`
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

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `sac_name` | `varchar(120)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sac_code` | `varchar(12)` | Code assigned by the source dataset. | code | Yes | No | No |
| `sac_area` | `double precision` | Numeric sac area value recorded for the feature. | measure | Yes | No | No |
| `grid_ref` | `varchar(8)` | Publisher-assigned grid reference for the record. | source_identifier | Yes | No | No |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. | x_coordinate | Yes | No | No |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. | y_coordinate | Yes | No | No |
| `latitude` | `varchar(12)` | Latitude coordinate, normally expressed in decimal degrees. | latitude | Yes | No | No |
| `longitude` | `varchar(12)` | Longitude coordinate, normally expressed in decimal degrees. | longitude | Yes | No | No |
| `name` | `varchar(80)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `status` | `varchar(32)` | Publisher-supplied status for the represented feature or record. | source_attribute | Yes | No | No |
| `file` | `varchar(20)` | Publisher-supplied file for the represented feature or record. | source_attribute | Yes | No | No |
| `area` | `double precision` | Numeric area value recorded for the feature. | measure | Yes | No | No |
| `easting0` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `northing0` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `gis_date` | `varchar(20)` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `version` | `integer` | Publisher-supplied version for the represented feature or record. | source_attribute | Yes | No | No |
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
