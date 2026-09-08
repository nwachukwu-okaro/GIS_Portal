# Boundary Census Health Ltla

## Overview

- **Identifier:** `a_ons_england_wales/boundary_census_health_ltla`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418601, 49.864798, 1.763680, 55.811118]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_census_health_ltla`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 331
- **Columns:** 42
- **Metadata status:** source_mapped

## Description

Boundary Census Health Ltla is an authoritative dataset published by Office for National Statistics. It represents boundary census health ltla features using multipolygon geometry.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `general_health_total` | `bigint` | Count or numeric value for general health total in the represented area. |
| `very_good_health` | `bigint` | Count or numeric value for very good health in the represented area. |
| `good_health` | `bigint` | Count or numeric value for good health in the represented area. |
| `fair_health` | `bigint` | Count or numeric value for fair health in the represented area. |
| `bad_health` | `bigint` | Count or numeric value for bad health in the represented area. |
| `very_bad_health` | `bigint` | Count or numeric value for very bad health in the represented area. |
| `very_good_health_2` | `double precision` | Count or numeric value for very good health 2 in the represented area. |
| `good_health_2` | `double precision` | Count or numeric value for good health 2 in the represented area. |
| `fair_health_2` | `double precision` | Count or numeric value for fair health 2 in the represented area. |
| `bad_health_2` | `double precision` | Count or numeric value for bad health 2 in the represented area. |
| `very_bad_health_2` | `double precision` | Count or numeric value for very bad health 2 in the represented area. |
| `disability_total` | `bigint` | Count or numeric value for disability total in the represented area. |
| `disabled_under_the_equality_act` | `bigint` | Count or numeric value for disabled under the equality act in the represented area. |
| `disabled_ea_daily_limited_a_lot_t1` | `bigint` | Count or numeric value for disabled ea daily limited a lot t1 in the represented area. |
| `disabled_ea_daily_limited_a_little_t1` | `bigint` | Count or numeric value for disabled ea daily limited a little t1 in the represented area. |
| `not_disabled_under_the_equality_act_t1` | `bigint` | Count or numeric value for not disabled under the equality act t1 in the represented area. |
| `not_disabled_ea_lt_condition_not_limited` | `bigint` | Count or numeric value for not disabled ea lt condition not limited in the represented area. |
| `not_disabled_ea_no_lt_conditions` | `bigint` | Count or numeric value for not disabled ea number lt conditions in the represented area. |
| `disabled_ea_daily_limited_a_lot_t2` | `double precision` | Count or numeric value for disabled ea daily limited a lot t2 in the represented area. |
| `disabled_ea_daily_limited_a_little_t2` | `double precision` | Count or numeric value for disabled ea daily limited a little t2 in the represented area. |
| `not_disabled_under_the_equality_act_t2` | `double precision` | Count or numeric value for not disabled under the equality act t2 in the represented area. |
| `unpaid_care_total` | `bigint` | Count or numeric value for unpaid care total in the represented area. |
| `provides_no_unpaid_care_t1` | `bigint` | Count or numeric value for provides number unpaid care t1 in the represented area. |
| `provides_19_hours_or_less_unpaid_care_a_week` | `bigint` | Count or numeric value for provides 19 hours or less unpaid care a week in the represented area. |
| `provides_9_hours_or_less_unpaid_care_a_week` | `bigint` | Count or numeric value for provides 9 hours or less unpaid care a week in the represented area. |
| `provides_10_to_19_hours_unpaid_care_a_week` | `bigint` | Count or numeric value for provides 10 to 19 hours unpaid care a week in the represented area. |
| `provides_20_to_49_hours_unpaid_care_a_week_t1` | `bigint` | Count or numeric value for provides 20 to 49 hours unpaid care a week t1 in the represented area. |
| `provides_20_to_34_hours_unpaid_care_a_week` | `bigint` | Count or numeric value for provides 20 to 34 hours unpaid care a week in the represented area. |
| `provides_35_to_49_hours_unpaid_care_a_week` | `bigint` | Count or numeric value for provides 35 to 49 hours unpaid care a week in the represented area. |
| `provides_50_or_more_hours_unpaid_care_a_week` | `bigint` | Count or numeric value for provides 50 or more hours unpaid care a week in the represented area. |
| `provides_no_unpaid_care_t2` | `double precision` | Count or numeric value for provides number unpaid care t2 in the represented area. |
| `provides_19_or_less_hours_unpaid_care_a_week` | `double precision` | Count or numeric value for provides 19 or less hours unpaid care a week in the represented area. |
| `provides_20_to_49_hours_unpaid_care_a_week_t2` | `double precision` | Count or numeric value for provides 20 to 49 hours unpaid care a week t2 in the represented area. |
| `provides_50_or_more_hours_unpaid_carea_week` | `double precision` | Numeric provides 50 or more hours unpaid carea week value recorded for the feature. |
| `num_disabled_in_hh_total` | `bigint` | Count or numeric value for num disabled in households total in the represented area. |
| `no_people_disabled_under_the_equality_act_in_hh` | `bigint` | Count or numeric value for number people disabled under the equality act in households in the represented area. |
| `person_disabled_under_the_equality_act_in_hh` | `bigint` | Count or numeric value for person disabled under the equality act in households in the represented area. |
| `or_more_people_disabled_ea_in_hh` | `bigint` | Count or numeric value for or more people disabled ea in households in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
