# National Inventory Of Architectural Inventory

## Overview

- **Identifier:** `a_irl_national_built_heritage_service/national_inventory_of_architectural_inventory`
- **Source organisation:** National Built Heritage Service
- **Source:** https://www.buildingsofireland.ie/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.514248, 51.413382, 169.323852, 78.263859]`
- **Topic category:** society
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_irl_national_built_heritage_service`
- **Table:** `national_inventory_of_architectural_inventory`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 43322
- **Columns:** 22
- **Metadata status:** source_mapped

## Description

National Inventory Of Architectural Inventory is an authoritative dataset published by National Built Heritage Service. It represents national inventory of architectural inventory features using point geometry.

## Lineage

Published by the National Built Heritage Service as open heritage data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `reg_no` | `bigint` |  |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `number` | `varchar` |  |
| `street1` | `varchar` |  |
| `street2` | `varchar` |  |
| `town` | `varchar` |  |
| `townland` | `varchar` |  |
| `county` | `varchar` |  |
| `county_id` | `varchar` | Identifier assigned by the source dataset. |
| `planauth` | `varchar` |  |
| `composition` | `varchar` |  |
| `appraisal` | `varchar` |  |
| `datefrom` | `bigint` |  |
| `dateto` | `bigint` |  |
| `rating` | `varchar` |  |
| `original_type` | `varchar` |  |
| `image_link` | `varchar` |  |
| `website_link` | `varchar` |  |
| `survey_id` | `varchar` | Identifier assigned by the source dataset. |
| `niah_area` | `varchar` |  |
| `niah_pk` | `integer` | Primary-key identifier for records in national_inventory_of_architectural_inventory. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
