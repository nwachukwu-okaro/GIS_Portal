# Air Zone

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/air_zone`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.621856, 51.388882, -5.996275, 55.384383]`
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `air_zone`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29902
- **Rows:** 27
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Air Zone is an authoritative dataset published by Environmental Protection Agency Ireland. It represents air zone features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `az_pk` | `integer` | Count or numeric value for az pk in the represented area. | statistical_value | Yes | No | No |
| `air_zone` | `varchar(35)` | Publisher-supplied air zone for the represented feature or record. | source_attribute | Yes | No | No |
| `name` | `varchar(30)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `location` | `varchar(50)` | Publisher-supplied location for the represented feature or record. | source_attribute | Yes | No | No |
| `global_id` | `varchar(38)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
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
