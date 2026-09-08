# River Waterbodies Active

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/river_waterbodies_active`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.468183, 51.450434, -6.005639, 55.380124]`
- **Topic category:** environment
- **Temporal extent:** 2019-11-20 to 2026-03-19
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `river_waterbodies_active`
- **Geometry:** MULTILINESTRINGM
- **CRS:** EPSG:29903
- **Rows:** 3208
- **Columns:** 45
- **Metadata status:** source_mapped

## Description

River Waterbodies Active is an authoritative dataset published by Environmental Protection Agency Ireland. It represents river waterbodies active features using multilinestringm geometry.

## Lineage

Published by the Environmental Protection Agency Ireland as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `eu_cd` | `varchar` |  |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `ms_cd` | `varchar` |  |
| `region_cd` | `varchar` |  |
| `ins_when` | `date` |  |
| `ins_by` | `varchar` |  |
| `basin_cd` | `varchar` |  |
| `lat` | `double precision` |  |
| `long` | `double precision` |  |
| `lengthkm` | `double precision` |  |
| `sub_cd` | `varchar` |  |
| `alt_eu_cd` | `varchar` |  |
| `alt_ms_cd` | `varchar` |  |
| `date_change` | `date` |  |
| `change` | `varchar` |  |
| `geology` | `integer` |  |
| `catchment_a` | `double precision` |  |
| `catchment_b` | `double precision` |  |
| `slope` | `double precision` |  |
| `altitude` | `double precision` |  |
| `water_manag` | `varchar` |  |
| `eden_entity` | `varchar` |  |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `canal` | `integer` |  |
| `transbound` | `integer` |  |
| `local_autho` | `varchar` |  |
| `modified` | `varchar` |  |
| `artificial` | `varchar` |  |
| `system` | `varchar` |  |
| `category` | `varchar` | Publisher-supplied category for the represented feature or record. |
| `type` | `varchar` | Publisher-supplied type for the represented feature or record. |
| `alt_cat` | `varchar` |  |
| `size_cat` | `varchar` |  |
| `dist_cd` | `varchar` |  |
| `protected_a` | `varchar` |  |
| `wise_refere` | `varchar` |  |
| `processing` | `varchar` |  |
| `intercalib` | `integer` |  |
| `hydrometri` | `varchar` |  |
| `stn_definin` | `varchar` |  |
| `donor_water` | `varchar` |  |
| `defining_ch` | `varchar` |  |
| `rwba_pk` | `integer` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
