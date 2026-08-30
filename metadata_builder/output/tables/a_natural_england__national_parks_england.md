# National Parks England

## Overview

- **Identifier:** `a_natural_england/national_parks_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Local dataset version:** 20251009 (9 October 2025)
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-4.165771, 50.392027, 1.728156, 55.591511]`
- **Schema:** `a_natural_england`
- **Table:** `national_parks_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 10
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Version: 20251009
Source: https://www.data.gov.uk/dataset/334e1b27-e193-4ef5-b14e-696b58bb7e95/national-parks-england1

Attribution: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year]. Attribution statement: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year].

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `code` | `smallint` | Count or numeric value for code in the represented area. | statistical_value | Yes | No | No |
| `name` | `varchar(200)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `measure` | `double precision` | Count or numeric value for measure in the represented area. | statistical_value | Yes | No | No |
| `desig_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `hotlink` | `varchar(200)` | Publisher-supplied hotlink for the represented feature or record. | source_attribute | Yes | No | No |
| `status` | `varchar(32)` | Publisher-supplied status for the represented feature or record. | source_attribute | Yes | No | No |
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
