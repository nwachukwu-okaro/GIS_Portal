# Watercourse Link

## Overview

- **Identifier:** `a_os_open_rivers/watercourse_link`
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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_open_rivers`
- **Table:** `watercourse_link`
- **Geometry:** LINESTRING
- **CRS:** EPSG:27700
- **Rows:** 193040
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Watercourse Link is part of OS Open Rivers, published by Ordnance Survey. It represents watercourse link features using linestring geometry.

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
| `flow_direction` | `varchar` | Publisher-supplied flow direction for the represented feature or record. |
| `length` | `real` | Numeric length value recorded for the feature. |
| `fictitious` | `varchar` | Publisher-supplied fictitious for the represented feature or record. |
| `form` | `varchar` | Publisher-supplied form for the represented feature or record. |
| `watercourse_name` | `varchar` | Name associated with the represented feature. |
| `watercourse_name_alternative` | `varchar` | Publisher-supplied watercourse name alternative for the represented feature or record. |
| `start_node` | `varchar` | Publisher-supplied start node for the represented feature or record. |
| `end_node` | `varchar` | Publisher-supplied end node for the represented feature or record. |
| `fid` | `integer` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
