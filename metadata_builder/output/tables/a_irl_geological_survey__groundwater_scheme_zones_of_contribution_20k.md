# Groundwater Scheme Zones Of Contribution 20k

## Overview

- **Identifier:** `a_irl_geological_survey/groundwater_scheme_zones_of_contribution_20k`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.046017, 51.626105, -6.017837, 55.327257]`
- **Topic category:** geoscientificInformation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_geological_survey`
- **Table:** `groundwater_scheme_zones_of_contribution_20k`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 254
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Groundwater Scheme Zones Of Contribution 20k is an authoritative dataset published by Geological Survey Ireland. It represents groundwater scheme zones of contribution 20k features using multipolygon geometry.

## Lineage

Published by Geological Survey Ireland as open geological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `gwsz_pk` | `integer` | Count or numeric value for gwsz pk in the represented area. |
| `gws_zoc_id` | `varchar(25)` | Identifier assigned by the source dataset. |
| `gws_name` | `varchar(50)` | Name associated with the represented feature. |
| `year` | `integer` | Count or numeric value for year in the represented area. |
| `consultant` | `varchar(50)` | Publisher-supplied consultant for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
