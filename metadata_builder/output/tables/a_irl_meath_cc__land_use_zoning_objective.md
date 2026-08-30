# Land Use Zoning Objective

## Overview

- **Identifier:** `a_irl_meath_cc/land_use_zoning_objective`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Schema:** `a_irl_meath_cc`
- **Table:** `land_use_zoning_objective`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 2201
- **Metadata status:** source_mapped

## Description

Land Use Zoning Objective is an authoritative dataset published by Meath County Council. It represents land use zoning objective features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `luzo_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `guid` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `site_code` | `varchar(100)` | Code assigned by the source dataset. | code | Yes | No | No |
| `zoning_code` | `varchar(6)` | Code assigned by the source dataset. | code | Yes | No | No |
| `zoning_description` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `zoning_objective` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `area_acres` | `real` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `area_hectares` | `real` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `residential` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `settlement` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `settlement_01` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `plan_name` | `varchar(120)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `lifetime` | `varchar(25)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `more_info` | `varchar(250)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
