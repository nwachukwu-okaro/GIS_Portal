# Groundwater Vunerability40k

## Overview

- **Identifier:** `a_irl_geological_survey/groundwater_vunerability40k`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.469285, 51.428451, -5.998674, 55.381240]`
- **Topic category:** geoscientificInformation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_geological_survey`
- **Table:** `groundwater_vunerability40k`
- **Geometry:** POLYGON
- **CRS:** EPSG:2157
- **Rows:** 35000
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Groundwater Vunerability40k is an authoritative dataset published by Geological Survey Ireland. It represents groundwater vunerability40k features using polygon geometry.

## Lineage

Published by Geological Survey Ireland as open geological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `gwv_pk` | `integer` | Primary-key identifier for records in groundwater_vunerability40k. |
| `vul40kid` | `varchar(25)` |  |
| `vul_category` | `varchar(10)` |  |
| `vul_description` | `varchar(40)` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
