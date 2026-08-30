# BGS Geology 625K - Dykes

## Overview

- **Identifier:** `a_british_geological_survey/625k_dykes_geology`
- **Source organisation:** British Geological Survey
- **Product:** BGS geological data
- **Source:** https://www.bgs.ac.uk/geological-data/
- **Local dataset version:** 5.17 (released 11 February 2008)
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.861517, 50.077907, -0.603331, 60.684427]`
- **Schema:** `a_british_geological_survey`
- **Table:** `625k_dykes_geology`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 3263
- **Columns:** 57
- **Metadata status:** context_curated

## Description

Generalised 1:625,000-scale mapped dyke features for Great Britain, classified by BGS geological unit, rock type and geological age.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `lex` | `varchar(5)` | BGS Lexicon code — short alphanumeric code uniquely identifying the named lithostratigraphic or lithodemic unit. | geological_unit_code | Yes | No | Yes |
| `lex_d` | `varchar(200)` | Lexicon description — full name of the lithostratigraphic or lithodemic unit corresponding to the lex code. | geological_unit_name | Yes | No | No |
| `lex_rcs` | `varchar(12)` | Combined lexicon and Rock Classification Scheme code linking the named unit to its rock type. | geological_unit_rock_code | Yes | No | Yes |
| `rcs` | `varchar(6)` | Rock Classification Scheme code — short code for the lithological rock type. | rock_classification_code | Yes | No | Yes |
| `rcs_x` | `varchar(50)` | Expanded Rock Classification Scheme expression describing one or more rock types present in the unit. | rock_composition | Yes | No | No |
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
| `max_time_d` | `varchar(32)` | Maximum (oldest) geological time period label for the unit. | geological_time_label | Yes | No | No |
| `min_time_d` | `varchar(32)` | Minimum (youngest) geological time period label for the unit. | geological_time_label | Yes | No | No |
| `max_time_y` | `bigint` | Maximum age in years before present. | geological_age_years | Yes | No | No |
| `min_time_y` | `bigint` | Minimum age in years before present. | geological_age_years | Yes | No | No |
| `max_index` | `bigint` | BGS numerical index for the older time boundary. | geological_time_index | Yes | No | No |
| `min_index` | `bigint` | BGS numerical index for the younger time boundary. | geological_time_index | Yes | No | No |
| `max_age` | `varchar(32)` | Oldest chronostratigraphic age assigned to the geological unit. | oldest_geological_age | Yes | No | No |
| `min_age` | `varchar(32)` | Youngest chronostratigraphic age assigned to the geological unit. | youngest_geological_age | Yes | No | No |
| `max_epoch` | `varchar(32)` | Oldest geological epoch assigned to the unit. | oldest_geological_epoch | Yes | No | No |
| `min_epoch` | `varchar(32)` | Youngest geological epoch assigned to the unit. | youngest_geological_epoch | Yes | No | No |
| `max_subper` | `varchar(32)` | Oldest geological subperiod assigned to the unit. | oldest_geological_subperiod | Yes | No | No |
| `min_ubper` | `varchar(32)` | Youngest geological subperiod assigned to the unit; field name is retained from the source data. | youngest_geological_subperiod | Yes | No | No |
| `maax_period` | `varchar(32)` | Oldest geological period assigned to the unit; field name is retained from the source data. | oldest_geological_period | Yes | No | No |
| `min_period` | `varchar(32)` | Youngest geological period assigned to the unit. | youngest_geological_period | Yes | No | No |
| `max_era` | `varchar(32)` | Oldest geological era assigned to the unit. | oldest_geological_era | Yes | No | No |
| `min_era` | `varchar(32)` | Youngest geological era assigned to the unit. | youngest_geological_era | Yes | No | No |
| `max_eon` | `varchar(32)` | Oldest geological eon assigned to the unit. | oldest_geological_eon | Yes | No | No |
| `min_eon` | `varchar(32)` | Youngest geological eon assigned to the unit. | youngest_geological_eon | Yes | No | No |
| `prev_name` | `varchar(250)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `bgstype` | `varchar(32)` | BGS code identifying the geological dataset or layer type, such as 625k_BEDROCK. | dataset_type_code | Yes | No | No |
| `lex_rcs_i` | `varchar(20)` | Internal composite identifier combining BGS lexicon and rock-classification references. | geological_unit_rock_identifier | Yes | No | No |
| `lex_rcs_d` | `varchar(100)` | Human-readable description associated with the corresponding coded attribute. | description | Yes | Yes | No |
| `map_code` | `varchar(10)` | Code assigned by the source dataset. | code | Yes | No | No |
| `age_onegl` | `varchar(32)` | Generalised geological age label used for map display and broad classification. | generalised_geological_age | Yes | No | No |
| `bgsref` | `bigint` | Internal BGS reference number for the mapped geological feature. | source_record_identifier | Yes | No | No |
| `bgsref_lex` | `bigint` | Internal BGS reference number for the associated lexicon unit. | lexicon_reference | Yes | No | No |
| `bgsref_fm` | `bigint` | Internal BGS reference number for the associated formation. | formation_reference | Yes | No | No |
| `bgsref_gp` | `bigint` | Internal BGS reference number for the associated geological group. | group_reference | Yes | No | No |
| `bgsref_rk` | `bigint` | Internal BGS reference number for the associated rock classification. | rock_reference | Yes | No | No |
| `sheet` | `varchar(60)` | Name of the source geological map sheet or digital layer. | source_map_sheet | Yes | No | No |
| `version` | `varchar(10)` | Version number of the published BGS dataset. | dataset_version | Yes | No | No |
| `released` | `varchar(10)` | Date on which this version of the dataset was released. | release_date | Yes | No | No |
| `nom_scale` | `varchar(10)` | Nominal map scale denominator, such as 625000 for 1:625,000 mapping. | nominal_scale | Yes | No | No |
| `nom_os_yr` | `varchar(10)` | Nominal year or edition of the Ordnance Survey base mapping. | os_base_map_year | Yes | No | No |
| `nom_bgs_yr` | `varchar(10)` | Nominal year of the BGS geological compilation. | geological_compilation_year | Yes | No | No |
| `mslink` | `bigint` | Internal source-system link identifier used by the original mapping database. | source_system_identifier | Yes | No | No |
| `625dg_pk` | `integer` | Primary-key value for a 1:625,000 dyke geology feature. | record_identifier | Yes | No | No |
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

- Generalised regional mapping is not suitable for site-scale geological interpretation.
- Verify reuse terms against the individual BGS product licence.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
