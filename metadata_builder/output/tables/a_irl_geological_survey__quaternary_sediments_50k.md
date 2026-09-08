# Quaternary Sediments 50k

## Overview

- **Identifier:** `a_irl_geological_survey/quaternary_sediments_50k`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.462670, 51.480004, -6.095197, 55.050588]`
- **Topic category:** geoscientificInformation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_geological_survey`
- **Table:** `quaternary_sediments_50k`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 2000
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Quaternary Sediments 50k is an authoritative dataset published by Geological Survey Ireland. It represents quaternary sediments 50k features using multipolygon geometry.

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
| `qsed_type` | `varchar` |  |
| `qsed_code` | `varchar` | Code assigned by the source dataset. |
| `legend_desc` | `varchar` |  |
| `global_id` | `varchar` | Identifier assigned by the source dataset. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
