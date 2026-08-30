# Areas Of Outstanding Natural Beauty England

## Overview

- **Identifier:** `a_natural_england/areas_of_outstanding_natural_beauty_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Local dataset version:** 20251009 (9 October 2025)
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.462536, 49.854671, 1.729622, 55.748905]`
- **Schema:** `a_natural_england`
- **Table:** `areas_of_outstanding_natural_beauty_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 33
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Version: 20251009
Source: https://www.data.gov.uk/dataset/8e3ae3b9-a827-47f1-b025-f08527a4e84e/areas-of-outstanding-natural-beauty-england1

Attribution: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year].

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `code` | `integer` | Count or numeric value for code in the represented area. | statistical_value | Yes | No | No |
| `name` | `varchar(200)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `measure` | `real` | Count or numeric value for measure in the represented area. | statistical_value | Yes | No | No |
| `desig_date` | `varchar(14)` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `hotlink` | `varchar(200)` | Publisher-supplied hotlink for the represented feature or record. | source_attribute | Yes | No | No |
| `stat_area` | `varchar(32)` | Publisher-supplied stat area for the represented feature or record. | source_attribute | Yes | No | No |
| `shape_length` | `real` | Numeric shape length value recorded for the feature. | measure | Yes | No | No |
| `shape_area` | `real` | Numeric shape area value recorded for the feature. | measure | Yes | No | No |
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
