# UK Land 2024

## Overview

- **Identifier:** `a_verisk_sample/uk_land_2024`
- **Source organisation:** Verisk
- **Source:** https://www.verisk.com/en-gb/
- **WGS84 extent:** `[-2.730521, 53.327298, -1.909622, 53.685719]`
- **Topic category:** planningCadastre
- **Temporal extent:** 2024-05-31 to 2024-05-31
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_verisk_sample`
- **Table:** `uk_land_2024`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 31863
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

UK Land 2024 is an authoritative dataset published by Verisk. It represents uk land 2024 features using multipolygon geometry.

## Lineage

Published by Verisk as commercial sample data. Confirm licence and permitted use before treating as production lineage. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `landuse_code` | `double precision` | Code assigned by the source dataset. |
| `landuse_text` | `text` | Publisher-supplied landuse text for the represented feature or record. |
| `high_level_landuse` | `text` | Publisher-supplied high level landuse for the represented feature or record. |
| `luid` | `text` | Publisher-assigned luid for the record. |
| `date_created` | `date` | Publisher-supplied date created for the represented feature or record. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
