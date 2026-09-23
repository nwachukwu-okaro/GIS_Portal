# Delivery Point

## Overview

- **Identifier:** `a_os_addressbase_premium/delivery_point`
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
- **Table:** `delivery_point`
- **Geometry:** GEOMETRY
- **CRS:** Not applicable or unknown
- **Rows:** 8678000
- **Columns:** 29
- **Metadata status:** source_mapped

## Description

Delivery Point is part of AddressBase Premium, published by Ordnance Survey. It represents delivery point features using geometry geometry.

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
| `udprn` | `bigint` |  |
| `organisation_name` | `text` | Name associated with the represented feature. |
| `department_name` | `text` | Name associated with the represented feature. |
| `sub_building_name` | `text` | Name associated with the represented feature. |
| `building_name` | `text` | Name associated with the represented feature. |
| `building_number` | `bigint` | Building number used in the address. |
| `dependent_thoroughfare` | `text` | Dependent thoroughfare component of the address. |
| `thoroughfare` | `text` |  |
| `double_dependent_locality` | `text` |  |
| `dependent_locality` | `text` |  |
| `post_town` | `text` | Postal town component of the address. |
| `postcode` | `text` |  |
| `postcode_type` | `text` |  |
| `delivery_point_suffix` | `text` |  |
| `welsh_dependent_thoroughfare` | `text` |  |
| `welsh_thoroughfare` | `text` |  |
| `welsh_double_dependent_locality` | `text` |  |
| `welsh_dependent_locality` | `text` |  |
| `welsh_post_town` | `text` |  |
| `po_box_number` | `text` |  |
| `process_date` | `text` | Date associated with the represented feature or source record. |
| `start_date` | `text` | Date associated with the represented feature or source record. |
| `end_date` | `text` | Date associated with the represented feature or source record. |
| `last_update_date` | `text` | Date associated with the represented feature or source record. |
| `entry_date` | `text` | Date associated with the represented feature or source record. |
| `id` | `bigint` | Primary-key identifier for records in delivery_point. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
