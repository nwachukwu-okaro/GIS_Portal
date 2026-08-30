# Licensed Facilities Ie 26052025

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/licensed_facilities_ie_26052025`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.777210, 51.608037, -6.050323, 55.061859]`
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `licensed_facilities_ie_26052025`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:29903
- **Rows:** 725
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Licensed Facilities Ie 26052025 is an authoritative dataset published by Environmental Protection Agency Ireland. It represents licensed facilities ie 26052025 features using multipoint geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `lfie_pk` | `integer` | Count or numeric value for lfie pk in the represented area. | statistical_value | Yes | No | No |
| `registration_code` | `varchar(50)` | Code assigned by the source dataset. | code | Yes | No | No |
| `name` | `varchar(250)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `date_from` | `date` | Publisher-supplied date from for the represented feature or record. | source_attribute | Yes | No | No |
| `sub_category` | `varchar(100)` | Publisher-supplied sub category for the represented feature or record. | source_attribute | Yes | No | No |
| `category` | `varchar(50)` | Publisher-supplied category for the represented feature or record. | source_attribute | Yes | No | No |
| `licence_status_type` | `varchar(100)` | Publisher-supplied licence status type for the represented feature or record. | source_attribute | Yes | No | No |
| `active_licence_number` | `varchar(50)` | Publisher-supplied active licence number for the represented feature or record. | source_attribute | Yes | No | No |
| `major_class_of_activity` | `varchar(50)` | Publisher-supplied major class of activity for the represented feature or record. | source_attribute | Yes | No | No |
| `licence_type_name` | `varchar(100)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `address` | `varchar(250)` | Publisher-supplied address for the represented feature or record. | source_attribute | Yes | No | No |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. | x_coordinate | Yes | No | No |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. | y_coordinate | Yes | No | No |
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
