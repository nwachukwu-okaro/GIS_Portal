# Rail

## Overview

- **Identifier:** `a_os_zoomstack/rail`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Zoomstack
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-zoomstack
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-6.145539, 50.120798, 1.749664, 60.424421]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_zoomstack`
- **Table:** `rail`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 115413
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

Rail is part of OS Open Zoomstack, published by Ordnance Survey. It represents rail features using multilinestring geometry.

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
| `id` | `integer` | Count or numeric value for identifier in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
