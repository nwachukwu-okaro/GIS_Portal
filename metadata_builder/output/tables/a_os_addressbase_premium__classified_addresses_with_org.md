# Classified Addresses With Org

## Overview

- **Identifier:** `a_os_addressbase_premium/classified_addresses_with_org`
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
- **Table:** `classified_addresses_with_org`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 41546546
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Classified Addresses With Org is part of AddressBase Premium, published by Ordnance Survey. It represents classified addresses with org features using geometry geometry.

## Lineage

Published by Ordnance Survey as part of AddressBase Premium. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `uprn` | `bigint` | Count or numeric value for uprn in the represented area. |
| `ctyua24nm` | `varchar(36)` |  |
| `classification_code` | `text` | Code assigned by the source dataset. |
| `organisation` | `text` | Publisher-supplied organisation for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
