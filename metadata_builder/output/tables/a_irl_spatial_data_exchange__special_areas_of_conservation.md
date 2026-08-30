# Special Areas Of Conservation

## Overview

- **Identifier:** `a_irl_spatial_data_exchange/special_areas_of_conservation`
- **Source organisation:** Government of Ireland
- **Source:** https://data.gov.ie/
- **Schema:** `a_irl_spatial_data_exchange`
- **Table:** `special_areas_of_conservation`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 433
- **Metadata status:** source_mapped

## Description

Special Areas Of Conservation is an authoritative dataset published by Government of Ireland. It represents special areas of conservation features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `sac_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `site_code` | `varchar(6)` | Code assigned by the source dataset. | code | Yes | No | No |
| `site_name` | `varchar(100)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `version` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `county` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ha` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `source_crs` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `source_sale` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `url` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
