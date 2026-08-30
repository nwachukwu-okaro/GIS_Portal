# Land Use Zoning Objective

## Overview

- **Identifier:** `a_irl_meath_cc/land_use_zoning_objective`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.343668, 53.381919, -6.212613, 53.917668]`
- **Schema:** `a_irl_meath_cc`
- **Table:** `land_use_zoning_objective`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 2201
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Land Use Zoning Objective is an authoritative dataset published by Meath County Council. It represents land use zoning objective features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `luzo_pk` | `integer` | Count or numeric value for luzo pk in the represented area. | statistical_value | Yes | No | No |
| `guid` | `double precision` | Count or numeric value for guid in the represented area. | statistical_value | Yes | No | No |
| `site_code` | `varchar(100)` | Code assigned by the source dataset. | code | Yes | No | No |
| `zoning_code` | `varchar(6)` | Code assigned by the source dataset. | code | Yes | No | No |
| `zoning_description` | `varchar(100)` | Publisher-supplied zoning description for the represented feature or record. | source_attribute | Yes | No | No |
| `zoning_objective` | `varchar(254)` | Publisher-supplied zoning objective for the represented feature or record. | source_attribute | Yes | No | No |
| `area_acres` | `real` | Numeric area acres value recorded for the feature. | measure | Yes | No | No |
| `area_hectares` | `real` | Numeric area hectares value recorded for the feature. | measure | Yes | No | No |
| `residential` | `varchar(100)` | Publisher-supplied residential for the represented feature or record. | source_attribute | Yes | No | No |
| `settlement` | `double precision` | Count or numeric value for settlement in the represented area. | statistical_value | Yes | No | No |
| `settlement_01` | `varchar(100)` | Publisher-supplied settlement 01 for the represented feature or record. | source_attribute | Yes | No | No |
| `plan_name` | `varchar(120)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `lifetime` | `varchar(25)` | Publisher-supplied lifetime for the represented feature or record. | source_attribute | Yes | No | No |
| `more_info` | `varchar(250)` | Publisher-supplied more info for the represented feature or record. | source_attribute | Yes | No | No |
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
