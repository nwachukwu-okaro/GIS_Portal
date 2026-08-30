# Blue Green Infra Module10 Agi Statistics Lsoa Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Module10_AGI_Statistics_LSOA_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418601, 49.864674, 1.763680, 55.811091]`
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Module10_AGI_Statistics_LSOA_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 33755
- **Columns:** 72
- **Metadata status:** source_mapped

## Description

Blue Green Infra Module10 Agi Statistics Lsoa Ogl is an authoritative dataset published by Natural England. It represents blue green infra module10 agi statistics lsoa ogl features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `lsoa21cd` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lsoa21nm` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `globalid` | `varchar(255)` | Publisher-assigned globalid for the record. | source_identifier | Yes | No | No |
| `lad22cd` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lad22nm` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `msoa21cd` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `msoa21nm` | `varchar(255)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `age_total_2021` | `integer` | Count or numeric value for age total 2021 in the represented area. | statistical_value | Yes | No | No |
| `population_2021` | `integer` | Numeric population 2021 value recorded for the feature. | measure | Yes | No | No |
| `lnrs_id` | `varchar(255)` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `lnrs_name` | `varchar(255)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `oa_code` | `varchar(255)` | Code assigned by the source dataset. | code | Yes | No | No |
| `area_ha` | `double precision` | Area enclosed by the feature, measured in hectares. | area | Yes | No | No |
| `area_m` | `double precision` | Numeric area male value recorded for the feature. | measure | Yes | No | No |
| `totalagi_area` | `double precision` | Numeric totalagi area value recorded for the feature. | measure | Yes | No | No |
| `totalagi_per1000pop` | `double precision` | Count or numeric value for totalagi per1000pop in the represented area. | statistical_value | Yes | No | No |
| `totalagi_limited_area` | `double precision` | Numeric totalagi limited area value recorded for the feature. | measure | Yes | No | No |
| `totalagi_limited_per1000pop` | `double precision` | Count or numeric value for totalagi limited per1000pop in the represented area. | statistical_value | Yes | No | No |
| `totalagilnr_area` | `double precision` | Numeric totalagilnr area value recorded for the feature. | measure | Yes | No | No |
| `totalagi_lnr_per1000pop` | `double precision` | Count or numeric value for totalagi lnr per1000pop in the represented area. | statistical_value | Yes | No | No |
| `totalagi_accessland_area` | `double precision` | Numeric totalagi accessland area value recorded for the feature. | measure | Yes | No | No |
| `totalagi_accessland_per1000pop` | `double precision` | Count or numeric value for totalagi accessland per1000pop in the represented area. | statistical_value | Yes | No | No |
| `totalagi_coastalmargin_area` | `double precision` | Numeric totalagi coastalmargin area value recorded for the feature. | measure | Yes | No | No |
| `totalagi_coastalmargin_per1000p` | `double precision` | Count or numeric value for totalagi coastalmargin per1000p in the represented area. | statistical_value | Yes | No | No |
| `gardenspace_totalarea_m` | `double precision` | Numeric gardenspace totalarea male value recorded for the feature. | measure | Yes | No | No |
| `gardenspace_totalarea_ha` | `double precision` | Numeric gardenspace totalarea ha value recorded for the feature. | measure | Yes | No | No |
| `gardenspace_m_per1000pop` | `double precision` | Count or numeric value for gardenspace male per1000pop in the represented area. | statistical_value | Yes | No | No |
| `gardenspace_ha_per1000pop` | `double precision` | Count or numeric value for gardenspace ha per1000pop in the represented area. | statistical_value | Yes | No | No |
| `gardenspace_perclsoa` | `double precision` | Count or numeric value for gardenspace perclsoa in the represented area. | statistical_value | Yes | No | No |
| `inlandwaterside_length` | `double precision` | Numeric inlandwaterside length value recorded for the feature. | measure | Yes | No | No |
| `accesswaterside_length` | `double precision` | Numeric accesswaterside length value recorded for the feature. | measure | Yes | No | No |
| `accesswaterside_percentage` | `double precision` | Percentage for the accesswaterside percentage measure in the represented area. | percentage | Yes | No | No |
| `age_total_2021_2022` | `double precision` | Count or numeric value for age total 2021 2022 in the represented area. | statistical_value | Yes | No | No |
| `close2home_percentage` | `double precision` | Percentage for the close2home percentage measure in the represented area. | percentage | Yes | No | No |
| `cohort_under16` | `double precision` | Count or numeric value for cohort under16 in the represented area. | statistical_value | Yes | No | No |
| `cohort_65plus` | `double precision` | Count or numeric value for cohort 65plus in the represented area. | statistical_value | Yes | No | No |
| `popn_close2home_under16` | `double precision` | Count or numeric value for popn close2home under16 in the represented area. | statistical_value | Yes | No | No |
| `popn_close2home_65plus` | `double precision` | Count or numeric value for popn close2home 65plus in the represented area. | statistical_value | Yes | No | No |
| `imd_decile` | `double precision` | Count or numeric value for imd decile in the represented area. | statistical_value | Yes | No | No |
| `angstbuff200_area` | `double precision` | Numeric angstbuff200 area value recorded for the feature. | measure | Yes | No | No |
| `angstbuff200_percentage` | `double precision` | Percentage for the angstbuff200 percentage measure in the represented area. | percentage | Yes | No | No |
| `angstbuff300_area` | `double precision` | Numeric angstbuff300 area value recorded for the feature. | measure | Yes | No | No |
| `angstbuff300_percentage` | `double precision` | Percentage for the angstbuff300 percentage measure in the represented area. | percentage | Yes | No | No |
| `angstbuff1k_area` | `double precision` | Numeric angstbuff1k area value recorded for the feature. | measure | Yes | No | No |
| `angstbuff1k_percentage` | `double precision` | Percentage for the angstbuff1k percentage measure in the represented area. | percentage | Yes | No | No |
| `angstbuff2k_area` | `double precision` | Numeric angstbuff2k area value recorded for the feature. | measure | Yes | No | No |
| `angstbuff2k_percentage` | `double precision` | Percentage for the angstbuff2k percentage measure in the represented area. | percentage | Yes | No | No |
| `angstbuff5k_area` | `double precision` | Numeric angstbuff5k area value recorded for the feature. | measure | Yes | No | No |
| `angstbuff5k_percentage` | `double precision` | Percentage for the angstbuff5k percentage measure in the represented area. | percentage | Yes | No | No |
| `angstbuff10k_area` | `double precision` | Numeric angstbuff10k area value recorded for the feature. | measure | Yes | No | No |
| `angstbuff10k_percentage` | `double precision` | Percentage for the angstbuff10k percentage measure in the represented area. | percentage | Yes | No | No |
| `population_density_2021` | `double precision` | Numeric population density 2021 value recorded for the feature. | measure | Yes | No | No |
| `angst200_pop_inequality_code` | `varchar(255)` | Code assigned by the source dataset. | code | Yes | No | No |
| `angst300_pop_inequality_code` | `varchar(255)` | Code assigned by the source dataset. | code | Yes | No | No |
| `angst1k_pop_inequality_code` | `varchar(255)` | Code assigned by the source dataset. | code | Yes | No | No |
| `angst2k_pop_inequality_code` | `varchar(255)` | Code assigned by the source dataset. | code | Yes | No | No |
| `angst5k_pop_inequality_code` | `varchar(255)` | Code assigned by the source dataset. | code | Yes | No | No |
| `angst10k_pop_inequality_code` | `varchar(255)` | Code assigned by the source dataset. | code | Yes | No | No |
| `angst200_imd_inequality_code` | `varchar(512)` | Code assigned by the source dataset. | code | Yes | No | No |
| `angst300_imd_inequality_code` | `varchar(512)` | Code assigned by the source dataset. | code | Yes | No | No |
| `angst1k_imd_inequality_code` | `varchar(512)` | Code assigned by the source dataset. | code | Yes | No | No |
| `angst2k_imd_inequality_code` | `varchar(512)` | Code assigned by the source dataset. | code | Yes | No | No |
| `angst5k_imd_inequality_code` | `varchar(512)` | Code assigned by the source dataset. | code | Yes | No | No |
| `angst10k_imd_inequality_code` | `varchar(512)` | Code assigned by the source dataset. | code | Yes | No | No |
| `angst200_l1_status` | `varchar(512)` | Publisher-supplied angst200 l1 status for the represented feature or record. | source_attribute | Yes | No | No |
| `angst300_l1_status` | `varchar(512)` | Publisher-supplied angst300 l1 status for the represented feature or record. | source_attribute | Yes | No | No |
| `angst1k_l1_status` | `varchar(512)` | Publisher-supplied angst1k l1 status for the represented feature or record. | source_attribute | Yes | No | No |
| `angst2k_l1_status` | `varchar(512)` | Publisher-supplied angst2k l1 status for the represented feature or record. | source_attribute | Yes | No | No |
| `angst5k_l1_status` | `varchar(512)` | Publisher-supplied angst5k l1 status for the represented feature or record. | source_attribute | Yes | No | No |
| `angst10k_l1_status` | `varchar(512)` | Publisher-supplied angst10k l1 status for the represented feature or record. | source_attribute | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

## Supported operations

- filter
- select
- reproject
- validate_geometry
- buffer
- clip
- intersect
- spatial_join
- export

## Operation requirements

- Intersect, clip and spatial-join inputs must use matching coordinate reference systems.
- Buffer operations require a suitable projected coordinate reference system.
- Reprojection is performed on working outputs; source tables remain unchanged.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
