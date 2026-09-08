# Groundwater Wells Springs 100k Ie26 Itm

## Overview

- **Identifier:** `a_irl_geological_survey/groundwater_wells_springs_100k_ie26_itm`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.455240, 51.434929, -6.013121, 55.379072]`
- **Topic category:** geoscientificInformation
- **Temporal extent:** 1899-12-30 to 7972-07-10
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_geological_survey`
- **Table:** `groundwater_wells_springs_100k_ie26_itm`
- **Geometry:** POLYGON
- **CRS:** EPSG:2157
- **Rows:** 36273
- **Columns:** 36
- **Metadata status:** source_mapped

## Description

Groundwater Wells Springs 100k Ie26 Itm is an authoritative dataset published by Geological Survey Ireland. It represents groundwater wells springs 100k ie26 itm features using polygon geometry.

## Lineage

Published by Geological Survey Ireland as open geological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `gws_pk` | `integer` | Count or numeric value for gws pk in the represented area. |
| `well_id` | `varchar(25)` | Identifier assigned by the source dataset. |
| `gsi_name` | `varchar(11)` | Name associated with the represented feature. |
| `orig_name` | `varchar(50)` | Name associated with the represented feature. |
| `source_name` | `varchar(100)` | Name associated with the represented feature. |
| `source_type` | `varchar(20)` | Publisher-supplied source type for the represented feature or record. |
| `holedepthm` | `double precision` | Numeric holedepthm value recorded for the feature. |
| `dtb_m` | `double precision` | Count or numeric value for dtb male in the represented area. |
| `dtb_confid` | `varchar(20)` | Publisher-assigned dtb confid for the record. |
| `drill_date` | `date` | Date associated with the represented feature or source record. |
| `x_ing` | `double precision` | Count or numeric value for x ing in the represented area. |
| `y_ing` | `double precision` | Count or numeric value for y ing in the represented area. |
| `xy_accuracy` | `varchar(20)` | Publisher-supplied xy accuracy for the represented feature or record. |
| `town_land` | `varchar(50)` | Publisher-supplied town land for the represented feature or record. |
| `town` | `varchar(50)` | Publisher-supplied town for the represented feature or record. |
| `county` | `varchar(9)` | Publisher-supplied county for the represented feature or record. |
| `sheet_06in` | `double precision` | Count or numeric value for sheet 06in in the represented area. |
| `source_use` | `varchar(30)` | Publisher-supplied source use for the represented feature or record. |
| `yield_class` | `varchar(20)` | Publisher-supplied yield class for the represented feature or record. |
| `prod_class` | `varchar(5)` | Publisher-supplied prod class for the represented feature or record. |
| `yield_m3d` | `double precision` | Count or numeric value for yield m3d in the represented area. |
| `avdayabstr` | `double precision` | Count or numeric value for avdayabstr in the represented area. |
| `avdayoverf` | `double precision` | Count or numeric value for avdayoverf in the represented area. |
| `drawdown_m` | `double precision` | Count or numeric value for drawdown male in the represented area. |
| `capacity` | `double precision` | Count or numeric value for capacity in the represented area. |
| `casingdiam` | `double precision` | Count or numeric value for casingdiam in the represented area. |
| `h2o_strike1` | `double precision` | Count or numeric value for h2o strike1 in the represented area. |
| `h2o_strike2` | `double precision` | Count or numeric value for h2o strike2 in the represented area. |
| `h2o_strike3` | `double precision` | Count or numeric value for h2o strike3 in the represented area. |
| `h2o_strike4` | `double precision` | Count or numeric value for h2o strike4 in the represented area. |
| `dpth_20_loss` | `double precision` | Count or numeric value for dpth 20 loss in the represented area. |
| `comments` | `varchar(254)` | Publisher-supplied comments for the represented feature or record. |
| `drill_notes` | `varchar(254)` | Publisher-supplied drill notes for the represented feature or record. |
| `casing_note` | `varchar(254)` | Publisher-supplied casing note for the represented feature or record. |
| `buffer` | `integer` | Count or numeric value for buffer in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
