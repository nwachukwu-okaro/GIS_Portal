# Blue Green Infra Heat Mitigation Lsoa Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Heat_Mitigation_LSOA_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418942, 49.864636, 1.768912, 55.811660]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Heat_Mitigation_LSOA_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 32844
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Blue Green Infra Heat Mitigation Lsoa Ogl is an authoritative dataset published by Natural England. It represents blue green infra heat mitigation lsoa ogl features using multipolygon geometry.

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
| `code` | `varchar(9)` | Count or numeric value for code in the represented area. |
| `name` | `varchar(254)` | Official or publisher-assigned name of the represented feature. |
| `label` | `varchar(36)` | Publisher-supplied label for the represented feature or record. |
| `area` | `integer` | Numeric area value recorded for the feature. |
| `mean` | `double precision` | Count or numeric value for mean in the represented area. |
| `provision` | `double precision` | Count or numeric value for provision in the represented area. |
| `need` | `double precision` | Count or numeric value for need in the represented area. |
| `lackprov` | `double precision` | Count or numeric value for lackprov in the represented area. |
| `zpriority` | `double precision` | Count or numeric value for zpriority in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
