# Public Water Supply Source Protection Areas 20k

## Overview

- **Identifier:** `a_irl_geological_survey/public_water_supply_source_protection_areas_20k`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Schema:** `a_irl_geological_survey`
- **Table:** `public_water_supply_source_protection_areas_20k`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 357
- **Metadata status:** source_mapped

## Description

Public Water Supply Source Protection Areas 20k is an authoritative dataset published by Geological Survey Ireland. It represents public water supply source protection areas 20k features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `pwsspa_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `spa_id` | `varchar(25)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `spa_code` | `varchar(10)` | Code assigned by the source dataset. | code | Yes | No | No |
| `spa_name` | `varchar(150)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `datasource` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `dw_code` | `varchar(15)` | Code assigned by the source dataset. | code | Yes | No | No |
| `eu_report` | `varchar(20)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `county` | `varchar(20)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `report_url` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `rep_creator` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `active` | `varchar(20)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `gsi_review` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `publish` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `reportdate` | `date` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `updatedate` | `date` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
