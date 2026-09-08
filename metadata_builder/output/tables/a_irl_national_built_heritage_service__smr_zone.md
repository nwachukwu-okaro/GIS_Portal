# Smr Zone

## Overview

- **Identifier:** `a_irl_national_built_heritage_service/smr_zone`
- **Source organisation:** National Built Heritage Service
- **Source:** https://www.buildingsofireland.ie/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-15.923815, 31.172954, 172.617639, 64.210928]`
- **Topic category:** society
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_national_built_heritage_service`
- **Table:** `smr_zone`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 82731
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

Smr Zone is an authoritative dataset published by National Built Heritage Service. It represents smr zone features using multipolygon geometry.

## Lineage

Published by the National Built Heritage Service as open heritage data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `zone_id` | `varchar` | Identifier assigned by the source dataset. |
| `smrz_pk` | `integer` | Count or numeric value for smrz pk in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
