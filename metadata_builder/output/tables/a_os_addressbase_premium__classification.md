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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
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
| `change_type` | `text` |  |
| `uprn` | `bigint` | Unique Property Reference Number identifying the addressable location. |
| `class_key` | `text` |  |
| `classification_code` | `text` | Code assigned by the source dataset. |
| `class_scheme` | `text` |  |
| `scheme_version` | `double precision` |  |
| `start_date` | `text` | Date associated with the represented feature or source record. |
| `end_date` | `text` | Date associated with the represented feature or source record. |
| `last_update_date` | `text` | Date associated with the represented feature or source record. |
| `entry_date` | `text` | Date associated with the represented feature or source record. |
| `id` | `bigint` | Primary-key identifier for records in classification. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
