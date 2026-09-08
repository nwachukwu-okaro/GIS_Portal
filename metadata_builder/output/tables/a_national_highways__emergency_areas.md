# Emergency Areas

## Overview

- **Identifier:** `a_national_highways/emergency_areas`
- **Source organisation:** National Highways
- **Source:** https://developer.data.nationalhighways.co.uk/
- **Geographic coverage:** England
- **WGS84 extent:** `[-2.591876, 50.867387, 0.464372, 53.747101]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_national_highways`
- **Table:** `emergency_areas`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 438
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

Emergency Areas is an authoritative dataset published by National Highways. It represents emergency areas features using multilinestring geometry.

## Lineage

Published by National Highways as open roads data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `objectid_1` | `integer` | Count or numeric value for objectid 1 in the represented area. |
| `globalid_1` | `varchar` | Publisher-supplied globalid 1 for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
