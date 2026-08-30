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
- **Schema:** `a_british_geological_survey`
- **Table:** `625k_superficial_geology`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 10651
- **Columns:** 50
- **Metadata status:** context_curated

## Description

Generalised 1:625,000-scale polygons of superficial deposits across Great Britain, including deposit names, sediment or rock classifications and geological age ranges.

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
| `max_age` | `varchar(2)` | Oldest chronostratigraphic age assigned to the geological unit. | oldest_geological_age | Yes | No | No |
| `min_age` | `varchar(2)` | Youngest chronostratigraphic age assigned to the geological unit. | youngest_geological_age | Yes | No | No |
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
| `lex_rock` | `varchar(12)` | Combined BGS lexicon and rock-classification code for a superficial deposit. | geological_unit_rock_code | Yes | No | No |
| `rock` | `varchar(6)` | Short BGS rock or sediment code, such as SAND, PEAT, CLAY or UNKN. | rock_classification_code | Yes | No | No |
| `rock_d` | `varchar(200)` | Human-readable description associated with the corresponding coded attribute. | description | Yes | Yes | No |
| `max_age_no` | `bigint` | Numeric BGS index for the oldest age boundary of the deposit. | oldest_geological_age_index | Yes | No | No |
| `min_age_no` | `bigint` | Numeric BGS index for the youngest age boundary of the deposit. | youngest_geological_age_index | Yes | No | No |
| `max_stage` | `varchar(32)` | Oldest geological stage assigned to the deposit. | oldest_geological_stage | Yes | No | No |
| `min_stage` | `varchar(32)` | Youngest geological stage assigned to the deposit. | youngest_geological_stage | Yes | No | No |
| `max_series` | `varchar(32)` | Oldest geological series assigned to the deposit. | oldest_geological_series | Yes | No | No |
| `min_series` | `varchar(32)` | Youngest geological series assigned to the deposit. | youngest_geological_series | Yes | No | No |
| `max_subsys` | `varchar(32)` | Oldest geological subsystem assigned to the deposit. | oldest_geological_subsystem | Yes | No | No |
| `min_subsys` | `varchar(32)` | Youngest geological subsystem assigned to the deposit. | youngest_geological_subsystem | Yes | No | No |
| `max_system` | `varchar(32)` | Oldest geological system assigned to the deposit. | oldest_geological_system | Yes | No | No |
| `min_system` | `varchar(32)` | Youngest geological system assigned to the deposit. | youngest_geological_system | Yes | No | No |
| `max_earth` | `varchar(32)` | Oldest broad Earth-history division assigned to the deposit. | oldest_earth_history_division | Yes | No | No |
| `min_earth` | `varchar(32)` | Youngest broad Earth-history division assigned to the deposit. | youngest_earth_history_division | Yes | No | No |
| `max_eonoth` | `varchar(32)` | Oldest eon or equivalent broad age division assigned to the deposit. | oldest_geological_eon | Yes | No | No |
| `min_eonoth` | `varchar(32)` | Youngest eon or equivalent broad age division assigned to the deposit. | youngest_geological_eon | Yes | No | No |
| `625sg_pk` | `integer` | Primary-key value for a 1:625,000 superficial geology feature. | record_identifier | Yes | No | No |
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

- Generalised regional mapping is not suitable for site-scale ground investigation.
- Verify reuse terms against the individual BGS product licence.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
