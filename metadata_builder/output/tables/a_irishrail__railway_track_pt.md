# Railway Track Pt

## Overview

- **Identifier:** `a_irishrail/railway_track_pt`
- **Source organisation:** Iarnrod Eireann / Irish Rail
- **Source:** https://www.irishrail.ie/travel-information/iarnrod-eireann-open-data
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.699184, 51.846274, -6.034982, 54.274002]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_irishrail`
- **Table:** `railway_track_pt`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:29903
- **Rows:** 478313
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Railway Track Pt is an authoritative dataset published by Iarnrod Eireann / Irish Rail. It represents railway track pt features using multipoint geometry.

## Lineage

Published by Iarnrod Eireann / Irish Rail as open transport data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `railway_track_pt_pk` | `integer` | Count or numeric value for railway track pt pk in the represented area. |
| `z` | `real` |  |
| `text_string` | `varchar(8)` | Publisher-supplied text string for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
