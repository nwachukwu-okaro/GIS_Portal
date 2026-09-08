# Railway Track Ln

## Overview

- **Identifier:** `a_irishrail/railway_track_ln`
- **Source organisation:** Iarnrod Eireann / Irish Rail
- **Source:** https://www.irishrail.ie/travel-information/iarnrod-eireann-open-data
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.699184, 51.846274, -6.034981, 54.274002]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irishrail`
- **Table:** `railway_track_ln`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:29903
- **Rows:** 10891
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

Railway Track Ln is an authoritative dataset published by Iarnrod Eireann / Irish Rail. It represents railway track ln features using multilinestring geometry.

## Lineage

Published by Iarnrod Eireann / Irish Rail as open transport data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `railway_track_ln_pk` | `integer` | Count or numeric value for railway track ln pk in the represented area. |
| `route` | `varchar(200)` | Publisher-supplied route for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
