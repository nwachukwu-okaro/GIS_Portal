# Greater Manchester Acb

## Overview

- **Identifier:** `a_greater_manchester_ecology_unit/greater_manchester_acb`
- **Source organisation:** Greater Manchester Ecology Unit
- **Source:** https://www.gmenvironment.org.uk/gmeu/
- **WGS84 extent:** `[-2.727031, 53.327182, -1.909622, 53.685720]`
- **Schema:** `a_greater_manchester_ecology_unit`
- **Table:** `greater_manchester_acb`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 12796
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Greater Manchester Acb is an authoritative dataset published by Greater Manchester Ecology Unit. It represents greater manchester acb features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `lnrs_id` | `varchar(254)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `acb_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `gmacb_pk` | `integer` | Internal primary-key value for the Greater Manchester biodiversity area record. | record_identifier | Yes | No | No |
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
