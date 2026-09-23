# Boundary Census Disability Carers Health Smoking Csolea

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_disability_carers_health_smoking_csolea`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.726726, 54.563349, 3.417194, 58.519873]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_disability_carers_health_smoking_csolea`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 166
- **Columns:** 35
- **Metadata status:** source_mapped

## Description

Boundary Census Disability Carers Health Smoking Csolea is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census disability carers health smoking csolea features using geometry geometry.

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
| `geogdesc` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `males` | `bigint` |  |
| `females` | `bigint` |  |
| `total_perons` | `bigint` |  |
| `males_1` | `bigint` |  |
| `females_1` | `bigint` |  |
| `total` | `bigint` |  |
| `very_good_males` | `bigint` |  |
| `very_good_females` | `bigint` |  |
| `very_good_total` | `bigint` |  |
| `good_males` | `bigint` |  |
| `good_females` | `bigint` |  |
| `good_total` | `bigint` |  |
| `fair_males` | `bigint` |  |
| `fair_females` | `bigint` |  |
| `fair_total` | `bigint` |  |
| `bad_males` | `bigint` |  |
| `bad_females` | `bigint` |  |
| `bad_total` | `bigint` |  |
| `very_bad_males` | `bigint` |  |
| `very_bad_females` | `bigint` |  |
| `very_bad_total` | `bigint` |  |
| `not_stated_males` | `bigint` |  |
| `not_stated_females` | `bigint` |  |
| `not_stated_total` | `bigint` |  |
| `total_males` | `bigint` | Census total for males in the represented geographical area; measurement unit requires the table documentation. |
| `total_females` | `bigint` | Census total for females in the represented geographical area; measurement unit requires the table documentation. |
| `total_1` | `bigint` |  |
| `persons_who_smoke` | `bigint` |  |
| `persons_who_dont_smoke` | `bigint` |  |
| `non_stated` | `bigint` |  |
| `total_persons` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
