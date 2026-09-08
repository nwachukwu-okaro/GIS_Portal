# County Boundary

## Overview

- **Identifier:** `a_irl_meath_cc/county_boundary`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.343668, 53.381919, -6.212613, 53.917668]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_meath_cc`
- **Table:** `county_boundary`
- **Geometry:** POLYGON
- **CRS:** EPSG:2157
- **Rows:** 1
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

County Boundary is an authoritative dataset published by Meath County Council. It represents county boundary features using polygon geometry.

## Lineage

Published by Meath County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `county` | `varchar(25)` | Publisher-supplied county for the represented feature or record. |
| `cb_pk` | `integer` | Count or numeric value for cb pk in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
