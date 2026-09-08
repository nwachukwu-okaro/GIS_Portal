# BGS Geology 625K - Bedrock

## Overview

- **Identifier:** `a_british_geological_survey/625k_bedrock_geology`
- **Source organisation:** British Geological Survey
- **Product:** BGS geological data
- **Source:** https://www.bgs.ac.uk/geological-data/
- **Local dataset version:** 5.17 (released February 2008)
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.648370, 49.863814, 1.767563, 60.860981]`
- **Topic category:** geoscientificInformation
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Equivalent scale:** 1:625,000
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_british_geological_survey`
- **Table:** `625k_bedrock_geology`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 11244
- **Columns:** 57
- **Metadata status:** context_curated

## Description

Generalised 1:625,000-scale bedrock geology polygons for Great Britain. Features identify the mapped lithostratigraphic unit, rock classification and oldest-to-youngest geological age range.

## Lineage

Published by British Geological Survey as part of BGS geological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `lex` | `varchar(5)` | BGS Lexicon code — short alphanumeric code uniquely identifying the named lithostratigraphic or lithodemic unit. |
| `lex_d` | `varchar(200)` | Lexicon description — full name of the lithostratigraphic or lithodemic unit corresponding to the lex code. |
| `lex_rcs` | `varchar(12)` | Combined lexicon and Rock Classification Scheme code linking the named unit to its rock type. |
| `rcs` | `varchar(6)` | Rock Classification Scheme code — short code for the lithological rock type. |
| `rcs_x` | `varchar(50)` | Expanded Rock Classification Scheme expression describing one or more rock types present in the unit. |
| `rcs_d` | `varchar(200)` | Rock Classification Scheme description — full plain-English description of the rock type. |
| `rank` | `varchar(16)` | Geological unit rank such as formation, group, member, intrusion or supergroup. |
| `bed_eq` | `varchar(5)` | Bed-level equivalent code for the geological unit. |
| `bed_eq_d` | `varchar(200)` | Bed-level equivalent description. |
| `mb_eq` | `varchar(5)` | Member-level equivalent code. |
| `mb_eq_d` | `varchar(200)` | Member-level equivalent description. |
| `fm_eq` | `varchar(5)` | Formation-level equivalent code. |
| `fm_eq_d` | `varchar(200)` | Formation-level equivalent description. |
| `subgp_eq` | `varchar(5)` | Subgroup-level equivalent code. |
| `subgp_eq_d` | `varchar(200)` | Subgroup-level equivalent description. |
| `gp_eq` | `varchar(5)` | Group-level equivalent code. |
| `gp_eq_d` | `varchar(200)` | Group-level equivalent description. |
| `supgp_eq` | `varchar(5)` | Supergroup-level equivalent code. |
| `supgp_eq_d` | `varchar(200)` | Supergroup-level equivalent description. |
| `max_time_d` | `varchar(32)` | Maximum (oldest) geological time period label for the unit. |
| `min_time_d` | `varchar(32)` | Minimum (youngest) geological time period label for the unit. |
| `max_time_y` | `bigint` | Maximum age in years before present. |
| `min_time_y` | `bigint` | Minimum age in years before present. |
| `max_index` | `bigint` | BGS numerical index for the older time boundary. |
| `min_index` | `bigint` | BGS numerical index for the younger time boundary. |
| `max_age` | `varchar(32)` | Oldest chronostratigraphic age assigned to the geological unit. |
| `min_age` | `varchar(32)` | Youngest chronostratigraphic age assigned to the geological unit. |
| `max_epoch` | `varchar(32)` | Oldest geological epoch assigned to the unit. |
| `min_epoch` | `varchar(32)` | Youngest geological epoch assigned to the unit. |
| `max_subper` | `varchar(32)` | Oldest geological subperiod assigned to the unit. |
| `min_ubper` | `varchar(32)` | Youngest geological subperiod assigned to the unit; field name is retained from the source data. |
| `maax_period` | `varchar(32)` | Oldest geological period assigned to the unit; field name is retained from the source data. |
| `min_period` | `varchar(32)` | Youngest geological period assigned to the unit. |
| `max_era` | `varchar(32)` | Oldest geological era assigned to the unit. |
| `min_era` | `varchar(32)` | Youngest geological era assigned to the unit. |
| `max_eon` | `varchar(32)` | Oldest geological eon assigned to the unit. |
| `min_eon` | `varchar(32)` | Youngest geological eon assigned to the unit. |
| `prev_name` | `varchar(250)` | Name associated with the represented feature. |
| `bgstype` | `varchar(32)` | BGS code identifying the geological dataset or layer type, such as 625k_BEDROCK. |
| `lex_rcs_i` | `varchar(20)` | Internal composite identifier combining BGS lexicon and rock-classification references. |
| `lex_rcs_d` | `varchar(100)` | Human-readable description associated with the corresponding coded attribute. |
| `map_code` | `varchar(10)` | Code assigned by the source dataset. |
| `age_onegl` | `varchar(32)` | Generalised geological age label used for map display and broad classification. |
| `bgsref` | `bigint` | Internal BGS reference number for the mapped geological feature. |
| `bgsref_lex` | `bigint` | Internal BGS reference number for the associated lexicon unit. |
| `bgsref_fm` | `bigint` | Internal BGS reference number for the associated formation. |
| `bgsref_gp` | `bigint` | Internal BGS reference number for the associated geological group. |
| `bgsref_rk` | `bigint` | Internal BGS reference number for the associated rock classification. |
| `sheet` | `varchar(60)` | Name of the source geological map sheet or digital layer. |
| `version` | `varchar(10)` | Version number of the published BGS dataset. |
| `released` | `varchar(10)` | Date on which this version of the dataset was released. |
| `nom_scale` | `varchar(10)` | Nominal map scale denominator, such as 625000 for 1:625,000 mapping. |
| `nom_os_yr` | `varchar(10)` | Nominal year or edition of the Ordnance Survey base mapping. |
| `nom_bgs_yr` | `varchar(10)` | Nominal year of the BGS geological compilation. |
| `mslink` | `bigint` | Internal source-system link identifier used by the original mapping database. |
| `625bg_pk` | `integer` | Primary-key value for a 1:625,000 bedrock geology feature. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
