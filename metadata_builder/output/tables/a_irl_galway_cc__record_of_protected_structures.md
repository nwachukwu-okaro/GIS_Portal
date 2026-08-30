# Record Of Protected Structures

## Overview

- **Identifier:** `a_irl_galway_cc/record_of_protected_structures`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.233900, 52.984950, 8.225051, 53.705427]`
- **Schema:** `a_irl_galway_cc`
- **Table:** `record_of_protected_structures`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 1514
- **Columns:** 19
- **Metadata status:** source_mapped

## Description

Record Of Protected Structures is an authoritative dataset published by Galway County Council. It represents record of protected structures features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `administrative_authority_id` | `varchar` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `adiministrative_authority` | `varchar` | Publisher-supplied adiministrative authority for the represented feature or record. | source_attribute | Yes | No | No |
| `registration_no` | `varchar` | Publisher-supplied registration number for the represented feature or record. | source_attribute | Yes | No | No |
| `building_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `address` | `varchar` | Publisher-supplied address for the represented feature or record. | source_attribute | Yes | No | No |
| `county` | `varchar` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
| `eircode` | `varchar` | Publisher-assigned eircode for the record. | source_identifier | Yes | No | No |
| `building_type` | `varchar` | Publisher-supplied building type for the represented feature or record. | source_attribute | Yes | No | No |
| `description` | `varchar` | Publisher-supplied description for the represented feature or record. | source_attribute | Yes | No | No |
| `appraisal` | `varchar` | Publisher-supplied appraisal for the represented feature or record. | source_attribute | Yes | No | No |
| `current_use` | `varchar` | Publisher-supplied current use for the represented feature or record. | source_attribute | Yes | No | No |
| `niah_number` | `varchar` | Publisher-supplied niah number for the represented feature or record. | source_attribute | Yes | No | No |
| `rmp_number` | `varchar` | Publisher-supplied rmp number for the represented feature or record. | source_attribute | Yes | No | No |
| `date_registered` | `bigint` | Count or numeric value for date registered in the represented area. | statistical_value | Yes | No | No |
| `latitude` | `double precision` | Latitude coordinate, normally expressed in decimal degrees. | latitude | Yes | No | No |
| `longitude` | `double precision` | Longitude coordinate, normally expressed in decimal degrees. | longitude | Yes | No | No |
| `global_id` | `varchar` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `object_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
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
