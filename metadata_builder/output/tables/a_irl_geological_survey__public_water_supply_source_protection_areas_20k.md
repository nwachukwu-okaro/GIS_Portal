# Public Water Supply Source Protection Areas 20k

## Overview

- **Identifier:** `a_irl_geological_survey/public_water_supply_source_protection_areas_20k`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.812542, 51.658715, -6.146651, 55.287975]`
- **Topic category:** geoscientificInformation
- **Temporal extent:** 1995-12-01 to 2017-03-01
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_geological_survey`
- **Table:** `public_water_supply_source_protection_areas_20k`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 357
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Public Water Supply Source Protection Areas 20k is an authoritative dataset published by Geological Survey Ireland. It represents public water supply source protection areas 20k features using multipolygon geometry.

## Lineage

Published by Geological Survey Ireland as open geological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `pwsspa_pk` | `integer` | Count or numeric value for pwsspa pk in the represented area. |
| `spa_id` | `varchar(25)` | Identifier assigned by the source dataset. |
| `spa_code` | `varchar(10)` | Code assigned by the source dataset. |
| `spa_name` | `varchar(150)` | Name associated with the represented feature. |
| `datasource` | `varchar(10)` | Publisher-supplied datasource for the represented feature or record. |
| `dw_code` | `varchar(15)` | Code assigned by the source dataset. |
| `eu_report` | `varchar(20)` | Publisher-supplied eu report for the represented feature or record. |
| `county` | `varchar(20)` | Publisher-supplied county for the represented feature or record. |
| `report_url` | `varchar(254)` | Publisher-supplied report url for the represented feature or record. |
| `rep_creator` | `varchar(50)` | Publisher-supplied rep creator for the represented feature or record. |
| `active` | `varchar(20)` | Publisher-supplied active for the represented feature or record. |
| `gsi_review` | `varchar(10)` | Publisher-supplied gsi review for the represented feature or record. |
| `publish` | `varchar(10)` | Publisher-supplied publish for the represented feature or record. |
| `reportdate` | `date` | Date or year recorded for reportdate. |
| `updatedate` | `date` | Date or year recorded for updatedate. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
