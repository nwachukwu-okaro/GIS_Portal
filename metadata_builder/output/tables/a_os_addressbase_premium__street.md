# Street

## Overview

- **Identifier:** `a_os_addressbase_premium/street`
- **Source organisation:** Ordnance Survey
- **Product:** AddressBase Premium
- **Source:** https://www.ordnancesurvey.co.uk/products/addressbase-premium
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.571197, 49.872875, 1.761354, 60.814182]`
- **Topic category:** location
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_addressbase_premium`
- **Table:** `street`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 1526341
- **Columns:** 24
- **Metadata status:** source_mapped

## Description

Street is part of AddressBase Premium, published by Ordnance Survey. It represents street features using geometry geometry.

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
| `usrn` | `bigint` | Count or numeric value for usrn in the represented area. |
| `record_type` | `bigint` | Count or numeric value for record type in the represented area. |
| `swa_org_ref_naming` | `bigint` | Count or numeric value for swa org reference naming in the represented area. |
| `state` | `bigint` | Count or numeric value for state in the represented area. |
| `state_date` | `text` | Date associated with the represented feature or source record. |
| `street_surface` | `bigint` | Count or numeric value for street surface in the represented area. |
| `street_classification` | `bigint` | Count or numeric value for street classification in the represented area. |
| `version` | `bigint` | Count or numeric value for version in the represented area. |
| `street_start_date` | `text` | Date associated with the represented feature or source record. |
| `street_end_date` | `text` | Date associated with the represented feature or source record. |
| `last_update_date` | `text` | Date associated with the represented feature or source record. |
| `record_entry_date` | `text` | Date associated with the represented feature or source record. |
| `street_start_x` | `double precision` | Count or numeric value for street start x in the represented area. |
| `street_start_y` | `double precision` | Count or numeric value for street start y in the represented area. |
| `street_start_lat` | `double precision` | Numeric street start lat value recorded for the feature. |
| `street_start_long` | `double precision` | Numeric street start long value recorded for the feature. |
| `street_end_x` | `double precision` | Count or numeric value for street end x in the represented area. |
| `street_end_y` | `double precision` | Count or numeric value for street end y in the represented area. |
| `street_end_lat` | `double precision` | Numeric street end lat value recorded for the feature. |
| `street_end_long` | `double precision` | Numeric street end long value recorded for the feature. |
| `street_tolerance` | `bigint` | Count or numeric value for street tolerance in the represented area. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
