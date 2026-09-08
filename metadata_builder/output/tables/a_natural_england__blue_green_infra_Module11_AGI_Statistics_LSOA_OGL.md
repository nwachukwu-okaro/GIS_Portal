# Blue Green Infra Module11 Agi Statistics Lsoa Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Module11_AGI_Statistics_LSOA_OGL`
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
- **Table:** `blue_green_infra_Module11_AGI_Statistics_LSOA_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 33755
- **Columns:** 72
- **Metadata status:** source_mapped

## Description

Blue Green Infra Module11 Agi Statistics Lsoa Ogl is an authoritative dataset published by Natural England. It represents blue green infra module11 agi statistics lsoa ogl features using multipolygon geometry.

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
| `globalid` | `varchar(255)` | Publisher-assigned globalid for the record. |
| `lad22cd` | `varchar(255)` |  |
| `lad22nm` | `varchar(255)` |  |
| `msoa21cd` | `varchar(255)` |  |
| `msoa21nm` | `varchar(255)` |  |
| `age_total_2021` | `integer` | Count or numeric value for age total 2021 in the represented area. |
| `population_2021` | `integer` | Numeric population 2021 value recorded for the feature. |
| `lnrs_id` | `varchar(255)` | Identifier assigned by the source dataset. |
| `lnrs_name` | `varchar(255)` | Name associated with the represented feature. |
| `oa_code` | `varchar(255)` | Code assigned by the source dataset. |
| `area_ha` | `double precision` | Area enclosed by the feature, measured in hectares. |
| `area_m` | `double precision` | Numeric area male value recorded for the feature. |
| `totalagi_area` | `double precision` | Numeric totalagi area value recorded for the feature. |
| `totalagi_per1000pop` | `double precision` | Count or numeric value for totalagi per1000pop in the represented area. |
| `totalagi_limited_area` | `double precision` | Numeric totalagi limited area value recorded for the feature. |
| `totalagi_limited_per1000pop` | `double precision` | Count or numeric value for totalagi limited per1000pop in the represented area. |
| `totalagilnr_area` | `double precision` | Numeric totalagilnr area value recorded for the feature. |
| `totalagi_lnr_per1000pop` | `double precision` | Count or numeric value for totalagi lnr per1000pop in the represented area. |
| `totalagi_accessland_area` | `double precision` | Numeric totalagi accessland area value recorded for the feature. |
| `totalagi_accessland_per1000pop` | `double precision` | Count or numeric value for totalagi accessland per1000pop in the represented area. |
| `totalagi_coastalmargin_area` | `double precision` | Numeric totalagi coastalmargin area value recorded for the feature. |
| `totalagi_coastalmargin_per1000p` | `double precision` | Count or numeric value for totalagi coastalmargin per1000p in the represented area. |
| `gardenspace_totalarea_m` | `double precision` | Numeric gardenspace totalarea male value recorded for the feature. |
| `gardenspace_totalarea_ha` | `double precision` | Numeric gardenspace totalarea ha value recorded for the feature. |
| `gardenspace_m_per1000pop` | `double precision` | Count or numeric value for gardenspace male per1000pop in the represented area. |
| `gardenspace_ha_per1000pop` | `double precision` | Count or numeric value for gardenspace ha per1000pop in the represented area. |
| `gardenspace_perclsoa` | `double precision` | Count or numeric value for gardenspace perclsoa in the represented area. |
| `inlandwaterside_length` | `double precision` | Numeric inlandwaterside length value recorded for the feature. |
| `accesswaterside_length` | `double precision` | Numeric accesswaterside length value recorded for the feature. |
| `accesswaterside_percentage` | `double precision` | Percentage for the accesswaterside percentage measure in the represented area. |
| `age_total_2021_2022` | `double precision` | Count or numeric value for age total 2021 2022 in the represented area. |
| `close2home_percentage` | `double precision` | Percentage for the close2home percentage measure in the represented area. |
| `cohort_under16` | `double precision` | Count or numeric value for cohort under16 in the represented area. |
| `cohort_65plus` | `double precision` | Count or numeric value for cohort 65plus in the represented area. |
| `popn_close2home_under16` | `double precision` | Count or numeric value for popn close2home under16 in the represented area. |
| `popn_close2home_65plus` | `double precision` | Count or numeric value for popn close2home 65plus in the represented area. |
| `imd_decile` | `double precision` | Count or numeric value for imd decile in the represented area. |
| `angstbuff200_area` | `double precision` | Numeric angstbuff200 area value recorded for the feature. |
| `angstbuff200_percentage` | `double precision` | Percentage for the angstbuff200 percentage measure in the represented area. |
| `angstbuff300_area` | `double precision` | Numeric angstbuff300 area value recorded for the feature. |
| `angstbuff300_percentage` | `double precision` | Percentage for the angstbuff300 percentage measure in the represented area. |
| `angstbuff1k_area` | `double precision` | Numeric angstbuff1k area value recorded for the feature. |
| `angstbuff1k_percentage` | `double precision` | Percentage for the angstbuff1k percentage measure in the represented area. |
| `angstbuff2k_area` | `double precision` | Numeric angstbuff2k area value recorded for the feature. |
| `angstbuff2k_percentage` | `double precision` | Percentage for the angstbuff2k percentage measure in the represented area. |
| `angstbuff5k_area` | `double precision` | Numeric angstbuff5k area value recorded for the feature. |
| `angstbuff5k_percentage` | `double precision` | Percentage for the angstbuff5k percentage measure in the represented area. |
| `angstbuff10k_area` | `double precision` | Numeric angstbuff10k area value recorded for the feature. |
| `angstbuff10k_percentage` | `double precision` | Percentage for the angstbuff10k percentage measure in the represented area. |
| `population_density_2021` | `double precision` | Numeric population density 2021 value recorded for the feature. |
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
| `angst200_l1_status` | `varchar(512)` | Publisher-supplied angst200 l1 status for the represented feature or record. |
| `angst300_l1_status` | `varchar(512)` | Publisher-supplied angst300 l1 status for the represented feature or record. |
| `angst1k_l1_status` | `varchar(512)` | Publisher-supplied angst1k l1 status for the represented feature or record. |
| `angst2k_l1_status` | `varchar(512)` | Publisher-supplied angst2k l1 status for the represented feature or record. |
| `angst5k_l1_status` | `varchar(512)` | Publisher-supplied angst5k l1 status for the represented feature or record. |
| `angst10k_l1_status` | `varchar(512)` | Publisher-supplied angst10k l1 status for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
