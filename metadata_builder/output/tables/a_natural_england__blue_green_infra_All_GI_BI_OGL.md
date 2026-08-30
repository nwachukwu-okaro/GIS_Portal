# Blue Green Infra All Gi Bi Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_All_GI_BI_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418945, 49.864637, 1.768950, 55.811668]`
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_All_GI_BI_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1765624
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Blue Green Infra All Gi Bi Ogl is an authoritative dataset published by Natural England. It represents blue green infra all gi bi ogl features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `parent_id` | `varchar(254)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `dataset` | `varchar(255)` | Publisher-supplied dataset for the represented feature or record. | source_attribute | Yes | No | No |
| `accessible` | `varchar(255)` | Publisher-supplied accessible for the represented feature or record. | source_attribute | Yes | No | No |
| `angst` | `varchar(255)` | Publisher-supplied angst for the represented feature or record. | source_attribute | Yes | No | No |
| `naturalness` | `integer` | Count or numeric value for naturalness in the represented area. | statistical_value | Yes | No | No |
| `typologytitle` | `varchar(255)` | Publisher-supplied typologytitle for the represented feature or record. | source_attribute | Yes | No | No |
| `likely_cricket` | `varchar(255)` | Publisher-supplied likely cricket for the represented feature or record. | source_attribute | Yes | No | No |
| `license` | `varchar(255)` | Publisher-supplied license for the represented feature or record. | source_attribute | Yes | No | No |
| `typologycode` | `varchar(255)` | Publisher-assigned typologycode for the record. | source_identifier | Yes | No | No |
| `perc_manmade` | `double precision` | Count or numeric value for perc manmade in the represented area. | statistical_value | Yes | No | No |
| `join_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `attribute` | `varchar(255)` | Publisher-supplied attribute for the represented feature or record. | source_attribute | Yes | No | No |
| `shape_length` | `double precision` | Numeric shape length value recorded for the feature. | measure | Yes | No | No |
| `shape_area` | `double precision` | Numeric shape area value recorded for the feature. | measure | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
