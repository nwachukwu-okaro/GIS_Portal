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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
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
| `theme` | `varchar(10)` | Publisher-supplied theme for the represented feature or record. |
| `county` | `varchar(50)` | Publisher-supplied county for the represented feature or record. |
| `features` | `varchar(255)` | Publisher-supplied features for the represented feature or record. |
| `townland` | `varchar(255)` | Publisher-supplied townland for the represented feature or record. |
| `description` | `varchar(255)` | Publisher-supplied description for the represented feature or record. |
| `references` | `varchar(255)` | Publisher-supplied references for the represented feature or record. |
| `designat` | `varchar(50)` | Publisher-supplied designat for the represented feature or record. |
| `x_ig` | `integer` | Count or numeric value for x ig in the represented area. |
| `y_ig` | `integer` | Count or numeric value for y ig in the represented area. |
| `x_itm` | `double precision` | Count or numeric value for x itm in the represented area. |
| `y_itm` | `double precision` | Count or numeric value for y itm in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
