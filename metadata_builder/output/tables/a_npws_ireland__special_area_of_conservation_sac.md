# Special Area Of Conservation Sac

## Overview

- **Identifier:** `a_npws_ireland/special_area_of_conservation_sac`
- **Source organisation:** National Parks and Wildlife Service Ireland
- **Source:** https://www.npws.ie/maps-and-data
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.691667, 51.410000, -5.591380, 55.471236]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_npws_ireland`
- **Table:** `special_area_of_conservation_sac`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 433
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Special Area Of Conservation Sac is an authoritative dataset published by National Parks and Wildlife Service Ireland. It represents special area of conservation sac features using multipolygon geometry.

## Lineage

Published by the National Parks and Wildlife Service Ireland as open protected-areas data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `sitecode` | `varchar(6)` | Publisher-assigned sitecode for the record. |
| `site_name` | `varchar(100)` | Name associated with the represented feature. |
| `version` | `double precision` | Count or numeric value for version in the represented area. |
| `county` | `varchar(50)` | Publisher-supplied county for the represented feature or record. |
| `ha` | `double precision` | Count or numeric value for ha in the represented area. |
| `source_crs` | `varchar(254)` | Publisher-supplied source crs for the represented feature or record. |
| `sourcscale` | `varchar(50)` | Publisher-supplied sourcscale for the represented feature or record. |
| `url` | `varchar(50)` | Publisher-supplied url for the represented feature or record. |
