# Flood Zones 2 and 3 - Rivers and Sea

## Overview

- **Identifier:** `a_environment_agency/flood_zones_2_3_rivers_and_sea`
- **Source organisation:** Environment Agency
- **Source:** https://environment.data.gov.uk/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.366581, 49.882243, 1.763602, 55.811634]`
- **Schema:** `a_environment_agency`
- **Table:** `flood_zones_2_3_rivers_and_sea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 12804126
- **Columns:** 5
- **Metadata status:** context_curated

## Description

Modelled Flood Zone 2 and Flood Zone 3 extents showing land at risk from flooding from rivers or the sea, without accounting for defences.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `origin` | `text` | Evidence or modelling source used to define the flood-zone extent. | flood_model_origin | Yes | No | No |
| `flood_zone` | `text` | Flood-zone class, such as FZ2 or FZ3. | flood_zone_class | Yes | No | No |
| `flood_source` | `text` | Source of flooding represented, such as river, sea or surface water. | flood_source | Yes | No | No |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
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

- Schema default only; verify dataset-specific restrictions and third-party rights.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
