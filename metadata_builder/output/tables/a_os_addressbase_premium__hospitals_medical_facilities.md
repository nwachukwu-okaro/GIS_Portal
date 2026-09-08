# Hospitals Medical Facilities

## Overview

- **Identifier:** `a_os_addressbase_premium/hospitals_medical_facilities`
- **Source organisation:** Ordnance Survey
- **Product:** AddressBase Premium
- **Source:** https://www.ordnancesurvey.co.uk/products/addressbase-premium
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.365395, 50.099682, 1.754639, 58.983653]`
- **Topic category:** location
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_addressbase_premium`
- **Table:** `hospitals_medical_facilities`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 13169
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Hospitals Medical Facilities is part of AddressBase Premium, published by Ordnance Survey. It represents hospitals medical facilities features using geometry geometry.

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
