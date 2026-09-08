# Roads National

## Overview

- **Identifier:** `a_os_zoomstack/roads_national`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Zoomstack
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-zoomstack
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-6.376816, 50.091927, 1.756298, 58.612378]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_zoomstack`
- **Table:** `roads_national`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 123341
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Roads National is part of OS Open Zoomstack, published by Ordnance Survey. It represents roads national features using multilinestring geometry.

## Lineage

Published by Ordnance Survey as part of OS Open Zoomstack. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `type` | `varchar` | Publisher-supplied type for the represented feature or record. |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `number` | `varchar` | Publisher-supplied number for the represented feature or record. |
| `level` | `integer` | Count or numeric value for level in the represented area. |
| `id` | `integer` | Count or numeric value for identifier in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
