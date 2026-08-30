# Special Areas Of Conservation

## Overview

- **Identifier:** `a_irl_spatial_data_exchange/special_areas_of_conservation`
- **Source organisation:** Government of Ireland
- **Source:** https://data.gov.ie/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.691667, 51.410000, -5.591380, 55.471236]`
- **Schema:** `a_irl_spatial_data_exchange`
- **Table:** `special_areas_of_conservation`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 433
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Special Areas Of Conservation is an authoritative dataset published by Government of Ireland. It represents special areas of conservation features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `sac_pk` | `integer` | Count or numeric value for sac pk in the represented area. | statistical_value | Yes | No | No |
| `site_code` | `varchar(6)` | Code assigned by the source dataset. | code | Yes | No | No |
| `site_name` | `varchar(100)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `version` | `double precision` | Count or numeric value for version in the represented area. | statistical_value | Yes | No | No |
| `county` | `varchar(50)` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
| `ha` | `double precision` | Count or numeric value for ha in the represented area. | statistical_value | Yes | No | No |
| `source_crs` | `varchar(254)` | Publisher-supplied source crs for the represented feature or record. | source_attribute | Yes | No | No |
| `source_sale` | `varchar(50)` | Publisher-supplied source sale for the represented feature or record. | source_attribute | Yes | No | No |
| `url` | `varchar(50)` | Publisher-supplied url for the represented feature or record. | source_attribute | Yes | No | No |
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

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
