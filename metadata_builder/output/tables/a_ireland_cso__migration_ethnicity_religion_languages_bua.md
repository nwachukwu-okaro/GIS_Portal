# Migration Ethnicity Religion Languages Bua

## Overview

- **Identifier:** `a_ireland_cso/migration_ethnicity_religion_languages_bua`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Schema:** `a_ireland_cso`
- **Table:** `migration_ethnicity_religion_languages_bua`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 868
- **Columns:** 47
- **Metadata status:** source_mapped

## Description

Migration Ethnicity Religion Languages Bua is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to migration ethnicity religion languages bua.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `geogid` | `text` | Publisher-assigned geogid for the record. | source_identifier | Yes | No | No |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `ireland_birthplace` | `bigint` | Count or numeric value for ireland birthplace in the represented area. | statistical_value | Yes | No | No |
| `uk_birthplace` | `bigint` | Count or numeric value for uk birthplace in the represented area. | statistical_value | Yes | No | No |
| `poland_birthplace` | `bigint` | Count or numeric value for poland birthplace in the represented area. | statistical_value | Yes | No | No |
| `india_birthplace` | `bigint` | Count or numeric value for india birthplace in the represented area. | statistical_value | Yes | No | No |
| `other_eu27_2020_birthplace` | `bigint` | Count or numeric value for other eu27 2020 birthplace in the represented area. | statistical_value | Yes | No | No |
| `rest_of_world_birthplace` | `bigint` | Count or numeric value for rest of world birthplace in the represented area. | statistical_value | Yes | No | No |
| `total_birthplace` | `bigint` | Count or numeric value for total birthplace in the represented area. | statistical_value | Yes | No | No |
| `ireland_citizenship` | `bigint` | Count or numeric value for ireland citizenship in the represented area. | statistical_value | Yes | No | No |
| `uk_citizenship` | `bigint` | Count or numeric value for uk citizenship in the represented area. | statistical_value | Yes | No | No |
| `poland_citizenship` | `bigint` | Count or numeric value for poland citizenship in the represented area. | statistical_value | Yes | No | No |
| `india_citizenship` | `bigint` | Count or numeric value for india citizenship in the represented area. | statistical_value | Yes | No | No |
| `other_eu27_2020_citizenship` | `bigint` | Count or numeric value for other eu27 2020 citizenship in the represented area. | statistical_value | Yes | No | No |
| `rest_of_world_citizenship` | `bigint` | Count or numeric value for rest of world citizenship in the represented area. | statistical_value | Yes | No | No |
| `not_stated_citizenship` | `bigint` | Count or numeric value for not stated citizenship in the represented area. | statistical_value | Yes | No | No |
| `total_citizenship` | `bigint` | Count or numeric value for total citizenship in the represented area. | statistical_value | Yes | No | No |
| `white_irish` | `bigint` | Count or numeric value for white irish in the represented area. | statistical_value | Yes | No | No |
| `white_irish_traveller` | `bigint` | Count or numeric value for white irish traveller in the represented area. | statistical_value | Yes | No | No |
| `other_white` | `bigint` | Count or numeric value for other white in the represented area. | statistical_value | Yes | No | No |
| `black_or_black_irish` | `bigint` | Count or numeric value for black or black irish in the represented area. | statistical_value | Yes | No | No |
| `asian_or_asian_irish` | `bigint` | Count or numeric value for asian or asian irish in the represented area. | statistical_value | Yes | No | No |
| `other` | `bigint` | Count or numeric value for other in the represented area. | statistical_value | Yes | No | No |
| `not_stated` | `bigint` | Count or numeric value for not stated in the represented area. | statistical_value | Yes | No | No |
| `total` | `bigint` | Count or numeric value for total in the represented area. | statistical_value | Yes | No | No |
| `same_address` | `bigint` | Count or numeric value for same address in the represented area. | statistical_value | Yes | No | No |
| `elsewhere_in_county` | `bigint` | Count or numeric value for elsewhere in county in the represented area. | statistical_value | Yes | No | No |
| `elsewhere_in_ireland` | `bigint` | Count or numeric value for elsewhere in ireland in the represented area. | statistical_value | Yes | No | No |
| `outside_ireland` | `bigint` | Count or numeric value for outside ireland in the represented area. | statistical_value | Yes | No | No |
| `total_1` | `bigint` | Count or numeric value for total 1 in the represented area. | statistical_value | Yes | No | No |
| `catholic` | `bigint` | Count or numeric value for catholic in the represented area. | statistical_value | Yes | No | No |
| `other_religion` | `bigint` | Count or numeric value for other religion in the represented area. | statistical_value | Yes | No | No |
| `no_religion` | `bigint` | Count or numeric value for number religion in the represented area. | statistical_value | Yes | No | No |
| `not_stated_1` | `bigint` | Count or numeric value for not stated 1 in the represented area. | statistical_value | Yes | No | No |
| `total_2` | `bigint` | Count or numeric value for total 2 in the represented area. | statistical_value | Yes | No | No |
| `polish` | `bigint` | Count or numeric value for polish in the represented area. | statistical_value | Yes | No | No |
| `french` | `bigint` | Count or numeric value for french in the represented area. | statistical_value | Yes | No | No |
| `spanish` | `bigint` | Count or numeric value for spanish in the represented area. | statistical_value | Yes | No | No |
| `other_incl_not_stated` | `bigint` | Count or numeric value for other incl not stated in the represented area. | statistical_value | Yes | No | No |
| `total_3` | `bigint` | Count or numeric value for total 3 in the represented area. | statistical_value | Yes | No | No |
| `very_well` | `bigint` | Count or numeric value for very well in the represented area. | statistical_value | Yes | No | No |
| `well` | `bigint` | Count or numeric value for well in the represented area. | statistical_value | Yes | No | No |
| `not_well` | `bigint` | Count or numeric value for not well in the represented area. | statistical_value | Yes | No | No |
| `not_at_all` | `bigint` | Count or numeric value for not at all in the represented area. | statistical_value | Yes | No | No |
| `not_stated_2` | `bigint` | Count or numeric value for not stated 2 in the represented area. | statistical_value | Yes | No | No |
| `total_4` | `bigint` | Count or numeric value for total 4 in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
