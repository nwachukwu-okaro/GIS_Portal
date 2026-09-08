# Ground Waterbodies Active

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/ground_waterbodies_active`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.618876, 51.420165, -5.994737, 55.382938]`
- **Topic category:** environment
- **Temporal extent:** 2015-08-14 to 2019-12-18
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `ground_waterbodies_active`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29903
- **Rows:** 514
- **Columns:** 29
- **Metadata status:** source_mapped

## Description

Ground Waterbodies Active is an authoritative dataset published by Environmental Protection Agency Ireland. It represents ground waterbodies active features using multipolygon geometry.

## Lineage

Published by the Environmental Protection Agency Ireland as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `object_id` | `integer` | Identifier assigned by the source dataset. |
| `eu_cd` | `varchar` |  |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `ms_cd` | `varchar` |  |
| `region_cd` | `varchar` |  |
| `ins_when` | `date` |  |
| `ins_by` | `varchar` |  |
| `horizon` | `varchar` |  |
| `descrip` | `varchar` |  |
| `full_type` | `varchar` |  |
| `date_change` | `date` |  |
| `change` | `varchar` |  |
| `lat` | `double precision` |  |
| `lon` | `double precision` |  |
| `area_hectar` | `double precision` |  |
| `area_km2` | `double precision` |  |
| `eden_code` | `varchar` | Code assigned by the source dataset. |
| `transbound` | `integer` |  |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `horz_type` | `varchar` |  |
| `dist_cd` | `varchar` |  |
| `protected_a` | `varchar` |  |
| `out_of_rbd` | `varchar` |  |
| `local_autho` | `varchar` |  |
| `category` | `varchar` | Publisher-supplied category for the represented feature or record. |
| `shape_star` | `double precision` |  |
| `shape_stle` | `double precision` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
