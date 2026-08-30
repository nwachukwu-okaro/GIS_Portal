# Watercourse Link

## Overview

- **Identifier:** `a_os_open_rivers/watercourse_link`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Rivers
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-rivers
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.524879, 49.974616, 1.756276, 60.825228]`
- **Schema:** `a_os_open_rivers`
- **Table:** `watercourse_link`
- **Geometry:** LINESTRING
- **CRS:** EPSG:27700
- **Rows:** 193040
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Watercourse Link is part of OS Open Rivers, published by Ordnance Survey. It represents watercourse link features using linestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `flow_direction` | `varchar` | Publisher-supplied flow direction for the represented feature or record. | source_attribute | Yes | No | No |
| `length` | `real` | Numeric length value recorded for the feature. | measure | Yes | No | No |
| `fictitious` | `varchar` | Publisher-supplied fictitious for the represented feature or record. | source_attribute | Yes | No | No |
| `form` | `varchar` | Publisher-supplied form for the represented feature or record. | source_attribute | Yes | No | No |
| `watercourse_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `watercourse_name_alternative` | `varchar` | Publisher-supplied watercourse name alternative for the represented feature or record. | source_attribute | Yes | No | No |
| `start_node` | `varchar` | Publisher-supplied start node for the represented feature or record. | source_attribute | Yes | No | No |
| `end_node` | `varchar` | Publisher-supplied end node for the represented feature or record. | source_attribute | Yes | No | No |
| `fid` | `integer` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
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
