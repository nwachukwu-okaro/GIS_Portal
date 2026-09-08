# Source Protection Zone

## Overview

- **Identifier:** `a_environment_agency/source_protection_zone`
- **Source organisation:** Environment Agency
- **Source:** https://environment.data.gov.uk/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.358951, 49.889744, 1.741691, 55.770821]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_environment_agency`
- **Table:** `source_protection_zone`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 4686
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

version: 20260306
Source: https://environment.data.gov.uk/dataset/6fd0120f-d465-11e4-abee-f0def148f590 https://environment.data.gov.uk/spatialdata/source-protection-zones-merged/wfs

Attribution: © Environment Agency copyright and/or database right 2016. All rights reserved.

## Lineage

Published by Environment Agency as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `gml_id` | `varchar(35)` | Identifier assigned by the source dataset. |
| `gml_original_coordinate_system` | `varchar(45)` |  |
| `gml_parent_property` | `varchar(13)` |  |
| `number` | `varchar(2)` |  |
| `spz_pk` | `integer` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
