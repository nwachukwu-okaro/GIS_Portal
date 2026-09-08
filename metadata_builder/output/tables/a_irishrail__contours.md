# Contours

## Overview

- **Identifier:** `a_irishrail/contours`
- **Source organisation:** Iarnrod Eireann / Irish Rail
- **Source:** https://www.irishrail.ie/travel-information/iarnrod-eireann-open-data
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.706042, 51.846086, -6.034629, 54.274006]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irishrail`
- **Table:** `contours`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:29903
- **Rows:** 365055
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Contours is an authoritative dataset published by Iarnrod Eireann / Irish Rail. It represents contours features using multilinestring geometry.

## Lineage

Published by Iarnrod Eireann / Irish Rail as open transport data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `contour_pk` | `integer` | Count or numeric value for contour pk in the represented area. |
| `contour_type` | `varchar(5)` | Publisher-supplied contour type for the represented feature or record. |
| `z` | `real` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
