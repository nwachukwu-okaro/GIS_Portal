# Public Water Supply Source Protection Areas 20k

## Overview

- **Identifier:** `a_irl_geological_survey/public_water_supply_source_protection_areas_20k`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.812542, 51.658715, -6.146651, 55.287975]`
- **Schema:** `a_irl_geological_survey`
- **Table:** `public_water_supply_source_protection_areas_20k`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 357
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Public Water Supply Source Protection Areas 20k is an authoritative dataset published by Geological Survey Ireland. It represents public water supply source protection areas 20k features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `pwsspa_pk` | `integer` | Count or numeric value for pwsspa pk in the represented area. | statistical_value | Yes | No | No |
| `spa_id` | `varchar(25)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `spa_code` | `varchar(10)` | Code assigned by the source dataset. | code | Yes | No | No |
| `spa_name` | `varchar(150)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `datasource` | `varchar(10)` | Publisher-supplied datasource for the represented feature or record. | source_attribute | Yes | No | No |
| `dw_code` | `varchar(15)` | Code assigned by the source dataset. | code | Yes | No | No |
| `eu_report` | `varchar(20)` | Publisher-supplied eu report for the represented feature or record. | source_attribute | Yes | No | No |
| `county` | `varchar(20)` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
| `report_url` | `varchar(254)` | Publisher-supplied report url for the represented feature or record. | source_attribute | Yes | No | No |
| `rep_creator` | `varchar(50)` | Publisher-supplied rep creator for the represented feature or record. | source_attribute | Yes | No | No |
| `active` | `varchar(20)` | Publisher-supplied active for the represented feature or record. | source_attribute | Yes | No | No |
| `gsi_review` | `varchar(10)` | Publisher-supplied gsi review for the represented feature or record. | source_attribute | Yes | No | No |
| `publish` | `varchar(10)` | Publisher-supplied publish for the represented feature or record. | source_attribute | Yes | No | No |
| `reportdate` | `date` | Date or year recorded for reportdate. | date | Yes | No | No |
| `updatedate` | `date` | Date or year recorded for updatedate. | date | Yes | No | No |
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
