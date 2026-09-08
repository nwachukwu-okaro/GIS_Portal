# Boundary Datazone2022

## Overview

- **Identifier:** `a_nrs_scotland/boundary_datazone2022`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.650007, 54.633240, -0.724609, 60.860766]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_datazone2022`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 7392
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Boundary Datazone2022 is an authoritative dataset published by National Records of Scotland. It represents boundary datazone2022 features using multipolygon geometry.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `dzcode` | `varchar(254)` | Publisher-assigned dzcode for the record. |
| `dzname` | `varchar(254)` | Publisher-supplied dzname for the represented feature or record. |
| `totpop2022` | `double precision` |  |
| `hhres2022` | `double precision` |  |
| `hhcnt2022` | `double precision` |  |
| `stdareaha` | `double precision` | Numeric stdareaha value recorded for the feature. |
| `stdareakm2` | `double precision` |  |
| `st_area_sh` | `double precision` | Numeric st area sh value recorded for the feature. |
| `st_length_` | `double precision` | Numeric st length value recorded for the feature. |
