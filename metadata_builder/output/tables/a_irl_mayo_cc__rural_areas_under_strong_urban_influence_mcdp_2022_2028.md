# Rural Areas Under Strong Urban Influence Mcdp 2022 2028

## Overview

- **Identifier:** `a_irl_mayo_cc/rural_areas_under_strong_urban_influence_mcdp_2022_2028`
- **Source organisation:** Mayo County Council
- **Source:** https://data.gov.ie/organization/mayo-county-council
- **Geographic coverage:** County Mayo
- **WGS84 extent:** `[-9.891384, 53.602042, -8.743192, 54.162191]`
- **Schema:** `a_irl_mayo_cc`
- **Table:** `rural_areas_under_strong_urban_influence_mcdp_2022_2028`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:3857
- **Rows:** 6
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Rural Areas Under Strong Urban Influence Mcdp 2022 2028 is an authoritative dataset published by Mayo County Council. It represents rural areas under strong urban influence mcdp 2022 2028 features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `field1` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `object_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `rasui_pk` | `integer` | Count or numeric value for rasui pk in the represented area. | statistical_value | Yes | No | No |
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
