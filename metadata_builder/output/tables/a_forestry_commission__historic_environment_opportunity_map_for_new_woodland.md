# Historic Environment Opportunity Map For New Woodland

## Overview

- **Identifier:** `a_forestry_commission/historic_environment_opportunity_map_for_new_woodland`
- **Source organisation:** Forestry Commission
- **Source:** https://www.forestresearch.gov.uk/tools-and-resources/national-forest-inventory/
- **Schema:** `a_forestry_commission`
- **Table:** `historic_environment_opportunity_map_for_new_woodland`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 552503
- **Metadata status:** source_mapped

## Description

version: 20250408
Source: https://environment.data.gov.uk/dataset/00354b01-c138-4aca-b2a1-4504dc40be5c

Attribution: © Forestry Commission copyright and/or database right 2025. All rights reserved.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system object identifier. | identifier | Yes | No | No |
| `opportunit` | `varchar(32)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `area_ha` | `double precision` | Area of the feature in hectares. | area | Yes | No | No |
| `fcid` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
