# Classification

## Overview

- **Identifier:** `a_os_addressbase_premium/classification`
- **Source organisation:** Ordnance Survey
- **Product:** AddressBase Premium
- **Source:** https://www.ordnancesurvey.co.uk/products/addressbase-premium
- **Geographic coverage:** Great Britain
- **Topic category:** location
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_addressbase_premium`
- **Table:** `classification`
- **Geometry:** GEOMETRY
- **CRS:** Not applicable or unknown
- **Rows:** 45333097
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Classification is part of AddressBase Premium, published by Ordnance Survey. It represents classification features using geometry geometry.

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
| `class_key` | `text` | Publisher-supplied class key for the represented feature or record. |
| `classification_code` | `text` | Code assigned by the source dataset. |
| `class_scheme` | `text` | Publisher-supplied class scheme for the represented feature or record. |
| `scheme_version` | `double precision` | Count or numeric value for scheme version in the represented area. |
| `start_date` | `text` | Date associated with the represented feature or source record. |
| `end_date` | `text` | Date associated with the represented feature or source record. |
| `last_update_date` | `text` | Date associated with the represented feature or source record. |
| `entry_date` | `text` | Date associated with the represented feature or source record. |
| `id` | `bigint` | Count or numeric value for identifier in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
