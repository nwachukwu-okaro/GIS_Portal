# Hospitals Medical Facilities

## Overview

- **Identifier:** `a_os_addressbase_premium/hospitals_medical_facilities`
- **Source organisation:** Ordnance Survey
- **Product:** AddressBase Premium
- **Source:** https://www.ordnancesurvey.co.uk/products/addressbase-premium
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.365395, 50.099682, 1.754639, 58.983653]`
- **Schema:** `a_os_addressbase_premium`
- **Table:** `hospitals_medical_facilities`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 13169
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Hospitals Medical Facilities is part of AddressBase Premium, published by Ordnance Survey. It represents hospitals medical facilities features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `uprn` | `bigint` | Count or numeric value for uprn in the represented area. | statistical_value | Yes | No | No |
| `ctyua24nm` | `varchar(36)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `classification_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `organisation` | `text` | Publisher-supplied organisation for the represented feature or record. | source_attribute | Yes | No | No |
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
