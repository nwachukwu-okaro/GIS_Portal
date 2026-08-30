# Corine Land Cover 2018

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/corine_land_cover_2018`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-11.032268, 51.195129, -5.615331, 55.627838]`
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `corine_land_cover_2018`
- **Geometry:** POLYGON
- **CRS:** EPSG:29902
- **Rows:** 18882
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Corine Land Cover 2018 is an authoritative dataset published by Environmental Protection Agency Ireland. It represents corine land cover 2018 features using polygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `clc18_pk` | `integer` | Count or numeric value for clc18 pk in the represented area. | statistical_value | Yes | No | No |
| `code_18` | `varchar(10)` | Publisher-supplied code 18 for the represented feature or record. | source_attribute | Yes | No | No |
| `class_description` | `varchar(200)` | Publisher-supplied class description for the represented feature or record. | source_attribute | Yes | No | No |
| `area_ha` | `double precision` | Area enclosed by the feature, measured in hectares. | area | Yes | No | No |
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
