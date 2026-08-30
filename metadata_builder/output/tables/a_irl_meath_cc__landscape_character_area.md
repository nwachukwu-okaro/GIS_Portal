# Landscape Character Area

## Overview

- **Identifier:** `a_irl_meath_cc/landscape_character_area`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.342768, 53.381706, -6.211721, 53.917564]`
- **Schema:** `a_irl_meath_cc`
- **Table:** `landscape_character_area`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 20
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Landscape Character Area is an authoritative dataset published by Meath County Council. It represents landscape character area features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `lca_pk` | `integer` | Count or numeric value for lca pk in the represented area. | statistical_value | Yes | No | No |
| `description` | `varchar(50)` | Publisher-supplied description for the represented feature or record. | source_attribute | Yes | No | No |
| `character` | `varchar(100)` | Publisher-supplied character for the represented feature or record. | source_attribute | Yes | No | No |
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
