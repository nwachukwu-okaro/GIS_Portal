# Groundwater Wells Springs 100k Ie26 Itm

## Overview

- **Identifier:** `a_irl_geological_survey/groundwater_wells_springs_100k_ie26_itm`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.455240, 51.434929, -6.013121, 55.379072]`
- **Schema:** `a_irl_geological_survey`
- **Table:** `groundwater_wells_springs_100k_ie26_itm`
- **Geometry:** POLYGON
- **CRS:** EPSG:2157
- **Rows:** 36273
- **Columns:** 36
- **Metadata status:** source_mapped

## Description

Groundwater Wells Springs 100k Ie26 Itm is an authoritative dataset published by Geological Survey Ireland. It represents groundwater wells springs 100k ie26 itm features using polygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `gws_pk` | `integer` | Count or numeric value for gws pk in the represented area. | statistical_value | Yes | No | No |
| `well_id` | `varchar(25)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `gsi_name` | `varchar(11)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `orig_name` | `varchar(50)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `source_name` | `varchar(100)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `source_type` | `varchar(20)` | Publisher-supplied source type for the represented feature or record. | source_attribute | Yes | No | No |
| `holedepthm` | `double precision` | Numeric holedepthm value recorded for the feature. | measure | Yes | No | No |
| `dtb_m` | `double precision` | Count or numeric value for dtb male in the represented area. | statistical_value | Yes | No | No |
| `dtb_confid` | `varchar(20)` | Publisher-assigned dtb confid for the record. | source_identifier | Yes | No | No |
| `drill_date` | `date` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `x_ing` | `double precision` | Count or numeric value for x ing in the represented area. | statistical_value | Yes | No | No |
| `y_ing` | `double precision` | Count or numeric value for y ing in the represented area. | statistical_value | Yes | No | No |
| `xy_accuracy` | `varchar(20)` | Publisher-supplied xy accuracy for the represented feature or record. | source_attribute | Yes | No | No |
| `town_land` | `varchar(50)` | Publisher-supplied town land for the represented feature or record. | source_attribute | Yes | No | No |
| `town` | `varchar(50)` | Publisher-supplied town for the represented feature or record. | source_attribute | Yes | No | No |
| `county` | `varchar(9)` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
| `sheet_06in` | `double precision` | Count or numeric value for sheet 06in in the represented area. | statistical_value | Yes | No | No |
| `source_use` | `varchar(30)` | Publisher-supplied source use for the represented feature or record. | source_attribute | Yes | No | No |
| `yield_class` | `varchar(20)` | Publisher-supplied yield class for the represented feature or record. | source_attribute | Yes | No | No |
| `prod_class` | `varchar(5)` | Publisher-supplied prod class for the represented feature or record. | source_attribute | Yes | No | No |
| `yield_m3d` | `double precision` | Count or numeric value for yield m3d in the represented area. | statistical_value | Yes | No | No |
| `avdayabstr` | `double precision` | Count or numeric value for avdayabstr in the represented area. | statistical_value | Yes | No | No |
| `avdayoverf` | `double precision` | Count or numeric value for avdayoverf in the represented area. | statistical_value | Yes | No | No |
| `drawdown_m` | `double precision` | Count or numeric value for drawdown male in the represented area. | statistical_value | Yes | No | No |
| `capacity` | `double precision` | Count or numeric value for capacity in the represented area. | statistical_value | Yes | No | No |
| `casingdiam` | `double precision` | Count or numeric value for casingdiam in the represented area. | statistical_value | Yes | No | No |
| `h2o_strike1` | `double precision` | Count or numeric value for h2o strike1 in the represented area. | statistical_value | Yes | No | No |
| `h2o_strike2` | `double precision` | Count or numeric value for h2o strike2 in the represented area. | statistical_value | Yes | No | No |
| `h2o_strike3` | `double precision` | Count or numeric value for h2o strike3 in the represented area. | statistical_value | Yes | No | No |
| `h2o_strike4` | `double precision` | Count or numeric value for h2o strike4 in the represented area. | statistical_value | Yes | No | No |
| `dpth_20_loss` | `double precision` | Count or numeric value for dpth 20 loss in the represented area. | statistical_value | Yes | No | No |
| `comments` | `varchar(254)` | Publisher-supplied comments for the represented feature or record. | source_attribute | Yes | No | No |
| `drill_notes` | `varchar(254)` | Publisher-supplied drill notes for the represented feature or record. | source_attribute | Yes | No | No |
| `casing_note` | `varchar(254)` | Publisher-supplied casing note for the represented feature or record. | source_attribute | Yes | No | No |
| `buffer` | `integer` | Count or numeric value for buffer in the represented area. | statistical_value | Yes | No | No |
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
