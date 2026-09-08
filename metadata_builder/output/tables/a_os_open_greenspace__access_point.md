# Access Point

## Overview

- **Identifier:** `a_os_open_greenspace/access_point`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Greenspace
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-greenspace
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.566909, 49.893298, 1.760894, 60.804307]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_os_open_greenspace`
- **Table:** `access_point`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 355705
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Access Point is part of OS Open Greenspace, published by Ordnance Survey. It represents access point features using point geometry.

## Lineage

Published by Ordnance Survey as part of OS Open Greenspace. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. |
| `access_type` | `varchar` | Publisher-supplied access type for the represented feature or record. |
| `ref_to_greenspace_site` | `varchar` | Publisher-supplied reference to greenspace site for the represented feature or record. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
