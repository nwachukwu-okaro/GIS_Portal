# Record Of Protected Structures

## Overview

- **Identifier:** `a_irl_mayo_cc/record_of_protected_structures`
- **Source organisation:** Mayo County Council
- **Source:** https://data.gov.ie/organization/mayo-county-council
- **Geographic coverage:** County Mayo
- **WGS84 extent:** `[-10.082216, 53.487135, -8.697148, 54.299548]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_irl_mayo_cc`
- **Table:** `record_of_protected_structures`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 273
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

Record Of Protected Structures is an authoritative dataset published by Mayo County Council. It represents record of protected structures features using point geometry.

## Lineage

Published by Mayo County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `object_id` | `integer` | Identifier assigned by the source dataset. |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
