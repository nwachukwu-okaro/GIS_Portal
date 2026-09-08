# Scenic Routes

## Overview

- **Identifier:** `a_irl_galway_cc/scenic_routes`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.174339, 53.055206, -8.222288, 53.614337]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_galway_cc`
- **Table:** `scenic_routes`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:2157
- **Rows:** 8
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Scenic Routes is an authoritative dataset published by Galway County Council. It represents scenic routes features using multilinestring geometry.

## Lineage

Published by Galway County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `object_id` | `integer` | Identifier assigned by the source dataset. |
| `route_id` | `integer` | Identifier assigned by the source dataset. |
| `route` | `varchar` | Publisher-supplied route for the represented feature or record. |
| `shape__length` | `double precision` | Numeric shape length value recorded for the feature. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
