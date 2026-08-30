# Geoheritage Unaudited Sites

## Overview

- **Identifier:** `a_irl_geological_survey/geoheritage_unaudited_sites`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.549891, 51.769375, -9.211730, 52.574371]`
- **Schema:** `a_irl_geological_survey`
- **Table:** `geoheritage_unaudited_sites`
- **Geometry:** POLYGON
- **CRS:** EPSG:2157
- **Rows:** 116
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Geoheritage Unaudited Sites is an authoritative dataset published by Geological Survey Ireland. It represents geoheritage unaudited sites features using polygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `gus_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `site_name` | `varchar(100)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `theme` | `varchar(10)` | Publisher-supplied theme for the represented feature or record. | source_attribute | Yes | No | No |
| `county` | `varchar(50)` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
| `features` | `varchar(255)` | Publisher-supplied features for the represented feature or record. | source_attribute | Yes | No | No |
| `townland` | `varchar(255)` | Publisher-supplied townland for the represented feature or record. | source_attribute | Yes | No | No |
| `description` | `varchar(255)` | Publisher-supplied description for the represented feature or record. | source_attribute | Yes | No | No |
| `references` | `varchar(255)` | Publisher-supplied references for the represented feature or record. | source_attribute | Yes | No | No |
| `designat` | `varchar(50)` | Publisher-supplied designat for the represented feature or record. | source_attribute | Yes | No | No |
| `x_ig` | `integer` | Count or numeric value for x ig in the represented area. | statistical_value | Yes | No | No |
| `y_ig` | `integer` | Count or numeric value for y ig in the represented area. | statistical_value | Yes | No | No |
| `x_itm` | `double precision` | Count or numeric value for x itm in the represented area. | statistical_value | Yes | No | No |
| `y_itm` | `double precision` | Count or numeric value for y itm in the represented area. | statistical_value | Yes | No | No |
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
