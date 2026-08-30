# Licensed Facilities Ipc 26052025

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/licensed_facilities_ipc_26052025`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `licensed_facilities_ipc_26052025`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:29903
- **Rows:** 166
- **Metadata status:** source_mapped

## Description

Licensed Facilities Ipc 26052025 is an authoritative dataset published by Environmental Protection Agency Ireland. It represents licensed facilities ipc 26052025 features using multipoint geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `registration_code` | `varchar(50)` | Code assigned by the source dataset. | code | Yes | No | No |
| `name` | `varchar(250)` | Name of the represented feature. | feature_name | Yes | Yes | No |
| `date_from` | `date` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sub_category` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `category` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `licence_status_type` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `active_licence_number` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `major_class_of_activity` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `licence_type_name` | `varchar(100)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `address` | `varchar(250)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `easting` | `double precision` | Easting coordinate in the dataset coordinate reference system. | x_coordinate | Yes | No | No |
| `northing` | `double precision` | Northing coordinate in the dataset coordinate reference system. | y_coordinate | Yes | No | No |
| `lfipc_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
