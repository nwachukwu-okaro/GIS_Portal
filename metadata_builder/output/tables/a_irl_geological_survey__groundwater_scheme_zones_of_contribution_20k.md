# Groundwater Scheme Zones Of Contribution 20k

## Overview

- **Identifier:** `a_irl_geological_survey/groundwater_scheme_zones_of_contribution_20k`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.046017, 51.626105, -6.017837, 55.327257]`
- **Schema:** `a_irl_geological_survey`
- **Table:** `groundwater_scheme_zones_of_contribution_20k`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 254
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Groundwater Scheme Zones Of Contribution 20k is an authoritative dataset published by Geological Survey Ireland. It represents groundwater scheme zones of contribution 20k features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `gwsz_pk` | `integer` | Count or numeric value for gwsz pk in the represented area. | statistical_value | Yes | No | No |
| `gws_zoc_id` | `varchar(25)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `gws_name` | `varchar(50)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `year` | `integer` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `consultant` | `varchar(50)` | Publisher-supplied consultant for the represented feature or record. | source_attribute | Yes | No | No |
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
