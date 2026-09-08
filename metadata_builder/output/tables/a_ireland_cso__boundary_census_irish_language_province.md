# Boundary Census Irish Language Province

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_irish_language_province`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.682125, 51.420091, -5.996278, 55.446936]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_irish_language_province`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 4
- **Columns:** 42
- **Metadata status:** source_mapped

## Description

Boundary Census Irish Language Province is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census irish language province features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. |
| `geogid` | `text` | Publisher-assigned geogid for the record. |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. |
| `yes` | `bigint` | Count or numeric value for yes in the represented area. |
| `no` | `bigint` | Count or numeric value for number in the represented area. |
| `not_stated` | `bigint` | Count or numeric value for not stated in the represented area. |
| `total` | `bigint` | Count or numeric value for total in the represented area. |
| `daily_only_within_the_education_system_males` | `bigint` | Count or numeric value for daily only within the education system males in the represented area. |
| `daily_within_and_daily_outside_the_education_system_males` | `bigint` | Count or numeric value for daily within and daily outside the education system males in the represented area. |
| `daily_within_and_weekly_outside_the_education_system_males` | `bigint` | Count or numeric value for daily within and weekly outside the education system males in the represented area. |
| `daily_within_and_less_often_outside_the_education_system_males` | `bigint` | Count or numeric value for daily within and less often outside the education system males in the represented area. |
| `daily_within_and_never_outside_the_education_system_males` | `bigint` | Count or numeric value for daily within and never outside the education system males in the represented area. |
| `daily_only_outside_the_education_system_males` | `bigint` | Count or numeric value for daily only outside the education system males in the represented area. |
| `weekly_only_outside_the_education_system_males` | `bigint` | Count or numeric value for weekly only outside the education system males in the represented area. |
| `less_often_only_outside_the_education_system_males` | `bigint` | Count or numeric value for less often only outside the education system males in the represented area. |
| `never_speaks_irish_males` | `bigint` | Count or numeric value for never speaks irish males in the represented area. |
| `not_stated_males` | `bigint` | Count or numeric value for not stated males in the represented area. |
| `all_irish_speakers_males` | `bigint` | Count or numeric value for all irish speakers males in the represented area. |
| `daily_only_within_the_education_system_females` | `bigint` | Count or numeric value for daily only within the education system females in the represented area. |
| `daily_within_and_daily_outside_the_education_system_females` | `bigint` | Count or numeric value for daily within and daily outside the education system females in the represented area. |
| `daily_within_and_weekly_outside_the_education_system_females` | `bigint` | Count or numeric value for daily within and weekly outside the education system females in the represented area. |
| `daily_within_and_less_often_outside_the_education_system_female` | `bigint` | Count or numeric value for daily within and less often outside the education system female in the represented area. |
| `daily_within_and_never_outside_the_education_system_females` | `bigint` | Count or numeric value for daily within and never outside the education system females in the represented area. |
| `daily_only_outside_the_education_system_females` | `bigint` | Count or numeric value for daily only outside the education system females in the represented area. |
| `weekly_only_outside_the_education_system_females` | `bigint` | Count or numeric value for weekly only outside the education system females in the represented area. |
| `less_often_only_outside_the_education_system_females` | `bigint` | Count or numeric value for less often only outside the education system females in the represented area. |
| `never_speaks_irish_females` | `bigint` | Count or numeric value for never speaks irish females in the represented area. |
| `not_stated_females` | `bigint` | Count or numeric value for not stated females in the represented area. |
| `all_irish_speakers_females` | `bigint` | Count or numeric value for all irish speakers females in the represented area. |
| `daily_only_within_the_education_system_total` | `bigint` | Count or numeric value for daily only within the education system total in the represented area. |
| `daily_within_and_daily_outside_the_education_system_total` | `bigint` | Count or numeric value for daily within and daily outside the education system total in the represented area. |
| `daily_within_and_weekly_outside_the_education_system_total` | `bigint` | Count or numeric value for daily within and weekly outside the education system total in the represented area. |
| `daily_within_and_less_often_outside_the_education_system_total` | `bigint` | Count or numeric value for daily within and less often outside the education system total in the represented area. |
| `daily_within_and_never_outside_the_education_system_total` | `bigint` | Count or numeric value for daily within and never outside the education system total in the represented area. |
| `daily_only_outside_the_education_system_total` | `bigint` | Count or numeric value for daily only outside the education system total in the represented area. |
| `weekly_only_outside_the_education_system_total` | `bigint` | Count or numeric value for weekly only outside the education system total in the represented area. |
| `less_often_only_outside_the_education_system_total` | `bigint` | Count or numeric value for less often only outside the education system total in the represented area. |
| `never_speaks_irish_total` | `bigint` | Count or numeric value for never speaks irish total in the represented area. |
| `not_stated_total` | `bigint` | Count or numeric value for not stated total in the represented area. |
| `all_irish_speakers_total` | `bigint` | Count or numeric value for all irish speakers total in the represented area. |
| `area` | `double precision` | Numeric area value recorded for the feature. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
