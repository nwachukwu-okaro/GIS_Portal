# Green Belt

## Overview

- **Identifier:** `a_os_open_data/green_belt`
- **Source organisation:** Ordnance Survey
- **Product:** OS OpenData
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-data
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-3.199715, 50.679562, 0.866302, 55.274430]`
- **Topic category:** imageryBaseMapsEarthCover
- **Temporal extent:** 2019-12-01 to 2025-12-01
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_open_data`
- **Table:** `green_belt`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 190
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Green Belt is part of OS OpenData, published by Ordnance Survey. It represents green belt features using multipolygon geometry.

## Lineage

Published by Ordnance Survey as part of OS OpenData. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Primary-key identifier for records in green_belt. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `dataset` | `varchar` |  |
| `end-date` | `varchar` |  |
| `entity` | `varchar` |  |
| `entry-date` | `date` |  |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `organisation-entity` | `varchar` |  |
| `prefix` | `varchar` |  |
| `quality` | `varchar` |  |
| `reference` | `varchar` |  |
| `start-date` | `varchar` |  |
| `typology` | `varchar` |  |
| `green-belt-core` | `varchar` |  |
| `local-authority-district` | `varchar` |  |
