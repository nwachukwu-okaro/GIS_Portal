# Proposed Natural Heritage Area

## Overview

- **Identifier:** `a_npws_ireland/proposed_natural_heritage_area`
- **Source organisation:** National Parks and Wildlife Service Ireland
- **Source:** https://www.npws.ie/maps-and-data
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.549752, 51.418022, -5.990496, 55.449214]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_npws_ireland`
- **Table:** `proposed_natural_heritage_area`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 1180
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Proposed Natural Heritage Area is an authoritative dataset published by National Parks and Wildlife Service Ireland. It represents proposed natural heritage area features using multipolygon geometry.

## Lineage

Published by the National Parks and Wildlife Service Ireland as open protected-areas data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Primary-key identifier for records in proposed_natural_heritage_area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `sitecode` | `varchar(6)` |  |
| `site_name` | `varchar(100)` | Name associated with the represented feature. |
| `county` | `varchar(2)` |  |
| `version` | `double precision` |  |
| `ha` | `double precision` |  |
| `source_crs` | `varchar(254)` |  |
| `sourcscale` | `varchar(50)` |  |
| `url` | `varchar(50)` |  |
