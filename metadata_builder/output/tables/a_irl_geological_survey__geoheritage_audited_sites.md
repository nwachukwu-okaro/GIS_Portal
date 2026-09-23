# Geoheritage Audited Sites

## Overview

- **Identifier:** `a_irl_geological_survey/geoheritage_audited_sites`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.302365, 51.448601, -5.994569, 55.451694]`
- **Topic category:** geoscientificInformation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_geological_survey`
- **Table:** `geoheritage_audited_sites`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 1148
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

Geoheritage Audited Sites is an authoritative dataset published by Geological Survey Ireland. It represents geoheritage audited sites features using multipolygon geometry.

## Lineage

Published by Geological Survey Ireland as open geological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `gas_id` | `integer` | Identifier assigned by the source dataset. |
| `sitecode` | `varchar(7)` |  |
| `sitename` | `varchar(75)` |  |
| `igh1` | `varchar(5)` |  |
| `igh2` | `varchar(5)` |  |
| `igh3` | `varchar(5)` |  |
| `igh4` | `varchar(5)` |  |
| `county` | `varchar(25)` |  |
| `description` | `varchar(200)` |  |
| `geological` | `varchar(254)` |  |
| `designat` | `varchar(50)` |  |
| `report` | `varchar(200)` |  |
| `x_ig` | `integer` |  |
| `y_ig` | `integer` |  |
| `x_itm` | `double precision` |  |
| `y_itm` | `double precision` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
