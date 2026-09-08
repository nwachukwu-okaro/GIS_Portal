# Blpu

## Overview

- **Identifier:** `a_os_addressbase_premium/blpu`
- **Source organisation:** Ordnance Survey
- **Product:** AddressBase Premium
- **Source:** https://www.ordnancesurvey.co.uk/products/addressbase-premium
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.596588, 49.872879, 1.762748, 60.855283]`
- **Topic category:** location
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_addressbase_premium`
- **Table:** `blpu`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 41546482
- **Columns:** 22
- **Metadata status:** source_mapped

## Description

Blpu is part of AddressBase Premium, published by Ordnance Survey. It represents blpu features using geometry geometry.

## Lineage

Published by Ordnance Survey as part of AddressBase Premium. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `change_type` | `text` | Publisher-supplied change type for the represented feature or record. |
| `uprn` | `bigint` | Count or numeric value for uprn in the represented area. |
| `logical_status` | `bigint` | Count or numeric value for logical status in the represented area. |
| `blpu_state` | `bigint` | Count or numeric value for blpu state in the represented area. |
| `blpu_state_date` | `text` | Date associated with the represented feature or source record. |
| `parent_uprn` | `bigint` | Count or numeric value for parent uprn in the represented area. |
| `x_coordinate` | `double precision` | Count or numeric value for x coordinate in the represented area. |
| `y_coordinate` | `double precision` | Count or numeric value for y coordinate in the represented area. |
| `latitude` | `double precision` | Latitude coordinate, normally expressed in decimal degrees. |
| `longitude` | `double precision` | Longitude coordinate, normally expressed in decimal degrees. |
| `rpc` | `bigint` |  |
| `local_custodian_code` | `bigint` | Code assigned by the source dataset. |
| `country` | `text` | Publisher-supplied country for the represented feature or record. |
| `start_date` | `text` | Date associated with the represented feature or source record. |
| `end_date` | `text` | Date associated with the represented feature or source record. |
| `last_update_date` | `text` | Date associated with the represented feature or source record. |
| `entry_date` | `text` | Date associated with the represented feature or source record. |
| `addressbase_postal` | `text` | Publisher-supplied addressbase postal for the represented feature or record. |
| `postcode_locator` | `text` | Publisher-supplied postcode locator for the represented feature or record. |
| `multi_occ_count` | `bigint` | Count or numeric value for multi occ count in the represented area. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
