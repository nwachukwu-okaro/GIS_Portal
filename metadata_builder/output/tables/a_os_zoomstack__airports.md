# Airports

## Overview

- **Identifier:** `a_os_zoomstack/airports`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Zoomstack
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-zoomstack
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.448727, 49.913600, 1.282248, 60.191828]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_os_zoomstack`
- **Table:** `airports`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 45
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

Airports is part of OS Open Zoomstack, published by Ordnance Survey. It represents airports features using multipoint geometry.

## Lineage

Published by Ordnance Survey as part of OS Open Zoomstack. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `id` | `integer` | Count or numeric value for identifier in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
