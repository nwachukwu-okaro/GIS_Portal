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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
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
| `adiministrative_authority` | `varchar` | Publisher-supplied adiministrative authority for the represented feature or record. |
| `registration_no` | `varchar` | Publisher-supplied registration number for the represented feature or record. |
| `building_name` | `varchar` | Name associated with the represented feature. |
| `address` | `varchar` | Publisher-supplied address for the represented feature or record. |
| `county` | `varchar` | Publisher-supplied county for the represented feature or record. |
| `eircode` | `varchar` | Publisher-assigned eircode for the record. |
| `building_type` | `varchar` | Publisher-supplied building type for the represented feature or record. |
| `description` | `varchar` | Publisher-supplied description for the represented feature or record. |
| `appraisal` | `varchar` | Publisher-supplied appraisal for the represented feature or record. |
| `current_use` | `varchar` | Publisher-supplied current use for the represented feature or record. |
| `niah_number` | `varchar` | Publisher-supplied niah number for the represented feature or record. |
| `rmp_number` | `varchar` | Publisher-supplied rmp number for the represented feature or record. |
| `date_registered` | `bigint` | Count or numeric value for date registered in the represented area. |
| `latitude` | `double precision` | Latitude coordinate, normally expressed in decimal degrees. |
| `longitude` | `double precision` | Longitude coordinate, normally expressed in decimal degrees. |
| `global_id` | `varchar` | Identifier assigned by the source dataset. |
| `object_id` | `integer` | Identifier assigned by the source dataset. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
