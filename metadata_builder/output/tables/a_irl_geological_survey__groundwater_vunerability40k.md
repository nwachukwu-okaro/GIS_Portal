# Groundwater Vunerability40k

## Overview

- **Identifier:** `a_irl_geological_survey/groundwater_vunerability40k`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Schema:** `a_irl_geological_survey`
- **Table:** `groundwater_vunerability40k`
- **Geometry:** POLYGON
- **CRS:** EPSG:2157
- **Rows:** 35000
- **Metadata status:** source_mapped

## Description

Groundwater Vunerability40k is an authoritative dataset published by Geological Survey Ireland. It represents groundwater vunerability40k features using polygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `gwv_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `vul40kid` | `varchar(25)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `vul_category` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `vul_description` | `varchar(40)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
