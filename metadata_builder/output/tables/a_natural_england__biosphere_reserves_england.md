# Biosphere Reserves England

## Overview

- **Identifier:** `a_natural_england/biosphere_reserves_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-4.889167, 50.553811, 0.096717, 51.292573]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `biosphere_reserves_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 3
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

version: 20251009
Source: https://naturalengland-defra.opendata.arcgis.com/datasets/Defra::biosphere-reserves-england/about

Attribution: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year]. Attribution statement: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year].

## Lineage

Published by Natural England as open environmental and conservation data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `status` | `varchar` | Publisher-supplied status for the represented feature or record. |
| `area` | `real` | Numeric area value recorded for the feature. |
| `globalid` | `varchar` | Publisher-assigned globalid for the record. |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
