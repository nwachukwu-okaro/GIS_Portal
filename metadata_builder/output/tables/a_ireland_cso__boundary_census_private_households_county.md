# Boundary Census Private Households County

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_private_households_county`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.746471, 54.563349, 3.417194, 58.520162]`
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_private_households_county`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 31
- **Columns:** 53
- **Metadata status:** source_mapped

## Description

Boundary Census Private Households County is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census private households county features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `geogid` | `text` | Publisher-assigned geogid for the record. | source_identifier | Yes | No | No |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `one_person_households_no_of_households` | `bigint` | Count or numeric value for one person households number of households in the represented area. | statistical_value | Yes | No | No |
| `married_couple_households_no_of_households` | `bigint` | Count or numeric value for married couple households number of households in the represented area. | statistical_value | Yes | No | No |
| `cohabiting_couple_households_no_of_households` | `bigint` | Count or numeric value for cohabiting couple households number of households in the represented area. | statistical_value | Yes | No | No |
| `married_couple_with_children_households_hhs` | `bigint` | Count or numeric value for married couple with children households hhs in the represented area. | statistical_value | Yes | No | No |
| `cohabiting_couple_with_children_households_hhs` | `bigint` | Count or numeric value for cohabiting couple with children households hhs in the represented area. | statistical_value | Yes | No | No |
| `lone_parent_father_with_children_households_hhs` | `bigint` | Numeric lone parent father with children households hhs value recorded for the feature. | measure | Yes | No | No |
| `lone_parent_mother_and_children_households_hhs` | `bigint` | Numeric lone parent mother and children households hhs value recorded for the feature. | measure | Yes | No | No |
| `couple_and_others_households_no_of_households` | `bigint` | Count or numeric value for couple and others households number of households in the represented area. | statistical_value | Yes | No | No |
| `couple_with_children_and_others_households_hhs` | `bigint` | Count or numeric value for couple with children and others households hhs in the represented area. | statistical_value | Yes | No | No |
| `lone_parent_father_with_children_others_hhs` | `bigint` | Numeric lone parent father with children others hhs value recorded for the feature. | measure | Yes | No | No |
| `lone_parent_mother_with_children_others_hhs` | `bigint` | Numeric lone parent mother with children others hhs value recorded for the feature. | measure | Yes | No | No |
| `two_or_more_family_units_households_hhs` | `bigint` | Count or numeric value for two or more family units households hhs in the represented area. | statistical_value | Yes | No | No |
| `nonfamily_households_and_relations_households_hhs` | `bigint` | Numeric nonfamily households and relations households hhs value recorded for the feature. | measure | Yes | No | No |
| `two_or_more_nonrelated_persons_households_hhs` | `bigint` | Numeric two or more nonrelated persons households hhs value recorded for the feature. | measure | Yes | No | No |
| `total_households_no_of_households` | `bigint` | Count or numeric value for total households number of households in the represented area. | statistical_value | Yes | No | No |
| `one_person_households_no_of_persons` | `bigint` | Count or numeric value for one person households number of persons in the represented area. | statistical_value | Yes | No | No |
| `married_couple_households_no_of_persons` | `bigint` | Count or numeric value for married couple households number of persons in the represented area. | statistical_value | Yes | No | No |
| `cohabiting_couple_households_no_of_persons` | `bigint` | Count or numeric value for cohabiting couple households number of persons in the represented area. | statistical_value | Yes | No | No |
| `married_couple_with_children_households_persons` | `bigint` | Count or numeric value for married couple with children households persons in the represented area. | statistical_value | Yes | No | No |
| `cohabiting_couple_with_children_households_persons` | `bigint` | Count or numeric value for cohabiting couple with children households persons in the represented area. | statistical_value | Yes | No | No |
| `lone_parent_father_with_children_households_persons` | `bigint` | Numeric lone parent father with children households persons value recorded for the feature. | measure | Yes | No | No |
| `lone_parent_mother_and_children_households_persons` | `bigint` | Numeric lone parent mother and children households persons value recorded for the feature. | measure | Yes | No | No |
| `couple_and_others_households_no_of_persons` | `bigint` | Count or numeric value for couple and others households number of persons in the represented area. | statistical_value | Yes | No | No |
| `couple_with_children_and_others_households_persons` | `bigint` | Count or numeric value for couple with children and others households persons in the represented area. | statistical_value | Yes | No | No |
| `lone_parent_father_with_children_others_persons` | `bigint` | Numeric lone parent father with children others persons value recorded for the feature. | measure | Yes | No | No |
| `lone_parent_mother_with_children_others_persons` | `bigint` | Numeric lone parent mother with children others persons value recorded for the feature. | measure | Yes | No | No |
| `two_or_more_family_units_households_no_of_persons` | `bigint` | Count or numeric value for two or more family units households number of persons in the represented area. | statistical_value | Yes | No | No |
| `nonfamily_households_and_relations_households_persons` | `bigint` | Numeric nonfamily households and relations households persons value recorded for the feature. | measure | Yes | No | No |
| `two_or_more_nonrelated_persons_households_persons` | `bigint` | Numeric two or more nonrelated persons households persons value recorded for the feature. | measure | Yes | No | No |
| `total_households_no_of_persons` | `bigint` | Count or numeric value for total households number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_1_person_households_no_of_households` | `bigint` | Count or numeric value for t 1 person households number of households in the represented area. | statistical_value | Yes | No | No |
| `t_2_person_households_no_of_households` | `bigint` | Count or numeric value for t 2 person households number of households in the represented area. | statistical_value | Yes | No | No |
| `t_3_person_households_no_of_households` | `bigint` | Count or numeric value for t 3 person households number of households in the represented area. | statistical_value | Yes | No | No |
| `t_4_person_households_no_of_households` | `bigint` | Count or numeric value for t 4 person households number of households in the represented area. | statistical_value | Yes | No | No |
| `t_5_person_households_no_of_households` | `bigint` | Count or numeric value for t 5 person households number of households in the represented area. | statistical_value | Yes | No | No |
| `t_6_person_households_no_of_households` | `bigint` | Count or numeric value for t 6 person households number of households in the represented area. | statistical_value | Yes | No | No |
| `t_7_person_households_no_of_households` | `bigint` | Count or numeric value for t 7 person households number of households in the represented area. | statistical_value | Yes | No | No |
| `t_8_or_more_persons_households_no_of_households` | `bigint` | Count or numeric value for t 8 or more persons households number of households in the represented area. | statistical_value | Yes | No | No |
| `total_households_no_of_households_1` | `bigint` | Count or numeric value for total households number of households 1 in the represented area. | statistical_value | Yes | No | No |
| `t_1_person_households_no_of_persons` | `bigint` | Count or numeric value for t 1 person households number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_2_person_households_no_of_persons` | `bigint` | Count or numeric value for t 2 person households number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_3_person_households_no_of_persons` | `bigint` | Count or numeric value for t 3 person households number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_4_person_households_no_of_persons` | `bigint` | Count or numeric value for t 4 person households number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_5_person_households_no_of_persons` | `bigint` | Count or numeric value for t 5 person households number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_6_person_households_no_of_persons` | `bigint` | Count or numeric value for t 6 person households number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_7_person_households_no_of_persons` | `bigint` | Count or numeric value for t 7 person households number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_8_or_more_persons_households_no_of_persons` | `bigint` | Count or numeric value for t 8 or more persons households number of persons in the represented area. | statistical_value | Yes | No | No |
| `total_households_no_of_persons_1` | `bigint` | Count or numeric value for total households number of persons 1 in the represented area. | statistical_value | Yes | No | No |
| `area` | `double precision` | Numeric area value recorded for the feature. | measure | Yes | No | No |
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

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
