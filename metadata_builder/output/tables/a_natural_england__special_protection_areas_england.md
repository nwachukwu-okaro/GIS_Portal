# Special Protection Areas England

## Overview

- **Identifier:** `a_natural_england/special_protection_areas_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.458328, 49.854235, 2.305270, 55.754242]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `special_protection_areas_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1079
- **Columns:** 21
- **Metadata status:** source_mapped

## Description

Special Protection Areas England is an authoritative dataset published by Natural England. It represents special protection areas england features using multipolygon geometry.

## Lineage

Published by Natural England as open environmental and conservation data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Primary-key identifier for records in special_protection_areas_england. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `spa_name` | `varchar(120)` | Name associated with the represented feature. |
| `spa_code` | `varchar(12)` | Code assigned by the source dataset. |
| `spa_area` | `double precision` |  |
| `grid_ref` | `varchar(8)` |  |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `latitude` | `varchar(12)` | Latitude coordinate, normally expressed in decimal degrees. |
| `longitude` | `varchar(12)` | Longitude coordinate, normally expressed in decimal degrees. |
| `name` | `varchar(80)` | Official or publisher-assigned name of the represented feature. |
| `status` | `varchar(32)` |  |
| `file` | `varchar(20)` |  |
| `area` | `double precision` |  |
| `easting0` | `double precision` |  |
| `northing0` | `double precision` |  |
| `gis_date` | `varchar(20)` | Date associated with the represented feature or source record. |
| `version` | `integer` |  |
| `shape_length` | `double precision` |  |
| `shape_area` | `double precision` |  |
