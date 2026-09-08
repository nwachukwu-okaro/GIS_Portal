# Mile Post

## Overview

- **Identifier:** `a_irishrail/mile_post`
- **Source organisation:** Iarnrod Eireann / Irish Rail
- **Source:** https://www.irishrail.ie/travel-information/iarnrod-eireann-open-data
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.699179, 51.846434, -6.035095, 54.272267]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_irishrail`
- **Table:** `mile_post`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:29903
- **Rows:** 4282
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Mile Post is an authoritative dataset published by Iarnrod Eireann / Irish Rail. It represents mile post features using multipoint geometry.

## Lineage

Published by Iarnrod Eireann / Irish Rail as open transport data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `mile_post_pk` | `integer` | Count or numeric value for mile post pk in the represented area. |
| `route` | `varchar` | Publisher-supplied route for the represented feature or record. |
| `mile` | `integer` | Count or numeric value for mile in the represented area. |
| `quarter` | `smallint` | Count or numeric value for quarter in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
