# Application Xref

## Overview

- **Identifier:** `a_os_addressbase_premium/application_xref`
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
- **Table:** `application_xref`
- **Geometry:** GEOMETRY
- **CRS:** Not applicable or unknown
- **Rows:** 2480000
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Application Xref is part of AddressBase Premium, published by Ordnance Survey. It represents application xref features using geometry geometry.

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
| `xref_key` | `text` | Publisher-supplied xref key for the represented feature or record. |
| `cross_reference` | `text` | Publisher-supplied cross reference for the represented feature or record. |
| `version` | `bigint` | Count or numeric value for version in the represented area. |
| `source` | `text` | Publisher-supplied source for the represented feature or record. |
| `start_date` | `text` | Date associated with the represented feature or source record. |
| `end_date` | `text` | Date associated with the represented feature or source record. |
| `last_update_date` | `text` | Date associated with the represented feature or source record. |
| `entry_date` | `text` | Date associated with the represented feature or source record. |
| `id` | `bigint` | Count or numeric value for identifier in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
