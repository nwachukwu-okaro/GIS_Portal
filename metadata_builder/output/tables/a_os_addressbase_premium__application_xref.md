# Application Xref

## Overview

- **Identifier:** `a_os_addressbase_premium/application_xref`
- **Source organisation:** Ordnance Survey
- **Product:** AddressBase Premium
- **Source:** https://www.ordnancesurvey.co.uk/products/addressbase-premium
- **Geographic coverage:** Great Britain
- **Schema:** `a_os_addressbase_premium`
- **Table:** `application_xref`
- **Geometry:** GEOMETRY
- **CRS:** Not applicable or unknown
- **Rows:** 2480000
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Application Xref is part of AddressBase Premium, published by Ordnance Survey. It represents application xref features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `change_type` | `text` | Publisher-supplied change type for the represented feature or record. | source_attribute | Yes | No | No |
| `uprn` | `bigint` | Count or numeric value for uprn in the represented area. | statistical_value | Yes | No | No |
| `xref_key` | `text` | Publisher-supplied xref key for the represented feature or record. | source_attribute | Yes | No | No |
| `cross_reference` | `text` | Publisher-supplied cross reference for the represented feature or record. | source_attribute | Yes | No | No |
| `version` | `bigint` | Count or numeric value for version in the represented area. | statistical_value | Yes | No | No |
| `source` | `text` | Publisher-supplied source for the represented feature or record. | source_attribute | Yes | No | No |
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
