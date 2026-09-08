# Nhs Hospitals Medical Facilities

## Overview

- **Identifier:** `a_os_addressbase_premium/nhs_hospitals_medical_facilities`
- **Source organisation:** Ordnance Survey
- **Product:** AddressBase Premium
- **Source:** https://www.ordnancesurvey.co.uk/products/addressbase-premium
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-6.362094, 50.230649, 1.752721, 58.963640]`
- **Topic category:** location
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_addressbase_premium`
- **Table:** `nhs_hospitals_medical_facilities`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 3153
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Nhs Hospitals Medical Facilities is part of AddressBase Premium, published by Ordnance Survey. It represents nhs hospitals medical facilities features using geometry geometry.

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
| `nhs_category` | `text` | Publisher-supplied nhs category for the represented feature or record. |
