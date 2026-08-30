# Delivery Point

## Overview

- **Identifier:** `a_os_addressbase_premium/delivery_point`
- **Source organisation:** Ordnance Survey
- **Product:** AddressBase Premium
- **Source:** https://www.ordnancesurvey.co.uk/products/addressbase-premium
- **Schema:** `a_os_addressbase_premium`
- **Table:** `delivery_point`
- **Geometry:** GEOMETRY
- **CRS:** Not applicable or unknown
- **Rows:** 8678000
- **Metadata status:** source_mapped

## Description

Delivery Point is part of AddressBase Premium, published by Ordnance Survey. It represents delivery point features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `change_type` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `uprn` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `udprn` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `organisation_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `department_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sub_building_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `building_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `building_number` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `dependent_thoroughfare` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `thoroughfare` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `double_dependent_locality` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `dependent_locality` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `post_town` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `postcode` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `postcode_type` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `delivery_point_suffix` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `welsh_dependent_thoroughfare` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `welsh_thoroughfare` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `welsh_double_dependent_locality` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `welsh_dependent_locality` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `welsh_post_town` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `po_box_number` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `process_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
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
