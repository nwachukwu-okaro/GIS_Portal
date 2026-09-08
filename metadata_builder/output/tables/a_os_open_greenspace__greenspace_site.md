# Greenspace Site

## Overview

- **Identifier:** `a_os_open_greenspace/greenspace_site`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Greenspace
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-greenspace
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.574607, 49.893017, 1.761148, 60.804777]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_open_greenspace`
- **Table:** `greenspace_site`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 165978
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Greenspace Site is part of OS Open Greenspace, published by Ordnance Survey. It represents greenspace site features using multipolygon geometry.

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
| `function` | `varchar` | Publisher-supplied function for the represented feature or record. |
| `distinctive_name_1` | `varchar` | Publisher-supplied distinctive name 1 for the represented feature or record. |
| `distinctive_name_2` | `varchar` | Publisher-supplied distinctive name 2 for the represented feature or record. |
| `distinctive_name_3` | `varchar` | Publisher-supplied distinctive name 3 for the represented feature or record. |
| `distinctive_name_4` | `varchar` | Publisher-supplied distinctive name 4 for the represented feature or record. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
