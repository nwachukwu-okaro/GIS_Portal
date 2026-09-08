# Boundary Census Disability Carers Health Smoking Small Area

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_disability_carers_health_smoking_small_area`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.726726, 54.563349, 3.417194, 58.519873]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_disability_carers_health_smoking_small_area`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 18919
- **Columns:** 37
- **Metadata status:** source_mapped

## Description

Boundary Census Disability Carers Health Smoking Small Area is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census disability carers health smoking small area features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `guid` | `text` | Publisher-assigned guid for the record. |
| `geogid` | `text` | Publisher-assigned geogid for the record. |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. |
| `ur_category` | `double precision` | Count or numeric value for ur category in the represented area. |
| `ur_category_desc` | `text` | Publisher-supplied ur category description for the represented feature or record. |
| `males` | `bigint` | Count or numeric value for males in the represented area. |
| `females` | `bigint` | Count or numeric value for females in the represented area. |
| `total_perons` | `bigint` | Count or numeric value for total perons in the represented area. |
| `males_1` | `bigint` | Count or numeric value for males 1 in the represented area. |
| `females_1` | `bigint` | Count or numeric value for females 1 in the represented area. |
| `total` | `bigint` | Count or numeric value for total in the represented area. |
| `very_good_males` | `bigint` | Count or numeric value for very good males in the represented area. |
| `very_good_females` | `bigint` | Count or numeric value for very good females in the represented area. |
| `very_good_total` | `bigint` | Count or numeric value for very good total in the represented area. |
| `good_males` | `bigint` | Count or numeric value for good males in the represented area. |
| `good_females` | `bigint` | Count or numeric value for good females in the represented area. |
| `good_total` | `bigint` | Count or numeric value for good total in the represented area. |
| `fair_males` | `bigint` | Count or numeric value for fair males in the represented area. |
| `fair_females` | `bigint` | Count or numeric value for fair females in the represented area. |
| `fair_total` | `bigint` | Count or numeric value for fair total in the represented area. |
| `bad_males` | `bigint` | Count or numeric value for bad males in the represented area. |
| `bad_females` | `bigint` | Count or numeric value for bad females in the represented area. |
| `bad_total` | `bigint` | Count or numeric value for bad total in the represented area. |
| `very_bad_males` | `bigint` | Count or numeric value for very bad males in the represented area. |
| `very_bad_females` | `bigint` | Count or numeric value for very bad females in the represented area. |
| `very_bad_total` | `bigint` | Count or numeric value for very bad total in the represented area. |
| `not_stated_males` | `bigint` | Count or numeric value for not stated males in the represented area. |
| `not_stated_females` | `bigint` | Count or numeric value for not stated females in the represented area. |
| `not_stated_total` | `bigint` | Count or numeric value for not stated total in the represented area. |
| `total_males` | `bigint` | Count or numeric value for total males in the represented area. |
| `total_females` | `bigint` | Count or numeric value for total females in the represented area. |
| `total_1` | `bigint` | Count or numeric value for total 1 in the represented area. |
| `persons_who_smoke` | `bigint` | Count or numeric value for persons who smoke in the represented area. |
| `persons_who_dont_smoke` | `bigint` | Count or numeric value for persons who dont smoke in the represented area. |
| `non_stated` | `bigint` | Count or numeric value for non stated in the represented area. |
| `total_persons` | `bigint` | Count or numeric value for total persons in the represented area. |
