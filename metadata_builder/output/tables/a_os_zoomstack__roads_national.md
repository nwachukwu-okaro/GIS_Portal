# Roads National

## Overview

- **Identifier:** `a_os_zoomstack/roads_national`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Zoomstack
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-zoomstack
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-6.376816, 50.091927, 1.756298, 58.612378]`
- **Schema:** `a_os_zoomstack`
- **Table:** `roads_national`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 123341
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Roads National is part of OS Open Zoomstack, published by Ordnance Survey. It represents roads national features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `type` | `varchar` | Publisher-supplied type for the represented feature or record. | source_attribute | Yes | No | No |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `number` | `varchar` | Publisher-supplied number for the represented feature or record. | source_attribute | Yes | No | No |
| `level` | `integer` | Count or numeric value for level in the represented area. | statistical_value | Yes | No | No |
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
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
