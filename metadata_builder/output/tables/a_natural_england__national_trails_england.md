# National Trails England

## Overview

- **Identifier:** `a_natural_england/national_trails_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.715260, 49.959466, 1.319627, 55.547168]`
- **Schema:** `a_natural_england`
- **Table:** `national_trails_england`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:3857
- **Rows:** 14
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

National Trails England is an authoritative dataset published by Natural England. It represents national trails england features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `objectid_1` | `bigint` | Count or numeric value for objectid 1 in the represented area. | statistical_value | Yes | No | No |
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `name` | `varchar(50)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `opened` | `timestamp` | Publisher-supplied opened for the represented feature or record. | source_attribute | Yes | No | No |
| `start` | `varchar(100)` | Publisher-supplied start for the represented feature or record. | source_attribute | Yes | No | No |
| `end_` | `varchar(100)` | Publisher-supplied end for the represented feature or record. | source_attribute | Yes | No | No |
| `length_km` | `integer` | Numeric length km value recorded for the feature. | measure | Yes | No | No |
| `length_mil` | `integer` | Numeric length mil value recorded for the feature. | measure | Yes | No | No |
| `updated` | `timestamp` | Publisher-supplied updated for the represented feature or record. | source_attribute | Yes | No | No |
| `last_vr` | `integer` | Count or numeric value for last vr in the represented area. | statistical_value | Yes | No | No |
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
