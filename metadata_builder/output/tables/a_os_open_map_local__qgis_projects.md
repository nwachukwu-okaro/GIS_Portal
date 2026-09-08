# Qgis Projects

## Overview

- **Identifier:** `a_os_open_map_local/qgis_projects`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Map Local
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-map-local
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **Topic category:** imageryBaseMapsEarthCover
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_os_open_map_local`
- **Table:** `qgis_projects`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

Qgis Projects is part of OS Open Map Local, published by Ordnance Survey. It contains records relating to qgis projects.

## Lineage

Published by Ordnance Survey as part of OS Open Map Local. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `name` | `text` | Official or publisher-assigned name of the represented feature. |
| `metadata` | `jsonb` | Publisher-supplied metadata for the represented feature or record. |
| `content` | `bytea` | Publisher-supplied content for the represented feature or record. |
