# Landscape Sensitivity Ratings Cdp 2022 2028

## Overview

- **Identifier:** `a_irl_galway_cc/landscape_sensitivity_ratings_cdp_2022_2028`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.302290, 52.968151, -7.967334, 53.718912]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_galway_cc`
- **Table:** `landscape_sensitivity_ratings_cdp_2022_2028`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 49
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Landscape Sensitivity Ratings Cdp 2022 2028 is an authoritative dataset published by Galway County Council. It represents landscape sensitivity ratings cdp 2022 2028 features using multipolygon geometry.

## Lineage

Published by Galway County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `object_id` | `smallint` | Identifier assigned by the source dataset. |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `unit` | `varchar` | Publisher-supplied unit for the represented feature or record. |
| `sensitivit` | `varchar` | Publisher-supplied sensitivit for the represented feature or record. |
| `value` | `smallint` | Count or numeric value for value in the represented area. |
| `urban_name` | `varchar` | Name associated with the represented feature. |
| `urban_source` | `varchar` | Publisher-supplied urban source for the represented feature or record. |
| `lsr_pk` | `integer` | Count or numeric value for lsr pk in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
