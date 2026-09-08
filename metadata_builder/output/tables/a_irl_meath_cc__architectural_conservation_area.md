# Architectural Conservation Area

## Overview

- **Identifier:** `a_irl_meath_cc/architectural_conservation_area`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.167175, 53.418413, -6.238061, 53.792893]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_meath_cc`
- **Table:** `architectural_conservation_area`
- **Geometry:** POLYGON
- **CRS:** EPSG:2157
- **Rows:** 23
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Architectural Conservation Area is an authoritative dataset published by Meath County Council. It represents architectural conservation area features using polygon geometry.

## Lineage

Published by Meath County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `aca_pk` | `integer` | Count or numeric value for aca pk in the represented area. |
| `aca` | `varchar(100)` | Publisher-supplied aca for the represented feature or record. |
| `plan_name` | `varchar(120)` | Name associated with the represented feature. |
| `map_label` | `varchar(100)` | Publisher-supplied map label for the represented feature or record. |
| `more_information` | `varchar(254)` | Publisher-supplied more information for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
