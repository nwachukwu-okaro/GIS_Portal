# Boundary Output Area2022

## Overview

- **Identifier:** `a_nrs_scotland/boundary_output_area2022`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.649996, 54.633220, -0.724450, 60.860787]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_output_area2022`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 46363
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Boundary Output Area2022 is an authoritative dataset published by National Records of Scotland. It represents boundary output area2022 features using geometry geometry.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `code` | `varchar(9)` | Publisher-assigned code for the record. |
| `hhcount` | `integer` | Count or numeric value for hhcount in the represented area. |
| `popcount` | `integer` | Count or numeric value for popcount in the represented area. |
| `council` | `varchar(9)` | Publisher-supplied council for the represented feature or record. |
| `sqkm` | `double precision` |  |
| `hect` | `double precision` | Count or numeric value for hect in the represented area. |
| `masterpc` | `varchar(9)` | Publisher-supplied masterpc for the represented feature or record. |
| `easting` | `varchar(6)` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `varchar(7)` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `shape_leng` | `double precision` | Count or numeric value for shape leng in the represented area. |
| `shape_area` | `double precision` | Numeric shape area value recorded for the feature. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
