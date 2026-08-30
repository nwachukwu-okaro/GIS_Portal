# Air Quality Annual Evaluation Report

## Overview

- **Identifier:** `a_national_highways/air_quality_annual_evaluation_report`
- **Source organisation:** National Highways
- **Source:** https://developer.data.nationalhighways.co.uk/
- **Geographic coverage:** England
- **WGS84 extent:** `[-4.140956, 50.391032, 0.754152, 55.008339]`
- **Schema:** `a_national_highways`
- **Table:** `air_quality_annual_evaluation_report`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 256
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Air Quality Annual Evaluation Report is an authoritative dataset published by National Highways. It represents air quality annual evaluation report features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `smallint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `pcm_link_i` | `integer` | Count or numeric value for pcm link i in the represented area. | statistical_value | Yes | No | No |
| `road_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `road_descr` | `varchar` | Publisher-supplied road descr for the represented feature or record. | source_attribute | Yes | No | No |
| `qf_within_` | `varchar` | Publisher-supplied qf within for the represented feature or record. | source_attribute | Yes | No | No |
| `no2_conc` | `varchar` | Publisher-supplied no2 conc for the represented feature or record. | source_attribute | Yes | No | No |
| `annual_eva` | `varchar` | Publisher-supplied annual eva for the represented feature or record. | source_attribute | Yes | No | No |
| `annual_e_1` | `varchar` | Publisher-supplied annual e 1 for the represented feature or record. | source_attribute | Yes | No | No |
| `local_no2_` | `varchar` | Publisher-supplied local no2 for the represented feature or record. | source_attribute | Yes | No | No |
| `datasets_r` | `varchar` | Publisher-supplied datasets r for the represented feature or record. | source_attribute | Yes | No | No |
| `aer_based_` | `varchar` | Publisher-supplied aer based for the represented feature or record. | source_attribute | Yes | No | No |
| `commentary` | `varchar` | Publisher-supplied commentary for the represented feature or record. | source_attribute | Yes | No | No |
| `view_techn` | `varchar` | Publisher-supplied view techn for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `smallint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `globalid` | `varchar` | Publisher-assigned globalid for the record. | source_identifier | Yes | No | No |
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

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
