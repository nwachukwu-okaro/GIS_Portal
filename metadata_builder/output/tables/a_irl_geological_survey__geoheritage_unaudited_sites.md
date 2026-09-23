# Geoheritage Unaudited Sites

## Overview

- **Identifier:** `a_irl_geological_survey/geoheritage_unaudited_sites`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.549891, 51.769375, -9.211730, 52.574371]`
- **Topic category:** geoscientificInformation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_geological_survey`
- **Table:** `geoheritage_unaudited_sites`
- **Geometry:** POLYGON
- **CRS:** EPSG:2157
- **Rows:** 116
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Geoheritage Unaudited Sites is an authoritative dataset published by Geological Survey Ireland. It represents geoheritage unaudited sites features using polygon geometry.

## Lineage

Published by Geological Survey Ireland as open geological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `gus_id` | `integer` | Identifier assigned by the source dataset. |
| `site_name` | `varchar(100)` | Name associated with the represented feature. |
| `theme` | `varchar(10)` |  |
| `county` | `varchar(50)` |  |
| `features` | `varchar(255)` |  |
| `townland` | `varchar(255)` |  |
| `description` | `varchar(255)` |  |
| `references` | `varchar(255)` |  |
| `designat` | `varchar(50)` |  |
| `x_ig` | `integer` |  |
| `y_ig` | `integer` |  |
| `x_itm` | `double precision` |  |
| `y_itm` | `double precision` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
