# Blue Green Infra Sport Facilities Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Sport_Facilities_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.321213, 49.913103, 1.757088, 55.787087]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Sport_Facilities_OGL`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 44114
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Blue Green Infra Sport Facilities Ogl is an authoritative dataset published by Natural England. It represents blue green infra sport facilities ogl features using multipoint geometry.

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
| `site_name` | `varchar(254)` | Name associated with the represented feature. |
| `post_code` | `varchar(254)` | Code assigned by the source dataset. |
| `ownership` | `varchar(254)` | Publisher-supplied ownership for the represented feature or record. |
| `management` | `varchar(254)` | Publisher-supplied management for the represented feature or record. |
| `facility_type` | `varchar(255)` | Publisher-supplied facility type for the represented feature or record. |
| `access_group` | `varchar(255)` | Publisher-supplied access group for the represented feature or record. |
| `access_type` | `varchar(255)` | Publisher-supplied access type for the represented feature or record. |
| `lsoa_code` | `varchar(255)` | Code assigned by the source dataset. |
| `msoa_code` | `varchar(255)` | Code assigned by the source dataset. |
| `local_authority_code` | `varchar(255)` | Code assigned by the source dataset. |
| `local_authority_name` | `varchar(255)` | Name associated with the represented feature. |
| `county_code` | `varchar(255)` | Code assigned by the source dataset. |
| `county_name` | `varchar(255)` | Name associated with the represented feature. |
| `site_id` | `integer` | Identifier assigned by the source dataset. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
