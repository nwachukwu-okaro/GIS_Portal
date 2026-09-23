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
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
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
| `gws_pk` | `integer` | Primary-key identifier for records in groundwater_wells_springs_100k_ie26_itm. |
| `well_id` | `varchar(25)` | Identifier assigned by the source dataset. |
| `gsi_name` | `varchar(11)` | Name associated with the represented feature. |
| `orig_name` | `varchar(50)` | Name associated with the represented feature. |
| `source_name` | `varchar(100)` | Name associated with the represented feature. |
| `source_type` | `varchar(20)` |  |
| `holedepthm` | `double precision` |  |
| `dtb_m` | `double precision` |  |
| `dtb_confid` | `varchar(20)` |  |
| `drill_date` | `date` | Date associated with the represented feature or source record. |
| `x_ing` | `double precision` |  |
| `y_ing` | `double precision` |  |
| `xy_accuracy` | `varchar(20)` |  |
| `town_land` | `varchar(50)` |  |
| `town` | `varchar(50)` |  |
| `county` | `varchar(9)` |  |
| `sheet_06in` | `double precision` |  |
| `source_use` | `varchar(30)` |  |
| `yield_class` | `varchar(20)` |  |
| `prod_class` | `varchar(5)` |  |
| `yield_m3d` | `double precision` |  |
| `avdayabstr` | `double precision` |  |
| `avdayoverf` | `double precision` |  |
| `drawdown_m` | `double precision` |  |
| `capacity` | `double precision` |  |
| `casingdiam` | `double precision` |  |
| `h2o_strike1` | `double precision` |  |
| `h2o_strike2` | `double precision` |  |
| `h2o_strike3` | `double precision` |  |
| `h2o_strike4` | `double precision` |  |
| `dpth_20_loss` | `double precision` |  |
| `comments` | `varchar(254)` |  |
| `drill_notes` | `varchar(254)` |  |
| `casing_note` | `varchar(254)` |  |
| `buffer` | `integer` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
