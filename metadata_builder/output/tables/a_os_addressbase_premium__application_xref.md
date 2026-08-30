# Application Xref

## Overview

- **Identifier:** `a_os_addressbase_premium/application_xref`
- **Source organisation:** Ordnance Survey
- **Product:** AddressBase Premium
- **Source:** https://www.ordnancesurvey.co.uk/products/addressbase-premium
- **Schema:** `a_os_addressbase_premium`
- **Table:** `application_xref`
- **Geometry:** GEOMETRY
- **CRS:** Not applicable or unknown
- **Rows:** 2480000
- **Metadata status:** source_mapped

## Description

Application Xref is part of AddressBase Premium, published by Ordnance Survey. It represents application xref features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `change_type` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `uprn` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `xref_key` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `cross_reference` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `version` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `source` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `start_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `end_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `last_update_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `entry_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `id` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
