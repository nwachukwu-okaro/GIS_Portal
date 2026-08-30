# Statutory Main Rivers

## Overview

- **Identifier:** `a_environment_agency/statutory_main_river`
- **Source organisation:** Environment Agency
- **Source:** https://environment.data.gov.uk/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.703383, 49.986932, 1.756276, 55.707770]`
- **Schema:** `a_environment_agency`
- **Table:** `statutory_main_river`
- **Geometry:** MULTICURVE
- **CRS:** EPSG:27700
- **Rows:** 183911
- **Columns:** 5
- **Metadata status:** context_curated

## Description

Line network of watercourses legally designated as Main River in England, where the Environment Agency has permissive powers for flood-risk management.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `fid` | `bigint` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `status` | `text` | Legal or operational classification of the watercourse, such as Main River. | river_status | Yes | No | No |
| `length_km` | `double precision` | Calculated length of the watercourse feature in kilometres. | length | Yes | No | No |
| `shape_length` | `double precision` | Source GIS length measurement for the line geometry in dataset units. | geometry_length | Yes | No | No |

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

- Schema default only; verify dataset-specific restrictions and third-party rights.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
