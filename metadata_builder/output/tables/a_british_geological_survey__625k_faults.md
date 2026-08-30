# BGS Geology 625K - Faults

## Overview

- **Identifier:** `a_british_geological_survey/625k_faults`
- **Source organisation:** British Geological Survey
- **Product:** BGS geological data
- **Source:** https://www.bgs.ac.uk/geological-data/
- **Local dataset version:** 5.17 (released 23 April 2008)
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.097029, 49.967884, 0.781719, 60.836755]`
- **Schema:** `a_british_geological_survey`
- **Table:** `625k_faults`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 2741
- **Columns:** 14
- **Metadata status:** context_curated

## Description

Generalised 1:625,000-scale linework representing mapped geological faults and thrust faults in Great Britain.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `category` | `varchar(32)` | Map-series category assigned to the fault feature, such as 625k. | map_series_category | Yes | No | No |
| `feature` | `varchar(60)` | Fault feature type, such as a fault or thrust fault with hanging-wall barbs. | fault_feature_type | Yes | No | No |
| `feature_d` | `varchar(100)` | Human-readable description associated with the corresponding coded attribute. | description | Yes | Yes | No |
| `fltname_c` | `varchar(6)` | Source code for the named fault, where a recognised fault name is available. | fault_name_code | Yes | No | No |
| `fltname_d` | `varchar(100)` | Human-readable description associated with the corresponding coded attribute. | description | Yes | Yes | No |
| `sheet` | `varchar(60)` | Name of the source geological map sheet or digital layer. | source_map_sheet | Yes | No | No |
| `version` | `varchar(10)` | Version number of the published BGS dataset. | dataset_version | Yes | No | No |
| `released` | `varchar(10)` | Date on which this version of the dataset was released. | release_date | Yes | No | No |
| `nom_scale` | `varchar(10)` | Nominal map scale denominator, such as 625000 for 1:625,000 mapping. | nominal_scale | Yes | No | No |
| `nom_os_yr` | `varchar(10)` | Nominal year or edition of the Ordnance Survey base mapping. | os_base_map_year | Yes | No | No |
| `nom_bgs_yr` | `varchar(10)` | Nominal year of the BGS geological compilation. | geological_compilation_year | Yes | No | No |
| `mslink` | `bigint` | Internal source-system link identifier used by the original mapping database. | source_system_identifier | Yes | No | No |
| `625f_pk` | `integer` | Primary-key value for a 1:625,000 fault feature. | record_identifier | Yes | No | No |
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

- Fault positions are generalised for regional-scale use and should not be treated as surveyed site boundaries.
- Verify reuse terms against the individual BGS product licence.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
