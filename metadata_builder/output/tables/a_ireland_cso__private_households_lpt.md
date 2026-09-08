# Private Households Lpt

## Overview

- **Identifier:** `a_ireland_cso/private_households_lpt`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_ireland_cso`
- **Table:** `private_households_lpt`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 27
- **Columns:** 51
- **Metadata status:** source_mapped

## Description

Private Households Lpt is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to private households lpt.

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
| `one_person_households_no_of_households` | `bigint` | Count or numeric value for one person households number of households in the represented area. |
| `married_couple_households_no_of_households` | `bigint` | Count or numeric value for married couple households number of households in the represented area. |
| `cohabiting_couple_households_no_of_households` | `bigint` | Count or numeric value for cohabiting couple households number of households in the represented area. |
| `married_couple_with_children_households_hhs` | `bigint` | Count or numeric value for married couple with children households hhs in the represented area. |
| `cohabiting_couple_with_children_households_hhs` | `bigint` | Count or numeric value for cohabiting couple with children households hhs in the represented area. |
| `lone_parent_father_with_children_households_hhs` | `bigint` | Numeric lone parent father with children households hhs value recorded for the feature. |
| `lone_parent_mother_and_children_households_hhs` | `bigint` | Numeric lone parent mother and children households hhs value recorded for the feature. |
| `couple_and_others_households_no_of_households` | `bigint` | Count or numeric value for couple and others households number of households in the represented area. |
| `couple_with_children_and_others_households_hhs` | `bigint` | Count or numeric value for couple with children and others households hhs in the represented area. |
| `lone_parent_father_with_children_others_hhs` | `bigint` | Numeric lone parent father with children others hhs value recorded for the feature. |
| `lone_parent_mother_with_children_others_hhs` | `bigint` | Numeric lone parent mother with children others hhs value recorded for the feature. |
| `two_or_more_family_units_households_hhs` | `bigint` | Count or numeric value for two or more family units households hhs in the represented area. |
| `nonfamily_households_and_relations_households_hhs` | `bigint` | Numeric nonfamily households and relations households hhs value recorded for the feature. |
| `two_or_more_nonrelated_persons_households_hhs` | `bigint` | Numeric two or more nonrelated persons households hhs value recorded for the feature. |
| `total_households_no_of_households` | `bigint` | Count or numeric value for total households number of households in the represented area. |
| `one_person_households_no_of_persons` | `bigint` | Count or numeric value for one person households number of persons in the represented area. |
| `married_couple_households_no_of_persons` | `bigint` | Count or numeric value for married couple households number of persons in the represented area. |
| `cohabiting_couple_households_no_of_persons` | `bigint` | Count or numeric value for cohabiting couple households number of persons in the represented area. |
| `married_couple_with_children_households_persons` | `bigint` | Count or numeric value for married couple with children households persons in the represented area. |
| `cohabiting_couple_with_children_households_persons` | `bigint` | Count or numeric value for cohabiting couple with children households persons in the represented area. |
| `lone_parent_father_with_children_households_persons` | `bigint` | Numeric lone parent father with children households persons value recorded for the feature. |
| `lone_parent_mother_and_children_households_persons` | `bigint` | Numeric lone parent mother and children households persons value recorded for the feature. |
| `couple_and_others_households_no_of_persons` | `bigint` | Count or numeric value for couple and others households number of persons in the represented area. |
| `couple_with_children_and_others_households_persons` | `bigint` | Count or numeric value for couple with children and others households persons in the represented area. |
| `lone_parent_father_with_children_others_persons` | `bigint` | Numeric lone parent father with children others persons value recorded for the feature. |
| `lone_parent_mother_with_children_others_persons` | `bigint` | Numeric lone parent mother with children others persons value recorded for the feature. |
| `two_or_more_family_units_households_no_of_persons` | `bigint` | Count or numeric value for two or more family units households number of persons in the represented area. |
| `nonfamily_households_and_relations_households_persons` | `bigint` | Numeric nonfamily households and relations households persons value recorded for the feature. |
| `two_or_more_nonrelated_persons_households_persons` | `bigint` | Numeric two or more nonrelated persons households persons value recorded for the feature. |
| `total_households_no_of_persons` | `bigint` | Count or numeric value for total households number of persons in the represented area. |
| `t_1_person_households_no_of_households` | `bigint` | Count or numeric value for t 1 person households number of households in the represented area. |
| `t_2_person_households_no_of_households` | `bigint` | Count or numeric value for t 2 person households number of households in the represented area. |
| `t_3_person_households_no_of_households` | `bigint` | Count or numeric value for t 3 person households number of households in the represented area. |
| `t_4_person_households_no_of_households` | `bigint` | Count or numeric value for t 4 person households number of households in the represented area. |
| `t_5_person_households_no_of_households` | `bigint` | Count or numeric value for t 5 person households number of households in the represented area. |
| `t_6_person_households_no_of_households` | `bigint` | Count or numeric value for t 6 person households number of households in the represented area. |
| `t_7_person_households_no_of_households` | `bigint` | Count or numeric value for t 7 person households number of households in the represented area. |
| `t_8_or_more_persons_households_no_of_households` | `bigint` | Count or numeric value for t 8 or more persons households number of households in the represented area. |
| `total_households_no_of_households_1` | `bigint` | Count or numeric value for total households number of households 1 in the represented area. |
| `t_1_person_households_no_of_persons` | `bigint` | Count or numeric value for t 1 person households number of persons in the represented area. |
| `t_2_person_households_no_of_persons` | `bigint` | Count or numeric value for t 2 person households number of persons in the represented area. |
| `t_3_person_households_no_of_persons` | `bigint` | Count or numeric value for t 3 person households number of persons in the represented area. |
| `t_4_person_households_no_of_persons` | `bigint` | Count or numeric value for t 4 person households number of persons in the represented area. |
| `t_5_person_households_no_of_persons` | `bigint` | Count or numeric value for t 5 person households number of persons in the represented area. |
| `t_6_person_households_no_of_persons` | `bigint` | Count or numeric value for t 6 person households number of persons in the represented area. |
| `t_7_person_households_no_of_persons` | `bigint` | Count or numeric value for t 7 person households number of persons in the represented area. |
| `t_8_or_more_persons_households_no_of_persons` | `bigint` | Count or numeric value for t 8 or more persons households number of persons in the represented area. |
| `total_households_no_of_persons_1` | `bigint` | Count or numeric value for total households number of persons 1 in the represented area. |
