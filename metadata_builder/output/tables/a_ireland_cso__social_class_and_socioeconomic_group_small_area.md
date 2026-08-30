# Social Class And Socioeconomic Group Small Area

## Overview

- **Identifier:** `a_ireland_cso/social_class_and_socioeconomic_group_small_area`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Schema:** `a_ireland_cso`
- **Table:** `social_class_and_socioeconomic_group_small_area`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 18920
- **Columns:** 53
- **Metadata status:** source_mapped

## Description

Social Class And Socioeconomic Group Small Area is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to social class and socioeconomic group small area.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `geogid` | `text` | Publisher-assigned geogid for the record. | source_identifier | Yes | No | No |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `ur_category` | `double precision` | Count or numeric value for ur category in the represented area. | statistical_value | Yes | No | No |
| `ur_category_desc` | `text` | Publisher-supplied ur category description for the represented feature or record. | source_attribute | Yes | No | No |
| `professional_workers_males` | `bigint` | Count or numeric value for professional workers males in the represented area. | statistical_value | Yes | No | No |
| `managerial_and_technical_males` | `bigint` | Count or numeric value for managerial and technical males in the represented area. | statistical_value | Yes | No | No |
| `nonmanual_males` | `bigint` | Count or numeric value for nonmanual males in the represented area. | statistical_value | Yes | No | No |
| `skilled_manual_males` | `bigint` | Count or numeric value for skilled manual males in the represented area. | statistical_value | Yes | No | No |
| `semiskilled_males` | `bigint` | Count or numeric value for semiskilled males in the represented area. | statistical_value | Yes | No | No |
| `unskilled_males` | `bigint` | Count or numeric value for unskilled males in the represented area. | statistical_value | Yes | No | No |
| `all_others_gainfully_occupied_and_unknown_males` | `bigint` | Count or numeric value for all others gainfully occupied and unknown males in the represented area. | statistical_value | Yes | No | No |
| `total_males` | `bigint` | Count or numeric value for total males in the represented area. | statistical_value | Yes | No | No |
| `professional_workers_females` | `bigint` | Count or numeric value for professional workers females in the represented area. | statistical_value | Yes | No | No |
| `managerial_and_technical_females` | `bigint` | Count or numeric value for managerial and technical females in the represented area. | statistical_value | Yes | No | No |
| `nonmanual_females` | `bigint` | Count or numeric value for nonmanual females in the represented area. | statistical_value | Yes | No | No |
| `skilled_manual_females` | `bigint` | Count or numeric value for skilled manual females in the represented area. | statistical_value | Yes | No | No |
| `semiskilled_females` | `bigint` | Count or numeric value for semiskilled females in the represented area. | statistical_value | Yes | No | No |
| `unskilled_females` | `bigint` | Count or numeric value for unskilled females in the represented area. | statistical_value | Yes | No | No |
| `all_others_gainfully_occupied_and_unknown_females` | `bigint` | Count or numeric value for all others gainfully occupied and unknown females in the represented area. | statistical_value | Yes | No | No |
| `total_females` | `bigint` | Count or numeric value for total females in the represented area. | statistical_value | Yes | No | No |
| `professional_workers_total` | `bigint` | Count or numeric value for professional workers total in the represented area. | statistical_value | Yes | No | No |
| `managerial_and_technical_total` | `bigint` | Count or numeric value for managerial and technical total in the represented area. | statistical_value | Yes | No | No |
| `nonmanual_total` | `bigint` | Count or numeric value for nonmanual total in the represented area. | statistical_value | Yes | No | No |
| `skilled_manual_total` | `bigint` | Count or numeric value for skilled manual total in the represented area. | statistical_value | Yes | No | No |
| `semiskilled_total` | `bigint` | Count or numeric value for semiskilled total in the represented area. | statistical_value | Yes | No | No |
| `unskilled_total` | `bigint` | Count or numeric value for unskilled total in the represented area. | statistical_value | Yes | No | No |
| `all_others_gainfully_occupied_and_unknown_total` | `bigint` | Count or numeric value for all others gainfully occupied and unknown total in the represented area. | statistical_value | Yes | No | No |
| `total` | `bigint` | Count or numeric value for total in the represented area. | statistical_value | Yes | No | No |
| `a_employers_and_managers_no_of_households` | `bigint` | Count or numeric value for a employers and managers number of households in the represented area. | statistical_value | Yes | No | No |
| `b_higher_professional_no_of_households` | `bigint` | Count or numeric value for b higher professional number of households in the represented area. | statistical_value | Yes | No | No |
| `c_lower_professional_no_of_households` | `bigint` | Count or numeric value for c lower professional number of households in the represented area. | statistical_value | Yes | No | No |
| `d_nonmanual_no_of_households` | `bigint` | Count or numeric value for d nonmanual number of households in the represented area. | statistical_value | Yes | No | No |
| `e_manual_skilled_no_of_households` | `bigint` | Count or numeric value for e manual skilled number of households in the represented area. | statistical_value | Yes | No | No |
| `f_semiskilled_no_of_households` | `bigint` | Count or numeric value for female semiskilled number of households in the represented area. | statistical_value | Yes | No | No |
| `g_unskilled_no_of_households` | `bigint` | Count or numeric value for g unskilled number of households in the represented area. | statistical_value | Yes | No | No |
| `h_own_account_workers_no_of_households` | `bigint` | Count or numeric value for h own account workers number of households in the represented area. | statistical_value | Yes | No | No |
| `i_farmers_no_of_households` | `bigint` | Count or numeric value for i farmers number of households in the represented area. | statistical_value | Yes | No | No |
| `j_agricultural_workers_no_of_households` | `bigint` | Count or numeric value for j agricultural workers number of households in the represented area. | statistical_value | Yes | No | No |
| `z_all_others_gainfully_occupied_and_unknown_no_of_households` | `bigint` | Count or numeric value for z all others gainfully occupied and unknown number of households in the represented area. | statistical_value | Yes | No | No |
| `total_no_of_households` | `bigint` | Count or numeric value for total number of households in the represented area. | statistical_value | Yes | No | No |
| `a_employers_and_managers_no_of_persons` | `bigint` | Count or numeric value for a employers and managers number of persons in the represented area. | statistical_value | Yes | No | No |
| `b_higher_professional_no_of_persons` | `bigint` | Count or numeric value for b higher professional number of persons in the represented area. | statistical_value | Yes | No | No |
| `c_lower_professional_no_of_persons` | `bigint` | Count or numeric value for c lower professional number of persons in the represented area. | statistical_value | Yes | No | No |
| `d_nonmanual_no_of_persons` | `bigint` | Count or numeric value for d nonmanual number of persons in the represented area. | statistical_value | Yes | No | No |
| `e_manual_skilled_no_of_persons` | `bigint` | Count or numeric value for e manual skilled number of persons in the represented area. | statistical_value | Yes | No | No |
| `f_semiskilled_no_of_persons` | `bigint` | Count or numeric value for female semiskilled number of persons in the represented area. | statistical_value | Yes | No | No |
| `g_unskilled_no_of_persons` | `bigint` | Count or numeric value for g unskilled number of persons in the represented area. | statistical_value | Yes | No | No |
| `h_own_account_workers_no_of_persons` | `bigint` | Count or numeric value for h own account workers number of persons in the represented area. | statistical_value | Yes | No | No |
| `i_farmers_no_of_persons` | `bigint` | Count or numeric value for i farmers number of persons in the represented area. | statistical_value | Yes | No | No |
| `j_agricultural_workers_no_of_persons` | `bigint` | Count or numeric value for j agricultural workers number of persons in the represented area. | statistical_value | Yes | No | No |
| `z_all_others_gainfully_occupied_and_unknown_no_of_persons` | `bigint` | Count or numeric value for z all others gainfully occupied and unknown number of persons in the represented area. | statistical_value | Yes | No | No |
| `total_no_of_persons` | `bigint` | Count or numeric value for total number of persons in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
