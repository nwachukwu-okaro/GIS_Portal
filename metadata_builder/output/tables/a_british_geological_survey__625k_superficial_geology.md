# 625k Superficial Geology

## Overview

- **Identifier:** `a_british_geological_survey/625k_superficial_geology`
- **Source organisation:** British Geological Survey
- **Product:** BGS geological data
- **Source:** https://www.bgs.ac.uk/geological-data/
- **Schema:** `a_british_geological_survey`
- **Table:** `625k_superficial_geology`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 10651
- **Metadata status:** source_mapped

## Description

Contains British Geological Survey materials © UKRI 2026

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `lex` | `varchar(5)` | BGS Lexicon code — short alphanumeric code uniquely identifying the named lithostratigraphic or lithodemic unit. | geological_unit_code | Yes | No | Yes |
| `lex_d` | `varchar(200)` | Lexicon description — full name of the lithostratigraphic or lithodemic unit corresponding to the lex code. | geological_unit_name | Yes | No | No |
| `rcs` | `varchar(50)` | Rock Classification Scheme code — short code for the lithological rock type. | rock_classification_code | Yes | No | Yes |
| `rcs_d` | `varchar(200)` | Rock Classification Scheme description — full plain-English description of the rock type. | rock_type_description | Yes | No | No |
| `rank` | `varchar(16)` | Geological unit rank such as formation, group, member, intrusion or supergroup. | geological_unit_rank | Yes | No | No |
| `bed_eq` | `varchar(5)` | Bed-level equivalent code for the geological unit. | geological_unit_code | Yes | No | Yes |
| `bed_eq_d` | `varchar(200)` | Bed-level equivalent description. | geological_unit_name | Yes | No | No |
| `mb_eq` | `varchar(5)` | Member-level equivalent code. | geological_unit_code | Yes | No | Yes |
| `mb_eq_d` | `varchar(200)` | Member-level equivalent description. | geological_unit_name | Yes | No | No |
| `fm_eq` | `varchar(5)` | Formation-level equivalent code. | geological_unit_code | Yes | No | Yes |
| `fm_eq_d` | `varchar(200)` | Formation-level equivalent description. | geological_unit_name | Yes | No | No |
| `subgp_eq` | `varchar(5)` | Subgroup-level equivalent code. | geological_unit_code | Yes | No | Yes |
| `subgp_eq_d` | `varchar(200)` | Subgroup-level equivalent description. | geological_unit_name | Yes | No | No |
| `gp_eq` | `varchar(5)` | Group-level equivalent code. | geological_unit_code | Yes | No | Yes |
| `gp_eq_d` | `varchar(200)` | Group-level equivalent description. | geological_unit_name | Yes | No | No |
| `supgp_eq` | `varchar(5)` | Supergroup-level equivalent code. | geological_unit_code | Yes | No | Yes |
| `supgp_eq_d` | `varchar(200)` | Supergroup-level equivalent description. | geological_unit_name | Yes | No | No |
| `max_age` | `varchar(2)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `min_age` | `varchar(2)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `bgsref` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `bgsref_lex` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `bgsref_fm` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `bgsref_gp` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `bgsref_rk` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sheet` | `varchar(60)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `version` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `released` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `nom_scale` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `nom_os_yr` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `nom_bgs_yr` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `mslink` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lex_rock` | `varchar(12)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `rock` | `varchar(6)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `rock_d` | `varchar(200)` | Human-readable description associated with the corresponding coded attribute. | description | Yes | Yes | No |
| `max_age_no` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `min_age_no` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `max_stage` | `varchar(32)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `min_stage` | `varchar(32)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `max_series` | `varchar(32)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `min_series` | `varchar(32)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `max_subsys` | `varchar(32)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `min_subsys` | `varchar(32)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `max_system` | `varchar(32)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `min_system` | `varchar(32)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `max_earth` | `varchar(32)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `min_earth` | `varchar(32)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `max_eonoth` | `varchar(32)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `min_eonoth` | `varchar(32)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `625sg_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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

## Metadata warnings

- Verify the licence against the individual BGS product; not all BGS products are open.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
