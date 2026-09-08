# Landscape Character Area

## Overview

- **Identifier:** `a_irl_meath_cc/landscape_character_area`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.342768, 53.381706, -6.211721, 53.917564]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_meath_cc`
- **Table:** `landscape_character_area`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 20
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Landscape Character Area is an authoritative dataset published by Meath County Council. It represents landscape character area features using multipolygon geometry.

## Lineage

Published by Meath County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `lca_pk` | `integer` | Count or numeric value for lca pk in the represented area. |
| `description` | `varchar(50)` | Publisher-supplied description for the represented feature or record. |
| `character` | `varchar(100)` | Publisher-supplied character for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
