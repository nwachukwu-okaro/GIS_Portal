# Special Area Of Conservation Sac

## Overview

- **Identifier:** `a_npws_ireland/special_area_of_conservation_sac`
- **Source organisation:** National Parks and Wildlife Service Ireland
- **Source:** https://www.npws.ie/maps-and-data
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.691667, 51.410000, -5.591380, 55.471236]`
- **Schema:** `a_npws_ireland`
- **Table:** `special_area_of_conservation_sac`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 433
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Special Area Of Conservation Sac is an authoritative dataset published by National Parks and Wildlife Service Ireland. It represents special area of conservation sac features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `sitecode` | `varchar(6)` | Publisher-assigned sitecode for the record. | source_identifier | Yes | No | No |
| `site_name` | `varchar(100)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `version` | `double precision` | Count or numeric value for version in the represented area. | statistical_value | Yes | No | No |
| `county` | `varchar(50)` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
| `ha` | `double precision` | Count or numeric value for ha in the represented area. | statistical_value | Yes | No | No |
| `source_crs` | `varchar(254)` | Publisher-supplied source crs for the represented feature or record. | source_attribute | Yes | No | No |
| `sourcscale` | `varchar(50)` | Publisher-supplied sourcscale for the represented feature or record. | source_attribute | Yes | No | No |
| `url` | `varchar(50)` | Publisher-supplied url for the represented feature or record. | source_attribute | Yes | No | No |

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

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
