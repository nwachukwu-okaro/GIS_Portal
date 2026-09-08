# Families County

## Overview

- **Identifier:** `a_ireland_cso/families_county`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_ireland_cso`
- **Table:** `families_county`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 32
- **Columns:** 99
- **Metadata status:** source_mapped

## Description

Families County is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to families county.

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
| `t_2_persons_no_of_families` | `bigint` | Count or numeric value for t 2 persons number of families in the represented area. |
| `t_3_persons_no_of_families` | `bigint` | Count or numeric value for t 3 persons number of families in the represented area. |
| `t_4_persons_no_of_families` | `bigint` | Count or numeric value for t 4 persons number of families in the represented area. |
| `t_5_persons_no_of_families` | `bigint` | Count or numeric value for t 5 persons number of families in the represented area. |
| `t_6_or_more_persons_no_of_families` | `bigint` | Count or numeric value for t 6 or more persons number of families in the represented area. |
| `total_no_of_families` | `bigint` | Count or numeric value for total number of families in the represented area. |
| `t_2_persons_no_of_persons` | `bigint` | Count or numeric value for t 2 persons number of persons in the represented area. |
| `t_3_persons_no_of_persons` | `bigint` | Count or numeric value for t 3 persons number of persons in the represented area. |
| `t_4_persons_no_of_persons` | `bigint` | Count or numeric value for t 4 persons number of persons in the represented area. |
| `t_5_persons_no_of_persons` | `bigint` | Count or numeric value for t 5 persons number of persons in the represented area. |
| `t_6_or_more_persons_no_of_persons` | `bigint` | Count or numeric value for t 6 or more persons number of persons in the represented area. |
| `total_no_of_persons` | `bigint` | Count or numeric value for total number of persons in the represented area. |
| `t_2_persons_no_of_children` | `bigint` | Count or numeric value for t 2 persons number of children in the represented area. |
| `t_3_persons_no_of_children` | `bigint` | Count or numeric value for t 3 persons number of children in the represented area. |
| `t_4_persons_no_of_children` | `bigint` | Count or numeric value for t 4 persons number of children in the represented area. |
| `t_5_persons_no_of_children` | `bigint` | Count or numeric value for t 5 persons number of children in the represented area. |
| `t_6_or_more_persons_no_of_children` | `bigint` | Count or numeric value for t 6 or more persons number of children in the represented area. |
| `total_no_of_children` | `bigint` | Count or numeric value for total number of children in the represented area. |
| `families_with_1_child_all_children_aged_under_15` | `bigint` | Count or numeric value for families with 1 child all children aged under 15 in the represented area. |
| `families_with_2_children_all_children_under_15` | `bigint` | Count or numeric value for families with 2 children all children under 15 in the represented area. |
| `familes_with_3_children_all_children_aged_under_15` | `bigint` | Count or numeric value for familes with 3 children all children aged under 15 in the represented area. |
| `families_with_4_children_all_children_under_15` | `bigint` | Count or numeric value for families with 4 children all children under 15 in the represented area. |
| `families_with_5_plus_children_all_children_under_15` | `bigint` | Count or numeric value for families with 5 plus children all children under 15 in the represented area. |
| `total_families_all_children_aged_under_15` | `bigint` | Count or numeric value for total families all children aged under 15 in the represented area. |
| `families_with_1_child_all_children_15_plus` | `bigint` | Count or numeric value for families with 1 child all children 15 plus in the represented area. |
| `families_with_2_children_all_children_15_plus` | `bigint` | Count or numeric value for families with 2 children all children 15 plus in the represented area. |
| `familes_with_3_children_all_children_15_plus` | `bigint` | Count or numeric value for familes with 3 children all children 15 plus in the represented area. |
| `families_with_4_children_all_children_15_plus` | `bigint` | Count or numeric value for families with 4 children all children 15 plus in the represented area. |
| `families_with_5_plus_children_all_children_15_plus` | `bigint` | Count or numeric value for families with 5 plus children all children 15 plus in the represented area. |
| `total_families_all_children_aged_15_and_over` | `bigint` | Count or numeric value for total families all children aged 15 and over in the represented area. |
| `families_2_children_mixed_ages` | `bigint` | Count or numeric value for families 2 children mixed ages in the represented area. |
| `familes_with_3_children_children_mixed_ages` | `bigint` | Count or numeric value for familes with 3 children children mixed ages in the represented area. |
| `families_4_children_mixed_ages` | `bigint` | Count or numeric value for families 4 children mixed ages in the represented area. |
| `families_5_plus_children_mixed_ages` | `bigint` | Count or numeric value for families 5 plus children mixed ages in the represented area. |
| `total_families_children_mixed_ages` | `bigint` | Count or numeric value for total families children mixed ages in the represented area. |
| `families_without_children_total` | `bigint` | Count or numeric value for families without children total in the represented area. |
| `families_with_1_child_total` | `bigint` | Count or numeric value for families with 1 child total in the represented area. |
| `families_with_2_children_total` | `bigint` | Count or numeric value for families with 2 children total in the represented area. |
| `familes_with_3_children_total` | `bigint` | Count or numeric value for familes with 3 children total in the represented area. |
| `families_with_4_children_total` | `bigint` | Count or numeric value for families with 4 children total in the represented area. |
| `families_with_5_or_more_children_total` | `bigint` | Count or numeric value for families with 5 or more children total in the represented area. |
| `total_families_total` | `bigint` | Count or numeric value for total families total in the represented area. |
| `couples_all_children_under_15_no_of_families` | `bigint` | Count or numeric value for couples all children under 15 number of families in the represented area. |
| `couples_all_children_15_plus_no_of_families` | `bigint` | Count or numeric value for couples all children 15 plus number of families in the represented area. |
| `couples_children_mixed_ages_no_of_families` | `bigint` | Count or numeric value for couples children mixed ages number of families in the represented area. |
| `total_couples_with_children_no_of_families` | `bigint` | Count or numeric value for total couples with children number of families in the represented area. |
| `lone_parent_mother_all_children_under_15_families` | `bigint` | Numeric lone parent mother all children under 15 families value recorded for the feature. |
| `lone_parent_mother_all_children_15_plus_families` | `bigint` | Numeric lone parent mother all children 15 plus families value recorded for the feature. |
| `lone_parent_mother_children_mixed_ages_families` | `bigint` | Numeric lone parent mother children mixed ages families value recorded for the feature. |
| `total_lone_parent_mother_with_children_families` | `bigint` | Numeric total lone parent mother with children families value recorded for the feature. |
| `lone_parent_father_all_children_under_15_families` | `bigint` | Numeric lone parent father all children under 15 families value recorded for the feature. |
| `lone_parent_father_all_children_15_plus_families` | `bigint` | Numeric lone parent father all children 15 plus families value recorded for the feature. |
| `lone_parent_father_children_mixed_ages_families` | `bigint` | Numeric lone parent father children mixed ages families value recorded for the feature. |
| `total_lone_parent_father_with_children_families` | `bigint` | Numeric total lone parent father with children families value recorded for the feature. |
| `couples_all_children_under_15_no_of_children` | `bigint` | Count or numeric value for couples all children under 15 number of children in the represented area. |
| `couples_all_children_15_plus_no_of_children` | `bigint` | Count or numeric value for couples all children 15 plus number of children in the represented area. |
| `couples_children_mixed_ages_no_of_children` | `bigint` | Count or numeric value for couples children mixed ages number of children in the represented area. |
| `total_couples_with_children_no_of_children` | `bigint` | Count or numeric value for total couples with children number of children in the represented area. |
| `lone_parent_mother_all_children_under_15_children` | `bigint` | Numeric lone parent mother all children under 15 children value recorded for the feature. |
| `lone_parent_mother_all_children_15_plus_children` | `bigint` | Numeric lone parent mother all children 15 plus children value recorded for the feature. |
| `lone_parent_mother_children_mixed_ages_children` | `bigint` | Numeric lone parent mother children mixed ages children value recorded for the feature. |
| `total_lone_parent_mother_with_children_children` | `bigint` | Numeric total lone parent mother with children children value recorded for the feature. |
| `lone_parent_father_all_children_under_15_children` | `bigint` | Numeric lone parent father all children under 15 children value recorded for the feature. |
| `lone_parent_father_all_children_15_plus_children` | `bigint` | Numeric lone parent father all children 15 plus children value recorded for the feature. |
| `lone_parent_father_children_mixed_ages_children` | `bigint` | Numeric lone parent father children mixed ages children value recorded for the feature. |
| `total_lone_parent_father_with_children_children` | `bigint` | Numeric total lone parent father with children children value recorded for the feature. |
| `families_with_youngest_child_aged_0_4_families` | `bigint` | Count or numeric value for families with youngest child aged 0 4 families in the represented area. |
| `families_with_youngest_child_aged_5_9_families` | `bigint` | Count or numeric value for families with youngest child aged 5 9 families in the represented area. |
| `families_with_youngest_child_aged_10_14_families` | `bigint` | Count or numeric value for families with youngest child aged 10 14 families in the represented area. |
| `families_with_youngest_child_aged_15_19_families` | `bigint` | Count or numeric value for families with youngest child aged 15 19 families in the represented area. |
| `families_with_youngest_child_aged_20_plus_families` | `bigint` | Count or numeric value for families with youngest child aged 20 plus families in the represented area. |
| `total_no_of_families_1` | `bigint` | Count or numeric value for total number of families 1 in the represented area. |
| `families_with_youngest_child_aged_0_4_persons` | `bigint` | Count or numeric value for families with youngest child aged 0 4 persons in the represented area. |
| `families_with_youngest_child_aged_5_9_persons` | `bigint` | Count or numeric value for families with youngest child aged 5 9 persons in the represented area. |
| `families_with_youngest_child_aged_10_14_persons` | `bigint` | Count or numeric value for families with youngest child aged 10 14 persons in the represented area. |
| `families_with_youngest_child_aged_15_19_persons` | `bigint` | Count or numeric value for families with youngest child aged 15 19 persons in the represented area. |
| `families_with_youngest_child_aged_20_plus_persons` | `bigint` | Count or numeric value for families with youngest child aged 20 plus persons in the represented area. |
| `total_no_of_persons_1` | `bigint` | Count or numeric value for total number of persons 1 in the represented area. |
| `prefamily_no_of_families` | `bigint` | Count or numeric value for prefamily number of families in the represented area. |
| `empty_nest_no_of_families` | `bigint` | Count or numeric value for empty nest number of families in the represented area. |
| `retired_no_of_families` | `bigint` | Count or numeric value for retired number of families in the represented area. |
| `preschool_no_of_families` | `bigint` | Count or numeric value for preschool number of families in the represented area. |
| `early_school_no_of_families` | `bigint` | Count or numeric value for early school number of families in the represented area. |
| `preadolescent_no_of_families` | `bigint` | Count or numeric value for preadolescent number of families in the represented area. |
| `adolescent_no_of_families` | `bigint` | Count or numeric value for adolescent number of families in the represented area. |
| `adult_no_of_families` | `bigint` | Count or numeric value for adult number of families in the represented area. |
| `total_no_of_families_2` | `bigint` | Count or numeric value for total number of families 2 in the represented area. |
| `prefamily_no_of_persons` | `bigint` | Count or numeric value for prefamily number of persons in the represented area. |
| `empty_nest_no_of_persons` | `bigint` | Count or numeric value for empty nest number of persons in the represented area. |
| `retired_no_of_persons` | `bigint` | Count or numeric value for retired number of persons in the represented area. |
| `preschool_no_of_persons` | `bigint` | Count or numeric value for preschool number of persons in the represented area. |
| `early_school_no_of_persons` | `bigint` | Count or numeric value for early school number of persons in the represented area. |
| `preadolescent_no_of_persons` | `bigint` | Count or numeric value for preadolescent number of persons in the represented area. |
| `adolescent_no_of_persons` | `bigint` | Count or numeric value for adolescent number of persons in the represented area. |
| `adult_no_of_persons` | `bigint` | Count or numeric value for adult number of persons in the represented area. |
| `total_no_of_persons_2` | `bigint` | Count or numeric value for total number of persons 2 in the represented area. |
