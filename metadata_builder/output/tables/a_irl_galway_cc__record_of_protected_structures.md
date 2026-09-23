# Record Of Protected Structures

## Overview

- **Identifier:** `a_irl_galway_cc/record_of_protected_structures`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.233900, 52.984950, 8.225051, 53.705427]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_irl_galway_cc`
- **Table:** `record_of_protected_structures`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 1514
- **Columns:** 19
- **Metadata status:** source_mapped

## Description

Record Of Protected Structures is an authoritative dataset published by Galway County Council. It represents record of protected structures features using point geometry.

## Lineage

Published by Galway County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `administrative_authority_id` | `varchar` | Identifier assigned by the source dataset. |
| `adiministrative_authority` | `varchar` |  |
| `registration_no` | `varchar` |  |
| `building_name` | `varchar` | Name associated with the represented feature. |
| `address` | `varchar` |  |
| `county` | `varchar` |  |
| `eircode` | `varchar` |  |
| `building_type` | `varchar` |  |
| `description` | `varchar` |  |
| `appraisal` | `varchar` |  |
| `current_use` | `varchar` |  |
| `niah_number` | `varchar` |  |
| `rmp_number` | `varchar` |  |
| `date_registered` | `bigint` |  |
| `latitude` | `double precision` | Latitude coordinate, normally expressed in decimal degrees. |
| `longitude` | `double precision` | Longitude coordinate, normally expressed in decimal degrees. |
| `global_id` | `varchar` | Identifier assigned by the source dataset. |
| `object_id` | `integer` | Identifier assigned by the source dataset. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
