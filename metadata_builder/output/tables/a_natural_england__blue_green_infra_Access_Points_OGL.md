# Blue Green Infra Access Points Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Access_Points_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.351368, 49.893298, 1.758079, 55.787125]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Access_Points_OGL`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 333676
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Blue Green Infra Access Points Ogl is an authoritative dataset published by Natural England. It represents blue green infra access points ogl features using multipoint geometry.

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
| `accesstype` | `varchar(255)` | Publisher-supplied accesstype for the represented feature or record. |
| `accessible_for` | `varchar(255)` | Publisher-supplied accessible for for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
