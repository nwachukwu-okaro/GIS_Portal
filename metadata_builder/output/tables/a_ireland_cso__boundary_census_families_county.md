# Boundary Census Families County

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_families_county`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.746471, 54.563349, 3.417194, 58.520162]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_families_county`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 31
- **Columns:** 101
- **Metadata status:** source_mapped

## Description

Boundary Census Families County is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census families county features using geometry geometry.

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
| `t_2_persons_no_of_families` | `bigint` |  |
| `t_3_persons_no_of_families` | `bigint` |  |
| `t_4_persons_no_of_families` | `bigint` |  |
| `t_5_persons_no_of_families` | `bigint` |  |
| `t_6_or_more_persons_no_of_families` | `bigint` |  |
| `total_no_of_families` | `bigint` | Recorded census measure for the category "total number of families" in the represented area. Units and population base require the source table. |
| `t_2_persons_no_of_persons` | `bigint` |  |
| `t_3_persons_no_of_persons` | `bigint` |  |
| `t_4_persons_no_of_persons` | `bigint` |  |
| `t_5_persons_no_of_persons` | `bigint` |  |
| `t_6_or_more_persons_no_of_persons` | `bigint` |  |
| `total_no_of_persons` | `bigint` | Recorded census measure for the category "total number of persons" in the represented area. Units and population base require the source table. |
| `t_2_persons_no_of_children` | `bigint` |  |
| `t_3_persons_no_of_children` | `bigint` |  |
| `t_4_persons_no_of_children` | `bigint` |  |
| `t_5_persons_no_of_children` | `bigint` |  |
| `t_6_or_more_persons_no_of_children` | `bigint` |  |
| `total_no_of_children` | `bigint` | Recorded census measure for the category "total number of children" in the represented area. Units and population base require the source table. |
| `families_with_1_child_all_children_aged_under_15` | `bigint` |  |
| `families_with_2_children_all_children_under_15` | `bigint` |  |
| `familes_with_3_children_all_children_aged_under_15` | `bigint` |  |
| `families_with_4_children_all_children_under_15` | `bigint` |  |
| `families_with_5_plus_children_all_children_under_15` | `bigint` |  |
| `total_families_all_children_aged_under_15` | `bigint` |  |
| `families_with_1_child_all_children_15_plus` | `bigint` |  |
| `families_with_2_children_all_children_15_plus` | `bigint` |  |
| `familes_with_3_children_all_children_15_plus` | `bigint` |  |
| `families_with_4_children_all_children_15_plus` | `bigint` |  |
| `families_with_5_plus_children_all_children_15_plus` | `bigint` |  |
| `total_families_all_children_aged_15_and_over` | `bigint` |  |
| `families_2_children_mixed_ages` | `bigint` |  |
| `familes_with_3_children_children_mixed_ages` | `bigint` |  |
| `families_4_children_mixed_ages` | `bigint` |  |
| `families_5_plus_children_mixed_ages` | `bigint` |  |
| `total_families_children_mixed_ages` | `bigint` |  |
| `families_without_children_total` | `bigint` |  |
| `families_with_1_child_total` | `bigint` |  |
| `families_with_2_children_total` | `bigint` |  |
| `familes_with_3_children_total` | `bigint` |  |
| `families_with_4_children_total` | `bigint` |  |
| `families_with_5_or_more_children_total` | `bigint` |  |
| `total_families_total` | `bigint` |  |
| `couples_all_children_under_15_no_of_families` | `bigint` |  |
| `couples_all_children_15_plus_no_of_families` | `bigint` |  |
| `couples_children_mixed_ages_no_of_families` | `bigint` |  |
| `total_couples_with_children_no_of_families` | `bigint` |  |
| `lone_parent_mother_all_children_under_15_families` | `bigint` |  |
| `lone_parent_mother_all_children_15_plus_families` | `bigint` |  |
| `lone_parent_mother_children_mixed_ages_families` | `bigint` |  |
| `total_lone_parent_mother_with_children_families` | `bigint` |  |
| `lone_parent_father_all_children_under_15_families` | `bigint` |  |
| `lone_parent_father_all_children_15_plus_families` | `bigint` |  |
| `lone_parent_father_children_mixed_ages_families` | `bigint` |  |
| `total_lone_parent_father_with_children_families` | `bigint` |  |
| `couples_all_children_under_15_no_of_children` | `bigint` |  |
| `couples_all_children_15_plus_no_of_children` | `bigint` |  |
| `couples_children_mixed_ages_no_of_children` | `bigint` |  |
| `total_couples_with_children_no_of_children` | `bigint` |  |
| `lone_parent_mother_all_children_under_15_children` | `bigint` |  |
| `lone_parent_mother_all_children_15_plus_children` | `bigint` |  |
| `lone_parent_mother_children_mixed_ages_children` | `bigint` |  |
| `total_lone_parent_mother_with_children_children` | `bigint` |  |
| `lone_parent_father_all_children_under_15_children` | `bigint` |  |
| `lone_parent_father_all_children_15_plus_children` | `bigint` |  |
| `lone_parent_father_children_mixed_ages_children` | `bigint` |  |
| `total_lone_parent_father_with_children_children` | `bigint` |  |
| `families_with_youngest_child_aged_0_4_families` | `bigint` |  |
| `families_with_youngest_child_aged_5_9_families` | `bigint` |  |
| `families_with_youngest_child_aged_10_14_families` | `bigint` |  |
| `families_with_youngest_child_aged_15_19_families` | `bigint` |  |
| `families_with_youngest_child_aged_20_plus_families` | `bigint` |  |
| `total_no_of_families_1` | `bigint` |  |
| `families_with_youngest_child_aged_0_4_persons` | `bigint` |  |
| `families_with_youngest_child_aged_5_9_persons` | `bigint` |  |
| `families_with_youngest_child_aged_10_14_persons` | `bigint` |  |
| `families_with_youngest_child_aged_15_19_persons` | `bigint` |  |
| `families_with_youngest_child_aged_20_plus_persons` | `bigint` |  |
| `total_no_of_persons_1` | `bigint` |  |
| `prefamily_no_of_families` | `bigint` |  |
| `empty_nest_no_of_families` | `bigint` |  |
| `retired_no_of_families` | `bigint` |  |
| `preschool_no_of_families` | `bigint` |  |
| `early_school_no_of_families` | `bigint` |  |
| `preadolescent_no_of_families` | `bigint` |  |
| `adolescent_no_of_families` | `bigint` |  |
| `adult_no_of_families` | `bigint` |  |
| `total_no_of_families_2` | `bigint` |  |
| `prefamily_no_of_persons` | `bigint` |  |
| `empty_nest_no_of_persons` | `bigint` |  |
| `retired_no_of_persons` | `bigint` |  |
| `preschool_no_of_persons` | `bigint` |  |
| `early_school_no_of_persons` | `bigint` |  |
| `preadolescent_no_of_persons` | `bigint` |  |
| `adolescent_no_of_persons` | `bigint` |  |
| `adult_no_of_persons` | `bigint` |  |
| `total_no_of_persons_2` | `bigint` |  |
| `area` | `double precision` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
