# Boundary Census Health Oa

## Overview

- **Identifier:** `a_ons_england_wales/boundary_census_health_oa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418601, 49.864798, 1.763680, 55.811120]`
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_census_health_oa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 188880
- **Columns:** 26
- **Metadata status:** source_mapped

## Description

Boundary Census Health Oa is an authoritative dataset published by Office for National Statistics. It represents boundary census health oa features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `general_health_total` | `bigint` | Count or numeric value for general health total in the represented area. | statistical_value | Yes | No | No |
| `very_good_health` | `bigint` | Count or numeric value for very good health in the represented area. | statistical_value | Yes | No | No |
| `good_health` | `bigint` | Count or numeric value for good health in the represented area. | statistical_value | Yes | No | No |
| `fair_health` | `bigint` | Count or numeric value for fair health in the represented area. | statistical_value | Yes | No | No |
| `bad_health` | `bigint` | Count or numeric value for bad health in the represented area. | statistical_value | Yes | No | No |
| `very_bad_health` | `bigint` | Count or numeric value for very bad health in the represented area. | statistical_value | Yes | No | No |
| `disability_total` | `bigint` | Count or numeric value for disability total in the represented area. | statistical_value | Yes | No | No |
| `disabled_under_the_equality_act` | `bigint` | Count or numeric value for disabled under the equality act in the represented area. | statistical_value | Yes | No | No |
| `disabled_ea_daily_limited_a_lot` | `bigint` | Count or numeric value for disabled ea daily limited a lot in the represented area. | statistical_value | Yes | No | No |
| `disabled_ea_daily_limited_a_little` | `bigint` | Count or numeric value for disabled ea daily limited a little in the represented area. | statistical_value | Yes | No | No |
| `not_disabled_under_the_equality_act` | `bigint` | Count or numeric value for not disabled under the equality act in the represented area. | statistical_value | Yes | No | No |
| `not_disabled_ea_lt_condition_not_limited` | `bigint` | Count or numeric value for not disabled ea lt condition not limited in the represented area. | statistical_value | Yes | No | No |
| `not_disabled_ea_no_lt_conditions` | `bigint` | Count or numeric value for not disabled ea number lt conditions in the represented area. | statistical_value | Yes | No | No |
| `unpaid_care_total` | `bigint` | Count or numeric value for unpaid care total in the represented area. | statistical_value | Yes | No | No |
| `provides_no_unpaid_care` | `bigint` | Count or numeric value for provides number unpaid care in the represented area. | statistical_value | Yes | No | No |
| `provides_19_hours_or_less_unpaid_care_a_week` | `bigint` | Count or numeric value for provides 19 hours or less unpaid care a week in the represented area. | statistical_value | Yes | No | No |
| `provides_9_hours_or_less_unpaid_care_a_week` | `bigint` | Count or numeric value for provides 9 hours or less unpaid care a week in the represented area. | statistical_value | Yes | No | No |
| `provides_10_to_19_hours_unpaid_care_a_week` | `bigint` | Count or numeric value for provides 10 to 19 hours unpaid care a week in the represented area. | statistical_value | Yes | No | No |
| `provides_20_to_49_hours_unpaid_care_a_week` | `bigint` | Count or numeric value for provides 20 to 49 hours unpaid care a week in the represented area. | statistical_value | Yes | No | No |
| `provides_20_to_34_hours_unpaid_care_a_week` | `bigint` | Count or numeric value for provides 20 to 34 hours unpaid care a week in the represented area. | statistical_value | Yes | No | No |
| `provides_35_to_49_hours_unpaid_care_a_week` | `bigint` | Count or numeric value for provides 35 to 49 hours unpaid care a week in the represented area. | statistical_value | Yes | No | No |
| `provides_50_or_more_hours_unpaid_care_a_week` | `bigint` | Count or numeric value for provides 50 or more hours unpaid care a week in the represented area. | statistical_value | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
