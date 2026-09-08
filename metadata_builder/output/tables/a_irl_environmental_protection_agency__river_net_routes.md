# River Net Routes

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/river_net_routes`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.468183, 51.450434, -6.005639, 55.380124]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `river_net_routes`
- **Geometry:** LINESTRING
- **CRS:** EPSG:29903
- **Rows:** 102108
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

River Net Routes is an authoritative dataset published by Environmental Protection Agency Ireland. It represents river net routes features using linestring geometry.

## Lineage

Published by the Environmental Protection Agency Ireland as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `segment_code` | `varchar(20)` | Code assigned by the source dataset. |
| `epa_name` | `varchar(100)` | Name associated with the represented feature. |
| `epa_code` | `varchar(5)` | Code assigned by the source dataset. |
| `stream_order` | `integer` | Count or numeric value for stream order in the represented area. |
| `continua` | `varchar(1)` | Publisher-supplied continua for the represented feature or record. |
| `river_water_body_code` | `varchar(100)` | Code assigned by the source dataset. |
| `lake_water_body_code` | `varchar(100)` | Code assigned by the source dataset. |
| `transitional_water_body_code` | `varchar(100)` | Code assigned by the source dataset. |
| `segment_length` | `double precision` | Numeric segment length value recorded for the feature. |
| `coastal_water_body_code` | `varchar(100)` | Code assigned by the source dataset. |
| `rnr_pk` | `integer` | Count or numeric value for rnr pk in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
