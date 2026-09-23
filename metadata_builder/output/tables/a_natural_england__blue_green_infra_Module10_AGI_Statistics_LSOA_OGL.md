# Blue Green Infra Module10 Agi Statistics Lsoa Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Module10_AGI_Statistics_LSOA_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418601, 49.864674, 1.763680, 55.811091]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Module10_AGI_Statistics_LSOA_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 33755
- **Columns:** 72
- **Metadata status:** source_mapped

## Description

Blue Green Infra Module10 Agi Statistics Lsoa Ogl is an authoritative dataset published by Natural England. It represents blue green infra module10 agi statistics lsoa ogl features using multipolygon geometry.

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
| `lsoa21cd` | `varchar(255)` |  |
| `lsoa21nm` | `varchar(255)` |  |
| `globalid` | `varchar(255)` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `lad22cd` | `varchar(255)` |  |
| `lad22nm` | `varchar(255)` |  |
| `msoa21cd` | `varchar(255)` |  |
| `msoa21nm` | `varchar(255)` |  |
| `age_total_2021` | `integer` |  |
| `population_2021` | `integer` |  |
| `lnrs_id` | `varchar(255)` | Identifier assigned by the source dataset. |
| `lnrs_name` | `varchar(255)` | Name associated with the represented feature. |
| `oa_code` | `varchar(255)` | Code assigned by the source dataset. |
| `area_ha` | `double precision` | Area enclosed by the feature, measured in hectares. |
| `area_m` | `double precision` |  |
| `totalagi_area` | `double precision` |  |
| `totalagi_per1000pop` | `double precision` |  |
| `totalagi_limited_area` | `double precision` |  |
| `totalagi_limited_per1000pop` | `double precision` |  |
| `totalagilnr_area` | `double precision` |  |
| `totalagi_lnr_per1000pop` | `double precision` |  |
| `totalagi_accessland_area` | `double precision` |  |
| `totalagi_accessland_per1000pop` | `double precision` |  |
| `totalagi_coastalmargin_area` | `double precision` |  |
| `totalagi_coastalmargin_per1000p` | `double precision` |  |
| `gardenspace_totalarea_m` | `double precision` |  |
| `gardenspace_totalarea_ha` | `double precision` |  |
| `gardenspace_m_per1000pop` | `double precision` |  |
| `gardenspace_ha_per1000pop` | `double precision` |  |
| `gardenspace_perclsoa` | `double precision` |  |
| `inlandwaterside_length` | `double precision` |  |
| `accesswaterside_length` | `double precision` |  |
| `accesswaterside_percentage` | `double precision` |  |
| `age_total_2021_2022` | `double precision` |  |
| `close2home_percentage` | `double precision` |  |
| `cohort_under16` | `double precision` |  |
| `cohort_65plus` | `double precision` |  |
| `popn_close2home_under16` | `double precision` |  |
| `popn_close2home_65plus` | `double precision` |  |
| `imd_decile` | `double precision` |  |
| `angstbuff200_area` | `double precision` |  |
| `angstbuff200_percentage` | `double precision` |  |
| `angstbuff300_area` | `double precision` |  |
| `angstbuff300_percentage` | `double precision` |  |
| `angstbuff1k_area` | `double precision` |  |
| `angstbuff1k_percentage` | `double precision` |  |
| `angstbuff2k_area` | `double precision` |  |
| `angstbuff2k_percentage` | `double precision` |  |
| `angstbuff5k_area` | `double precision` |  |
| `angstbuff5k_percentage` | `double precision` |  |
| `angstbuff10k_area` | `double precision` |  |
| `angstbuff10k_percentage` | `double precision` |  |
| `population_density_2021` | `double precision` |  |
| `angst200_pop_inequality_code` | `varchar(255)` | Code assigned by the source dataset. |
| `angst300_pop_inequality_code` | `varchar(255)` | Code assigned by the source dataset. |
| `angst1k_pop_inequality_code` | `varchar(255)` | Code assigned by the source dataset. |
| `angst2k_pop_inequality_code` | `varchar(255)` | Code assigned by the source dataset. |
| `angst5k_pop_inequality_code` | `varchar(255)` | Code assigned by the source dataset. |
| `angst10k_pop_inequality_code` | `varchar(255)` | Code assigned by the source dataset. |
| `angst200_imd_inequality_code` | `varchar(512)` | Code assigned by the source dataset. |
| `angst300_imd_inequality_code` | `varchar(512)` | Code assigned by the source dataset. |
| `angst1k_imd_inequality_code` | `varchar(512)` | Code assigned by the source dataset. |
| `angst2k_imd_inequality_code` | `varchar(512)` | Code assigned by the source dataset. |
| `angst5k_imd_inequality_code` | `varchar(512)` | Code assigned by the source dataset. |
| `angst10k_imd_inequality_code` | `varchar(512)` | Code assigned by the source dataset. |
| `angst200_l1_status` | `varchar(512)` |  |
| `angst300_l1_status` | `varchar(512)` |  |
| `angst1k_l1_status` | `varchar(512)` |  |
| `angst2k_l1_status` | `varchar(512)` |  |
| `angst5k_l1_status` | `varchar(512)` |  |
| `angst10k_l1_status` | `varchar(512)` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
