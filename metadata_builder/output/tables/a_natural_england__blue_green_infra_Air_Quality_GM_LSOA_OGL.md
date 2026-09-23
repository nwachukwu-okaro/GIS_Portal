# Blue Green Infra Air Quality Gm Lsoa Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Air_Quality_GM_LSOA_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-2.730524, 53.327304, -1.909622, 53.685719]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Air_Quality_GM_LSOA_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1673
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Blue Green Infra Air Quality Gm Lsoa Ogl is an authoritative dataset published by Natural England. It represents blue green infra air quality gm lsoa ogl features using multipolygon geometry.

## Lineage

Published by Natural England as open environmental and conservation data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `code` | `varchar(9)` |  |
| `name` | `varchar(254)` | Official or publisher-assigned name of the represented feature. |
| `provision` | `double precision` |  |
| `need` | `double precision` |  |
| `lackprov` | `double precision` |  |
| `zpriority` | `double precision` |  |
| `sumpm25kg` | `double precision` |  |
| `areakm` | `double precision` |  |
| `pm25kgkm2` | `double precision` |  |
| `pm25ugm3` | `double precision` |  |
| `zscoreaqprov` | `double precision` |  |
| `zaqneed` | `double precision` |  |
| `zsocneed` | `double precision` |  |
| `zneedcomb` | `double precision` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
