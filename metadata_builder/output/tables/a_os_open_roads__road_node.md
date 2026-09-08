# Road Node

## Overview

- **Identifier:** `a_os_open_roads/road_node`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Roads
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-roads
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.584537, 49.891062, 1.762169, 60.827676]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_os_open_roads`
- **Table:** `road_node`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 3346499
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Road Node is part of OS Open Roads, published by Ordnance Survey. It represents road node features using point geometry.

## Lineage

Published by Ordnance Survey as part of OS Open Roads. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `text` | Publisher-assigned identifier for the record. |
| `form_of_road_node` | `text` | Publisher-supplied form of road node for the represented feature or record. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
