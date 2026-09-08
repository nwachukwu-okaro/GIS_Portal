# Bedrock Aquifers 100k

## Overview

- **Identifier:** `a_irl_geological_survey/bedrock_aquifers_100k`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.663500, 51.389411, -5.994603, 55.384017]`
- **Topic category:** geoscientificInformation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_geological_survey`
- **Table:** `bedrock_aquifers_100k`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 2000
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Bedrock Aquifers 100k is an authoritative dataset published by Geological Survey Ireland. It represents bedrock aquifers 100k features using multipolygon geometry.

## Lineage

Published by Geological Survey Ireland as open geological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `object_id` | `integer` | Identifier assigned by the source dataset. |
| `aquifer_cat` | `varchar` |  |
| `aquifer_des` | `varchar` |  |
| `area_km2` | `double precision` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
