# Boundary Census Disability Carers Health Smoking County

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_disability_carers_health_smoking_county`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.746471, 54.563349, 3.417194, 58.520162]`
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_disability_carers_health_smoking_county`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 31
- **Columns:** 36
- **Metadata status:** source_mapped

## Description

Boundary Census Disability Carers Health Smoking County is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census disability carers health smoking county features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `geogid` | `text` | Publisher-assigned geogid for the record. | source_identifier | Yes | No | No |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `males` | `bigint` | Count or numeric value for males in the represented area. | statistical_value | Yes | No | No |
| `females` | `bigint` | Count or numeric value for females in the represented area. | statistical_value | Yes | No | No |
| `total_perons` | `bigint` | Count or numeric value for total perons in the represented area. | statistical_value | Yes | No | No |
| `males_1` | `bigint` | Count or numeric value for males 1 in the represented area. | statistical_value | Yes | No | No |
| `females_1` | `bigint` | Count or numeric value for females 1 in the represented area. | statistical_value | Yes | No | No |
| `total` | `bigint` | Count or numeric value for total in the represented area. | statistical_value | Yes | No | No |
| `very_good_males` | `bigint` | Count or numeric value for very good males in the represented area. | statistical_value | Yes | No | No |
| `very_good_females` | `bigint` | Count or numeric value for very good females in the represented area. | statistical_value | Yes | No | No |
| `very_good_total` | `bigint` | Count or numeric value for very good total in the represented area. | statistical_value | Yes | No | No |
| `good_males` | `bigint` | Count or numeric value for good males in the represented area. | statistical_value | Yes | No | No |
| `good_females` | `bigint` | Count or numeric value for good females in the represented area. | statistical_value | Yes | No | No |
| `good_total` | `bigint` | Count or numeric value for good total in the represented area. | statistical_value | Yes | No | No |
| `fair_males` | `bigint` | Count or numeric value for fair males in the represented area. | statistical_value | Yes | No | No |
| `fair_females` | `bigint` | Count or numeric value for fair females in the represented area. | statistical_value | Yes | No | No |
| `fair_total` | `bigint` | Count or numeric value for fair total in the represented area. | statistical_value | Yes | No | No |
| `bad_males` | `bigint` | Count or numeric value for bad males in the represented area. | statistical_value | Yes | No | No |
| `bad_females` | `bigint` | Count or numeric value for bad females in the represented area. | statistical_value | Yes | No | No |
| `bad_total` | `bigint` | Count or numeric value for bad total in the represented area. | statistical_value | Yes | No | No |
| `very_bad_males` | `bigint` | Count or numeric value for very bad males in the represented area. | statistical_value | Yes | No | No |
| `very_bad_females` | `bigint` | Count or numeric value for very bad females in the represented area. | statistical_value | Yes | No | No |
| `very_bad_total` | `bigint` | Count or numeric value for very bad total in the represented area. | statistical_value | Yes | No | No |
| `not_stated_males` | `bigint` | Count or numeric value for not stated males in the represented area. | statistical_value | Yes | No | No |
| `not_stated_females` | `bigint` | Count or numeric value for not stated females in the represented area. | statistical_value | Yes | No | No |
| `not_stated_total` | `bigint` | Count or numeric value for not stated total in the represented area. | statistical_value | Yes | No | No |
| `total_males` | `bigint` | Count or numeric value for total males in the represented area. | statistical_value | Yes | No | No |
| `total_females` | `bigint` | Count or numeric value for total females in the represented area. | statistical_value | Yes | No | No |
| `total_1` | `bigint` | Count or numeric value for total 1 in the represented area. | statistical_value | Yes | No | No |
| `persons_who_smoke` | `bigint` | Count or numeric value for persons who smoke in the represented area. | statistical_value | Yes | No | No |
| `persons_who_dont_smoke` | `bigint` | Count or numeric value for persons who dont smoke in the represented area. | statistical_value | Yes | No | No |
| `non_stated` | `bigint` | Count or numeric value for non stated in the represented area. | statistical_value | Yes | No | No |
| `total_persons` | `bigint` | Count or numeric value for total persons in the represented area. | statistical_value | Yes | No | No |
| `area` | `double precision` | Numeric area value recorded for the feature. | measure | Yes | No | No |
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
