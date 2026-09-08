# Bus Routes

## Overview

- **Identifier:** `a_tfgm/bus_routes`
- **Source organisation:** Transport for Greater Manchester
- **Source:** https://developer.tfgm.com/
- **Geographic coverage:** Greater Manchester
- **WGS84 extent:** `[-3.011828, 53.255054, -1.782201, 53.834496]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_tfgm`
- **Table:** `bus_routes`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 2852
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Bus Routes is an authoritative dataset published by Transport for Greater Manchester. It represents bus routes features using multilinestring geometry.

## Lineage

Published by Transport for Greater Manchester as open transport data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `service_pk` | `integer` | Count or numeric value for service pk in the represented area. |
| `service_id` | `varchar` | Identifier assigned by the source dataset. |
| `service_no` | `varchar` | Publisher-supplied service number for the represented feature or record. |
| `suffix` | `varchar` | Publisher-supplied suffix for the represented feature or record. |
| `direction` | `varchar` | Publisher-supplied direction for the represented feature or record. |
| `day` | `varchar` | Publisher-supplied day for the represented feature or record. |
| `variation` | `varchar` | Publisher-supplied variation for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
