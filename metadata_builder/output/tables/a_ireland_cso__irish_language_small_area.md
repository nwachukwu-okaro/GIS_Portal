# Irish Language Small Area

## Overview

- **Identifier:** `a_ireland_cso/irish_language_small_area`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_ireland_cso`
- **Table:** `irish_language_small_area`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 18920
- **Columns:** 42
- **Metadata status:** source_mapped

## Description

Irish Language Small Area is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to irish language small area.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `guid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `geogid` | `text` | Code identifying the geographical area represented by the row. |
| `geogdesc` | `text` |  |
| `ur_category` | `double precision` |  |
| `ur_category_desc` | `text` |  |
| `yes` | `bigint` |  |
| `no` | `bigint` |  |
| `not_stated` | `bigint` |  |
| `total` | `bigint` |  |
| `daily_only_within_the_education_system_males` | `bigint` |  |
| `daily_within_and_daily_outside_the_education_system_males` | `bigint` |  |
| `daily_within_and_weekly_outside_the_education_system_males` | `bigint` |  |
| `daily_within_and_less_often_outside_the_education_system_males` | `bigint` |  |
| `daily_within_and_never_outside_the_education_system_males` | `bigint` |  |
| `daily_only_outside_the_education_system_males` | `bigint` |  |
| `weekly_only_outside_the_education_system_males` | `bigint` |  |
| `less_often_only_outside_the_education_system_males` | `bigint` |  |
| `never_speaks_irish_males` | `bigint` |  |
| `not_stated_males` | `bigint` |  |
| `all_irish_speakers_males` | `bigint` |  |
| `daily_only_within_the_education_system_females` | `bigint` |  |
| `daily_within_and_daily_outside_the_education_system_females` | `bigint` |  |
| `daily_within_and_weekly_outside_the_education_system_females` | `bigint` |  |
| `daily_within_and_less_often_outside_the_education_system_female` | `bigint` |  |
| `daily_within_and_never_outside_the_education_system_females` | `bigint` |  |
| `daily_only_outside_the_education_system_females` | `bigint` |  |
| `weekly_only_outside_the_education_system_females` | `bigint` |  |
| `less_often_only_outside_the_education_system_females` | `bigint` |  |
| `never_speaks_irish_females` | `bigint` |  |
| `not_stated_females` | `bigint` |  |
| `all_irish_speakers_females` | `bigint` |  |
| `daily_only_within_the_education_system_total` | `bigint` |  |
| `daily_within_and_daily_outside_the_education_system_total` | `bigint` |  |
| `daily_within_and_weekly_outside_the_education_system_total` | `bigint` |  |
| `daily_within_and_less_often_outside_the_education_system_total` | `bigint` |  |
| `daily_within_and_never_outside_the_education_system_total` | `bigint` |  |
| `daily_only_outside_the_education_system_total` | `bigint` |  |
| `weekly_only_outside_the_education_system_total` | `bigint` |  |
| `less_often_only_outside_the_education_system_total` | `bigint` |  |
| `never_speaks_irish_total` | `bigint` |  |
| `not_stated_total` | `bigint` |  |
| `all_irish_speakers_total` | `bigint` |  |
