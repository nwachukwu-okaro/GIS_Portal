# Zone Of Archaeological Notification

## Overview

- **Identifier:** `a_irl_meath_cc/zone_of_archaeological_notification`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Schema:** `a_irl_meath_cc`
- **Table:** `zone_of_archaeological_notification`
- **Geometry:** POLYGON
- **CRS:** EPSG:2157
- **Rows:** 1948
- **Metadata status:** source_mapped

## Description

Zone Of Archaeological Notification is an authoritative dataset published by Meath County Council. It represents zone of archaeological notification features using polygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `zone_id` | `varchar(10)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `county_id` | `double precision` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `class_code` | `varchar(4)` | Code assigned by the source dataset. | code | Yes | No | No |
| `map_label` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `zan_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
