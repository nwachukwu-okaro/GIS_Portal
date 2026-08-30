# Access Point

## Overview

- **Identifier:** `a_os_open_greenspace/access_point`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Greenspace
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-greenspace
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.566909, 49.893298, 1.760894, 60.804307]`
- **Schema:** `a_os_open_greenspace`
- **Table:** `access_point`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 355705
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Access Point is part of OS Open Greenspace, published by Ordnance Survey. It represents access point features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `access_type` | `varchar` | Publisher-supplied access type for the represented feature or record. | source_attribute | Yes | No | No |
| `ref_to_greenspace_site` | `varchar` | Publisher-supplied reference to greenspace site for the represented feature or record. | source_attribute | Yes | No | No |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
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
