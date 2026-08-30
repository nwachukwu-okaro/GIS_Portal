# Classification

## Overview

- **Identifier:** `a_os_addressbase_premium/classification`
- **Source organisation:** Ordnance Survey
- **Product:** AddressBase Premium
- **Source:** https://www.ordnancesurvey.co.uk/products/addressbase-premium
- **Geographic coverage:** Great Britain
- **Schema:** `a_os_addressbase_premium`
- **Table:** `classification`
- **Geometry:** GEOMETRY
- **CRS:** Not applicable or unknown
- **Rows:** 45333097
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Classification is part of AddressBase Premium, published by Ordnance Survey. It represents classification features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `change_type` | `text` | Publisher-supplied change type for the represented feature or record. | source_attribute | Yes | No | No |
| `uprn` | `bigint` | Count or numeric value for uprn in the represented area. | statistical_value | Yes | No | No |
| `class_key` | `text` | Publisher-supplied class key for the represented feature or record. | source_attribute | Yes | No | No |
| `classification_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `class_scheme` | `text` | Publisher-supplied class scheme for the represented feature or record. | source_attribute | Yes | No | No |
| `scheme_version` | `double precision` | Count or numeric value for scheme version in the represented area. | statistical_value | Yes | No | No |
| `start_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `end_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `last_update_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `entry_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `id` | `bigint` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
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
