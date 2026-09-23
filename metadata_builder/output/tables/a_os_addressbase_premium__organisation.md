# Organisation

## Overview

- **Identifier:** `a_os_addressbase_premium/organisation`
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
- **Table:** `organisation`
- **Geometry:** GEOMETRY
- **CRS:** Not applicable or unknown
- **Rows:** 1389164
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Organisation is part of AddressBase Premium, published by Ordnance Survey. It represents organisation features using geometry geometry.

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
| `org_key` | `text` |  |
| `organisation` | `text` | Organisation name associated with the address. |
| `legal_name` | `text` | Name associated with the represented feature. |
| `start_date` | `text` | Date associated with the represented feature or source record. |
| `end_date` | `text` | Date associated with the represented feature or source record. |
| `last_update_date` | `text` | Date associated with the represented feature or source record. |
| `entry_date` | `text` | Date associated with the represented feature or source record. |
| `id` | `bigint` | Primary-key identifier for records in organisation. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
