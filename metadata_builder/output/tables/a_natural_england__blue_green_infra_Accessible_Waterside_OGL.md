# Blue Green Infra Accessible Waterside Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Accessible_Waterside_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.714067, 49.963839, 1.757875, 55.803013]`
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Accessible_Waterside_OGL`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 451956
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Blue Green Infra Accessible Waterside Ogl is an authoritative dataset published by Natural England. It represents blue green infra accessible waterside ogl features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `left_fid` | `integer` | Count or numeric value for left fid in the represented area. | statistical_value | Yes | No | No |
| `right_fid` | `integer` | Count or numeric value for right fid in the represented area. | statistical_value | Yes | No | No |
| `id` | `varchar(38)` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `featcode` | `integer` | Count or numeric value for featcode in the represented area. | statistical_value | Yes | No | No |
| `shape_length` | `double precision` | Numeric shape length value recorded for the feature. | measure | Yes | No | No |
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
