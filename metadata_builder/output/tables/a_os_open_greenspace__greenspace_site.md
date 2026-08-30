# Greenspace Site

## Overview

- **Identifier:** `a_os_open_greenspace/greenspace_site`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Greenspace
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-greenspace
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.574607, 49.893017, 1.761148, 60.804777]`
- **Schema:** `a_os_open_greenspace`
- **Table:** `greenspace_site`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 165978
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Greenspace Site is part of OS Open Greenspace, published by Ordnance Survey. It represents greenspace site features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `function` | `varchar` | Publisher-supplied function for the represented feature or record. | source_attribute | Yes | No | No |
| `distinctive_name_1` | `varchar` | Publisher-supplied distinctive name 1 for the represented feature or record. | source_attribute | Yes | No | No |
| `distinctive_name_2` | `varchar` | Publisher-supplied distinctive name 2 for the represented feature or record. | source_attribute | Yes | No | No |
| `distinctive_name_3` | `varchar` | Publisher-supplied distinctive name 3 for the represented feature or record. | source_attribute | Yes | No | No |
| `distinctive_name_4` | `varchar` | Publisher-supplied distinctive name 4 for the represented feature or record. | source_attribute | Yes | No | No |
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
