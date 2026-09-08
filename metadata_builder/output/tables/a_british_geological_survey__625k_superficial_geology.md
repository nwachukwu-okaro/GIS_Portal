# BGS Geology 625K - Superficial Deposits

## Overview

- **Identifier:** `a_british_geological_survey/625k_superficial_geology`
- **Source organisation:** British Geological Survey
- **Product:** BGS geological data
- **Source:** https://www.bgs.ac.uk/geological-data/
- **Local dataset version:** 1.10 (released 30 April 2003)
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.630142, 49.890099, 1.762637, 60.847681]`
- **Topic category:** geoscientificInformation
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Equivalent scale:** 1:625,000
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_british_geological_survey`
- **Table:** `625k_superficial_geology`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 10651
- **Columns:** 50
- **Metadata status:** context_curated

## Description

Generalised 1:625,000-scale polygons of superficial deposits across Great Britain, including deposit names, sediment or rock classifications and geological age ranges.

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
| `rcs` | `varchar(50)` | Rock Classification Scheme code — short code for the lithological rock type. |
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
| `max_age` | `varchar(2)` | Oldest chronostratigraphic age assigned to the geological unit. |
| `min_age` | `varchar(2)` | Youngest chronostratigraphic age assigned to the geological unit. |
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
| `lex_rock` | `varchar(12)` | Combined BGS lexicon and rock-classification code for a superficial deposit. |
| `rock` | `varchar(6)` | Short BGS rock or sediment code, such as SAND, PEAT, CLAY or UNKN. |
| `rock_d` | `varchar(200)` | Human-readable description associated with the corresponding coded attribute. |
| `max_age_no` | `bigint` | Numeric BGS index for the oldest age boundary of the deposit. |
| `min_age_no` | `bigint` | Numeric BGS index for the youngest age boundary of the deposit. |
| `max_stage` | `varchar(32)` | Oldest geological stage assigned to the deposit. |
| `min_stage` | `varchar(32)` | Youngest geological stage assigned to the deposit. |
| `max_series` | `varchar(32)` | Oldest geological series assigned to the deposit. |
| `min_series` | `varchar(32)` | Youngest geological series assigned to the deposit. |
| `max_subsys` | `varchar(32)` | Oldest geological subsystem assigned to the deposit. |
| `min_subsys` | `varchar(32)` | Youngest geological subsystem assigned to the deposit. |
| `max_system` | `varchar(32)` | Oldest geological system assigned to the deposit. |
| `min_system` | `varchar(32)` | Youngest geological system assigned to the deposit. |
| `max_earth` | `varchar(32)` | Oldest broad Earth-history division assigned to the deposit. |
| `min_earth` | `varchar(32)` | Youngest broad Earth-history division assigned to the deposit. |
| `max_eonoth` | `varchar(32)` | Oldest eon or equivalent broad age division assigned to the deposit. |
| `min_eonoth` | `varchar(32)` | Youngest eon or equivalent broad age division assigned to the deposit. |
| `625sg_pk` | `integer` | Primary-key value for a 1:625,000 superficial geology feature. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
