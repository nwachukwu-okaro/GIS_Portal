# Boundary Census Private Households Nuts3

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_private_households_nuts3`
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
- **Table:** `boundary_census_private_households_nuts3`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 8
- **Columns:** 52
- **Metadata status:** source_mapped

## Description

Boundary Census Private Households Nuts3 is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census private households nuts3 features using geometry geometry.

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
| `one_person_households_no_of_households` | `bigint` | Recorded census measure for the category "one person households number of households" in the represented area. Units and population base require the source table. |
| `married_couple_households_no_of_households` | `bigint` |  |
| `cohabiting_couple_households_no_of_households` | `bigint` |  |
| `married_couple_with_children_households_hhs` | `bigint` |  |
| `cohabiting_couple_with_children_households_hhs` | `bigint` |  |
| `lone_parent_father_with_children_households_hhs` | `bigint` |  |
| `lone_parent_mother_and_children_households_hhs` | `bigint` |  |
| `couple_and_others_households_no_of_households` | `bigint` |  |
| `couple_with_children_and_others_households_hhs` | `bigint` |  |
| `lone_parent_father_with_children_others_hhs` | `bigint` |  |
| `lone_parent_mother_with_children_others_hhs` | `bigint` |  |
| `two_or_more_family_units_households_hhs` | `bigint` |  |
| `nonfamily_households_and_relations_households_hhs` | `bigint` |  |
| `two_or_more_nonrelated_persons_households_hhs` | `bigint` |  |
| `total_households_no_of_households` | `bigint` |  |
| `one_person_households_no_of_persons` | `bigint` | Recorded census measure for the category "one person households number of persons" in the represented area. Units and population base require the source table. |
| `married_couple_households_no_of_persons` | `bigint` |  |
| `cohabiting_couple_households_no_of_persons` | `bigint` |  |
| `married_couple_with_children_households_persons` | `bigint` |  |
| `cohabiting_couple_with_children_households_persons` | `bigint` |  |
| `lone_parent_father_with_children_households_persons` | `bigint` |  |
| `lone_parent_mother_and_children_households_persons` | `bigint` |  |
| `couple_and_others_households_no_of_persons` | `bigint` |  |
| `couple_with_children_and_others_households_persons` | `bigint` |  |
| `lone_parent_father_with_children_others_persons` | `bigint` |  |
| `lone_parent_mother_with_children_others_persons` | `bigint` |  |
| `two_or_more_family_units_households_no_of_persons` | `bigint` |  |
| `nonfamily_households_and_relations_households_persons` | `bigint` |  |
| `two_or_more_nonrelated_persons_households_persons` | `bigint` |  |
| `total_households_no_of_persons` | `bigint` |  |
| `t_1_person_households_no_of_households` | `bigint` |  |
| `t_2_person_households_no_of_households` | `bigint` |  |
| `t_3_person_households_no_of_households` | `bigint` |  |
| `t_4_person_households_no_of_households` | `bigint` |  |
| `t_5_person_households_no_of_households` | `bigint` |  |
| `t_6_person_households_no_of_households` | `bigint` |  |
| `t_7_person_households_no_of_households` | `bigint` |  |
| `t_8_or_more_persons_households_no_of_households` | `bigint` |  |
| `total_households_no_of_households_1` | `bigint` |  |
| `t_1_person_households_no_of_persons` | `bigint` |  |
| `t_2_person_households_no_of_persons` | `bigint` |  |
| `t_3_person_households_no_of_persons` | `bigint` |  |
| `t_4_person_households_no_of_persons` | `bigint` |  |
| `t_5_person_households_no_of_persons` | `bigint` |  |
| `t_6_person_households_no_of_persons` | `bigint` |  |
| `t_7_person_households_no_of_persons` | `bigint` |  |
| `t_8_or_more_persons_households_no_of_persons` | `bigint` |  |
| `total_households_no_of_persons_1` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
