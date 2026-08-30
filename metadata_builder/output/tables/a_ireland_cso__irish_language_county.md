# Irish Language County

## Overview

- **Identifier:** `a_ireland_cso/irish_language_county`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Schema:** `a_ireland_cso`
- **Table:** `irish_language_county`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 32
- **Columns:** 40
- **Metadata status:** source_mapped

## Description

Irish Language County is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to irish language county.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `geogid` | `text` | Publisher-assigned geogid for the record. | source_identifier | Yes | No | No |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `yes` | `bigint` | Count or numeric value for yes in the represented area. | statistical_value | Yes | No | No |
| `no` | `bigint` | Count or numeric value for number in the represented area. | statistical_value | Yes | No | No |
| `not_stated` | `bigint` | Count or numeric value for not stated in the represented area. | statistical_value | Yes | No | No |
| `total` | `bigint` | Count or numeric value for total in the represented area. | statistical_value | Yes | No | No |
| `daily_only_within_the_education_system_males` | `bigint` | Count or numeric value for daily only within the education system males in the represented area. | statistical_value | Yes | No | No |
| `daily_within_and_daily_outside_the_education_system_males` | `bigint` | Count or numeric value for daily within and daily outside the education system males in the represented area. | statistical_value | Yes | No | No |
| `daily_within_and_weekly_outside_the_education_system_males` | `bigint` | Count or numeric value for daily within and weekly outside the education system males in the represented area. | statistical_value | Yes | No | No |
| `daily_within_and_less_often_outside_the_education_system_males` | `bigint` | Count or numeric value for daily within and less often outside the education system males in the represented area. | statistical_value | Yes | No | No |
| `daily_within_and_never_outside_the_education_system_males` | `bigint` | Count or numeric value for daily within and never outside the education system males in the represented area. | statistical_value | Yes | No | No |
| `daily_only_outside_the_education_system_males` | `bigint` | Count or numeric value for daily only outside the education system males in the represented area. | statistical_value | Yes | No | No |
| `weekly_only_outside_the_education_system_males` | `bigint` | Count or numeric value for weekly only outside the education system males in the represented area. | statistical_value | Yes | No | No |
| `less_often_only_outside_the_education_system_males` | `bigint` | Count or numeric value for less often only outside the education system males in the represented area. | statistical_value | Yes | No | No |
| `never_speaks_irish_males` | `bigint` | Count or numeric value for never speaks irish males in the represented area. | statistical_value | Yes | No | No |
| `not_stated_males` | `bigint` | Count or numeric value for not stated males in the represented area. | statistical_value | Yes | No | No |
| `all_irish_speakers_males` | `bigint` | Count or numeric value for all irish speakers males in the represented area. | statistical_value | Yes | No | No |
| `daily_only_within_the_education_system_females` | `bigint` | Count or numeric value for daily only within the education system females in the represented area. | statistical_value | Yes | No | No |
| `daily_within_and_daily_outside_the_education_system_females` | `bigint` | Count or numeric value for daily within and daily outside the education system females in the represented area. | statistical_value | Yes | No | No |
| `daily_within_and_weekly_outside_the_education_system_females` | `bigint` | Count or numeric value for daily within and weekly outside the education system females in the represented area. | statistical_value | Yes | No | No |
| `daily_within_and_less_often_outside_the_education_system_female` | `bigint` | Count or numeric value for daily within and less often outside the education system female in the represented area. | statistical_value | Yes | No | No |
| `daily_within_and_never_outside_the_education_system_females` | `bigint` | Count or numeric value for daily within and never outside the education system females in the represented area. | statistical_value | Yes | No | No |
| `daily_only_outside_the_education_system_females` | `bigint` | Count or numeric value for daily only outside the education system females in the represented area. | statistical_value | Yes | No | No |
| `weekly_only_outside_the_education_system_females` | `bigint` | Count or numeric value for weekly only outside the education system females in the represented area. | statistical_value | Yes | No | No |
| `less_often_only_outside_the_education_system_females` | `bigint` | Count or numeric value for less often only outside the education system females in the represented area. | statistical_value | Yes | No | No |
| `never_speaks_irish_females` | `bigint` | Count or numeric value for never speaks irish females in the represented area. | statistical_value | Yes | No | No |
| `not_stated_females` | `bigint` | Count or numeric value for not stated females in the represented area. | statistical_value | Yes | No | No |
| `all_irish_speakers_females` | `bigint` | Count or numeric value for all irish speakers females in the represented area. | statistical_value | Yes | No | No |
| `daily_only_within_the_education_system_total` | `bigint` | Count or numeric value for daily only within the education system total in the represented area. | statistical_value | Yes | No | No |
| `daily_within_and_daily_outside_the_education_system_total` | `bigint` | Count or numeric value for daily within and daily outside the education system total in the represented area. | statistical_value | Yes | No | No |
| `daily_within_and_weekly_outside_the_education_system_total` | `bigint` | Count or numeric value for daily within and weekly outside the education system total in the represented area. | statistical_value | Yes | No | No |
| `daily_within_and_less_often_outside_the_education_system_total` | `bigint` | Count or numeric value for daily within and less often outside the education system total in the represented area. | statistical_value | Yes | No | No |
| `daily_within_and_never_outside_the_education_system_total` | `bigint` | Count or numeric value for daily within and never outside the education system total in the represented area. | statistical_value | Yes | No | No |
| `daily_only_outside_the_education_system_total` | `bigint` | Count or numeric value for daily only outside the education system total in the represented area. | statistical_value | Yes | No | No |
| `weekly_only_outside_the_education_system_total` | `bigint` | Count or numeric value for weekly only outside the education system total in the represented area. | statistical_value | Yes | No | No |
| `less_often_only_outside_the_education_system_total` | `bigint` | Count or numeric value for less often only outside the education system total in the represented area. | statistical_value | Yes | No | No |
| `never_speaks_irish_total` | `bigint` | Count or numeric value for never speaks irish total in the represented area. | statistical_value | Yes | No | No |
| `not_stated_total` | `bigint` | Count or numeric value for not stated total in the represented area. | statistical_value | Yes | No | No |
| `all_irish_speakers_total` | `bigint` | Count or numeric value for all irish speakers total in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
