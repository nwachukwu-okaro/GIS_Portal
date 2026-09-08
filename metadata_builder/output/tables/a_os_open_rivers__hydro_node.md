# Hydro Node

## Overview

- **Identifier:** `a_os_open_rivers/hydro_node`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Rivers
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-rivers
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.524879, 49.974616, 1.756276, 60.825228]`
- **Topic category:** inlandWaters
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_os_open_rivers`
- **Table:** `hydro_node`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 197734
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Hydro Node is part of OS Open Rivers, published by Ordnance Survey. It represents hydro node features using point geometry.

## Lineage

Published by Ordnance Survey as part of OS Open Rivers. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. |
| `hydro_node_category` | `varchar` | Publisher-supplied hydro node category for the represented feature or record. |
| `fid` | `integer` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
