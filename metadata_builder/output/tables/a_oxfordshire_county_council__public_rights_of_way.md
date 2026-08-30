# Public Rights Of Way

## Overview

- **Identifier:** `a_oxfordshire_county_council/public_rights_of_way`
- **Source organisation:** Oxfordshire County Council
- **Source:** https://insight.oxfordshire.gov.uk/cms/open-data
- **Geographic coverage:** Oxfordshire
- **WGS84 extent:** `[-1.719517, 51.473502, -0.870555, 52.157764]`
- **Schema:** `a_oxfordshire_county_council`
- **Table:** `public_rights_of_way`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:4326
- **Rows:** 10469
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

Public Rights Of Way is an authoritative dataset published by Oxfordshire County Council. It represents public rights of way features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `legal_typed` | `varchar` | Publisher-supplied legal typed for the represented feature or record. | source_attribute | Yes | No | No |
| `status_description` | `varchar` | Publisher-supplied status description for the represented feature or record. | source_attribute | Yes | No | No |
| `route_number` | `varchar` | Publisher-supplied route number for the represented feature or record. | source_attribute | Yes | No | No |
| `parish_code` | `varchar` | Code assigned by the source dataset. | code | Yes | No | No |
| `route_code` | `varchar` | Code assigned by the source dataset. | code | Yes | No | No |
| `parish_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `status` | `varchar` | Publisher-supplied status for the represented feature or record. | source_attribute | Yes | No | No |
| `legal_type` | `varchar` | Publisher-supplied legal type for the represented feature or record. | source_attribute | Yes | No | No |
| `length_m` | `double precision` | Numeric length male value recorded for the feature. | measure | Yes | No | No |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. | x_coordinate | Yes | No | No |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. | y_coordinate | Yes | No | No |
| `easting_end` | `double precision` | Numeric easting end value recorded for the feature. | measure | Yes | No | No |
| `northing_end` | `double precision` | Numeric northing end value recorded for the feature. | measure | Yes | No | No |
| `easting_start` | `double precision` | Numeric easting start value recorded for the feature. | measure | Yes | No | No |
| `northing_start` | `double precision` | Numeric northing start value recorded for the feature. | measure | Yes | No | No |
| `oprow_pk` | `integer` | Count or numeric value for oprow pk in the represented area. | statistical_value | Yes | No | No |
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
