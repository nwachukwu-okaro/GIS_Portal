# Boundary Census Health Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/boundary_census_health_lsoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418601, 49.864798, 1.763680, 55.811120]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_census_health_lsoa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 35672
- **Columns:** 30
- **Metadata status:** source_mapped

## Description

Boundary Census Health Lsoa is an authoritative dataset published by Office for National Statistics. It represents boundary census health lsoa features using geometry geometry.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` |  |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `general_health_total` | `bigint` |  |
| `very_good_health` | `bigint` |  |
| `good_health` | `bigint` |  |
| `fair_health` | `bigint` |  |
| `bad_health` | `bigint` |  |
| `very_bad_health` | `bigint` |  |
| `disability_total` | `bigint` |  |
| `disabled_under_the_equality_act` | `bigint` |  |
| `disabled_ea_daily_limited_a_lot` | `bigint` |  |
| `disabled_ea_daily_limited_a_little` | `bigint` |  |
| `not_disabled_under_the_equality_act` | `bigint` |  |
| `not_disabled_ea_lt_condition_not_limited` | `bigint` |  |
| `not_disabled_ea_no_lt_conditions` | `bigint` |  |
| `unpaid_care_total` | `bigint` |  |
| `provides_no_unpaid_care` | `bigint` |  |
| `provides_19_hours_or_less_unpaid_care_a_week` | `bigint` |  |
| `provides_9_hours_or_less_unpaid_care_a_week` | `bigint` |  |
| `provides_10_to_19_hours_unpaid_care_a_week` | `bigint` |  |
| `provides_20_to_49_hours_unpaid_care_a_week` | `bigint` |  |
| `provides_20_to_34_hours_unpaid_care_a_week` | `bigint` |  |
| `provides_35_to_49_hours_unpaid_care_a_week` | `bigint` |  |
| `provides_50_or_more_hours_unpaid_care_a_week` | `bigint` |  |
| `num_disabled_in_hh_total` | `bigint` |  |
| `no_people_disabled_under_the_equality_act_in_hh` | `bigint` |  |
| `person_disabled_under_the_equality_act_in_hh` | `bigint` |  |
| `or_more_people_disabled_ea_in_hh` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
