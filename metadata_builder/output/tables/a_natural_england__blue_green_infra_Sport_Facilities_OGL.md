# Blue Green Infra Sport Facilities Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Sport_Facilities_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Sport_Facilities_OGL`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 44114
- **Metadata status:** source_mapped

## Description

Blue Green Infra Sport Facilities Ogl is an authoritative dataset published by Natural England. It represents blue green infra sport facilities ogl features using multipoint geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system object identifier. | identifier | Yes | No | No |
| `site_name` | `varchar(254)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `post_code` | `varchar(254)` | Code assigned by the source dataset. | code | Yes | No | No |
| `ownership` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `management` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `facility_type` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `access_group` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `access_type` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lsoa_code` | `varchar(255)` | Code assigned by the source dataset. | code | Yes | No | No |
| `msoa_code` | `varchar(255)` | Code assigned by the source dataset. | code | Yes | No | No |
| `local_authority_code` | `varchar(255)` | Code assigned by the source dataset. | code | Yes | No | No |
| `local_authority_name` | `varchar(255)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `county_code` | `varchar(255)` | Code assigned by the source dataset. | code | Yes | No | No |
| `county_name` | `varchar(255)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `site_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
