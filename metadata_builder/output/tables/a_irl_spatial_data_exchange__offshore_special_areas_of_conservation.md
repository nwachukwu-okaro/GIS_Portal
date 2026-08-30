# Offshore Special Areas Of Conservation

## Overview

- **Identifier:** `a_irl_spatial_data_exchange/offshore_special_areas_of_conservation`
- **Source organisation:** Government of Ireland
- **Source:** https://data.gov.ie/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-15.817580, 46.488600, -15.817498, 46.488672]`
- **Schema:** `a_irl_spatial_data_exchange`
- **Table:** `offshore_special_areas_of_conservation`
- **Geometry:** POLYGON
- **CRS:** EPSG:2157
- **Rows:** 8
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Offshore Special Areas Of Conservation is an authoritative dataset published by Government of Ireland. It represents offshore special areas of conservation features using polygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `osac_pk` | `integer` | Count or numeric value for osac pk in the represented area. | statistical_value | Yes | No | No |
| `site_name` | `varchar(50)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `site_code` | `varchar(6)` | Code assigned by the source dataset. | code | Yes | No | No |
| `n2k_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `centroid_x` | `double precision` | Count or numeric value for centroid x in the represented area. | statistical_value | Yes | No | No |
| `centroid_y` | `double precision` | Count or numeric value for centroid y in the represented area. | statistical_value | Yes | No | No |
| `laea_area` | `double precision` | Numeric laea area value recorded for the feature. | measure | Yes | No | No |
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
