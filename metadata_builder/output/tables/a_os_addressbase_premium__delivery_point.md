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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
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
| `change_type` | `text` | Publisher-supplied change type for the represented feature or record. |
| `uprn` | `bigint` | Count or numeric value for uprn in the represented area. |
| `udprn` | `bigint` | Count or numeric value for udprn in the represented area. |
| `organisation_name` | `text` | Name associated with the represented feature. |
| `department_name` | `text` | Name associated with the represented feature. |
| `sub_building_name` | `text` | Name associated with the represented feature. |
| `building_name` | `text` | Name associated with the represented feature. |
| `building_number` | `bigint` | Count or numeric value for building number in the represented area. |
| `dependent_thoroughfare` | `text` | Publisher-supplied dependent thoroughfare for the represented feature or record. |
| `thoroughfare` | `text` | Publisher-supplied thoroughfare for the represented feature or record. |
| `double_dependent_locality` | `text` | Publisher-supplied double dependent locality for the represented feature or record. |
| `dependent_locality` | `text` | Publisher-supplied dependent locality for the represented feature or record. |
| `post_town` | `text` | Publisher-supplied post town for the represented feature or record. |
| `postcode` | `text` | Publisher-assigned postcode for the record. |
| `postcode_type` | `text` | Publisher-supplied postcode type for the represented feature or record. |
| `delivery_point_suffix` | `text` | Publisher-supplied delivery point suffix for the represented feature or record. |
| `welsh_dependent_thoroughfare` | `text` | Publisher-supplied welsh dependent thoroughfare for the represented feature or record. |
| `welsh_thoroughfare` | `text` | Publisher-supplied welsh thoroughfare for the represented feature or record. |
| `welsh_double_dependent_locality` | `text` | Publisher-supplied welsh double dependent locality for the represented feature or record. |
| `welsh_dependent_locality` | `text` | Publisher-supplied welsh dependent locality for the represented feature or record. |
| `welsh_post_town` | `text` | Publisher-supplied welsh post town for the represented feature or record. |
| `po_box_number` | `text` | Publisher-supplied po box number for the represented feature or record. |
| `process_date` | `text` | Date associated with the represented feature or source record. |
| `start_date` | `text` | Date associated with the represented feature or source record. |
| `end_date` | `text` | Date associated with the represented feature or source record. |
| `last_update_date` | `text` | Date associated with the represented feature or source record. |
| `entry_date` | `text` | Date associated with the represented feature or source record. |
| `id` | `bigint` | Count or numeric value for identifier in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
