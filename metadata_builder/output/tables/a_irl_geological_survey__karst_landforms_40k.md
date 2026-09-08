# Karst Landforms 40k

## Overview

- **Identifier:** `a_irl_geological_survey/karst_landforms_40k`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.808804, 51.832320, -5.747848, 55.193150]`
- **Topic category:** geoscientificInformation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_irl_geological_survey`
- **Table:** `karst_landforms_40k`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:2157
- **Rows:** 2000
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Karst Landforms 40k is an authoritative dataset published by Geological Survey Ireland. It represents karst landforms 40k features using multipoint geometry.

## Lineage

Published by Geological Survey Ireland as open geological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `object_id` | `integer` | Identifier assigned by the source dataset. |
| `karst40kid` | `varchar` |  |
| `oldkarstid` | `varchar` |  |
| `karst_type` | `varchar` |  |
| `karst_name` | `varchar` | Name associated with the represented feature. |
| `within_kf` | `varchar` |  |
| `xyaccuracy` | `varchar` |  |
| `datasource` | `varchar` | Publisher-supplied datasource for the represented feature or record. |
| `comments` | `varchar` | Publisher-supplied comments for the represented feature or record. |
| `details` | `varchar` |  |
| `county` | `varchar` | Publisher-supplied county for the represented feature or record. |
| `x_itm` | `double precision` | Count or numeric value for x itm in the represented area. |
| `y_itm` | `double precision` | Count or numeric value for y itm in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
