# Car Charging Point

## Overview

- **Identifier:** `a_os_open_map_local/car_charging_point`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Map Local
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-map-local
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.489352, 50.019663, 1.761414, 60.759101]`
- **Schema:** `a_os_open_map_local`
- **Table:** `car_charging_point`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 42850
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Contains OS data © Crown copyright and database right 2026

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `charge_method` | `varchar` | Publisher-supplied charge method for the represented feature or record. | source_attribute | Yes | No | No |
| `feature_code` | `integer` | Code assigned by the source dataset. | code | Yes | No | No |
| `rated_voltage` | `integer` | Count or numeric value for rated voltage in the represented area. | statistical_value | Yes | No | No |
| `type` | `varchar` | Publisher-supplied type for the represented feature or record. | source_attribute | Yes | No | No |
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
