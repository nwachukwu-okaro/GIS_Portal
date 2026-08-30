# England Coast Path

## Overview

- **Identifier:** `a_natural_england/england_coast_path`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.715202, 49.959480, 1.755965, 55.810694]`
- **Schema:** `a_natural_england`
- **Table:** `england_coast_path`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 16667
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

England Coast Path is an authoritative dataset published by Natural England. It represents england coast path features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `stretch` | `varchar(75)` | Publisher-supplied stretch for the represented feature or record. | source_attribute | Yes | No | No |
| `section_id` | `varchar(15)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `chapter` | `varchar(16)` | Publisher-supplied chapter for the represented feature or record. | source_attribute | Yes | No | No |
| `status` | `varchar(65)` | Publisher-supplied status for the represented feature or record. | source_attribute | Yes | No | No |
| `alt_route` | `varchar(3)` | Publisher-supplied alt route for the represented feature or record. | source_attribute | Yes | No | No |
| `rollback_` | `varchar(40)` | Publisher-supplied rollback for the represented feature or record. | source_attribute | Yes | No | No |
| `pub_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `shape_leng` | `double precision` | Count or numeric value for shape leng in the represented area. | statistical_value | Yes | No | No |
| `globalid` | `varchar(38)` | Publisher-assigned globalid for the record. | source_identifier | Yes | No | No |

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
